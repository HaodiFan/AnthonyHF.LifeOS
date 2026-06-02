# Layer File Review

Generated: 2026-06-02

This review summarizes the file-level audit in `docs/file-role-inventory.yml`. It is an audit aid, not a truth source.

## Summary

- Total audited files: 329
- Unclassified current files: 0
- Files with duplicate policy: 39

## Layers

### root

- Files: 11
- Classes: root-entrypoint=11
- Representative files:
  - `.gitignore`: root control, human entrypoint, or machine-readable root index
  - `.gitmodules`: root control, human entrypoint, or machine-readable root index
  - `DELIVERY.md`: root control, human entrypoint, or machine-readable root index
  - `DESIGN.md`: root control, human entrypoint, or machine-readable root index
  - `LIFEOS-CATALOG.html`: root control, human entrypoint, or machine-readable root index
  - `LIFEOS_STATUS.yml`: root control, human entrypoint, or machine-readable root index
  - `README.md`: root control, human entrypoint, or machine-readable root index
  - `SKILL.md`: root control, human entrypoint, or machine-readable root index
  - `SOUL.md`: root control, human entrypoint, or machine-readable root index
  - `matrix.yml`: root control, human entrypoint, or machine-readable root index
  - `replicateme.yml`: root control, human entrypoint, or machine-readable root index

### artifacts

- Files: 2
- Classes: artifact-registry=2
- Representative files:
  - `artifacts/README.md`: latest/current artifact registry or artifact documentation
  - `artifacts/current.yml`: latest/current artifact registry or artifact documentation

### identity

- Files: 68
- Classes: identity-avatar-description=4, identity-cognition-contract=5, identity-design=4, identity-memory=4, identity-person-model=28, identity-public-profile=2, identity-soul=1, identity-support=2, identity-wenxin=18
- Representative files:
  - `identity/README.md`: identity layer index, registry, or support artifact
  - `identity/avatar-description/README.md`: product-facing avatar identity description and version ledger
  - `identity/avatar-description/changelog.md`: product-facing avatar identity description and version ledger
  - `identity/avatar-description/current.yml`: product-facing avatar identity description and version ledger
  - `identity/avatar-description/versions.yml`: product-facing avatar identity description and version ledger
  - `identity/cognition/README.md`: cognition object taxonomy, data contract, or source binding
  - `identity/cognition/data-contracts.yml`: cognition object taxonomy, data contract, or source binding
  - `identity/cognition/object-taxonomy.yml`: cognition object taxonomy, data contract, or source binding
  - `identity/cognition/skill-bindings/README.md`: cognition object taxonomy, data contract, or source binding
  - `identity/cognition/skill-bindings/data-sources.yml`: cognition object taxonomy, data contract, or source binding
  - `identity/current.yml`: identity layer index, registry, or support artifact
  - `identity/design/DESIGN-20260530-235550.md`: global design/aesthetic artifact and version ledger
  - ... see `docs/file-role-inventory.yml` for 56 more file entries.

### metabolism

- Files: 9
- Classes: metabolism-extracted=1, metabolism-inbox=2, metabolism-processing=6
- Representative files:
  - `metabolism/extracted/README.md`: digested/extracted material placeholder or index
  - `metabolism/inbox/README.md`: raw-material intake index or public-safe entrypoint
  - `metabolism/inbox/index.md`: raw-material intake index or public-safe entrypoint
  - `metabolism/processing/README.md`: material processing, evidence-intake, review, or extraction state
  - `metabolism/processing/evidence-intake/README.md`: material processing, evidence-intake, review, or extraction state
  - `metabolism/processing/evidence-intake/external-drive-afelite-20260530.md`: material processing, evidence-intake, review, or extraction state
  - `metabolism/processing/evidence-intake/external-drive-next-pass-20260530.md`: material processing, evidence-intake, review, or extraction state
  - `metabolism/processing/evidence-intake/external-drive-project-first-read-20260530.md`: material processing, evidence-intake, review, or extraction state
  - `metabolism/processing/evidence-intake/feishu-first-read-20260530.md`: material processing, evidence-intake, review, or extraction state

### runtime

