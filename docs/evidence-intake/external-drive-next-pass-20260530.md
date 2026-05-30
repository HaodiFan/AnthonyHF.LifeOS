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

First metadata read:

- `docs/evidence-intake/external-drive-project-first-read-20260530.md`

## Routing Correction

Anthony's alignment rule:

- Projects and delivered systems should first feed Wenxin: use them to answer "who I am", "where I stand", "how complete I am in my field", and "where I should go next".
- IPO Reverse is the analysis method for project evidence, not the final destination.
- Personal writing, reflections,感悟, corrections, conflict stories, and judgment samples should feed PSP/person model.
- Skills receive distilled reusable procedures only after the Wenxin/IPO/PSP routing decision is clear.

## Pass 1: Project Evidence For Wenxin

Goal: choose 10-20 project outputs that best reveal AnthonyHF's domain position, capability map, field completeness, gaps, and future path.

Method: run IPO Reverse on each selected project, then summarize the result into Wenxin and skill evidence. Do not treat project output as PSP evidence unless it contains an explicit personal reflection or decision sample.

Public-safe candidate clusters:

| Cluster | Likely LifeOS Use | Suggested Target |
| --- | --- | --- |
| AI data QA / dataset quality tooling | field capability, delivery scope, validation maturity | `identity/wenxin/`, `identity/wenxin/skill-recommendations.yml` |
| Web agent / browser environment / RL environment tooling | frontier direction, agent/data infrastructure ability | `identity/wenxin/`, `identity/wenxin/skill-recommendations.yml` proposal |
| Computer-use data pipeline and annotation workflow | data production operating model, AI data workflow position | `identity/wenxin/`, IPO Reverse note |
| PII / privacy / compliance data pipeline | privacy-aware data engineering capability | `identity/wenxin/`, `security/README.md` |
| Dataset acquisition / mining / crawler projects | data source strategy, acquisition workflow | `identity/wenxin/`, `identity/wenxin/skill-recommendations.yml` proposal |
| Public homepage / product presentation surfaces | public narrative and productization evidence | `identity/wenxin/`, `apps/homepage/` if public-safe |
| OCR / book / academic data extraction projects | unstructured data processing capability | `identity/wenxin/`, `identity/wenxin/skill-recommendations.yml` |
| Marketplace / data product experiments | productization and GTM direction | `identity/wenxin/`, `memory/working-lessons/` |

Rules:

- Read only selected project metadata first: README, package metadata, public docs, commit-independent file tree.
- Do not copy source code into LifeOS.
- If code inspection is needed, summarize design and evidence, not implementation body.
- Any customer-specific detail must be redacted or converted into a non-identifying Wenxin capability signal.

## Pass 2: Writing And Reflection Evidence For PSP

Goal: identify Anthony's own writing,感悟, retrospectives, corrections, conflict stories, and judgment samples that can improve the PSP/person model.

Allowed after owner selection:

- Personal essays, notes, reflections, self-review, work/life感悟.
- Redacted decision records and correction examples.
- Redacted conflict or disagreement reviews.
- Owner-authored principles, rules, and judgment samples.

Forbidden without explicit approval:

- contracts, customer materials, Feishu/Lark exports, financial records, raw private chats, meeting transcripts, identity documents, tokens, credentials, dataset bodies, source repository bodies.
- Language fingerprint extraction from private chats.
- Stable personality claims without evidence.

Suggested targets:

- `identity/psp/anthony-fan/PSP.md`
- `identity/psp/anthony-fan/update-log-*.md`
- `memory/working-lessons/` for provisional lessons before promotion

## Pass 3: Public Narrative / Profile Evidence

Goal: identify public-safe biography, product narrative, talks, homepage assets, and profile material.

Allowed after owner selection:

- Personal public bio or self-introduction.
- Public talks, public product pages, public README material.
- Approved case summaries with customer and private details removed.
- Approved portfolio screenshots or homepage assets.

Forbidden:

- raw private evidence;
- private relationship or customer details;
- public claims not backed by approved evidence.

Suggested targets:

- `identity/public-profile/profile.yml`
- `identity/wenxin/WENXIN_REPORT.md`
- `identity/wenxin/public-positioning.md`
- `apps/homepage/` only for owner-approved public assets

## Pass 4: Runtime Projection Refresh

After any canonical LifeOS update, regenerate runtime projections:

```bash
python3 scripts/translate_lifeos.py output/meta/AnthonyHF.LifeOS --runtime openclaw --profile-id anthonyhf --force --emit-review
python3 scripts/translate_lifeos.py output/meta/AnthonyHF.LifeOS --runtime hermes --profile-id anthonyhf --force --emit-review
```

Check that OpenClaw receives real `skills/*/SKILL.md` adapters and that Hermes receives only public-safe seed memory.

## Owner Selection Needed

Before reading bodies, Anthony should pick one of these routes:

1. `wenxin-project-first`: process 10-20 project roots into Wenxin capability/positioning evidence.
2. `psp-writing-first`: process owner-approved writing,感悟, retrospectives, and judgment samples into PSP evidence.
3. `identity-public-first`: process only public-safe identity/profile documents.
4. `runtime-first`: improve OpenClaw/Hermes projection quality without reading more private evidence.

Default recommended route: `wenxin-project-first`, because projects reveal field position and capability map while minimizing exposure of personal writing.
