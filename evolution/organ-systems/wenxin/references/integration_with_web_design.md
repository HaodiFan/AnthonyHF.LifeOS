# 和 web-design skill 的接力协议

「问心」与 `web-design` skill 的协同机制。

## 设计哲学：两个独立 skill，定义清楚的接力协议

不绑定、不耦合、不强制——通过**标准化文件**接力。

```
「问心」                       「web-design」
─────                          ─────
评估 ta 是谁          ──→     把 ta 的"是谁"做成网站
↓                              ↑
WENXIN_REPORT.md     ────→    PRD.md（自动识别）
（标准化协议）
```

### 为什么不融合

- 单一职责（每个 skill 只做一件事）
- 用户可以选择只跑评估 / 只做网站 / 两个串起来
- 接力协议可以被任何工具消费（不只是 web-design）
- 两个 skill 各自独立迭代

## 新的网页实现硬约束

如果下游要把 `WENXIN_REPORT.md` 做成网站，默认视为以下要求已经写进 PRD：

- 动画引擎：**GSAP**
- 叙事方式：**scroll 驱动**
- 呈现方式：**渐进式展开**
- 信息架构：**总览在前，细节随 scroll 分层释放**

这不是"可选风格建议"，而是默认实现约束。除非用户明确推翻，否则 web-design 或任何接力工具都应按此执行。

---

## 接力流程

### Step 1: 用户跑「问心」

按阶段 0-6 完整走完，输出：
- HTML / PDF / 长图（人类可读产物）
- **`WENXIN_REPORT.md`**（标准化协议，给下游消费）

### Step 2: 用户决定要做个人网站

用户在 Claude 里说："把我的问心报告做成个人网站"。

或者：用户已有 web-design skill，正常调用，web-design 自动检测项目目录里的 `WENXIN_REPORT.md`。

### Step 3: web-design 启动 Phase A4 (PRD 驱动)

web-design 的 SKILL.md 说："启动时自动扫描项目根目录"，按优先级：
1. `PRD.md` / `prd.md`
2. `SPEC.md` / `spec.md`
3. `README.md` 或任何 `.md` — 若含「产品定位 / Target Users / Pages」等关键字段

**`WENXIN_REPORT.md` 完全符合 web-design 的 Phase A4 协议**——它有结构化的字段，能被识别为 PRD。

### Step 4: web-design 自动消费 WENXIN_REPORT.md

web-design 从 `WENXIN_REPORT.md` 提取：

| WENXIN 段落 | 对应 web-design 字段 |
|---|---|
| 身份层 → 外号-接地气版 | Hero H1（巨大字号） |
| 身份层 → 一句话定位 | Hero 副标题 |
| 身份层 → 真实主线 (对外) | About 正文 |
| 雷达图 | "能力概览" section（如果用户要） |
| 核心壁垒 | "核心优势" section（用 web-design 的"3 个卧槽爆点"原则） |
| 里程碑 | "Timeline" / "经历" section |
| 卖点三段 | Hero 子标题 / Pitch section |
| 软实力质地 | About 隐藏深度 / Quote 风格的小段 |
| **给 web-design 的设计建议** | ⭐ Phase A 的风格输入（直接消费） |

除此之外，还应自动继承以下页面编排原则：

- 首页首屏只展示总判断，不在第一屏塞入全部信息
- 主要信息区按 scroll 分段 reveal
- 关键 section 间用 GSAP timeline 和 scroll trigger 做转场
- 报告页要像叙事阅读，而不是一张静态长简历

### Step 5: web-design 补充用户信息（接力的另一半）

「问心」**不问**联系方式 / 头像 / 项目列表（保持纯粹）。这些由 web-design 在 Phase C 收集：

```
web-design：我从 WENXIN_REPORT.md 读到了你的画像。但要做网站还需要补充：

            📷 头像照片：用什么？（我会帮你处理）
            🔗 联系方式：邮箱 / GitHub / X / LinkedIn / 微信？
            📁 项目列表：你想展示哪几个项目？（标题 + 一句话 + 链接）
            🎨 风格选择：「问心」推荐了 [X / Y / Z] 三种风格，你倾向哪个？
            🎬 交互档位：L1 (轻 GSAP) / L2 (scroll narrative) / L3 (沉浸式 scroll story)？

            [用户回答]

            [生成 DESIGN.md → 生成网站]
```

