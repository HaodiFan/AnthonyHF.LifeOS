# Runtime User Context

This file contains translated memory summaries. It should contain stable facts, preferences, claims, and constraints only.

## Long-Term Memory

### memory/long-term/README.md

# Long-term Memory

这里存放稳定、陈述式、可追溯的事实和偏好。

Allowed:

- user preference;
- environment fact;
- durable decision;
- stable relationship or constraint;
- source and validity metadata.

Forbidden:

- workflow;
- SOP;
- script;
- one-off task state;
- raw private evidence body.

If a memory entry tells the agent how to perform a task, split that procedure into a Skill proposal and leave only the fact here.

## Distilled Knowledge

### memory/distilled-knowledge/README.md

# Distilled Knowledge

这里存放从多条 evidence / memory / lesson 综合出来的结构化知识。

Recommended fields:

- `claim`;
- `evidence`;
- `confidence`;
- `freshness`;
- `contradiction_status`;
- `compiled_from`;
- `review_after`.

Use this layer for entity pages, claim/evidence summaries, contradiction notes, and reviewed digests. Do not store raw session notes or procedural workflows here.
