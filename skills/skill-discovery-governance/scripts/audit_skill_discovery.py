#!/usr/bin/env python3
"""Read-only Skill catalog audit; writes timestamped CSV and Markdown reports."""

from __future__ import annotations

import argparse
import csv
import re
import sys
import tempfile
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

CODEX_PACKAGE_DIR = Path(__file__).resolve().parents[3] / "python-packages"
if CODEX_PACKAGE_DIR.is_dir():
    sys.path.insert(0, str(CODEX_PACKAGE_DIR))

try:
    import yaml
except ImportError:
    print("PyYAML is required. Run this script with the Python used by Codex.", file=sys.stderr)
    raise SystemExit(2)


NEGATIVE_MARKERS = (
    "not for", "not used for", "not a", "does not", "instead of", "rather than",
    "不适用", "不用于", "不负责", "不要用于", "而非", "不包括",
)
TRIGGER_MARKERS = (
    "use when", "use for", "when ", "用于", "当用户", "当需要", "在需要", "适用于",
    "requests", "create", "build", "draft", "audit", "convert", "debug", "review",
)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def read_skill(skill_dir: Path):
    path = skill_dir / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        return {"name": "", "description": "", "error": "invalid or missing YAML frontmatter"}
    try:
        meta = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        return {"name": "", "description": "", "error": f"invalid YAML: {exc}"}
    if not isinstance(meta, dict):
        return {"name": "", "description": "", "error": "frontmatter must be a mapping"}
    return {
        "name": str(meta.get("name", "")).strip(),
        "description": str(meta.get("description", "")).strip(),
        "error": "" if isinstance(meta, dict) else "frontmatter must be a mapping",
    }


def category_registry(taxonomy_path: Path):
    taxonomy = load_yaml(taxonomy_path) or {}
    registry = {}
    for category_id, category in taxonomy.get("categories", {}).items():
        for folder in category.get("skills", []):
            registry.setdefault(folder, []).append((category_id, category.get("title", category_id)))
    return registry


def archived_directories(taxonomy_path: Path):
    taxonomy = load_yaml(taxonomy_path) or {}
    return set((taxonomy.get("archives") or {}).get("directories", []))


def audit(skill_root: Path, taxonomy_path: Path):
    registry = category_registry(taxonomy_path)
    archives = archived_directories(taxonomy_path)
    rows, issues = [], []
    skill_dirs = sorted(
        (p for p in skill_root.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()),
        key=lambda p: p.name.casefold(),
    )
    name_counts = Counter()
    for skill_dir in skill_dirs:
        data = read_skill(skill_dir)
        name_counts[data["name"]] += 1
        categories = registry.get(skill_dir.name, [])
        desc_lower = data["description"].casefold()
        has_trigger = any(marker in desc_lower for marker in TRIGGER_MARKERS)
        has_negative = any(marker in desc_lower for marker in NEGATIVE_MARKERS)
        row_issues = []
        if data["error"]:
            row_issues.append(data["error"])
        if not categories:
            row_issues.append("unclassified")
        elif len(categories) > 1:
            row_issues.append("multiple category assignments")
        if not data["name"]:
            row_issues.append("missing Skill name")
        if not data["description"]:
            row_issues.append("missing description")
        elif not has_trigger:
            row_issues.append("trigger context unclear; manual review")
        if data["description"] and not has_negative:
            row_issues.append("no explicit negative-scope wording; review if overlap risk exists")
        row = {
            "folder": skill_dir.name,
            "name": data["name"],
            "category": ", ".join(title for _, title in categories) or "未分类",
            "trigger_clear_heuristic": "yes" if has_trigger else "review",
            "negative_scope_heuristic": "yes" if has_negative else "review overlap",
            "description": data["description"],
            "issues": "; ".join(row_issues),
        }
        rows.append(row)
        for issue in row_issues:
            issues.append((skill_dir.name, issue))

    for folder, categories in registry.items():
        if not (skill_root / folder / "SKILL.md").is_file():
            issues.append((folder, "taxonomy entry has no immediate-child SKILL.md"))
    for directory in sorted(p for p in skill_root.iterdir() if p.is_dir() and not (p / "SKILL.md").is_file()):
        if directory.name != ".system" and directory.name not in archives:
            issues.append((directory.name, "directory has no immediate-child SKILL.md; not discoverable as a Skill"))
    by_name = defaultdict(list)
    for row in rows:
        if row["name"]:
            by_name[row["name"]].append(row["folder"])
    for name, folders in by_name.items():
        if len(folders) > 1:
            issues.append((", ".join(folders), f"duplicate Skill ID: {name}"))
    return rows, issues