- Files: 41
- Classes: runtime-lesson=2, runtime-local-profile=1, runtime-memory=1, runtime-projection=29, runtime-session=2, runtime-skill=4, runtime-support=2
- Representative files:
  - `runtime/README.md`: runtime layer index or support file
  - `runtime/index.md`: runtime layer index or support file
  - `runtime/memory/working-lessons/README.md`: session context, working lesson, or runtime memory support
  - `runtime/profiles/hermes/anthonyhf/PROFILE.md`: runtime projection/profile for external agent platform
  - `runtime/profiles/hermes/anthonyhf/README.md`: runtime projection/profile for external agent platform
  - `runtime/profiles/hermes/anthonyhf/SOUL.md`: runtime projection/profile for external agent platform; duplicate policy: allowed runtime projection duplicate
  - `runtime/profiles/hermes/anthonyhf/config.yaml`: runtime projection/profile for external agent platform
  - `runtime/profiles/hermes/anthonyhf/coverage-report.yml`: runtime projection/profile for external agent platform
  - `runtime/profiles/hermes/anthonyhf/learning_queue/skill-recommendations.yml`: runtime projection/profile for external agent platform
  - `runtime/profiles/hermes/anthonyhf/learning_queue/working-lessons.README.md`: runtime projection/profile for external agent platform
  - `runtime/profiles/hermes/anthonyhf/memories/seed.md`: runtime projection/profile for external agent platform; duplicate policy: allowed runtime projection duplicate
  - `runtime/profiles/hermes/anthonyhf/profile.manifest.yml`: runtime projection/profile for external agent platform
  - ... see `docs/file-role-inventory.yml` for 29 more file entries.

### capabilities

- Files: 44
- Classes: capability-catalog=2, capability-entrypoint=2, capability-internal-reference=39, capability-memory=1
- Representative files:
  - `capabilities/README.md`: capability-owned reference, data, schema, script, or support document
  - `capabilities/engineering-everything/README.md`: capability-owned reference, data, schema, script, or support document
  - `capabilities/engineering-everything/SKILL.md`: stable capability executable entrypoint
  - `capabilities/engineering-everything/SKILLS-CATALOG.html`: capability-specific HTML catalog
  - `capabilities/engineering-everything/agents/openai.yaml`: capability-owned reference, data, schema, script, or support document
  - `capabilities/engineering-everything/data/review_roles.yaml`: capability-owned reference, data, schema, script, or support document
  - `capabilities/engineering-everything/data/routes.yaml`: capability-owned reference, data, schema, script, or support document
  - `capabilities/engineering-everything/data/validation_commands.yaml`: capability-owned reference, data, schema, script, or support document
  - `capabilities/engineering-everything/references/agent-operating-standards.md`: capability-owned reference, data, schema, script, or support document
  - `capabilities/engineering-everything/references/architecture-cases-ai.md`: capability-owned reference, data, schema, script, or support document
  - `capabilities/engineering-everything/references/architecture-cases.md`: capability-owned reference, data, schema, script, or support document
  - `capabilities/engineering-everything/references/checklists.md`: capability-owned reference, data, schema, script, or support document
  - ... see `docs/file-role-inventory.yml` for 32 more file entries.

### evolution

- Files: 65
- Classes: evolution-alignment=1, evolution-ipo=2, evolution-mutation=1, evolution-support=2, organ-system-entrypoint=4, organ-system-internal=55
- Representative files:
  - `evolution/README.md`: evolution layer index or support file
  - `evolution/alignment/README.md`: owner alignment and cognitive-alignment process support
  - `evolution/index.md`: evolution layer index or support file
  - `evolution/ipo/README.md`: IPO evolution process index or artifact
  - `evolution/ipo/index.md`: IPO evolution process index or artifact
  - `evolution/mutations/README.md`: mutation proposal, changelog, or support index
  - `evolution/organ-systems/cognitive-alignment/SKILL.md`: self-evolution organ-system Skill entrypoint
  - `evolution/organ-systems/ipo-reverse/.openlifeos-skill-source.yml`: self-evolution organ-system reference, template, script, example, eval, or license
  - `evolution/organ-systems/ipo-reverse/LICENSE`: self-evolution organ-system reference, template, script, example, eval, or license
  - `evolution/organ-systems/ipo-reverse/README.md`: self-evolution organ-system reference, template, script, example, eval, or license
  - `evolution/organ-systems/ipo-reverse/SKILL.md`: self-evolution organ-system Skill entrypoint
  - `evolution/organ-systems/ipo-reverse/evals/evals.json`: self-evolution organ-system reference, template, script, example, eval, or license
  - ... see `docs/file-role-inventory.yml` for 53 more file entries.

