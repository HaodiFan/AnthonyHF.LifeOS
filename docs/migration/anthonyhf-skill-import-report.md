# AnthonyHF.Skill Import Report

Date: 2026-05-30
Source repo: `https://github.com/HaodiFan/AnthonyHF.Skill`
Target: `output/meta/AnthonyHF.LifeOS/`
Target repo name: `AnthonyHF.LifeOS`

## Summary

This output repo is the openLifeOS showroom instance derived from `HaodiFan/AnthonyHF.Skill`. The migration is additive: original homepage, assets, README, Skill routing, PSP, Wenxin artifact, package files, and public assets are preserved. openLifeOS protocol layers are added beside the original structure.

## Preserved Source Surfaces

- GitHub Pages / Vite / React homepage source moved from the original repo root into `apps/homepage/`, including `src/`, `components/`, `public/assets/`, `package.json`, `package-lock.json`, and `vite.config.ts`.
- Original root surfaces: `README.md`, `DESIGN.md`, `SKILL.md`, `matrix.yml`, `agents/openai.yaml`.
- Identity artifacts: `identity/wenxin/wenxin-report-continuous-founder-ascetic.pdf`, `identity/psp/anthony-fan/PSP.md`, PSP analysis and validation files.
- External skill/source pointers: `skills/engineering-everything`, `skills/self-evolution/psp`, `skills/self-evolution/wenxin`, `skills/self-evolution/ipo-reverse`, `skills/self-evolution/cognitive-alignment`.

## Added openLifeOS Layers

- Root delivery manifest: `DELIVERY.md`, declaring `lifeos`, `openclaw`, `hermes`, and `homepage` targets.
- Canonical root structure: root now keeps LifeOS identity, memory, skills, cognition, integrations, security, docs, and runtime projections.
- Public surface app: original Vite/React homepage is preserved under `apps/homepage/` so frontend dependencies and static assets do not compete with canonical LifeOS files at root.
- Cognition contracts: `cognition/object-taxonomy.yml`, `cognition/data-contracts.yml`.
- Memory tiers: `memory/working-lessons/`, `memory/long-term/`, `memory/distilled-knowledge/`.
- Skill taxonomy surfaces: `identity/wenxin/skill-recommendations.yml`, `identity/wenxin/skill-summaries/`, `cognition/skill-bindings/`, `integrations/skill-sources/default-skills/`.
- Integration contracts: `integrations/data-sources.yml`, `integrations/github.yml`, `integrations/feishu.yml`, `integrations/hermes.yml`.
- Evidence and output gates: `docs/evidence-sufficiency.md`, `docs/self-evolution-output-standards.md`.
- Runtime projections: `profiles/openclaw/anthonyhf/`, `profiles/hermes/anthonyhf/`.

## PSP Mirror

The original stable PSP entrypoint remains `identity/psp/anthony-fan/PSP.md`. A timestamped mirror exists at `identity/psp/anthony-fan/PSP-20260530-171725.md` so openLifeOS validation can find a versioned PSP artifact. Update `PSP.md` first, then refresh the timestamped mirror with provenance.

## Boundaries

- AF-wiki is AnthonyHF.LifeOS's configured memory wiki instance; it is not the openLifeOS default architecture.
- Feishu/Miaoji raw transcripts, private meeting links, customer details, source PDFs, tokens, and secrets are banned.
- Runtime profiles are projections, not sources of truth. Feedback returns as lesson evidence before changing canonical identity, memory, or skill files.

## Inventory

See `docs/migration/source-inventory.yml` for original tracked files, openLifeOS-added files, external source records, and private/external boundaries.

See `docs/migration/information-retention-audit-20260530.md` for the no-loss migration audit.

See `docs/migration/platform-migration-instructions.md` for LifeOS, OpenClaw, Hermes, Codex Skill, GitHub Pages, memory tiers, and local evidence source migration rules.
