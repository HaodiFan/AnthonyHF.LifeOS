# External Drive Project First Read

Date: 2026-05-30
Source ID: `external-drive-afelite-20260530`
Status: `first_read_metadata_only`
Visibility: `public-safe-summary`

## Scope

This first read used low-risk project metadata from the `Code` bucket only: README files, architecture notes, and lightweight package/config indicators.

No source code body, dataset body, customer file, Feishu/Lark private document, contract, credential, or private transcript was copied into LifeOS.

Wenxin projection:

- `identity/wenxin/project-evidence-external-drive-20260530.md`

## Read Set

| Project Cluster | Read Surface | LifeOS Signal |
| --- | --- | --- |
| QCAnything backend | README and docs index | event-sourced JSON document system, API/backend architecture, audit log, versioning, patch management |
| QCAnything plugin runtime | README | sandboxed IPC plugin runtime, wrapper/manifest install flow, process-level execution lifecycle |
| WebTwin / Website Extractor | README | website extraction, asset capture, UI/component analysis, AI agent training data preparation |
| DatasetGuard | README | dataset quality inspection, duplicate detection, sensitive information detection, data integrity/compliance |
| SmartBookMiner | README | book/document extraction, PDF/EPUB mining, practice problem/key concept extraction |
| TL_ComputerUseDatasets | README | modular computer-use data acquisition pipeline, platform modules, standardized fetchers, processing flow |
| PII dataset pipeline | README title only | likely privacy/PII data processing evidence; needs careful owner-approved review before body reading |
| WebAgentRLEnv | README title only | likely web-agent RL environment evidence; needs architecture docs or code tree pass next |

## Emerging Capability Signals

Routing rule: these project signals should primarily feed Wenxin. IPO Reverse is used to analyze project evidence, and skill targets receive distilled procedure after Wenxin has classified the capability. PSP should only receive project-adjacent material when the source is Anthony's own reflection,感悟, decision note, correction, or conflict review.

1. **Data quality and compliance systems**
   - Evidence: DatasetGuard, PII pipeline, QCAnything audit/versioning features.
   - Candidate LifeOS target: `identity/wenxin/WENXIN_REPORT.md`, then `identity/wenxin/skill-summaries/data-quality-compliance-index.md`.
   - Risk: PII/privacy material can contain sensitive examples; read only architecture and redacted summaries.

2. **Agent/web environment and data generation**
   - Evidence: WebTwin, WebAgentRLEnv, TL_ComputerUseDatasets.
   - Candidate LifeOS target: `identity/wenxin/WENXIN_REPORT.md`, then `identity/wenxin/skill-recommendations.ymlweb-agent-data-pipeline-index.md`.
   - Risk: captured website data and generated datasets may include third-party content; do not copy bodies.

3. **Plugin/runtime architecture**
   - Evidence: QCAnything plugin runtime.
   - Candidate LifeOS target: `identity/wenxin/WENXIN_REPORT.md`, then `identity/wenxin/skill-summaries/plugin-runtime-architecture-index.md`.
   - Risk: runtime manifests can expose local paths or private integration assumptions; summarize only design.

4. **Document/book mining**
   - Evidence: SmartBookMiner.
   - Candidate LifeOS target: `identity/wenxin/WENXIN_REPORT.md`, then `identity/wenxin/skill-recommendations.ymldocument-mining-index.md`.
   - Risk: extracted source documents may be copyrighted/private; treat bodies as forbidden unless explicitly approved.

5. **Productized AI tooling**
   - Evidence: QCAnything backend, desktop/plugin runtime, WebTwin, data marketplace candidates.
   - Candidate LifeOS target: `identity/wenxin/public-positioning.md` after owner review.
   - Risk: public positioning should not claim commercial/customer outcomes without approved evidence.

## Suggested Wenxin Project Queue

| Priority | Project | Why Next |
| --- | --- | --- |
| P0 | QCAnything backend + plugin runtime | Shows backend architecture, plugin lifecycle, product tooling, and delivery pattern; useful for Wenxin capability map. |
| P0 | WebTwin | Shows agent-facing data generation, website extraction, UI/component analysis, and product workflow; useful for future direction. |
| P1 | TL_ComputerUseDatasets | Shows modular data acquisition pipeline for computer-use datasets; useful for field position. |
| P1 | DatasetGuard | Shows data quality, privacy, duplicate detection, and compliance orientation; useful for capability completeness. |
| P1 | SmartBookMiner | Shows document mining / educational content extraction workflow; useful for applied AI/data tooling map. |
| P2 | WebAgentRLEnv | Needs architecture docs next; likely important for web-agent environment construction. |
| P2 | PII dataset pipeline | Important but privacy-sensitive; read only after explicit PII-safe scope selection. |

## Next Reading Rule

For each selected project, read in this order:

1. README / architecture docs.
2. Dependency/config files.
3. File tree and module names.
4. Only then, selected implementation files if needed to understand reusable design.

Every output should be an abstracted evidence note, not copied source content.

Project outputs should write first to:

- `identity/wenxin/project-evidence-*.md`
- `identity/wenxin/WENXIN_REPORT.md`
- `identity/wenxin/skill-recommendations.yml`

Only after Wenxin synthesis should reusable procedures move toward `identity/wenxin/skill-recommendations.yml` or `identity/wenxin/skill-summaries/`.

## LifeOS Maturity Impact

This first read creates early project evidence but does not yet change maturity from `scaffold`, because no owner-approved synthesis has been promoted into Wenxin, PSP, memory, or skill recommendations.

Maturity can move to `evidence-limited-v0` after at least one Wenxin project evidence note is written with:

- source pointer;
- project purpose;
- artifact summary;
- capability / field-position signal;
- reusable method candidates;
- privacy review;
- target Wenxin and skill path.
