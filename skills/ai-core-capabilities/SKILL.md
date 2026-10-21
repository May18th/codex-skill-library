---
name: ai-core-capabilities
description: Use when the user wants to improve AI-assisted work quality, distinguish surface requests from real needs, review an AI output, build reusable judgment or aesthetic standards, or run task/weekly retrospectives; not for adding a mandatory training workflow to a simple factual answer.
---

# AI时代核心能力积累

把产品感、判断力、审美力、学习能力落实到有证据的工作改进。目标是增强人的决策能力，不承诺“不可替代”或脱离数据宣称质量提升。

## 任务前：问题与验收

1. 从现有请求和上下文提取“谁在什么场景遇到什么障碍、真正想完成什么、怎样算成功”。区分用户事实与推测；只有会改变方向的未知决策才提问。
2. 写清表面需求→真实需求假设→最小解决方向。不要把“写更多”“加功能”直接等同于更有价值。
3. 按产物类型选取 [质量验收清单](references/quality-checklist.md)，把“高级”“清楚”“好用”转为可以观察的标准。与现有场景规则冲突时明确范围，不擅自覆盖。

## 任务中：三秒筛查，再按风险核验

- 是否解决核心问题？是否只有空话而没有可执行细节？是否有逻辑矛盾或编造事实？是否符合真实使用场景？
- 三秒筛查只用于快速定位风险，不能替代事实来源、代码测试、数据校验或完整视觉检查。
- 涉及视觉与文案时，检查层次、留白、对比和一致性；保留具体、真实、符合受众的表达，不为“人味”编造经历或细节。仅在当前任务适用时使用用户的设计偏好。

## 任务后：留下可复用判断

按需使用 [需求记录](references/needs-library.md)、[审美参考卡](references/aesthetic-card.md)、[复盘模板](references/retrospective.md)。记录“判断依据—实际结果—下一次改什么”，不写泛泛感想或虚构成绩。

单次临时调整只留在任务记录；可复用步骤进入对应 Skill；场景共同约束进入场景 `AGENTS.md`；稳定全局偏好只留简短索引。不要自动把每次结果写入全局记忆。需要持久化时使用用户指定目录，未指定则在 `D:\Codex\method-library\core-capabilities` 内按类型保存去标识化记录，不覆盖旧文件。

每周复盘在用户要求或已配置的定时机制触发时执行：抽取本周真实任务，找重复失败和有效决策，更新一项有证据的标准并回归旧案例。未创建定时机制时不要声称会在后台每周自动运行。
