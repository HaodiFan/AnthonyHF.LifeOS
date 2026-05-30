# Runtime Tool And Data Bindings

This file is advisory unless the target runtime enforces these bindings.

## Skill Bindings

```yaml
version: 1
owner: Anthony Fan
bindings:
  default_memory_lookup:
    purpose: Let skills read stable facts without embedding them.
    allowed_sources:
      - memory/long-term/
      - memory/distilled-knowledge/
      - memory/wiki-repo.yml
    forbidden_sources:
      - raw private files
      - secrets
      - unapproved transcripts
  runtime_skill_evidence:
    purpose: Let runtime skills produce evidence for promotion.
    writes_to:
      - memory/working-lessons/
      - skills/recommendations/skill-roadmap.yml
    promotion_gate: IPO Reverse plus owner alignment
  external_connector_data:
    purpose: Let skills declare external dependencies.
    registry: integrations/data-sources.yml
    token_policy: never store tokens in repo
split_rule:
  fact_goes_to: memory/long-term/ or memory/working-lessons/
  procedure_goes_to: skills/runtime/
  abstracted_judgment_goes_to: skills/meta/
```

## Data Sources

```yaml
version: 1
owner: Anthony Fan
visibility: public
purpose: Declare data sources before agents use them for memory, knowledge, or skill updates.
sources:
  memory_wiki:
    enabled: true
    config: memory/wiki-repo.yml
    authority: configured
    token_policy: no-token-in-repo
    allowed_targets:
      - memory/working-lessons/
      - memory/long-term/
      - memory/distilled-knowledge/
  github:
    enabled: false
    config: integrations/github.yml
    authority: repository-state
    token_policy: env-only-or-gh-auth
    allowed_targets:
      - skills/recommendations/skill-roadmap.yml
      - memory/working-lessons/
  feishu:
    enabled: false
    config: integrations/feishu.yml
    authority: external-app
    token_policy: env-only
    allowed_targets:
      - memory/working-lessons/
      - identity/wenxin/
  hermes:
    enabled: false
    config: integrations/hermes.yml
    authority: imported-evidence
    token_policy: env-only-or-platform-secret
    allowed_targets:
      - memory/working-lessons/
      - skills/recommendations/skill-roadmap.yml
      - identity/psp/
  local_external_drive_afelite:
    enabled: true
    config: docs/evidence-intake/external-drive-afelite-20260530.md
    authority: owner-local-evidence
    token_policy: no-token
    visibility: local-only-index
    body_policy: no-body-copy
    allowed_targets:
      - docs/evidence-sufficiency.md
      - identity/wenxin/
      - identity/psp/
      - skills/recommendations/skill-roadmap.yml
      - memory/working-lessons/
    forbidden_targets:
      - public raw file export
      - runtime prompt body injection
      - homepage assets without owner approval
public_export_gate:
  requires_owner_approval: true
  allowed:
    - approved facts
    - redacted summaries
    - abstracted patterns
  forbidden:
    - secrets
    - raw private bodies
    - unapproved personal records
```
