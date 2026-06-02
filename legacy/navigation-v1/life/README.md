# Life 导航层

这一层是给人看的 AnthonyHF.LifeOS 主入口。

它不新增真相源。这里原本用 symlink 把 v1/v1.5 目录重新排成一条线；schema v2 后 symlink 已删除，只保留历史说明。

```text
identity
-> identities
-> metabolism
-> runtime
-> work
-> evolution
-> capabilities
```

## 入口

- `identity/`：我是谁，Wenxin、PSP、Soul、公开 profile。
- `identities/`：我在不同社会身份中的边界和任务上下文。
- `metabolism/`：GitHub、Feishu、聊天、文档等待消化、处理和抽取。
- `runtime/`：真实 session、runtime skill、runtime lesson。
- `work/`：产出物、项目、报告、文章和工作场景索引。
- `evolution/`：IPO Reverse、对齐复盘、自我更新过程。
- `capabilities/`：已经沉淀的稳定能力和能力地图。
- `identity/memories/`：长期记忆入口和 memory wiki 配置。

当前工具和 agent 应读取根目录的 schema v2 canonical paths；本目录只用于解释历史迁移。
