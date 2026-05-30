# Cognition 认知对象层

这一层定义 AnthonyHF 的 LifeOS 如何把事实、流程、身份、策略和外部数据源分开存放。

核心规则：

> Memory 只回答“什么是真的”；Skill 只回答“应该怎么做”。同一段材料同时包含事实和流程时，写入前必须拆分。

## Files

- `object-taxonomy.yml`: 认知对象类型、默认路径和写入路由。
- `data-contracts.yml`: 外部数据源、authority、visibility、同步与导出边界。

## Write routing

- 临时任务状态不写入长期记忆。
- 稳定事实进入 `memory/long-term/` 或私有 memory wiki。
- 候选经验进入 `memory/working-lessons/`，等待复盘和晋升。
- 多源归纳的 claim 进入 `memory/distilled-knowledge/`。
- 可复用步骤进入 `skills/runtime/` 或外部 runtime skill repo。
- 可复用判断进入 `skills/meta/`。
- Skill 需要的事实和数据源放在 `skills/bindings/`，不要写死进 `SKILL.md`。
