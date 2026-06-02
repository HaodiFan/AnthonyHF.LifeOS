# Wenxin Changelog

This log records active Wenxin artifact changes. Raw evidence stays outside this public repo unless explicitly approved and summarized.

## 2026-06-02T12:00:00+08:00

- Added `WENXIN_REPORT.html` as the structured human-facing Wenxin output.
- Added `WENXIN_REPORT.xml` as the machine-readable Wenxin output.
- Updated registries to treat Markdown as `legacy_markdown_source` rather than the current Wenxin output artifact.

## 2026-05-30T23:55:50+08:00

- Activated `WENXIN-20260530-235550.md` as the timestamped version behind `WENXIN_REPORT.md`.
- Added `versions.yml` so future Wenxin outputs can build on the current active artifact instead of replacing it silently.
- Current status remains `evidence_sufficiency: insufficient` because the Markdown wrapper has not fully reconstructed the original Wenxin PDF fields.
- Runtime projections should use `identity/current.yml` to resolve the active Wenxin artifact.