### identities

- Files: 2
- Classes: identity-projection=2
- Representative files:
  - `identities/README.md`: social/work identity projection index or support file
  - `identities/index.md`: social/work identity projection index or support file

### work

- Files: 31
- Classes: work-avatar-page=1, work-homepage-app=28, work-support=2
- Representative files:
  - `work/README.md`: work layer index, project, report, publication, or support file
  - `work/apps/homepage/DESIGN.md`: homepage app source, public-safe asset, config, or package metadata
  - `work/apps/homepage/components.json`: homepage app source, public-safe asset, config, or package metadata
  - `work/apps/homepage/components/ui/story-scroll.tsx`: homepage app source, public-safe asset, config, or package metadata
  - `work/apps/homepage/index.html`: homepage app source, public-safe asset, config, or package metadata
  - `work/apps/homepage/lib/utils.ts`: homepage app source, public-safe asset, config, or package metadata
  - `work/apps/homepage/package-lock.json`: homepage app source, public-safe asset, config, or package metadata
  - `work/apps/homepage/package.json`: homepage app source, public-safe asset, config, or package metadata
  - `work/apps/homepage/public/assets/README.md`: homepage app source, public-safe asset, config, or package metadata
  - `work/apps/homepage/public/assets/hardware/jetson-orin.png`: homepage app source, public-safe asset, config, or package metadata; duplicate policy: current source asset duplicated only by legacy build output
  - `work/apps/homepage/public/assets/hardware/jetson-xavier-clean.png`: homepage app source, public-safe asset, config, or package metadata; duplicate policy: current source asset duplicated only by legacy build output
  - `work/apps/homepage/public/assets/logos/grainedai-logo-clean.png`: homepage app source, public-safe asset, config, or package metadata; duplicate policy: current source asset duplicated only by legacy build output
  - ... see `docs/file-role-inventory.yml` for 19 more file entries.

### integrations

- Files: 10
- Classes: integration-config=10
- Representative files:
  - `integrations/README.md`: external system, runtime sync, data source, or skill-source binding
  - `integrations/agents/openai.yaml`: external system, runtime sync, data source, or skill-source binding
  - `integrations/data-sources.yml`: external system, runtime sync, data source, or skill-source binding
  - `integrations/feishu.yml`: external system, runtime sync, data source, or skill-source binding
  - `integrations/github.yml`: external system, runtime sync, data source, or skill-source binding
  - `integrations/hermes-sync-log.md`: external system, runtime sync, data source, or skill-source binding
  - `integrations/hermes.yml`: external system, runtime sync, data source, or skill-source binding
  - `integrations/skill-sources/default-skills/README.md`: external system, runtime sync, data source, or skill-source binding
  - `integrations/skill-sources/default-skills/self-evolution.md`: external system, runtime sync, data source, or skill-source binding
  - `integrations/skill-sources/default-skills/skill-updates.yml`: external system, runtime sync, data source, or skill-source binding

### security

- Files: 2
- Classes: security-policy=2
- Representative files:
  - `security/README.md`: privacy, permission, public boundary, or security policy
  - `security/permissions.yml`: privacy, permission, public boundary, or security policy

### docs

- Files: 17
- Classes: avatar-page-ia=1, documentation-asset=1, file-role-inventory=1, governance-doc=8, layer-file-review=1, migration-doc=4, skill-system-doc=1
- Representative files:
  - `docs/README.md`: human-facing governance, review, status, or policy doc
  - `docs/assets/anthonyhf-readme-cover.png`: documentation visual asset; duplicate policy: documentation asset also used by app
  - `docs/avatar-description-eval.md`: human-facing governance, review, status, or policy doc
  - `docs/avatar-page-information-architecture.md`: third-person avatar page information architecture
  - `docs/evidence-sufficiency.md`: human-facing governance, review, status, or policy doc
  - `docs/file-role-inventory.yml`: generated file-level role audit
  - `docs/file-structure-policy.md`: human-facing governance, review, status, or policy doc
  - `docs/layer-file-review.md`: generated layer-level role review
  - `docs/lifeos-content-review.md`: human-facing governance, review, status, or policy doc
  - `docs/migration/anthonyhf-skill-import-report.md`: migration instruction, source inventory, or retention audit
  - `docs/migration/information-retention-audit-20260530.md`: migration instruction, source inventory, or retention audit
  - `docs/migration/platform-migration-instructions.md`: migration instruction, source inventory, or retention audit
  - ... see `docs/file-role-inventory.yml` for 5 more file entries.

