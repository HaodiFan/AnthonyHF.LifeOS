---
name: psp
description: PSP self-evolution Skill。用于在 owner 授权材料后更新 person model、行为边界、语言/判断模式、置信度和验证样例；匿名身份使用 PSP 化名。
---

# PSP

## 作用

PSP 负责更新：

- `identity/psp/anthony-fan/PSP-<timestamp>.md`
- `identity/psp/anthony-fan/update-log-<timestamp>.md`
- `identity/psp/anthony-fan/INITIALIZATION.md`

## 输入边界

- 只写抽象后的模型结论和证据摘要。
- 原始材料留在本地、私有 wiki 或 owner 指定系统。
- 匿名身份使用 `Anthony Fan` 作为 PSP 名称，不暴露真实身份。

## 更新规则

生成或更新 PSP 主产物前，必须读取 `docs/self-evolution-output-standards.md` 的 PSP Standard Output。

每次更新必须记录：

- source type。
- update summary。
- confidence。
- reviewer / owner alignment 状态。

如果资料不足以填充 PSP 标准产物的关键信息，必须在 `standard_output_gate.evidence_sufficiency` 标为 `insufficient`，并列出缺失的行为样本、判断样本、验证样例或反例；不要把 intake scaffold 或公开摘要伪装成完整 PSP。

## 产物命名规则

- PSP 主产物必须带生成时间，例如 `PSP-20260525-153012.md`。
- 更新日志必须带生成时间，例如 `update-log-20260525-153012.md`。
- 固定入口 `INITIALIZATION.md` 不存放人物事实本体，只说明如何把时间戳 PSP 产物适配到不同 Agent 框架。

## Agent 框架适配

- Hermes：可把 PSP 主产物中经过 owner approval 的人格/行为边界激活到 `SOUL.md`；稳定事实进入 `MEMORY.md` / `USER.md`；可复用流程进入 `skills/*/SKILL.md`。
- OpenClaw：PSP 主产物可激活到 `SOUL.md` / `IDENTITY.md`；本 Skill 的 procedural 规则可对应 workspace `AGENTS.md`；工具使用边界进入 `TOOLS.md`；长期事实进入 `MEMORY.md` 或 `memory/YYYY-MM-DD.md` 候选层。
- OpenAI/Codex 类 agents：PSP 中的 persona/policy 进入 system/developer prompt；流程进入 Skill/agent instructions；长期事实进入 memory/knowledge，不写进 Skill。

## Memory / Skill 分界

- Memory 只回答“什么是真的”：稳定事实、偏好、身份、长期上下文、证据来源。
- Skill 只回答“应该怎么做”：步骤、触发条件、验证门、失败处理。
- 同一段材料同时包含事实和做法时，落盘前必须拆成 memory fact 与 skill procedure，并在更新日志中记录拆分关系。
