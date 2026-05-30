# AGENTS.md

This file is a runtime policy projection generated from LifeOS.

## Operating Rules

- Treat LifeOS as the canonical source of truth.
- Do not promote runtime lessons directly into durable identity, memory, or meta skills.
- Send runtime feedback back as lesson evidence.
- Do not export raw private material, secrets, or unreviewed working lessons.

## Security Projection

```yaml
public_material_policy: private-by-default
raw_material_policy: never-commit
secret_storage: environment-or-password-manager-only
memory:
  source_policy: private-by-default
  public_mirror: index-only
  collaboration_policy: private-pr-or-owner-approved-extract
  allowed_public_exports: approved-facts, redacted-summaries, abstracted-patterns
  raw_material_policy: never-copy-raw-private-bodies
github:
  config: integrations/github.yml
  token_policy: do-not-store
feishu:
  config: integrations/feishu.yml
  token_policy: do-not-store
rule: 不提交 token、app_secret、cookie、refresh token、私钥或原始私密资料。
```

## Meta Skill Projection

No meta skill artifacts found.
