# Default Skills

`integrations/skill-sources/default-skills/` 保存 openLifeOS bridge/source update metadata，不是完整 self-evolution Skill 仓库，也不是用户后续蒸馏出来的个人能力仓库。

当前说明：

- 完整 Wenxin Skill 已安装在 `evolution/organ-systems/wenxin/`。
- 完整 PSP Skill 已安装在 `evolution/organ-systems/psp/`。
- 完整 IPO Reverse Skill 已安装在 `evolution/organ-systems/ipo-reverse/`。
- 不要在 `integrations/skill-sources/default-skills/` 下放同名 Skill 副本；runtime skill 放在 `runtime/runtime-skills/<skill-id>/manifest.yml` 或外部 repo，稳定能力放在 `capabilities/<capability-id>/SKILL.md`。

用户自己的 runtime skill 默认进入 `runtime/runtime-skills/`；distilled meta skill 默认进入 `capabilities/`。
