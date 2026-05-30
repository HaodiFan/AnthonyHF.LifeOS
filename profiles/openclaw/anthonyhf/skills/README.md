# Runtime Skills

Runtime Skill 负责执行具体任务。

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

Put fact dependencies in `skills/bindings/data-sources.yml`.
