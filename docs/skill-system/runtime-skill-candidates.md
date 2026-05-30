# Runtime Skills

Runtime Skill 负责执行具体任务。

当前 AnthonyHF.LifeOS 不再使用 `identity/wenxin/skill-recommendations.yml` 作为候选区。候选 Skill 先进入 `identity/wenxin/skill-recommendations.yml`；只有形成真实 `SKILL.md` 后才进入 `skills/<skill-id>/`。

A runtime skill may contain:

- when to use;
- procedure;
- tool and connector requirements;
- scripts and templates;
- validation gates;
- pitfalls and recovery steps.

A runtime skill must not embed:

- private user facts;
- long-term preferences;
- raw evidence;
- project memory that belongs in `memory/`.

Put fact dependencies in `cognition/skill-bindings/data-sources.yml`.
