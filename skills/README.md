# Skills 能力层

这一层只放真正的 Skill 包。

规则：`skills/` 可以有容器目录，但每条分支最终必须落到一个 `SKILL.md`。不是 Skill 的推荐列表、总结、数据绑定、source metadata、候选说明和 runtime 投影不要放在这里。

## 当前 Skill

- `engineering-everything/SKILL.md`：Anthony 的构建型工程判断 Skill。
- `self-evolution/cognitive-alignment/SKILL.md`：认知对齐与分歧复盘 Skill。
- `self-evolution/wenxin/SKILL.md`：问心 Skill。
- `self-evolution/psp/SKILL.md`：PSP Skill。
- `self-evolution/ipo-reverse/SKILL.md`：IPO Reverse Skill。

## 非 Skill 产物位置

- 推荐 Skill 列表：`identity/wenxin/skill-recommendations.yml`。
- Skill 总结和能力说明：`identity/wenxin/skill-summaries/`。
- Skill 读取 memory/wiki/source 的边界和依赖声明：`cognition/skill-bindings/`。
- factory bridge / source update metadata：`integrations/skill-sources/`。
- 候选 runtime Skill 说明：`docs/skill-system/`。

## Placement Policy

- 新能力只有形成可执行或可路由的 `SKILL.md` 后才进入 `skills/<skill-id>/`。
- 事实、偏好、长期上下文不写进 Skill；通过 `memory/`、配置的 memory wiki 或 `cognition/skill-bindings/` 查询。
- 推荐、总结和证据门控先留在 Wenxin 层，经过 IPO Reverse、owner alignment 和 privacy review 后再提升为真实 Skill。
