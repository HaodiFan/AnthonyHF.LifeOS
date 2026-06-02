# Delivery Architecture

Current delivery: `AnthonyHF.LifeOS`

This repo is delivered as a multi-architecture openLifeOS showroom. The LifeOS folder is the canonical source of truth; runtime profiles and homepage assets are projections or presentation surfaces.

Global lifecycle flag: `LIFEOS_STATUS.yml`

## Lifecycle State

Current lifecycle: `development`

| Version Slot | Value | Meaning |
| --- | --- | --- |
| Upload version | `anthonyhf-lifeos-upload-20260531` | Working-source version. Meta skills may be submodules/editable sources and can be uploaded upstream. |
| Delivery version | `anthonyhf-lifeos-delivery-unreleased` | Consumable release version. Meta skills should be resolved from latest approved release archives before publishing as delivery. |

Development state is for authoring and iteration. In this state, meta skills such as Engineering Everything may exist as submodules or editable working sources.

Delivery state is for consumers. In this state, meta skills should be downloaded from latest approved releases as ordinary vendored directories with source manifests.

## Architecture Targets

| Target | Status | Path | Role |
| --- | --- | --- | --- |
| `lifeos` | canonical | `/` | Identity, memories, capabilities, runtime, cognition contracts, integrations, security, and evidence gates. |
| `openclaw` | generated projection | `runtime/profiles/openclaw/anthonyhf/` | OpenClaw agent workspace projection generated from LifeOS artifacts. |
| `hermes` | generated projection | `runtime/profiles/hermes/anthonyhf/` | Hermes profile projection generated from LifeOS artifacts. |
| `homepage` | public surface | `work/apps/homepage/` | Vite/React public presentation surface; not a source of identity truth. |

## Source Of Truth

- Identity truth: `identity/`
- Memory truth and pointers: `identity/memories/`, configured external memory wiki, `runtime/memory/`, and `capabilities/*/memory/`
- Stable capability truth and promotion surfaces: `capabilities/`
- Runtime skill bindings and evidence: `runtime/runtime-skills/`, `runtime/runtime-lessons/`, and `runtime/sessions/`
- Self-evolution production systems: `evolution/organ-systems/`
- Runtime projections: `runtime/profiles/`
- Public presentation app: `work/apps/homepage/`

## Delivery Rules

- Runtime profiles are generated projections, not canonical identity or memory.
- Homepage content should point back to canonical LifeOS files instead of becoming a second truth source.
- OpenClaw and Hermes profiles must keep `profile.manifest.yml`, `coverage-report.yml`, and `translation.review.md`.
- Any runtime feedback must return as lesson evidence before changing LifeOS identity, memory, runtime skills, or capabilities.
