---
name: public-narrative-system
description: AnthonyHF 的公开叙事系统、内容产品化与产品传播资产化 meta skill。用于把 Anthony 的聊天想法、创业判断、产品矩阵、生命系统实验、数字分身、AI-native organization、公开身份、方法论和产品物料，沉淀成可跨渠道复用的叙事资产、intake、系列 brief、产品页、口播稿、文章、封面文案、发布检查和复盘模式。适用于 RedNote/小红书、视频口播、公众号、官网、产品页、路演文案、朋友圈、短视频脚本等渠道；渠道是输出面，不是 skill 边界。触发词包括公开叙事、内容系统、内容产品化、口播、写文章、产品宣传、产品矩阵、生命系统实验日记、开发公司、自进化企业、basebuilder、openLifeOS、cowdy studio、硬件体系。
version: 0.6.0
---

# Public Narrative System / 公开叙事系统

这个 skill 负责 Anthony 的公开叙事与内容资产化闭环。

它不是“小红书文案 skill”。小红书、RedNote、公众号、官网、朋友圈、视频口播、路演文案都只是渠道。真正的上层能力是：

```text
真实经历 / 产品进展 / 方法论判断
-> 可追踪 intake
-> 公开叙事资产
-> 渠道化表达
-> 发布复盘
-> 反哺产品与 AnthonyHF
```

当前主要落地仓库：

```text
/Users/anthonyf/Documents/publication/red-note
```

## 使用场景

- 用户要写公开内容：口播、文章、短视频脚本、产品页、官网文案、朋友圈、小红书、公众号、路演话术。
- 用户给一段聊天上下文，希望萃取成 intake 或长期叙事资产。
- 用户更新系列主线、产品矩阵、产品物料背景、公开定位或产品传播口径。
- 用户需要把某次共创经验沉淀成可复用的内容生产流程。
- 内容涉及 `生命系统实验日记`、数字分身、AI-native organization、产品矩阵、Anthony 的创业判断或公开身份。

## 判断先行

开写前先内化四件事，必要时简短说出来：

1. **叙事层级**：这是单篇内容、系列主线、产品叙事、公开身份，还是长期方法论？
2. **资产对象**：intake、series、product page、draft、article、cover、snippet、published record、pattern。
3. **来源路由**：要读哪些 `meta/`、`series/`、`products/`、`metabolism/inbox/`、AnthonyHF identity/memory 文件。
4. **公开风险**：是否涉及客户、内部路线图、未确认数字、私密人格材料、硬件采集边界或融资/GTM 敏感内容。

## Repo 读写顺序

进入 publication repo 后优先读：

1. `meta/voice.md`
2. `meta/claims-policy.md`
3. 相关 `series/<series>/series-brief.md`
4. 若涉及产品，读 `products/README.md` 和目标产品页
5. 相关 `metabolism/inbox/*.md`
6. 目标 draft、article 或 channel artifact

如果内容以 Anthony 第一人称发出，或用户反馈“语气不像我”，必须再读：

```text
identity/psp/anthony-fan/PSP.md
references/psp-voice-adapter.md
references/humanizer-zh-adapter.md
```

PSP 只用于公开/工作语气、判断方式和语言指纹适配；不要把 PSP 原文、私密证据、会议转写或完整人物模型复制到 publication repo。

`humanizer-zh-adapter.md` 用于最后一层去 AI 腔：删除填充、机械对比、三段式、宣传腔、模糊归因和变量清单。它不能抹平 Anthony 的工程判断密度。

如果用户明确指定渠道，或产物明显属于某个渠道，再读取对应 channel reference：

| Channel | Reference | When |
|---|---|---|
| RedNote / 小红书 | `references/channels/rednote.md` | 小红书、RedNote、口播首发、封面、标签、互动、平台风险检查 |

后续新增公众号、官网、朋友圈、路演等渠道时，也按 `references/channels/<channel>.md` 组织技巧。主 `SKILL.md` 只保留路由和跨渠道原则，不堆渠道细节。

## 产物路由

| 用户输入 | 写入位置 | 规则 |
|---|---|---|
| 原始想法、聊天上下文、标题讨论 | `metabolism/inbox/YYYY-MM-DD-*.md` | 保留触发、核心判断、可展开观点、风险 |
| 系列定位、主线目标、选题地图 | `series/<series>/` | 更新 brief、episode map、visual system |
| 产品介绍、宣传图、文章入口 | `products/<product>/` | 放对外安全口径和物料入口，不放原始私密材料 |
| 渠道稿件 | `drafts/active/` 或产品/系列 articles | 生成 frontmatter、短版/长版、标题、封面、风险检查 |
| 可复用短文案 | `products/<product>/snippets/` 或 `prompts/` | 保持来源路由和使用场景 |
| 发布后复盘 | `posts/published/` 或 `memory-bank/` | 记录链接、数据、复盘、可复用模式 |

## 内容生产协议

