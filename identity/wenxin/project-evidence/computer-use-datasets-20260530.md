# Wenxin Project Evidence: Computer-Use Dataset Pipeline

Date: 2026-05-30
Source ID: `external-drive-afelite-20260530`
Evidence Type: `project_output_metadata`
Status: `metadata_and_design_read`
Visibility: `public-safe-summary`

## Source Pointers

- `Code/screenshot-pc-version/TL_ComputerUseDatasets/README.md`
- `Code/screenshot-pc-version/TL_ComputerUseDatasets/modules/bilibili/TASK_DISPATCH_DESIGN.md`
- `Code/screenshot-pc-version/TL_ComputerUseDatasets/BAIDU_SEARCH_ISSUE_ANALYSIS.md`

Only README/design/issue-analysis material was read. No scraped data, downloaded media, dataset body, platform credential, private task output, or source implementation body was copied into LifeOS.

## Project Purpose

TL_ComputerUseDatasets is described as a modular pipeline for computer-use data processing, covering data acquisition, cleaning, query generation, and analysis/modeling of user behavior across devices or platforms.

The Bilibili module and Baidu issue analysis show this was not only a generic crawler, but a computer-use / web-agent data workflow that had to respond to real website interface changes.

## Artifact Summary

Pipeline architecture:

- Platform-specific modules with standardized fetcher interfaces.
- Data acquisition -> data modeling -> processing -> output.
- Planned Pydantic validation, YAML config, validation rules, and testable platform utilities.

Bilibili task dispatch:

- URL Fetcher inserts video tasks.
- Video Fetcher consumes pending tasks and updates state.
- PostgreSQL task table stores URL, title, duration, status, download type, log, timestamps.
- Indexes and modified-time trigger support operational tracking.

Baidu search issue analysis:

- Debugging found the target page had shifted from traditional search input to a chat-style interface.
- The system's element extraction was working, but interaction selection failed because the expected input no longer existed.
- Proposed solution: update prompts, element recognition, and monitoring for page structure changes.

## Wenxin Capability Signal

This project evidence strengthens the "AI data workflow and agent evaluation infrastructure" part of AnthonyHF's Wenxin profile:

- Ability to design modular data acquisition systems across platforms.
- Operational awareness: task queues, statuses, logs, retries, and database-backed dispatch.
- Agent-specific debugging ability: distinguishing tool bug from environment/page-structure shift.
- Recognition that data pipelines for computer-use agents require continuous adaptation to UI changes.

## Field-Position Signal

This positions AnthonyHF in a practical computer-use agent data stack:

- platform data acquisition;
- task dispatch and processing operations;
- UI/environment drift debugging;
- agent interaction robustness;
- data pipeline governance.

Compared with WebTwin, this project is less about extracting page artifacts and more about sustaining data operations over changing web interfaces.

## Gap / Incompleteness

- This pass did not inspect downloaded videos, datasets, or platform data bodies.
- The README includes planned components; completion status needs owner review.
- It is unclear which parts were prototype, internal delivery, or production process.
- Platform ToS and data rights need separate review before any public claim.

## Reusable Skill Candidates

- `identity/wenxin/skill-recommendations.ymlcomputer-use-data-pipeline-index.md`
- `identity/wenxin/skill-recommendations.ymlweb-agent-environment-debugging-index.md`
- `identity/wenxin/skill-summaries/data-pipeline-operations-index.md`

## Privacy Review

Safe to use for Wenxin capability mapping at design-summary level.

Do not copy:

- downloaded platform data;
- task rows or logs containing URLs/users/private context;
- platform credentials/cookies;
- raw media;
- source bodies beyond abstracted design.

## Suggested Wenxin Update

Add a project-backed signal under field coverage:

> AnthonyHF has evidence of building computer-use data pipelines and debugging agent-environment drift: modular platform fetchers, task dispatch, database-backed processing states, and adaptation to web interface changes.

