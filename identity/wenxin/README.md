# Wenxin 问心对外定位

这一层存放问心 Skill 产出的对外定位材料。

问心回答的是：“别人应该如何理解我？”

当前产出物：

- `WENXIN_REPORT.md`：当前 active Markdown entrypoint。
- `WENXIN-20260530-235550.md`：当前 active timestamped snapshot。
- `versions.yml`：问心产物版本 ledger。
- `changelog.md`：问心 active 变更记录。
- `wenxin-report-continuous-founder-ascetic.pdf`：问心报告《连续创业的苦行僧》，用于 README 的“我是谁”、对外履历、个人 BP 和公开叙事。

问心产物属于 Identity 层，但它不是 PSP。问心偏对外表达，PSP 偏分身内核。

问心 Skill 的源仓库现在作为自我更新工具接入在：

- `evolution/organ-systems/wenxin/`

当需要重新整理 Anthony 的公开定位、履历叙事或个人 BP 时，先读这个 Skill，再决定是否更新本目录下的公开产物。

更新规则：新问心报告必须基于当前 active artifact 叠加生成，先写入 `WENXIN-<timestamp>.md`，再同步 `WENXIN_REPORT.md`、`versions.yml`、`changelog.md` 和 `../current.yml`。项目/交付物证据优先进入问心，私密正文只能进入脱敏 evidence summary。