写公开内容时按这个顺序：

1. 从 intake 或用户输入抽一个核心判断，不要堆概念。
2. 选一个真实触发场景作为开头。
3. 用 Anthony 的工程化表达推进：判断 -> 原因 -> 系统结构 -> 现实意义。
4. 如果要带产品，先讲问题，再讲产品层，最后回到真实实验，不硬广。
5. 按渠道产出适配版本：
   - 60-75 秒口播短版
   - 2 分钟口播完整版
   - 图文/长文结构
   - 标题池
   - 封面主标题 + 副标题
   - 渠道标签、互动问题、soft CTA
   - 方法论映射：说明内容分布如何对应所用方法论
   - 发布前风险检查

每个正式 draft 必须补充 `Content Method Mapping / 方法论映射` 区块。这个区块不面向最终观众，服务于审稿和迭代，必须说明：

```text
结构位置 / 发布资产
-> 当前具体内容
-> 当前表达方式
-> 承担作用
-> 对应方法论模块和位置
-> 待用户确认 / 可替换点
```

这个表的核心用途是帮助用户分开确认：

```text
结构是否认同
具体内容是否准确
表达方式是否像 Anthony
承担作用是否成立
哪些格子需要替换
```

不要只写“用了什么方法论”。必须把结构、具体内容、表达方式、承担作用拆开写，方便用户指出“结构保留，但这一格内容换掉”或“内容对，但表达不像我”。

优先映射这些方法论：

- RedNote 8 层：第一眼包装、认知钩子、真实场景、身份投射、结构化获得感、可信证据、互动入口、系列化记忆点。
- 四维 hook：打断预测、奖励期待、损失厌恶、精准命名。
- 爆款口播案例模式：通用承诺、具体场景、普通做法/进化做法、差异命名、目的回收。
- Anthony voice / humanizer：判断先行、正向定义、系统状态变化、真实归因、实验边界、去防守式否定。
- 产品叙事：真实实验 -> 暴露问题 -> 对应产品层 -> 解释产品存在原因 -> 回到共演化。

RedNote/XHS 输出要额外读取 `prompts/channels/rednote.md`，并在 publish-ready 前运行：

```bash
node scripts/check-rednote-risk.mjs drafts/active/<draft>.md
```

RedNote 的具体技巧、标题模式、互动边界、风险类型见 `references/channels/rednote.md`。

Anthony 本人口播或第一人称文章必须先过 PSP voice adapter，再做渠道化。顺序是：

```text
PSP 判断/语气保真 -> public narrative structure -> Anthony humanizer pass -> channel packaging
```

Anthony humanizer pass 借鉴 `op7418/Humanizer-zh` 的 AI 写作痕迹检查，但只保留适合 Anthony 的部分：直接判断、真实归因、具体机制、去填充、去宣传腔、去机械清单。

## 系列编号规则

正式集数只按真实发布顺序和用户明确指定编号确定。不要为了世界观完整性、开场稿或预设选题地图自动占用 `#001`；未发布的开场、预告、置顶说明应放入 backlog 或 prelude candidate，不占 episode number。

## 产品叙事规则

产品出现必须来自真实系统问题：

```text
真实实验 -> 暴露问题 -> 对应产品层 -> 解释产品存在原因 -> 回到共演化
```

四个产品的默认关系：

```text
BaseBuilder = 给 Agent 建业务环境
openLifeOS = 给数字分身建长期灵魂系统
Cowdy Studio = 让数字分身上岗协同
硬件体系 = 让数字分身进入现实世界
```

不能说：

- “最强 AI 工具”
- “已经完成企业自进化系统”
- 未确认的客户数、营收、ROI、续约率
- 客户、会议、内部路线图、GTM 细节

## 渠道观

渠道不决定 skill 边界。

- 小红书 / RedNote：适合口播、封面、系列化实验记录；技巧放在 `references/channels/rednote.md`。
- 公众号：适合长文、方法论和产品叙事展开。
- 官网 / 产品页：适合稳定定位、产品结构、案例和 CTA。
- 朋友圈：适合创业阶段观察、轻量观点、发布记录。
- 路演 / 销售材料：适合价值证明、why-us、产品矩阵和交付口径。

## 完成检查

收尾时说明：

- 更新了哪些文件
- 是否运行了检索/校验
- 是否补了 `Content Method Mapping`
- 哪些材料仍需用户确认
- 是否需要 commit/push

## References

- `references/publication-repo-map.md`：publication repo 当前结构和路由。
- `references/psp-voice-adapter.md`：从 Anthony PSP 提炼的公开写作/口播语气适配规则。
- `references/humanizer-zh-adapter.md`：融合 `op7418/Humanizer-zh` 后的 Anthony 去 AI 腔检查。
- `references/lessons.md`：公开叙事协作中的单次纠偏记录。
- `references/channels/rednote.md`：RedNote/小红书渠道技巧、发布包、风险检查和 Anthony 账号边界。
