# Avatar Page Information Architecture

Generated: 2026-06-02

This document defines what a concrete digital-avatar page should explain from a third-person point of view.

The reference screenshot shows a practical agent-builder structure:

- `人设`: who the agent is, what it does, how it behaves.
- `记忆`: what context it can remember or retrieve.
- `工作身份`: what role it acts under.
- `工具 / MCP / 技能`: what it can call.
- `运行日志 / 用户反馈 / 版本历史 / 使用分析`: how it runs, evolves, and is governed.

openLifeOS should expose the same ideas, but with stronger evidence, lifecycle, and truth-source boundaries.

## Page Principle

An avatar page should not be a biography page and should not be a prompt editor.

It should answer, in third person:

1. Who is this digital person?
2. What can this digital person reliably do?
3. How does this digital person decide and behave?
4. What evidence supports those claims?
5. What memory, tools, and runtime surfaces does it use?
6. What has it produced recently?
7. How mature is it, and what is still missing?

## Common Versus Case-Specific

The common digital-person page model defines dimensions, not fixed role names.

Common dimensions:

- identity card: how to identify this digital person quickly.
- public identity: what verified public or owner-approved identity exists.
- person model: how it thinks, decides, communicates, and refuses unsupported claims.
- scene identity: under which evidence-backed context it can represent or act.
- capabilities: what it can reliably do and what is only a candidate.
- memory and evidence: what it knows, where evidence lives, and what is unavailable.
- runtime activity: what has happened recently in sessions, logs, feedback, and lessons.
- work and outputs: what it has produced or can safely point to.
- evolution: how it updates, promotes lessons, and changes versions.
- governance: what it must not do and what requires owner confirmation.

Case-specific outputs:

- Scene identity names under `identities/`.
- Capability names under `capabilities/`.
- Work output categories under `work/`.
- Runtime skill names under `runtime/runtime-skills/`.

These names must be generated from the person's own materials and evidence. They are not shared schema requirements.

## Recommended Page Layers

| Layer | Page Question | User-Facing Content | openLifeOS Source | Current AnthonyHF Status |
| --- | --- | --- | --- | --- |
| L0 Identity Card | Who is this avatar at a glance? | Name, one-line, current operating context, maturity badge, public boundary. | `identity/avatar-description/current.yml`, `identity/public-profile/profile.yml`, `artifacts/current.yml` | Available, evidence partial. |
| L1 Public Identity | What is the real/public identity behind the avatar? | Public positioning, story, domain, career line, known constraints. | `identity/wenxin/`, `identity/current.yml`, `identity/public-profile/` | Available, but Wenxin is evidence-limited. |
| L2 Person Model | How does it think, judge, and communicate? | Judgment model, operating principles, communication mode, anti-claims. | `identity/psp/<person_id>/`, `SOUL.md`, `identity/soul/` | Partial; PSP is v0.4 scaffold. |
| L3 Scene Identity | In which situations can it represent or speak for the owner? | Scene identities, what it can represent, what it cannot represent, and owner-confirmation rules. This layer is not a fixed role list. | `identities/`, `identity/wenxin/`, `identity/public-profile/`, `work/`, `security/` | Available as a scaffold; Anthony-specific scene identities should be derived from Wenxin/materials, not hard-coded into schema. |
| L4 Capabilities | What can it do reliably? | Stable capabilities, runtime skill bindings, promotion status, examples. | `capabilities/`, `runtime/runtime-skills/`, `identity/wenxin/skill-recommendations.yml` | Stable: Engineering Everything and Public Narrative System; runtime sample: snapAF. |
| L5 Memory And Evidence | What does it know, and where does evidence live? | Memory tiers, allowed sources, evidence sufficiency, source boundary, missing evidence. | `identity/memories/`, `runtime/memory/`, `capabilities/*/memory/`, `metabolism/`, `docs/evidence-sufficiency.md` | Available as boundary and index; actual private memory is external. |
| L6 Runtime Activity | Is it alive? What has it done recently? | Sessions, runtime lessons, external runtime versions, logs, feedback, latest actions. | `runtime/sessions/`, `runtime/runtime-lessons/`, `runtime/profiles/` | Mostly scaffold; few concrete sessions. |
| L7 Work And Outputs | What has this avatar/person produced? | Projects, apps, reports, publications, homepage, public surfaces. | `work/`, `capabilities/*/references/`, external project repos | Homepage available; project/output index needs richer examples. |
| L8 Evolution | How does it improve? | IPO Reverse, alignment loops, mutations, version history, promotion gates. | `evolution/`, `docs/lifeos-content-review.md`, `docs/schema-trim-completion-audit.md` | Available as process; needs more run evidence. |
| L9 Governance | What can it not do? | Privacy rules, public/private boundary, approval requirements, unavailable claims. | `security/`, `integrations/data-sources.yml`, `identity/cognition/` | Available. |

