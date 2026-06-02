# System 支撑层

这一层是给维护者和 agent 看的 AnthonyHF.LifeOS 支撑系统。

它原本收纳 v1/v1.5 中分散在顶层的协议、索引、投影、工具和安全边界。schema v2 后 symlink 已删除，只保留历史说明：

- `capabilities/`：稳定能力；可执行能力入口可在 capability 内提供 `SKILL.md`。
- `evolution/organ-systems/`：Wenxin、PSP、IPO Reverse 等能力生产系统。
- `artifacts/`：latest registry 和 active artifact 指针。
- `identity/cognition/`：认知对象 taxonomy、data contracts、skill bindings。
- `integrations/`：GitHub、Feishu/Lark、Hermes、data source 边界。
- `security/`：禁入材料、secret 策略和公开边界。
- `docs/`：evidence gate、迁移说明、公开展示材料。
- `runtime/profiles/`：OpenClaw / Hermes runtime projection。
- `integrations/agents/`：agent UI metadata。
- `work/apps/`：public homepage 等展示应用。
- `legacy/scripts/`：实例历史维护脚本；factory 脚本在 openLifeOS 根目录 `scripts/`。

如果只是理解 AnthonyHF 这个数字生命体，应先看根目录 `LIFEOS-CATALOG.html` 和 `docs/file-structure-policy.md`；如果要调试、验证、发布或迁移，再看当前 v2 canonical paths。
