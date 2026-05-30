# Platform Migration Instructions

This document defines how AnthonyHF.LifeOS should be migrated, projected, or adapted across platforms without losing source-of-truth boundaries.

## Core Rule

AnthonyHF.LifeOS is the canonical source of truth. Other platforms receive projections, adapters, summaries, or review proposals. They do not become the canonical identity, memory, or skill source.

```text
LifeOS canonical source
  -> deterministic projection or evidence intake
  -> platform-specific review
  -> confirmed platform package
  -> feedback returns as lesson evidence
```

Never copy raw private bodies, secrets, customer material, Feishu/Miaoji transcripts, full AF-wiki private notes, or unreviewed working lessons into a platform package.

## Migration Intake Protocol

Use this protocol before any platform-specific migration:

1. Identify the platform target: `lifeos`, `openclaw`, `hermes`, `codex-skill`, `af-wiki`, `github-pages`, or `local-evidence-source`.
2. Read `DELIVERY.md` to confirm which architecture target is being updated.
3. Read `cognition/object-taxonomy.yml`, `cognition/data-contracts.yml`, and `security/README.md`.
4. Classify each source as identity, memory, skill, integration, public surface, evidence, or raw/private material.
5. Write only the platform-safe projection, index, or proposal.
6. Update provenance and coverage notes.
7. If runtime behavior changes, record feedback as lesson evidence before modifying canonical LifeOS files.

## Target: openLifeOS / LifeOS

Use when importing new evidence, updating AnthonyHF identity, improving memory routing, promoting skills, or evolving the canonical LifeOS repo.

Source:

- `identity/`
- `memory/`
- `skills/`
- `cognition/`
- `integrations/`
- `security/`
- approved evidence pointers

Write targets:

- Public identity: `identity/public-profile/profile.yml`
- Wenxin output: `identity/wenxin/`
- PSP/person model: `identity/psp/anthony-fan/`
- Memory pointers and tiers: `memory/`
- Runtime skill candidates: `skills/runtime/`
- Distilled meta skills: `skills/meta/`
- Skill bindings: `skills/bindings/`
- Evidence maturity: `docs/evidence-sufficiency.md`

Rules:

- Raw source stays in the original system or local/private evidence source.
- Update `docs/evidence-sufficiency.md` whenever evidence maturity changes.
- Do not mark LifeOS complete unless evidence maturity reaches `research-grade` or `avatar-grade`.

## Target: OpenClaw

Use when AnthonyHF.LifeOS must become an OpenClaw agent workspace.

Command:

```bash
python3 scripts/translate_lifeos.py output/meta/AnthonyHF.LifeOS \
  --runtime openclaw \
  --profile-id anthonyhf \
  --force \
  --emit-review
```

Output:

- `profiles/openclaw/anthonyhf/SOUL.md`
- `profiles/openclaw/anthonyhf/IDENTITY.md`
- `profiles/openclaw/anthonyhf/USER.md`
- `profiles/openclaw/anthonyhf/AGENTS.md`
- `profiles/openclaw/anthonyhf/TOOLS.md`
- `profiles/openclaw/anthonyhf/skills/<skill>/SKILL.md`
- `profiles/openclaw/anthonyhf/skills/_source-links/`
- `profiles/openclaw/anthonyhf/profile.manifest.yml`
- `profiles/openclaw/anthonyhf/coverage-report.yml`
- `profiles/openclaw/anthonyhf/translation.review.md`

Review focus:

- `IDENTITY.md`: must fill the OpenClaw `IDENTITY.md` template fields (`Name`, `Creature`, `Vibe`, `Emoji`, `Avatar`) instead of dumping a generic identity summary.
- `SOUL.md`: runtime voice, source limitation wording, person-model boundaries.
- `AGENTS.md`: workspace behavior rules, skill promotion gates, security language.
- `USER.md`: stable fact ordering, memory summary readability.
- `TOOLS.md`: connector assumptions, unavailable tool notes.
- `skills/`: OpenClaw-discoverable wrapper skills must exist as real `SKILL.md` files under the workspace `skills/` directory. Symlinks are advisory only because sandboxed workspace copies may ignore links that resolve outside the workspace.

Do not:

- Put raw evidence into prompt files.
- Treat `translation.review.md` as applied changes.
- Edit manifest provenance, coverage status, or validation results by hand.
- Rely only on symlinks for OpenClaw skill loading.

## Target: Hermes

Use when AnthonyHF.LifeOS must become a Hermes profile.

Command:

```bash
python3 scripts/translate_lifeos.py output/meta/AnthonyHF.LifeOS \
  --runtime hermes \
  --profile-id anthonyhf \
  --force \
  --emit-review
```

Output:

- `profiles/hermes/anthonyhf/SOUL.md`
- `profiles/hermes/anthonyhf/PROFILE.md`
- `profiles/hermes/anthonyhf/config.yaml`
- `profiles/hermes/anthonyhf/memories/seed.md`
- `profiles/hermes/anthonyhf/profile.manifest.yml`
- `profiles/hermes/anthonyhf/coverage-report.yml`
- `profiles/hermes/anthonyhf/translation.review.md`

