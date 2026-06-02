# Capabilities 能力层

这里记录 AnthonyHF.LifeOS 当前可调用、候选、已验证和待提升的能力。

现有能力与候选入口包括：

- `capabilities/engineering-everything/`
- `capabilities/publication/public-narrative-system/`
- `runtime/runtime-skills/`
- `docs/skill-system/runtime-skill-candidates.md`
- `identity/wenxin/skill-recommendations.yml`
- `identity/cognition/skill-bindings/data-sources.yml`

能力说明不复制个人事实、客户信息或私密上下文；需要事实时通过 memory 或 data source binding 读取。

新能力只有形成稳定边界、证据、输入输出、验收标准和可路由入口后，才进入 `capabilities/<capability-id>/`。如果该能力需要可执行 Skill，可以在能力目录中提供 `SKILL.md`。`capabilities/memory/` 是能力层知识库，不是 capability package；top-level 不再使用 `skills/`，历史材料保留在 `legacy/skills-v1/`。
