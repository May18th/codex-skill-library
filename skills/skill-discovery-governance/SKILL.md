---
name: skill-discovery-governance
description: Use when Codex repeatedly misses the relevant Skill, invokes an unrelated Skill, or when auditing, organizing, adding, or improving a growing Codex Skill library; not for implementing the task handled by a domain Skill.
---

# Skill 命中治理

提升 Skill 的可发现性和路由准确度。Codex 按可见的名称与描述判断是否加载 Skill；不要假设它必然使用向量检索、固定 Top-K 重排或可测量的命中率。

## 工作流程

1. 先复现问题：记录用户原始请求、应命中的 Skill、实际是否调用、误选项和造成的结果。区分“描述未召回”“描述重叠”“正文流程不清”“Skill 本身不适用”。
2. 检查 Skill 的 `name`、`description`、正文边界和当前可发现目录。描述用用户会说的任务词、交付物和场景说明触发条件；在容易混淆时补充准确的排除条件及替代 Skill。避免把全部流程塞进描述。
3. 给每个可调用 Skill 标注逻辑业务类别，便于人和路由规范检索。Codex 当前发现目录如为平铺结构，分类只记在注册表/索引中；未经运行时文档确认，不要把 Skill 实体移到嵌套目录。
4. 优先改动有证据的问题 Skill，并检查相邻 Skill 是否因此产生新的重叠。第三方 Skill 保留原作者的行为和授权边界；编辑前读完整文件，最小化改动。
5. 运行 `python scripts/audit_skill_discovery.py`，处理未分类、重复 ID、缺少触发描述和边界不清等报告项。需要实际命中率时，使用代表性请求集记录真实调用结果，不用文本启发式分数冒充命中率。

## 描述质量标准

- 正向触发：明确用户要做什么、涉及什么材料/产物或典型场景；使用具体词汇，不用“通用助手”等泛称。
- 负向边界：对可能混淆的场景说明不适用范围，必要时指出应路由到哪个 Skill。不得添加不真实的排除项。
- 单一职责：描述只写何时调用，不复述 Skill 内部步骤；多个 Skill 重叠时比较触发词和职责边界后再改。
- 自动调用保持启用，除非用户明确要求关闭。显式 `$skill-name` 可用于诊断自动发现问题。

## 规模治理

分类树是管理索引，不等同于运行时检索器。Skill 数量增长后，先用分类索引和代表性请求集评估是否有必要建设关键词/Embedding 召回与模型重排；只有环境中确有该能力且可验证时才启用。不要宣称固定命中率或准确率，除非定义了测试集、统计口径和观测数据。

巡检频率、抽样比例和问题阈值是可配置的运营策略，不是 Codex 内建保证。查看 [references/taxonomy.md](references/taxonomy.md) 获取当前逻辑分类；查看 [references/measurement.md](references/measurement.md) 设计命中测试与周检。