## Page Shape

For a concrete avatar page, use three page depths:

| Depth | Purpose | Sections |
| --- | --- | --- |
| Overview | Fast third-person understanding. | L0 Identity Card, maturity, top capabilities, boundaries. |
| Profile | Explain why this avatar behaves this way. | L1 Public Identity, L2 Person Model, L3 Scene Identity, L5 Evidence. |
| Operations | Explain how it works and evolves. | L4 Capabilities, L6 Runtime Activity, L7 Work Outputs, L8 Evolution, L9 Governance. |

This avoids a flat page with too many cards. A human should first see "who/what/boundary", then inspect "thinking/evidence", then inspect "runtime/evolution".

## Third-Person Field Model

The page should use third-person language:

- "AnthonyHF is..." instead of "I am..."
- "This avatar can..." instead of "I can..."
- "Current evidence supports..." instead of "I know..."
- "Unavailable / not enough evidence..." instead of implying missing facts.

Recommended fields:

```yaml
avatar_page:
  identity_card:
    display_name:
    one_line:
    current_operating_context:
    maturity:
    public_boundary:
  public_identity:
    positioning:
    domain:
    career_line:
    visible_constraints:
  person_model:
    judgment_model:
    operating_principles:
    communication_mode:
    anti_claims:
  scene_identity:
    generated_scene_identities:
    representation_rules:
    owner_confirmation_required:
  capabilities:
    stable:
    runtime:
    candidates:
    promotion_gate:
  memory_and_evidence:
    memory_tiers:
    evidence_sources:
    evidence_sufficiency:
    missing_evidence:
  runtime_activity:
    sessions:
    lessons:
    profiles:
    feedback:
  work_outputs:
    apps:
    reports:
    projects:
    publications:
  evolution:
    organ_systems:
    ipo:
    alignment:
    versions:
  governance:
    security_boundary:
    data_sources:
    prohibited_claims:
```

## AnthonyHF Current Output Coverage

| Page Area | Can openLifeOS Produce Now? | Current Source | Missing / Weak |
| --- | --- | --- | --- |
| Identity card | Yes | `identity/avatar-description/current.yml` | Evidence remains partial. |
| Public identity | Yes | `identity/wenxin/WENXIN_REPORT.html`, `identity/public-profile/profile.yml` | Wenxin needs richer structured extraction. |
| Person model | Partial | `identity/psp/anthony-fan/PSP.html`, `SOUL.md` | PSP needs more validation examples and confidence by section. |
| Scene identity | Partial | `identities/`, `identity/wenxin/`, `identity/public-profile/`, `work/`, `security/` | Needs a generator or schema for evidence-backed scene identities. Scene identity names must come from the specific person's evidence, not from common required pages. |
| Stable capabilities | Yes | `capabilities/engineering-everything/`, `capabilities/publication/public-narrative-system/` | Need examples and capability-level memory/evidence pages. |
| Runtime skills | Partial | `runtime/runtime-skills/snapaf/manifest.yml` | External repo is bound but not deeply inspected; more runtime runs needed. |
| Memory/evidence | Yes as boundary | `identity/memories/`, `metabolism/`, `docs/evidence-sufficiency.md` | Actual memory wiki content is external/private. |
| Runtime activity | Weak | `runtime/sessions/`, `runtime/runtime-lessons/`, `runtime/profiles/` | Session and lesson indexes exist but have little concrete activity evidence. |
| Work outputs | Partial | `work/apps/homepage/`, `work/index.md` | Need richer project/report/publication index. |
| Evolution | Yes as process | `evolution/`, `docs/lifeos-content-review.md` | Needs more completed IPO/alignment runs. |
| Governance | Yes | `security/`, `identity/cognition/`, `integrations/data-sources.yml` | Good enough for current public boundary. |

## Trim Implication

This page model clarifies why some files should not be merged:

- `identity/avatar-description/current.yml` is the short product-facing identity card.
- `README.md` is public repo introduction.
- `LIFEOS-CATALOG.html` is global filesystem catalog.
- `docs/layer-file-review.md` and `docs/file-role-inventory.yml` are structure audit artifacts.
- `identities/` is a variable scene-identity layer. It should not require fixed role pages; scene identity names only appear when a specific person's evidence supports them.
- A future concrete avatar page should consume these sources, not replace them.

The current missing piece is not another root Markdown entry. The missing piece is a structured avatar-page view model, generated from existing artifacts and explicitly marking unavailable sections.
