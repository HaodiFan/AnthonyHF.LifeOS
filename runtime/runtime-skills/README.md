# Runtime Skills

这里记录 AnthonyHF.LifeOS 运行期可调用或正在验证的 skills。

Runtime skill 可以有两种形态：

- 本仓库内的轻量 manifest：`runtime/runtime-skills/<skill-id>/manifest.yml`
- 外部 repo：LifeOS 只保存 source、权限边界、输入输出、运行证据位置和 promotion gate。

现有入口包括：

- `runtime/runtime-skills/snapaf/manifest.yml`
- `docs/skill-system/runtime-skill-candidates.md`
- `identity/wenxin/skill-recommendations.yml`

Runtime skill 负责执行任务和产生日志；升级为稳定 meta skill 前需要 IPO Reverse、owner alignment 和 privacy review。
