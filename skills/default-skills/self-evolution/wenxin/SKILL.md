---
name: wenxin
description: 问心 self-evolution Skill。用于在 owner 明确授权材料后，生成“我是谁、我站在哪、离领域完整版差多少、我该往哪走”的自我发现报告，并把可公开部分沉淀到 public positioning 和 Skill candidates。
---

# Wenxin

## 作用

问心负责把 owner-approved evidence 转成自我发现产物：

- `identity/wenxin/WENXIN_REPORT.md`
- `identity/wenxin/public-positioning.md`
- `identity/wenxin/skill-candidates.yml`

## 输入边界

- 只使用 owner 明确授权的材料。
- 匿名身份只使用 `psp_display_name` 和授权标签，不反推真实身份。
- 不提交原始私密正文、客户细节、secret 或未脱敏材料。

## 输出要求

生成或更新 `identity/wenxin/WENXIN_REPORT.md` 前，必须读取 `docs/self-evolution-output-standards.md` 的 Wenxin Standard Output。

输出必须区分：

- 已确认事实。
- 基于证据的推断。
- 需要 owner 继续确认的问题。

如果资料不足以填充标准产物的关键信息，必须在 `standard_output_gate.evidence_sufficiency` 标为 `insufficient`，并列出 `missing_information` 和针对性补料问题；不要输出看起来完整但没有证据支撑的问心报告。
