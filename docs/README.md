# Docs 展示文档

这一层只保留对外展示和解释材料，不再作为 GitHub Pages 首页源码。

当前内容：

- `assets/anthonyhf-readme-cover.png`：README 顶部使用的“个人数字分身接口”封面图，用来让普通人快速看懂入口文件、核心模块、当前实例和底层组件。图里大卡片是模块名，小徽章是 AnthonyHF 当前实例，例如 `Memory-Wiki -> AF-wiki`、`Skills -> engineering-everything`、`Identity -> 问心报告 / PSP`。

GitHub Pages 首页现在由 `apps/homepage/` 下的 Vite React 应用生成：

- `apps/homepage/index.html`
- `apps/homepage/src/`
- `apps/homepage/components/ui/story-scroll.tsx`
- `apps/homepage/public/assets/`

这里放的是说明材料，不是真相源。身份真相源在 `identity/`，能力真相源在 `skills/`，长期记忆真相源在 `memory/`。
