---
name: book-to-skill
description: Use when the user wants to learn an unfamiliar field through a classic book, extract a book’s problem-solving method into a reusable Codex Skill, validate that Skill on real tasks, or maintain a cross-domain method library; not for generic book summaries, reproducing a book, or installing a Skill copied from an unrelated repository.
---

# 新领域方法论提炼

把书中适用于目标问题的高层方法转成原创、可验证的操作流程；不是把书全文压缩、复制或做成替代品。书龄 30 年以上是优先条件，不是适配度与事实核验的替代品。

## 流程

1. **定义问题。** 写清目标用户、具体任务、场景、约束和成功标准。避免只写“学习管理/谈判/产品设计”。
2. **选书并核实。** 如需推荐书籍，使用可用的联网研究 Skill 查找并核对作者、原版出版年份、版本和主题匹配度；优先推荐经长期使用且直接覆盖目标问题的经典书。没有合适的 30 年以上作品时，说明原因并给出较新的可靠替代，不虚构“经典”或出版年。
3. **确认材料边界。** 先用正规渠道取得材料或用户已有且有权使用的文本/笔记。上传前核对版权许可、所在 AI 平台的文件处理与数据使用规则及机构要求。未明确授权时只用用户提供的合法摘录、目录、笔记或可合法访问资料；不下载盗版，不要求上传整本受版权保护的书。
4. **提炼原创流程。** 从材料中提取问题框架、关键步骤、判断标准、常见失败与适用边界；用自己的语言形成可执行规则，并保留书名/版次/页码或章节作为内部溯源。引用只取完成任务所必需的短片段，不输出大段原文或逐章替代性摘要。
5. **创建独立 Skill。** 按 `writing-skills` 规范，使用小写连字符名称，写清正向触发和负向边界；保留 `D:\Codex\skills\<skill-name>\SKILL.md` 的直接子目录结构，默认开启隐式调用。将来源与版本记录放在 `D:\Codex\method-library\sources`，不把受限全文复制到 Skill 目录。
6. **验证再归档。** 选至少一个典型任务和一个边界/反例任务，按原方法独立检查输出。记录来源依据、步骤是否可执行、遗漏/偏差、限制和测试结果。失败时只修改有证据支持的部分并重测；未测试不得称为准确掌握。

## 方法库维护

目录索引建议为 `D:\Codex\method-library\index.md`，记录领域、目标问题、Skill 名、来源、版本、验证样本、最后复核日期和状态。跨领域复用同一抽取流程，但每个 Skill 只负责自己的领域，旧 Skill 过时时保留版本记录后再更新或停用。累计至少 5 个领域 Skill 是成长目标，不得通过生成空泛或重复的 Skill 凑数。

涉及书目事实时使用 [书目核验记录](references/book-selection.md)；生成 Skill 时用 [方法论提炼与验证卡](references/extraction-validation.md)。
