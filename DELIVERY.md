# Delivery Architecture

Current delivery: `AnthonyHF.LifeOS`

This repo is delivered as a multi-architecture openLifeOS showroom. The LifeOS folder is the canonical source of truth; runtime profiles and homepage assets are projections or presentation surfaces.

## Architecture Targets

| Target | Status | Path | Role |
| --- | --- | --- | --- |
| `lifeos` | canonical | `/` | Identity, memory, skills, cognition contracts, integrations, security, and evidence gates. |
| `openclaw` | generated projection | `profiles/openclaw/anthonyhf/` | OpenClaw agent workspace projection generated from LifeOS artifacts. |
| `hermes` | generated projection | `profiles/hermes/anthonyhf/` | Hermes profile projection generated from LifeOS artifacts. |
| `homepage` | public surface | `apps/homepage/` | Vite/React public presentation surface; not a source of identity truth. |

## Source Of Truth

- Identity truth: `identity/`
- Memory truth and pointers: `memory/`
- Skill truth and promotion surfaces: `skills/`
- Runtime projections: `profiles/`
- Public presentation app: `apps/homepage/`

## Delivery Rules

- Runtime profiles are generated projections, not canonical identity or memory.
- Homepage content should point back to canonical LifeOS files instead of becoming a second truth source.
- OpenClaw and Hermes profiles must keep `profile.manifest.yml`, `coverage-report.yml`, and `translation.review.md`.
- Any runtime feedback must return as lesson evidence before changing LifeOS identity, memory, or skills.

