# Wenxin Project Evidence: Feishu Project Ops First Read

Date: 2026-05-30
Source ID: `external-drive-afelite-20260530`
Evidence Type: `project_review_and_kt_summary`
Status: `redacted_first_read`
Visibility: `public-safe-summary`

## Source Pointers

This note summarizes selected Feishu export documents by filename only:

- `QCAnything Pivot Note.docx`
- `WebAgent 数据生产复盘.docx`
- `GitHub高星Repo-复盘.docx`
- `TML Pivot Note.docx`
- `[Project] Pivot Note.docx`

Raw document bodies are not copied into LifeOS. High-risk details, private links, customer-specific records, credentials, and exact snippets are excluded.

## Project Signals

### QCAnything

The pivot note frames QCAnything as a general structured multimodal data quality tool.

Evidence signals:

- Originated from WebAgent data quality pain: complex data modalities and deep field relationships lacked a good ready-made QC tool.
- Product direction included JSON/JSONL handling, version control, tree/form browsing modes, dataset copilot, and prebuilt agent/workflow plugins.
- Milestone trail shows a productization arc: frontend start, tree layout, config settings, image/video annotation, real business-data integration, then multiple releases through v1.0.
- Operational details include backend/frontend/desktop packaging, app build artifacts, and cache handling.

Wenxin interpretation:

- Strong evidence of moving from client/project pain to reusable internal product infrastructure.
- Capability sits at the intersection of data QC, productized tooling, desktop packaging, backend/frontend coordination, and agent workflow support.

### WebAgent Data Production

The WebAgent review describes a production chain for web-agent data delivery.

Evidence signals:

- Pipeline steps include raw data collection, processing, screenshot generation, annotated screenshot generation, translation, scroll merge, QC repair, optional pipeline QC, and delivery handling.
- Repeated issue classes include screenshot timing, scroll timing, bounding-box drift, native dropdowns, overflow, hardcoded/manual annotation, and instruction/bounding-box mismatch.
- Work was organized into plugin annotation, QC, repair, re-delegation, pipeline QC, and pipeline modification.
- Feishu table automation was used as part of the operational loop, but exact table/API details are excluded here.

Wenxin interpretation:

- Strong evidence of hands-on AI data production operations, not only model/tool conceptual work.
- Shows ability to identify data quality failure modes and build operational repair loops.
- Reinforces capability in web-agent evaluation/data pipelines and production-grade QC.

### GitHub High-Star Repo Delivery Review

The GitHub repo review captures delivery estimation and infrastructure lessons from a large repository data project.

Evidence signals:

- The project involved high-star repository filtering, large download/upload/storage operations, NAS/object storage selection, cloud transfer, and delivery timing.
- The retrospective explicitly identifies estimation mistakes around timeline, iteration, storage, bandwidth, cloud region/networking, compression, disk usage versus logical size, and zip-size estimation.
- It records a security lesson around token/secret exposure risk. No token or secret is copied here.

Wenxin interpretation:

- Strong evidence of infrastructure-heavy delivery learning: storage, network throughput, cloud object storage, large batch transfer, and project estimation.
- Shows a pattern of turning delivery failure/underestimate into explicit future rules.

### TML / Generic Project Pivot Notes

The first read found mostly scaffold headings for `TML Pivot Note` and `[Project] Pivot Note`.

Wenxin interpretation:

- Treat as structural placeholders, not substantive evidence yet.
- Useful signal: the team had a repeatable project-pivot template, but content is insufficient in this pass.

## Capability Map Update

Feishu project ops evidence strengthens these Wenxin areas:

1. AI data production and QC operations.
2. Productization from project pain to reusable tooling.
3. Web-agent data pipeline debugging and repair.
4. Large-scale data/repository acquisition and storage delivery.
5. Infrastructure estimation and delivery retrospective discipline.
6. Feishu/Bitable-like operational automation, with strict credential redaction.

## Gaps

- Need owner review before treating any customer/project outcome as public claim.
- Need separate handling for transcripts and AI notes.
- Need distinguish Anthony-authored reflections from team-authored operational logs.
- Need avoid exact project/customer identifiers beyond already public or owner-approved names.

## Suggested Wenxin Update

Add this capability signal:

> AnthonyHF has evidence of building and operating AI data production systems end to end: productizing QC tooling, running web-agent data pipelines, debugging screenshot/bbox/timing failures, automating operational tables, and retrospecting large-scale data delivery bottlenecks.

## Skill Candidates

- `skills/runtime/ai-data-qc-operations-index.md`
- `skills/runtime/web-agent-data-production-index.md`
- `skills/meta/delivery-estimation-retrospective-index.md`
- `skills/meta/data-infra-transfer-and-storage-index.md`

