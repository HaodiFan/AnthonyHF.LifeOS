# Runtime Skills

Runtime Skill 负责执行具体任务。

候选 Skill 可以先进入 `identity/wenxin/skill-recommendations.yml`，也可以在 `runtime/runtime-skills/<skill-id>/manifest.yml` 记录外部 repo 或本地 runtime 绑定。只有形成稳定边界、证据、输入输出和验收标准后，才升级到 `capabilities/<capability-id>/`。

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
- project memory that belongs in `identity/memories/` or an external memory wiki.

Put fact dependencies in `identity/cognition/skill-bindings/data-sources.yml`.
