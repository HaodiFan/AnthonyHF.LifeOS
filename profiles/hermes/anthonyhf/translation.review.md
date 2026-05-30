# Translation Review Proposal

Translation ID: `anthonyhf-hermes-20260530-223832`
Target runtime: `hermes`
Target profile: `/Users/anthonyf/projects/metainflow/openLifeOS/output/meta/AnthonyHF.LifeOS/profiles/hermes/anthonyhf`

This file is a proposal surface for SKILL.md-guided semantic tuning. It must not be applied automatically.

## Tuning Policy

- Mode: `proposal_only`.
- The deterministic script output is the baseline.
- A Skill or agent may propose edits to runtime projection files, but must not overwrite canonical LifeOS files.
- Manual confirmation or an explicit apply command is required before proposed changes are applied.

## Immutable Fields

- `profile.manifest.yml` source paths, rules, validation results, and timestamps.
- `coverage-report.yml` coverage status and generated audit categories.
- Secret scan and private body scan results.
- Canonical LifeOS identity, memory, skill, security, and integration files.

## Allowed Proposal Areas

- Runtime voice and structure in `SOUL.md`.
- Behavior-rule organization in `AGENTS.md` or `PROFILE.md`.
- Summary ordering in `USER.md` or `memories/seed.md`.
- Adapter backlog notes for partial or unsupported coverage.

## Suggested Review Items

### SOUL.md

- Status: `present`
- Source evidence: `identity/psp/*/PSP-*.md`
- Suggested change: Review Runtime voice, section order, boundary wording, and clarity of source limitations.
- Reason: Improve runtime fit without changing the LifeOS source of truth.
- Risk: May overfit runtime phrasing or weaken evidence boundaries if applied without review.
- Coverage impact: Advisory only; update adapter backlog if a feature remains partial or unsupported.

### PROFILE.md

- Status: `present`
- Source evidence: `identity/wenxin/WENXIN_REPORT.md and skills/meta/`
- Suggested change: Review Profile narrative, profile-level guidance, and meta-skill readability.
- Reason: Improve runtime fit without changing the LifeOS source of truth.
- Risk: May overfit runtime phrasing or weaken evidence boundaries if applied without review.
- Coverage impact: Advisory only; update adapter backlog if a feature remains partial or unsupported.

### config.yaml

- Status: `present`
- Source evidence: `security/permissions.yml, integrations/data-sources.yml, and skill bindings`
- Suggested change: Review Config comments, connector hints, and policy visibility.
- Reason: Improve runtime fit without changing the LifeOS source of truth.
- Risk: May overfit runtime phrasing or weaken evidence boundaries if applied without review.
- Coverage impact: Advisory only; update adapter backlog if a feature remains partial or unsupported.

### memories/seed.md

- Status: `present`
- Source evidence: `memory/long-term/ and memory/distilled-knowledge/`
- Suggested change: Review Stable fact ordering, preference grouping, and claim readability.
- Reason: Improve runtime fit without changing the LifeOS source of truth.
- Risk: May overfit runtime phrasing or weaken evidence boundaries if applied without review.
- Coverage impact: Advisory only; update adapter backlog if a feature remains partial or unsupported.

## Proposal Patch

No patch has been applied. Add human-reviewed diff notes here if runtime files need tuning.
