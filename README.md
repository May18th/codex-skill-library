# Codex Skill Library

用于保存可复用的 Codex Skill、Skill 命中治理资料、方法库索引和全局规则副本。

## 目录

- `skills/`：可复用 Skill。每个 Skill 保持一个直接子目录，并包含 `SKILL.md`。
- `governance/`：全局协作与文件管理规则副本。
- `method-library/`：跨领域方法库索引。
- `skill-audits/`：Skill 目录结构与描述质量的审计结果。

## 本地安装位置

Codex 的全局 Skill 目录是 `D:\Codex\skills`。仓库中的 Skill 目录需要复制到该目录后才能被当前环境发现：

```powershell
Copy-Item -Recurse -Force .\skills\* D:\Codex\skills\
```

Skill 必须保持以下结构：

```text
D:\Codex\skills\<skill-folder>\SKILL.md
```

## 当前收录

- `ai-core-capabilities`：AI 任务的需求、质量、审美和复盘能力框架。
- `book-to-skill`：从合法书籍材料提炼并验证方法论 Skill 的流程。
- `skill-discovery-governance`：Skill 描述、边界、分类和审计治理。
- `vue-django-mysql-fullstack`：Vue 3、Django REST Framework 与 MySQL 的通用全栈项目开发流程。

## 安全边界

本仓库不收录 Codex 会话、插件、缓存、数据库、密钥、Token、自动记忆、浏览器数据或其他运行时数据。新增内容提交前必须检查是否包含凭据、个人隐私和本机专属路径。

## 同步原则

先在 `D:\Codex` 中验证文件和 Skill，再将筛选后的可复用内容复制到本仓库；提交前运行敏感内容扫描和 Skill 结构审计。仓库内容变化不会自动改变本机 Codex 配置。
