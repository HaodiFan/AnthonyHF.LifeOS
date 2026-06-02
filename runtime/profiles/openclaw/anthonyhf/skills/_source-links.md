# OpenClaw Skill Source Pointers

OpenClaw workspace skills are exposed through real adapter `SKILL.md` files so discovery works even when sandboxing ignores symlinks that escape the workspace.

旧版 projection 曾生成 `_source-links/` advisory symlinks。schema v2 不再保留这些 symlink，因为它们容易指向已迁移的 `skills/` 旧目录并造成重复结构错觉。

Canonical sources are:

- root router: `SKILL.md`
- self-evolution organ systems: `evolution/organ-systems/`
- stable capabilities: `capabilities/`
- migration docs: `docs/migration/`

Adapters are runtime entrypoints. Canonical behavior remains in LifeOS sources.