---

## 标准目录结构

```
my-personal-site/
├── README.md                      # 项目说明 + 部署指引
├── WENXIN_REPORT.md               # ⭐ 「问心」标准产物（给 web-design 读）
├── DESIGN.md                      # web-design 生成的设计规范
├── archive/                       # 「问心」历史版本
│   ├── 2026-05-03.md
│   └── 2026-12-15.md
├── public/                        # ⭐ Vercel 部署目录
│   ├── index.html                 # 个人网站首页（web-design 生成）
│   ├── about.html                 # 关于
│   ├── projects.html              # 项目
│   ├── report.html                # 完整问心报告
│   ├── report.pdf
│   ├── poster.png                 # 长图
│   ├── compare.html               # 版本对比页（持续迭代后）
│   └── assets/                    # 头像 / 项目截图 / 等
├── poster-template/               # 长图模板
│   ├── poster.html
│   └── finalize.py
├── scripts/
│   ├── compare_versions.py        # 生成 compare.html
│   ├── update.py                  # 持续迭代主入口
│   └── deploy.sh
└── vercel.json
```

---

## URL 结构（Vercel 部署后）

```
https://yourname.vercel.app/              ← 个人网站首页（精心设计）
https://yourname.vercel.app/about         ← About 页
https://yourname.vercel.app/projects      ← 项目
https://yourname.vercel.app/report        ← 完整问心报告
https://yourname.vercel.app/report.pdf    ← PDF 直接下载
https://yourname.vercel.app/compare       ← 版本对比页
https://yourname.vercel.app/poster        ← 长图直接查看
```

## 页面叙事建议

默认不要把全部内容压在一个 HTML 页面里平铺到底。更合理的是：

- `/`：首页，负责第一印象和总览
- `/report`：完整问心报告，负责深读
- `/compare`：版本变化

其中首页本身也不是"一屏讲完"，而是：

1. 第一屏只给总览
2. 用户 scroll 后，逐段进入能力图谱 / 壁垒 / 里程碑
3. 再继续 scroll，才进入更私人、更深的诊断内容

如果用户坚持单页，也必须做成**scroll narrative**，不能做成传统长简历排版。

### 长图二维码 → 指向 `/`（首页）

之前版本的二维码直接跳到报告页——**太突兀**。现在指向首页，让访客先看到精心设计的个人网站，再深入看完整评估。

---

## 网站同步策略

每次「问心」持续迭代后处理：

| 文件 | 同步策略 | 理由 |
|---|---|---|
| `public/report.html` | **自动同步**：每次更新都自动重生成 | 报告页就是评估的视觉化，必须跟着评估走 |
| `public/report.pdf` | **自动同步** | 同上 |
| `public/poster.png` | **自动同步**（外号变化才重生成长图） | 同上 |
| `public/compare.html` | **每次都自动生成** | 对比页是迭代的核心产物 |
| `public/index.html`（首页） | **手动确认**：仅提示，由用户决定 | 首页是用户精心设计的个人品牌，不应自动改动 |

### 给用户的提示

```
✓ public/report.html 已更新
✓ public/report.pdf 已更新
✓ public/poster.png 已更新（外号未变 → 只更新水位）
✓ public/compare.html 已生成

⚠️ public/index.html (个人网站首页) 没有自动更新。

  这次更新可能影响首页的部分：
  - Hero 区的水位数字
  - 里程碑时间线（新增了 1 项）
  - 卖点三段（[列出有变化的部分]）

  要不要重新跑 web-design 更新首页？(yes/no)
```

---

## 给 web-design 的"设计建议"段：风格推导

「问心」生成 WENXIN_REPORT.md 时，必须**主动推导**风格调性候选（弱推荐）。

### 推导逻辑

基于人物特征 → 风格映射：

