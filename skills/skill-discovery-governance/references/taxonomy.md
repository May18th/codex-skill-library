# Codex Skill 逻辑分类树

Codex 当前要求每个 Skill 文件夹是 `skills/` 的直接子目录。以下是逻辑分类索引，不是移动目录的指令；保持每个 `SKILL.md` 所属文件夹位于 `D:\Codex\skills\<skill-folder>\SKILL.md`。

| 类别 | 当前 Skill 文件夹 |
|---|---|
| 工作流与治理 | `ai-core-capabilities`、`book-to-skill`、`brainstorming`、`codex-task-routing`、`diagnosing-superpowers`、`dispatching-parallel-agents`、`executing-plans`、`grill-me`、`Project-Governor`、`skill-discovery-governance`、`subagent-driven-development`、`SuperPowers`、`using-git-worktrees`、`using-superpowers`、`writing-plans`、`writing-skills` |
| 全栈应用开发 | `vue-django-mysql-fullstack` |
| 工程质量与调试 | `Code-Map`、`diagnose`、`receiving-code-review`、`requesting-code-review`、`systematic-debugging`、`test-driven-development`、`verification-before-completion` |
| Web、界面与可视化 | `high-end-web-design`、`ui-design-system`、`visual-dashboard-pipeline` |
| 文档、知识与表达 | `caveman`、`Humanizer-zh`、`markitdown` |
| 网络与学术研究 | `Agent-Reach`、`nature-academic-search`、`nature-citation`、`nature-data`、`nature-downloader`、`nature-experiment-log`、`nature-figure`、`nature-literature-pipeline`、`nature-paper-card`、`nature-paper-to-patent`、`nature-paper-trans`、`nature-paper2ppt`、`nature-polishing`、`nature-proposal-writer`、`nature-reader`、`nature-ref-verifier`、`nature-response`、`nature-reviewer`、`nature-shared`、`nature-statistics`、`nature-writing` |
| 演示文稿与可编辑幻灯片 | `codeximage-to-editable-ppt-v2-1`、`codeximage-to-editable-ppt-v2-2`、`nature-image2ppt` |

| 旧说明包（不可调用 Skill） | `web-dev-skills` |

新 Skill 必须先选一个主类别并登记文件夹名。一个 Skill 只登记一次；如确实跨类，说明主类并在说明中写清职责边界，不复制 Skill 文件夹。

## 已知整理事项

- `SuperPowers` 与 `using-superpowers` 当前使用同一个 Skill ID（`using-superpowers`）。这是发现歧义，应先比较两份正文并决定保留/合并策略；未审阅前不要删除、覆盖或重命名任何一份。
- `web-dev-skills` 当前没有根目录 `SKILL.md`，因此不是可直接发现的 Skill；审计会列为孤立目录，需人工确认用途。
- `.system` 是系统 Skill 区，不纳入这份用户 Skill 分类表，也不做批量改写。
