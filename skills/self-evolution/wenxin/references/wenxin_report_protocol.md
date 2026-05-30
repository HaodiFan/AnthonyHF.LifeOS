# WENXIN_REPORT.md · 接力协议详细规则

「问心」的标准化输出文件。给下游工具（web-design / 简历生成器 / 个人 BP 工具 / 任何消费者）读取。

## 设计哲学

### 为什么需要这个文件

之前「问心」的输出是 HTML / PDF / 长图——**人类可读，但下游工具不可读**。

下游工具要消费需要结构化数据。但是：
- **JSON 太死板**——失去"用户能阅读 / 修改"的属性
- **完全自由的 Markdown 无法机读**——下游工具不知道哪段是雷达图哪段是壁垒

**协议解法**：用 **Markdown + frontmatter + 严格段落标题**——既人类可读、用户可手动改、下游工具也能稳定提取字段。

### 核心原则

1. **frontmatter 提供元数据**（schema 版本 / 生成时间 / 外号 / 索引字段）
2. **段落标题严格固定**（不允许变化，下游工具按标题识别区段）
3. **段落内容相对自由**（可以是表格、列表、自然段，下游工具按段处理）
4. **"持续迭代记录"段是 append-only**（永远向下追加，不修改历史条目）

---

## 完整字段规范

### Frontmatter（必填）

```yaml
---
schema: wenxin-report           # 固定值，标识此文件是 wenxin 协议
version: 1.0                    # 协议版本（不是用户的版本）
generated_at: 2026-05-03        # 首次生成时间
last_updated: 2026-05-03        # 最近更新时间（增量更新时改这里）
nickname: 连续创业的苦行僧       # 接地气版外号（搜索 / 索引用）
nickname_serious: 连续创业的全栈 CTO  # 严肃版（可选）
---
```

### 段落 1: 身份层（必填）

```markdown
## 身份层

- 外号-接地气版: [killer 外号]
- 外号-严肃版: [精炼版]
- 一句话定位: [一句话描述，30-60 字]
- 真实主线 (对外): [对外可用的人物主线]
- 真实主线 (对内): [真实驱动的内核，可能和对外不同]
- 外号为什么成立: [1-2 句。说明它压缩了哪条全人生迁移链，为什么既让人记住，又对应真实稀缺价值]
- 外号稀缺性判断: [全国少见 / 全球少见 / 普通；必须给事实依据]
```

下游工具的关键消费场景：
- **网站 Hero**：用"外号-接地气版" + "一句话定位"
- **简历 Title**：用"外号-严肃版"
- **About 页正文**：用"真实主线 (对外)"
- **个人独白 / 博客 bio**：可以用"真实主线 (对内)"

### 段落 2: 雷达图（必填）

```markdown
## 雷达图

| 维度 | 来自人物 | 水位% | 证据 |
|---|---|---|---|
| 浪潮判断力 | 季逸超 | 85% | 2021 离开 NVIDIA / 2024 抢 GUI agent 数据窗口 / 2026 转 AI 落地 |
| 阅读纪律 | P. Collison | 90% | 6 年每日 2.5h + 周末，累计 7350+ 小时定向学习 |
...

**整体形状**: 双钉子型 — [一句话描述形状的含义]
```

下游工具关键消费：
- **网站的"能力概览"section**：直接重用此表
- **PDF / 报告页**：渲染成 SVG 雷达图
- **持续迭代**：版本对比时用此表算 diff

### 段落 3: 核心壁垒（必填，3-5 个）

```markdown
## 核心壁垒

### 壁垒 1: [名称]
- 来源: [哪些项目沉淀的]
- 稀缺性: [为什么别人短期学不会]
- 证据: [1-2 个具体事实]
- AI 时代耐受性: [强化 / 中性 / 削弱]

### 壁垒 2: ...
```

下游工具关键消费：
- **网站 Strengths section**：用 web-design 的"3 个卧槽爆点"原则展示
- **简历核心能力区**：直接列出
- **BP / 融资材料**：核心壁垒论证