def write_reports(rows, issues, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().astimezone().strftime("%Y%m%d-%H%M%S")
    csv_path = output_dir / f"skill-discovery-audit-{stamp}.csv"
    md_path = output_dir / f"skill-discovery-audit-{stamp}.md"
    with csv_path.open("w", newline="", encoding="utf-8-sig") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]) if rows else ["folder", "name", "category", "trigger_clear_heuristic", "negative_scope_heuristic", "description", "issues"])
        writer.writeheader()
        writer.writerows(rows)
    lines = [
        "# Codex Skill 发现审计",
        "",
        f"- 审计时间：{datetime.now().astimezone().isoformat(timespec='seconds')}",
        f"- 可发现 Skill 数：{len(rows)}",
        f"- 发现项：{len(issues)}（启发式提示需人工确认，不等同于命中率）",
        "",
        "| Skill 文件夹 | 类别 | 检查项 |",
        "|---|---|---|",
    ]
    for row in rows:
        lines.append(f"| `{row['folder']}` | {row['category']} | {row['issues'] or '未发现结构性问题'} |")
    if issues:
        lines.extend(["", "## 发现项", ""])
        for folder, issue in issues:
            lines.append(f"- `{folder}`：{issue}")
    lines.extend([
        "",
        "## 解释",
        "",
        "触发词与负向边界仅由有限关键词启发式检查。报告用于排序人工复核，不会编辑 Skill，也不代表 Skill 实际被调用的命中率。",
    ])
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return csv_path, md_path


def self_test():
    with tempfile.TemporaryDirectory(prefix="codex-skill-audit-") as temp:
        root = Path(temp) / "skills"
        root.mkdir()
        taxonomy = Path(temp) / "taxonomy.yaml"
        taxonomy.write_text(
            "categories:\n  sample:\n    title: Sample\n    skills: [alpha, beta]\n",
            encoding="utf-8",
        )
        fixture = {
            "alpha": "---\nname: duplicate\ndescription: Use when converting a DOCX; not for PDF conversion.\n---\n",
            "beta": "---\nname: duplicate\ndescription: Generic helper.\n---\n",
            "gamma": "---\nname: gamma\ndescription: Use for auditing.\n---\n",
        }
        for folder, content in fixture.items():
            (root / folder).mkdir()
            (root / folder / "SKILL.md").write_text(content, encoding="utf-8")
        rows, issues = audit(root, taxonomy)
        assert len(rows) == 3
        assert any(folder == "gamma" and "unclassified" in issue for folder, issue in issues)
        assert any("duplicate Skill ID" in issue for _, issue in issues)
        beta = next(row for row in rows if row["folder"] == "beta")
        assert beta["negative_scope_heuristic"] == "review overlap"
        alpha = next(row for row in rows if row["folder"] == "alpha")
        assert alpha["trigger_clear_heuristic"] == "yes"
    print("Self-test passed: category coverage, duplicate IDs, triggers, and negative-scope flags.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-dir", type=Path, help="Skill root; defaults to this Skill's parent directory")
    parser.add_argument("--output-dir", type=Path, help="Report directory; defaults to D:\\Codex\\skill-audits")
    parser.add_argument("--self-test", action="store_true", help="Run isolated audit behavior tests")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    skill_root = args.skills_dir or Path(__file__).resolve().parents[2]
    taxonomy_path = Path(__file__).resolve().parents[1] / "references" / "taxonomy.yaml"
    output_dir = args.output_dir or skill_root.parent / "skill-audits"
    rows, issues = audit(skill_root, taxonomy_path)
    csv_path, md_path = write_reports(rows, issues, output_dir)
    print(f"Audited {len(rows)} discoverable Skills; {len(issues)} review items.")
    print(f"Markdown: {md_path}")
    print(f"CSV: {csv_path}")


if __name__ == "__main__":
    main()