| 人物特征 | 推荐风格 | 推荐参照站 |
|---|---|---|
| 长期主义 + 工程深度 + 学术气质 | Cream Editorial / Minimal Pure | stripe.com / linear.app / cohere.com |
| 连续创业 + 反共识 + 科技 | Dark Tech / Editorial | x.ai / cursor.sh / vercel.com |
| 创意 + 美学敏感 + 视觉强 | Bold Typography / Brutalist | apple.com / figma.com / runwayml.com |
| 学者 / 研究者 / 内向 | Cream Editorial / Minimal Pure | mintlify.com / sanity.io |
| 销售 / 商业 / 外向 | Confident / Bold | stripe.com / wise.com |
| 苦行僧 / 修行 / 极致简洁 | Minimal Pure / Mono | claude.com / x.ai |
| 多元 / 跨域 / 不可定义 | Editorial 混搭 | notion.so / pinterest.com |
| 创意工作者 + 个性强 | 风格化 + 个人色彩 | figma.com / runwayml.com |

### 输出格式

`WENXIN_REPORT.md` 的"给 web-design 的设计建议"段应该包含：

```markdown
## 给 web-design 的设计建议

### 风格调性候选（按推荐度排序）

1. **Dark Editorial（暗黑编辑）** — 推荐度 ⭐⭐⭐⭐⭐
   理由：用户的"苦行僧"气质 + 长期主义 + 工程深度，配深色克制风格最匹配。
   参考：x.ai / linear.app

2. **Minimal Pure（极简纯净）** — 推荐度 ⭐⭐⭐⭐
   理由：苦行僧的"极致简洁"也可以走亮色极简方向，对个人网站更友好。
   参考：cohere.com / claude.com

3. **Cream Editorial（奶油编辑）** — 推荐度 ⭐⭐⭐
   理由：如果用户希望"温暖一些 / 不那么硬"，这个方向也可以。
   参考：mintlify.com

### 推荐参照站
- linear.app: 配色克制，工程感强，适合 CTO 调性
- x.ai: 反共识 + 工程派的代表
- cohere.com: 学术 + 工程的混搭

### 必须包含的内容板块
- Hero（巨字外号 + 一句话）
- 真实主线（About 正文）
- 4 个核心壁垒（用爆点原则展示）
- 时间线（里程碑）
- 完整问心报告链接（不显眼地放 footer）

### 动效与信息释放
- 必须使用 GSAP
- 首屏只承载总览，不一次放完所有模块
- 用 scroll trigger 让内容按层级依次进入
- 核心壁垒和里程碑优先做 scroll 驱动的分段转场
- 长段文字不要整屏同时出现，要按块 reveal

### 应该避开的
- 不要做成"传统简历"风格（违背"绕过标签"的精神）
- 不要堆 emoji / 不要 Playful 风格（和"苦行僧"调性冲突）
- 不要用过度饱和的渐变 / 霓虹色
```

---

## 常见问题

### Q1: 用户不想用 web-design 怎么办？

完全可以——`WENXIN_REPORT.md` 是开放协议。用户可以：
- 自己用任何工具读取这份 Markdown
- 把它扔给 GPT / Cursor 让它写网站
- 手动复制内容到自己模板

### Q2: web-design 没有 PRD 字段读取怎么办？

`WENXIN_REPORT.md` 完全符合 web-design Phase A4 的字段要求。如果 web-design 因为版本问题没识别，**用户可以手动指引**：

```
Claude，读取 WENXIN_REPORT.md 作为 PRD，启动 web-design 给我做个人网站
```

### Q3: 多人用同一个目录怎么办？

每个人开自己的 repo / 项目目录。「问心」 + web-design 都假设"一个目录 = 一个用户"。

### Q4: 历史归档版本要不要也部署上线？

**默认不部署**。`archive/` 是私有的，不在 `public/` 里。

如果用户想分享"我的成长史"，可以选择性把某些 archive 渲染成 HTML 放上线。

---

## 与未来其他 skill 的接力

`WENXIN_REPORT.md` 协议是**开放**的。未来可能有：

- **简历生成 skill**：读 WENXIN_REPORT.md → 生成 LaTeX / PDF 简历
- **BP 生成 skill**：读 WENXIN_REPORT.md → 生成融资 BP
- **播客 bio 生成 skill**：读 WENXIN_REPORT.md → 生成不同长度的 bio
- **Twitter / X bio 优化器**：读 WENXIN_REPORT.md → 生成 160 字以内的 bio

只要新工具支持读 `WENXIN_REPORT.md` 协议，就能加入这个生态。

---

## 迭代记录

| 日期 | 改动 |
|---|---|
| 2026-05-03 | 初始版本 |
