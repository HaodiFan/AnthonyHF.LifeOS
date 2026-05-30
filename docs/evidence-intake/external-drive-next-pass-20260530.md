# External Drive Next Pass Queue

Date: 2026-05-30
Source ID: `external-drive-afelite-20260530`
Status: `owner_selection_required`
Visibility: `public-safe-plan`

## Purpose

This file turns the local AFElite inventory into an executable LifeOS alignment queue without exposing private file paths or raw bodies in the public repo.

Concrete candidate paths remain local-only in:

- `~/LifeOS_Intake/AnthonyHF/external-drive/project-root-candidates.txt`
- `~/LifeOS_Intake/AnthonyHF/external-drive/document-candidates.txt`
- `~/LifeOS_Intake/AnthonyHF/external-drive/sensitive-document-candidates.txt`

## Current Inventory Signal

- Filtered files: 239,048
- Project root candidates: 143
- Document candidates: 38,142
- Sensitive document candidates: 13,977

This is enough to start selective synthesis, but not enough to raise content maturity by itself.

## Pass 1: Project Evidence For IPO Reverse

Goal: choose 10-20 project outputs that best reveal AnthonyHF's reusable engineering judgment, product judgment, data/AI workflow design, and delivery patterns.

Public-safe candidate clusters:

| Cluster | Likely LifeOS Use | Suggested Target |
| --- | --- | --- |
| AI data QA / dataset quality tooling | project delivery evidence, validation pattern, workflow design | `skills/recommendations/skill-roadmap.yml`, `memory/working-lessons/` |
| Web agent / browser environment / RL environment tooling | agent workflow evidence, evaluation harness pattern | `skills/runtime/`, `skills/meta/` proposal |
| Computer-use data pipeline and annotation workflow | data production operating model, QA loop | `memory/working-lessons/`, IPO Reverse note |
| PII / privacy / compliance data pipeline | privacy-aware data engineering pattern | `security/README.md`, `skills/meta/` proposal |
| Dataset acquisition / mining / crawler projects | data source strategy, acquisition workflow | `skills/runtime/` proposal |
| Public homepage / product presentation surfaces | public narrative and presentation system evidence | `identity/wenxin/`, `skills/runtime/` proposal |
| OCR / book / academic data extraction projects | unstructured data processing pattern | `skills/recommendations/skill-roadmap.yml` |
| Marketplace / data product experiments | productization and GTM evidence | `identity/wenxin/`, `memory/working-lessons/` |

Rules:

- Read only selected project metadata first: README, package metadata, public docs, commit-independent file tree.
- Do not copy source code into LifeOS.
- If code inspection is needed, summarize design and evidence, not implementation body.
- Any customer-specific detail must be redacted or converted into a non-identifying pattern.

## Pass 2: Public Identity / Wenxin Evidence

Goal: identify public-safe documents that can improve the public profile, Wenxin summary, and homepage narrative.

Allowed after owner selection:

- Personal public bio or self-introduction.
- Public talks, public product pages, public README material.
- Approved case summaries with customer and private details removed.
- Approved portfolio screenshots or homepage assets.

Forbidden without explicit approval:

- contracts, customer materials, Feishu/Lark exports, financial records, raw private chats, meeting transcripts, identity documents, tokens, credentials, dataset bodies, source repository bodies.

Suggested targets:

- `identity/public-profile/profile.yml`
- `identity/wenxin/WENXIN_REPORT.md`
- `identity/wenxin/public-positioning.md`
- `apps/homepage/` only for owner-approved public assets

## Pass 3: PSP / Behavior Pattern Evidence

Goal: improve the person model only from approved behavior or judgment samples.

Allowed after owner selection:

- Abstracted decision cases.
- Redacted conflict or correction examples.
- Repeated judgment patterns with evidence pointers.
- Validation samples written specifically for PSP review.

Forbidden:

- language fingerprint extraction from private chats;
- raw transcripts;
- private relationship or customer details;
- claims not backed by evidence.

Suggested targets:

- `identity/psp/anthony-fan/PSP.md`
- `identity/psp/anthony-fan/update-log-*.md`
- `memory/working-lessons/` for provisional lessons before promotion

## Pass 4: Runtime Projection Refresh

After any canonical LifeOS update, regenerate runtime projections:

```bash
python3 scripts/translate_lifeos.py output/meta/AnthonyHF.LifeOS --runtime openclaw --profile-id anthonyhf --force --emit-review
python3 scripts/translate_lifeos.py output/meta/AnthonyHF.LifeOS --runtime hermes --profile-id anthonyhf --force --emit-review
```

Check that OpenClaw receives real `skills/*/SKILL.md` adapters and that Hermes receives only public-safe seed memory.

## Owner Selection Needed

Before reading bodies, Anthony should pick one of these routes:

1. `project-first`: process 10-20 project roots for IPO Reverse and skill evidence.
2. `identity-first`: process only public-safe identity/profile documents.
3. `psp-first`: process owner-approved behavior/judgment samples.
4. `runtime-first`: improve OpenClaw/Hermes projection quality without reading more private evidence.

Default recommended route: `project-first`, because it improves skills and delivery evidence while minimizing exposure of personal documents.
