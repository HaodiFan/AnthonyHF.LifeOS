# Self-Evolution Output Standards

Generated: 2026-05-30
Owner: AnthonyHF

This file defines the minimum standard outputs for Wenxin, PSP, Soul, Design, and IPO Reverse.

The rule is simple:

- If the provided evidence is sufficient to fill the key fields, the artifact may pass.
- If the evidence is insufficient, the artifact must explicitly fail the sufficiency gate and list the missing information or targeted follow-up questions.
- A file that only contains generic summary text must not pass.

## Shared Gate

Every Wenxin, PSP, Soul, Design, and IPO Reverse artifact must include:

```yaml
standard_output_gate:
  artifact_type: wenxin | psp | soul | design | ipo-reverse
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

## Active Artifact Rule

Wenxin, PSP, Soul, and Design are cumulative artifacts, not one-off overwritten reports.

- Global latest registry: `artifacts/current.yml`.
- Global active identity registry: `identity/current.yml`.
- Wenxin current entrypoint: `identity/wenxin/WENXIN_REPORT.md`.
- Wenxin versioned artifacts: `identity/wenxin/WENXIN-<timestamp>.md`.
- PSP current entrypoint: `identity/psp/<person_id>/PSP.md`.
- PSP versioned artifacts: `identity/psp/<person_id>/PSP-<timestamp>.md`.
- Soul current entrypoint: `SOUL.md`.
- Soul versioned artifacts: `identity/psp/<person_id>/SOUL-<timestamp>.md`.
- Design current entrypoint: `DESIGN.md`.
- Design versioned artifacts: `design/DESIGN-<timestamp>.md`.

Update sequence:

1. Read `artifacts/current.yml`, `identity/current.yml` if identity-related, and the relevant `versions.yml`.
2. Generate the new timestamped artifact from the current active artifact plus approved new evidence.
3. Update the human-readable current entrypoint.
4. Update `versions.yml`, `changelog.md`, local PSP `current.yml` when applicable, global `identity/current.yml` when identity-related, and `artifacts/current.yml`.
5. Regenerate runtime projections so `profile.manifest.yml` records the active source artifacts used.

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
- Candidate Skill recommendations are backed by concrete work examples or repeated decision patterns.
- Each Skill candidate must satisfy one eligibility gate:
  - `top_5_percent_capability_hypothesis`: evidence suggests Anthony may be in the global top 5% or a clear high-percentile group for this capability.
  - `repeated_workflow`: evidence shows Anthony repeatedly performs this work and stable inputs, process, outputs, and acceptance criteria can be extracted.
- Do not recommend Skills merely because AnthonyHF.LifeOS has a self-evolution tool installed, the domain sounds useful, a one-off project exists, or the candidate is aspirational.

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

## Soul Standard Output

Path: `SOUL.md` and `identity/psp/<person_id>/SOUL-<timestamp>.md`

Passes only if it can fill these key sections or explicitly declares insufficiency:

- `standard_output_gate`
- `scope`
- `source_evidence`
- `operating_principles`
- `behavior_boundaries`
- `best_state_or_alignment_rules`
- `runtime_translation_boundary`
- `do_not_infer`
- `missing_information`

Minimum evidence for `sufficient`:

- Active PSP exists and has enough evidence-backed judgment patterns.
- Soul statements are derived from PSP or approved memory/skill evidence, not from runtime behavior alone.
- Runtime boundaries are explicit: Soul is an operating layer, not the PSP source or a production impersonation prompt.

## Design Standard Output

Path: `DESIGN.md` and `design/DESIGN-<timestamp>.md`

Passes only if it can fill these key sections or explicitly declares insufficiency:

- `standard_output_gate`
- `scope`
- `source_evidence`
- `expression_preferences`
- `visual_preferences`
- `product_surface_preferences`
- `narrative_rhythm`
- `anti_preferences`
- `local_override_policy`
- `missing_information`

Minimum evidence for `sufficient`:

- Owner-approved examples or counterexamples exist across more than one output surface.
- Global preferences are separated from local project design requirements.
- Private inspiration material is either excluded or summarized through an approved evidence note.

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
