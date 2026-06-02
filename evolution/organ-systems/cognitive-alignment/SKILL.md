---
name: anthonyhf-cognitive-alignment
description: AnthonyHF 的认知对齐与分歧复盘 Skill。用于 agent 需要先讲出自己的评判、与 Anthony 的判断校准、处理纠偏、复盘分歧，并把可复用规则沉淀到正确的 Skill、memory tier、Wenxin、PSP 或 LifeOS 路由时。
---

# Cognitive Alignment

Cognitive Alignment 是 AnthonyHF.LifeOS 的 self-evolution Skill。

它用于处理“agent 的判断”和“Anthony 的判断”之间的差异：先把 agent 的评判讲清楚，再根据 owner 纠偏定位根因，最后把可复用的对齐规则写回正确位置。

## 使用场景

- 用户要求“讲出你的判断”“和我认知对齐”“debug 一下你的判断”。
- 用户指出“不对”“这不是我想要的”“这个 skill 不全面”。
- 需要复盘分歧，把纠偏沉淀为 reusable rule。
- 需要判断更新应该进入 Skill、memory、Wenxin、PSP、Soul、Design 还是 routing。

## 工作方式

1. 先说明 agent 当前判断、依据和不确定性。
2. 对照用户纠偏，定位是事实缺失、路由错误、抽象层级错误、证据门槛错误，还是输出风格错误。
3. 把可复用结论写到正确产物，不把临时对话直接塞进 `SKILL.md`。
4. 涉及 Anthony-specific 事实时，优先查询 memory 和 current artifacts；证据不足时明确说明。

## 边界

- 这是对齐和复盘 Skill，不是 PSP 替代品。
- 不编造 Anthony 的稳定人格、关系姿态或私人事实。
- 如果只是身份定位或个人 BP，先走 Wenxin；如果是人物模型和分身边界，先走 PSP。
