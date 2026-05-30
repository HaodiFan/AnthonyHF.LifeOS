# External Drive Evidence Intake

Date: 2026-05-30
Owner: AnthonyHF
Source ID: `external-drive-afelite-20260530`
Status: `inventory_created_body_not_processed`
Visibility: `local-only-index`

## Summary

The local external drive `AFElite` is available as a private evidence source for LifeOS alignment and future synthesis.

This public LifeOS repo records only the intake summary and routing policy. It does not copy raw file bodies, private documents, customer material, contracts, Feishu exports, datasets, source repositories, or secrets from the drive.

## Local Intake Location

Local private inventory files are stored outside this repo:

- `~/LifeOS_Intake/AnthonyHF/external-drive/source.yml`
- `~/LifeOS_Intake/AnthonyHF/external-drive/file-list.txt`
- `~/LifeOS_Intake/AnthonyHF/external-drive/file-list.filtered.txt`
- `~/LifeOS_Intake/AnthonyHF/external-drive/top-level-counts.txt`
- `~/LifeOS_Intake/AnthonyHF/external-drive/extension-counts.txt`
- `~/LifeOS_Intake/AnthonyHF/external-drive/project-root-candidates.txt`
- `~/LifeOS_Intake/AnthonyHF/external-drive/document-candidates.txt`
- `~/LifeOS_Intake/AnthonyHF/external-drive/sensitive-document-candidates.txt`
- `~/LifeOS_Intake/AnthonyHF/external-drive/intake-summary.md`

## Inventory Result

- Mounted volume: `AFElite`
- Mount: local external drive mount for `AFElite`
- Filesystem: `ExFAT`
- Size: 256.0 GB
- Used: 249.9 GB
- Free: 6.1 GB
- Filtered file count: 239,048

Top-level buckets after excluding dependency/build/system noise:

- `Code`: 150,014 files
- `Datasets`: 72,351 files
- `Documents`: 16,683 files

Excluded from the filtered list:

- `node_modules`, `.git`, `dist`, `build`, `.next`, `__pycache__`, `.venv`, `venv`, `.Trashes`, `.Spotlight-V100`, `.fseventsd`, `System Volume Information`

## Initial Routing

| Bucket | LifeOS Use | Policy |
| --- | --- | --- |
| Code | project evidence for Wenxin capability map, field position, future path, and later skill evidence | index first; do not copy repos into public LifeOS |
| Datasets | research/data source provenance | index only unless a specific approved skill needs dataset evidence |
| Documents | writings/reflections for PSP, public profile evidence for Wenxin, memory pointers | private-by-default; owner approval required before summarization |

## Sensitive Zones

These categories are private-by-default and must not be copied into the public repo:

- contracts
- customer materials
- Feishu/Lark exports or links
- raw meeting transcripts
- financial records
- identity documents
- tokens, credentials, cookies, keys
- private chats
- dataset bodies
- source repository bodies

## Next Pass

Recommended next action is a selective, owner-approved evidence pass:

1. Pick 10-20 high-value project outputs from the Code bucket for Wenxin project evidence.
2. Pick Anthony-authored writings,感悟, reflections, corrections, or judgment samples for PSP only after owner approval.
3. Pick explicitly approved public-safe documents for public profile and Wenxin narrative.
4. Keep dataset material as provenance/index unless a specific skill needs it.

## Maturity Impact

This intake creates source availability but does not by itself increase LifeOS maturity beyond `scaffold`. Maturity can move to `evidence-limited-v0` after approved project evidence is summarized into Wenxin and approved writing/reflection evidence is summarized into PSP, skill roadmap, or memory pointers with provenance.