Review focus:

- `PROFILE.md`: profile consumability, role clarity, public-safe claims.
- `memories/seed.md`: ordering, provenance disclaimers, over-claiming risk.
- `config.yaml`: connector hints and runtime assumptions.
- `SOUL.md`: behavior boundary and maturity disclosure.

Do not:

- Promote unreviewed working lessons into Hermes memory.
- Treat Hermes memory as the canonical memory source.
- Rewrite LifeOS identity from Hermes feedback without owner-aligned evidence review.

## Target: Codex Skill

Use when a reusable AnthonyHF capability should become an installable Codex Skill.

Source:

- Mature repeated workflow from `skills/runtime/` or `skills/meta/`
- Evidence from completed tasks or IPO Reverse
- Owner alignment

Write target:

- A separate skill package, not the LifeOS root.
- The skill package must include its own `SKILL.md`.
- LifeOS should keep a binding or pointer in `skills/bindings/` or `matrix.yml`.

Rules:

- Do not put Anthony-specific private facts into a reusable Codex Skill.
- Put facts in memory or source bindings; put reusable procedure in the Skill.
- If the skill depends on AnthonyHF context, declare that dependency explicitly.

## Target: AF-wiki / Memory Wiki

Use when migrating long-term work, life, knowledge, project, or area context.

Write targets:

- AF-wiki or configured memory authority for private/long-term content.
- `memory/START-HERE.md` and `memory/wiki-repo.yml` for routing.
- `memory/long-term/` only for public-safe summaries or pointers.
- `memory/distilled-knowledge/` only for approved distilled knowledge.

Rules:

- AF-wiki remains the memory authority.
- Do not copy private AF-wiki bodies into this public repo.
- Use source IDs, area indexes, and summaries instead of raw bodies.

## Target: GitHub Pages / Homepage

Use when updating the public human-facing website.

Write target:

- `apps/homepage/`

Build check:

```bash
cd output/meta/AnthonyHF.LifeOS/apps/homepage
npm ci
npm run build
rm -rf node_modules
```

Rules:

- Homepage is a public surface, not identity truth.
- It may summarize `README.md`, `SKILL.md`, `matrix.yml`, and approved public assets.
- It must point back to LifeOS canonical files for claims.
- Do not put private evidence, raw memory, or unapproved identity claims into frontend assets.

## Target: Local Evidence Source / External Drive

Use when importing material from a local disk, export folder, archive, or backup drive.

First action:

- Create an inventory only. Do not copy files into LifeOS.

Use the factory intake script when available:

```bash
python3 scripts/intake_external_drive.py /Volumes/<drive-name> \
  --private-out ~/LifeOS_Intake/AnthonyHF/external-drive \
  --lifeos-repo output/meta/AnthonyHF.LifeOS \
  --source-id external-drive-<drive-name>-<yyyymmdd> \
  --owner AnthonyHF \
  --force
```

The script writes raw paths only to the private local intake directory and writes a public-safe summary to `docs/evidence-intake/`.

Manual fallback private workspace:

```bash
mkdir -p ~/LifeOS_Intake/AnthonyHF/external-drive
find "/Volumes/<drive-name>" -type f \
  -not -path "*/.Trashes/*" \
  -not -path "*/.Spotlight-V100/*" \
  -not -path "*/.fseventsd/*" \
  -print > ~/LifeOS_Intake/AnthonyHF/external-drive/file-list.txt
```

Then classify files into:

- public identity evidence
- project output for Wenxin capability and field-position evidence
- Anthony-authored writing,感悟, reflection, correction, conflict story, or judgment sample for PSP evidence
- skill evidence
- long-term memory pointer
- aesthetics/design preference
- raw private material
- banned material

Allowed LifeOS outputs:

- `docs/evidence-sufficiency.md` maturity update
- `docs/evidence-intake/` public-safe inventory and next-pass queue
- `identity/wenxin/` project-backed capability map, field position, gap analysis, and public-safe synthesis
- `identity/psp/anthony-fan/` abstracted patterns and boundaries from Anthony-authored writing,感悟, reflection, correction, or judgment samples
- `skills/recommendations/skill-roadmap.yml`
- `memory/` pointers or summaries

Do not:

- Copy the external drive into the repo.
- Commit file bodies from private archives.
- Scan or summarize private content before owner approves the category.
- Process secrets, financial records, ID documents, customer data, or raw private chats into public files.

## Migration Verification Checklist

Before calling a migration done:

- `profile.manifest.yml` exists for runtime projections.
- `coverage-report.yml` lists supported, partial, unsupported, and intentionally excluded areas.
- `translation.review.md` exists when SKILL-guided review is requested.
- `docs/evidence-sufficiency.md` reflects the new evidence level.
- No raw private body has entered the public repo.
- Secret scan and avatar validation pass.

Commands:

```bash
python3 scripts/validate_avatar_repo.py output/meta/AnthonyHF.LifeOS
python3 scripts/openlifeos_progress.py output/meta/AnthonyHF.LifeOS --json
```