### 段落 4: 里程碑（必填，按时间顺序）

```markdown
## 里程碑

- 2007 · 9 岁开始编程: 起点是想搞懂攻击脚本，反映"下到底层"的本能
- 2018 · UIUC ECE 中断: 因家庭原因肄业（不抹去这段，是真实主线的一部分）
- 2019 · NVIDIA Tegra SoC: 无学位 → 顶级硬件岗
- 2021 · 离开 NVIDIA 进入 AI 落地: 早于 LLM 浪潮 1 年
- 2025/1 · 第一次创业 CTO: GrainedAI，奇绩 F24
- 2026/2 · 第二次创业 CTO: MetaInflow
```

下游工具关键消费：
- **网站 About / Timeline section**：直接渲染时间线
- **简历经历区**：转换格式

### 段落 5: 卖点三段（必填）

```markdown
## 卖点三段

- 🎯 ta 是谁: [50-80 字]
- 💎 ta 凭什么: [50-80 字]
- 🚀 ta 能给你什么: [50-80 字]
```

下游工具关键消费：
- **网站 Hero 副文案** / **联系页 pitch** / **第三方介绍模板**

### 段落 6: 软实力质地（必填，4-7 条）

```markdown
## 软实力质地

- [模式句 1]: 在 [场景] 下，倾向于 [行为]。证据: [来源事件]
- [模式句 2]: ...
...
```

下游工具关键消费：
- **网站 About 隐藏深度**：作为"性格 / 工作方式"的细腻补充
- **博客 bio**：选 1-2 条作为标签

### 段落 7: 给 web-design 的设计建议（必填）

```markdown
## 给 web-design 的设计建议

### 风格调性候选（按推荐度排序）
1. **[Style A]** — 理由: [人格特征匹配解释]
2. **[Style B]** — 理由: ...
3. **[Style C]** — 理由: ...

### 推荐参照站
- [品牌 1]: [为什么参考]
- [品牌 2]: [为什么参考]

### 必须包含的内容板块
- [板块 1]: [为什么必须有]
- [板块 2]: ...
- [板块 3]: ...

### 应该避开的
- [不要做成什么样]
- ...
```

**这是「问心」给 web-design 的接力 PRD**——web-design 启动 Phase A4 时直接读取此段。

#### 风格推导映射表

「问心」如何根据人格 / 主线推导风格调性？参考下表：

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

⚠️ **不要硬套**——每个人的特征组合不一样。可以混搭，可以创造新方向。这是建议，不是强制。

### 段落 8: 持续迭代记录（首次为空）

```markdown
## 持续迭代记录

（首次生成时此段为空。后续每次更新追加一条，格式见 references/update_logic.md）
```

---

## 文件保存路径

```
项目根目录/
├── WENXIN_REPORT.md       # ⭐ 当前版本（最新）
├── archive/
│   ├── 2026-05-03.md      # 历史版本
│   └── 2026-12-15.md
└── public/
    ├── index.html          # 个人网站首页（web-design 生成）
    ├── report.html         # 完整问心报告
    ├── report.pdf
    ├── poster.png
    └── compare.html        # 版本对比（持续迭代时生成）
```

## 下游工具消费的标准做法

```python
# 伪代码，给下游工具参考
import frontmatter

with open('WENXIN_REPORT.md') as f:
    report = frontmatter.load(f)

# 元数据
nickname = report['nickname']
last_updated = report['last_updated']

# 段落（按标题分割）
sections = parse_sections_by_h2(report.content)
identity = sections['身份层']
radar = sections['雷达图']
strengths = sections['核心壁垒']
design_hints = sections['给 web-design 的设计建议']
```

---

## 协议演进

如果未来字段需要扩展：
- **加新段落** → version 不变（向后兼容，旧消费者忽略未知段）
- **改段落标题或字段语义** → version + 1（破坏性变更）
- **删段落** → version + 1（破坏性变更）

下游工具应该检查 `version` 字段，对不兼容的版本给出明确错误。
