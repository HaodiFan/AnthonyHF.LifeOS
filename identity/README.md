# Identity 身份层

这一层回答：“Anthony 到底是谁？”

它不是能力库，也不是知识库，而是数字分身的身份根目录。这里放三类材料：

- `public-profile/`：只放可公开的客观身份配置，例如公开账号、主页、公开联系方式说明。
- `wenxin/`：问心 Skill 的产出物，用来支持对外定位、履历、个人 BP 和 README 展示。
- `psp/`：PSP 方法的产出物，用来描述分身内核、判断方式、边界和行为倾向。

账号密码、Token、API Key、私密证件、合同、聊天记录不属于这一层，也不进入公开仓库。

## Current Active Registry

- `current.yml` 是 Identity 层的机器可读 active 指针。
- `wenxin/WENXIN_REPORT.md` 和 `psp/anthony-fan/PSP.md` 是人类可读 current entrypoint。
- `wenxin/WENXIN-<timestamp>.md` 和 `psp/<person_id>/PSP-<timestamp>.md` 是版本化产物。
- `versions.yml` 记录 artifact lineage；`changelog.md` 记录为什么激活新版本。

更新规则：先基于当前 active artifact 生成新时间戳产物，再更新 current entrypoint、versions ledger、changelog 和 `identity/current.yml`。不要直接覆盖 current 文件而不留下版本记录。
