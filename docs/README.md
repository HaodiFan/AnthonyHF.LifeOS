# Docs 展示文档

这一层只保留对外展示和解释材料，不再作为 GitHub Pages 首页源码。

当前内容：

- `assets/anthonyhf-readme-cover.png`：README 顶部使用的“个人数字分身接口”封面图，用来让普通人快速看懂入口文件、核心模块、当前实例和底层组件。图里大卡片是模块名，小徽章是 AnthonyHF 当前实例，例如 `Memory -> approved summaries`、`Skills -> engineering-everything`、`Identity -> 问心报告 / PSP`。
- `file-structure-policy.md`：schema v2 文件边界、trim 规则和重复保留策略。
- `file-role-inventory.yml`：每个当前文件的层级、类别、作用和重复保留理由；这是审计表，不是真相源。
- `layer-file-review.md`：按层级汇总文件作用、trim 决策和仍允许保留的重复。
- `schema-trim-completion-audit.md`：schema trim 完成审计，逐项列出要求、证据和结果。
- `user-guide.md`：用户说明书，说明这个 repo 看什么、能得到什么、哪些不是普通用户入口。
- `avatar-page-information-architecture.md`：第三人称 avatar 页面应该介绍哪些层级、字段、当前产物和缺口。
- `evidence-sufficiency.md`：证据充分性和成熟度说明。
- `lifeos-content-review.md`：内容完备度和下一步 review。

GitHub Pages 首页现在由 `work/apps/homepage/` 下的 Vite React 应用生成：

- `work/apps/homepage/index.html`
- `work/apps/homepage/src/`
- `work/apps/homepage/components/ui/story-scroll.tsx`
- `work/apps/homepage/public/assets/`

这里放的是说明材料，不是真相源。身份真相源在 `identity/`，能力真相源在 `capabilities/`，长期记忆入口在 `identity/memories/` 或配置的外部 memory wiki。
