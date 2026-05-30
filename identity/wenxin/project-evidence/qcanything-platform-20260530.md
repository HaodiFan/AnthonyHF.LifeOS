# Wenxin Project Evidence: QCAnything Platform

Date: 2026-05-30
Source ID: `external-drive-afelite-20260530`
Evidence Type: `project_output_metadata`
Status: `metadata_and_architecture_read`
Visibility: `public-safe-summary`

## Source Pointers

- `Code/repo-with-all-branches/raw_repo/QCAnything/qc_anything_backend/README.md`
- `Code/repo-with-all-branches/raw_repo/QCAnything/qc_anything_backend/docs/backend-design-specification.md`
- `Code/screenshot-pc-version/qcanything-plugin-runtime/README.md`
- `Code/screenshot-pc-version/qcanything-plugin-runtime/docs/ARCHITECTURE.md`
- `Code/screenshot-pc-version/qcanything-plugin-runtime/docs/SYSTEM_DESIGN.md`

Only project metadata and architecture/design documents were read. No source code body, customer data, runtime secret, plugin body, dataset body, or private document was copied into LifeOS.

## Project Purpose

QCAnything appears as a productized AI/data tooling platform with two connected layers:

- Backend layer: JSON document management, API service, versioning, patch management, resource management, and auditability.
- Plugin runtime layer: local long-running plugin runtime manager for sandboxed plugin execution, lifecycle control, task state, IPC/RPC, and cross-platform operation.

## Artifact Summary

Backend signals:

- FastAPI backend with PostgreSQL/SQLite modes.
- Event-sourced JSON document management.
- JSON Patch, version control, rollback, JSONPath query, resource upload/storage.
- Audit logs and standard API response/error conventions.
- Clear controller/service/model/view/core/db layering.

Plugin runtime signals:

- Runtime Manager is an independent OS process.
- Backend and Runtime are loosely coupled through JSON-RPC over IPC.
- Plugin sandbox processes are treated as untrusted workers.
- Task lifecycle uses a strict state machine from creation to terminal states.
- Runtime storage separates plugin source, virtual environments, and task sandboxes.
- stdout is reserved for JSON Lines protocol messages; stderr is human-readable logs.
- TCP is only fallback/loopback; runtime is not meant to be a public network service.

## Wenxin Capability Signal

This project evidence strengthens the "productized engineering system builder" part of AnthonyHF's Wenxin profile:

- Ability to turn messy AI/data workflows into governed product infrastructure.
- Strong concern for lifecycle boundaries: backend vs runtime, manager vs plugin, source vs task sandbox.
- Preference for explicit protocols, state machines, storage semantics, and auditability.
- Engineering taste favors operational control surfaces rather than one-off scripts.

## Field-Position Signal

QCAnything positions AnthonyHF around AI-native tooling infrastructure rather than only application-layer AI demos:

- Data/document operations.
- Pluginized AI workflows.
- Local runtime/process orchestration.
- Governance of untrusted or variable user code.
- Product architecture that can bridge desktop, backend, and plugin execution.

## Gap / Incompleteness

- This pass did not verify shipped usage, user adoption, commercial outcome, or production reliability.
- Architecture docs show intent and design quality, but not final delivery evidence.
- Backend and runtime relationship needs a project retrospective to clarify what was actually completed, abandoned, or learned.
- Customer/project-specific context remains excluded.

## Reusable Skill Candidates

- `identity/wenxin/skill-summaries/plugin-runtime-architecture-index.md`
- `identity/wenxin/skill-summaries/ai-tooling-platform-architecture-index.md`
- `identity/wenxin/skill-recommendations.ymlbackend-api-system-design-index.md`
- `identity/wenxin/skill-recommendations.ymljson-document-workflow-index.md`

## Privacy Review

Safe to use for Wenxin capability mapping at summary level.

Do not copy:

- source implementation bodies;
- actual plugin code;
- runtime local paths;
- task inputs/outputs;
- customer JSON documents;
- secrets or config values.

## Suggested Wenxin Update

Add a project-backed signal under field coverage:

> AnthonyHF has evidence of building governed AI/data tooling platforms: backend document systems, plugin runtime architecture, IPC/RPC process boundaries, task lifecycle management, and audit/versioning controls.

