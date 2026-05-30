# Self-Evolution Output Standards

Generated: 2026-05-30
Owner: AnthonyHF

This file defines the minimum standard outputs for Wenxin, PSP, and IPO Reverse.

The rule is simple:

- If the provided evidence is sufficient to fill the key fields, the artifact may pass.
- If the evidence is insufficient, the artifact must explicitly fail the sufficiency gate and list the missing information or targeted follow-up questions.
- A file that only contains generic summary text must not pass.

## Shared Gate

Every Wenxin, PSP, and IPO Reverse artifact must include:

```yaml
standard_output_gate:
  artifact_type: wenxin | psp | ipo-reverse
  evidence_sufficiency: sufficient | insufficient
  evidence_sources:
    - source_id:
      source_type:
      authority: primary | secondary | user-approved | inferred
      used_for:
  missing_information:
    - field:
      why_needed:
      suggested_prompt:
  confidence:
    overall: high | medium | low
    notes:
```

If `evidence_sufficiency=insufficient`, the artifact must stop before making stable identity/person/process claims and must provide missing-information prompts.

## Wenxin Standard Output

Path: `identity/wenxin/WENXIN_REPORT.md`

Passes only if it can fill these key sections or explicitly declares insufficiency:

- `standard_output_gate`
- `source_inventory`
- `一句话定位`
- `三段卖点`
- `我是谁`
- `我现在站在哪`
- `领域覆盖图`
- `完成度百分比`
- `Gap 分析`
- `三条未来路径`
- `公开定位 / public-positioning`
- `Skill 候选 / skill-candidates`
- `不能判断 / missing_information`

Minimum evidence for `sufficient`:

- At least 3 independent evidence items, or one dense first-party/self-authored corpus.
- Evidence covers identity/history, capability, representative outputs or decisions, and future direction.
- Skill candidates are backed by concrete work examples or repeated decision patterns.

## PSP Standard Output

Path: `identity/psp/<person_id>/PSP-<timestamp>.md`

Passes only if it can fill these key sections or explicitly declares insufficiency:

- `standard_output_gate`
- `scope_and_identity`
- `evidence_boundary`
- `stable_facts`
- `person_model`
- `judgment_model`
- `behavior_boundaries`
- `communication_model` if evidence exists; otherwise mark unavailable
- `confidence_by_section`
- `validation_examples`
- `anti_claims / do_not_infer`
- `missing_information`

Minimum evidence for `sufficient`:

- Enough behavior or decision samples to infer recurring judgment patterns.
- Enough source diversity to distinguish facts from third-party interpretation.
- At least 3 validation examples or counterexamples for how the model should and should not answer.

## IPO Reverse Standard Output

Path: `identity/ipo-reverse/<artifact_id>.md` or `memory/working-lessons/<artifact_id>-ipo.md`

Passes only if it can fill these key sections or explicitly declares insufficiency:

- `standard_output_gate`
- `finished_output_reference`
- `artifact_evidence_map`
- `hidden_cognitive_tasks`
- `methodology_selection`
- `middle_layer_artifacts`
- `process_chain`
- `final_IPO`
- `forward_reconstruction_check`
- `counterfactual_or_step_deletion_check`
- `assumptions_and_evidence_ledger`
- `downstream_usage`
- `missing_information`

Minimum evidence for `sufficient`:

- A finished output exists and is available for inspection.
- The output contains enough structure, decisions, or traces to infer process.
- High-impact unknowns are either answered or explicitly marked as assumptions with targeted prompts.

## Final Response Requirement

When generating or updating any of these artifacts, the agent's final response must state:

- Which standard artifacts were attempted.
- Which passed the standard output gate.
- Which failed due to insufficient evidence.
- The top missing information needed to pass.