### legacy

- Files: 27
- Classes: legacy-archive=27
- Representative files:
  - `legacy/build-output/README.md`: v1/v1.5 historical, generated, or unclassified material kept out of current schema
  - `legacy/build-output/homepage-dist-20260602/dist/assets/README.md`: v1/v1.5 historical, generated, or unclassified material kept out of current schema
  - `legacy/build-output/homepage-dist-20260602/dist/assets/hardware/jetson-orin.png`: v1/v1.5 historical, generated, or unclassified material kept out of current schema; duplicate policy: legacy duplicate not part of current schema
  - `legacy/build-output/homepage-dist-20260602/dist/assets/hardware/jetson-xavier-clean.png`: v1/v1.5 historical, generated, or unclassified material kept out of current schema; duplicate policy: legacy duplicate not part of current schema
  - `legacy/build-output/homepage-dist-20260602/dist/assets/index-BnLsZEj6.js`: v1/v1.5 historical, generated, or unclassified material kept out of current schema
  - `legacy/build-output/homepage-dist-20260602/dist/assets/index-uaf-mR80.css`: v1/v1.5 historical, generated, or unclassified material kept out of current schema
  - `legacy/build-output/homepage-dist-20260602/dist/assets/logos/grainedai-logo-clean.png`: v1/v1.5 historical, generated, or unclassified material kept out of current schema; duplicate policy: legacy duplicate not part of current schema
  - `legacy/build-output/homepage-dist-20260602/dist/assets/logos/grainedai.svg`: v1/v1.5 historical, generated, or unclassified material kept out of current schema; duplicate policy: legacy duplicate not part of current schema
  - `legacy/build-output/homepage-dist-20260602/dist/assets/logos/metainflow-logo.png`: v1/v1.5 historical, generated, or unclassified material kept out of current schema; duplicate policy: legacy duplicate not part of current schema
  - `legacy/build-output/homepage-dist-20260602/dist/assets/logos/metainflow.svg`: v1/v1.5 historical, generated, or unclassified material kept out of current schema; duplicate policy: legacy duplicate not part of current schema
  - `legacy/build-output/homepage-dist-20260602/dist/assets/logos/nvidia-logo-clean.png`: v1/v1.5 historical, generated, or unclassified material kept out of current schema; duplicate policy: legacy duplicate not part of current schema
  - `legacy/build-output/homepage-dist-20260602/dist/assets/logos/nvidia.svg`: v1/v1.5 historical, generated, or unclassified material kept out of current schema; duplicate policy: legacy duplicate not part of current schema
  - ... see `docs/file-role-inventory.yml` for 15 more file entries.

## Trim Boundary

- `SOUL.md`, `DESIGN.md`, `SKILL.md`, `README.md`, `matrix.yml`, `artifacts/current.yml`, and `identity/current.yml` are entrypoints or registries; they do not replace source artifacts.
- `runtime/runtime-profile/` is the local runtime context/profile placeholder; `runtime/profiles/` contains external runtime projections. Neither is a personality truth source.
- `work/avatar-page/view-model.yml` is a presentation model for a concrete avatar page; it consumes LifeOS artifacts and is not an identity truth source.
- `runtime/runtime-skills/` contains runtime or bound operational skills; stable reusable capabilities only belong in `capabilities/` after IPO and owner alignment.
- `legacy/` keeps v1/v1.5, generated, or unclassified historical material out of the current schema.

## Maintenance Rule

When a new file appears, it should either match a class in `docs/file-structure-policy.md` or be placed in `legacy/` until classified. Update `docs/file-role-inventory.yml` after structural changes.
