# AnthonyHF.LifeOS 用户说明书

这个说明书回答一个问题：用户打开这个 repo，应该看什么，能得到什么。

AnthonyHF.LifeOS 不是普通简历，也不是文件仓库目录说明。它是一个数字人的公开接口：普通人用它理解 AnthonyHF，AI 用它知道如何协作，维护者用它判断哪些内容可以更新、哪些不能公开。

## 先看什么

| 你想知道什么 | 先看哪里 | 能得到什么 |
| --- | --- | --- |
| 快速了解这个数字人是谁 | `README.md` | AnthonyHF 的一句话定位、公开主线、当前能做什么、公开边界。 |
| 浏览整个 LifeOS 有哪些入口 | `LIFEOS-CATALOG.html` | 按 Identity、Runtime、Capabilities、Evolution、Work、OS Layer 浏览所有主要入口。 |
| 看当前核心产物指向哪里 | `artifacts/current.yml` | 当前 Wenxin、PSP、Soul、Design、maturity 等 active artifact 的指针。 |
| 看当前 identity 真相源 | `identity/current.yml` | 当前身份层使用哪份 Wenxin、PSP、Soul、public profile。 |
| 让 AI 理解如何协作 | `SKILL.md` | AI 应该读什么、怎么路由任务、哪些内容不能编造或公开。 |

## 理解 AnthonyHF

| 入口 | 适合谁看 | 能得到什么 | 注意 |
| --- | --- | --- | --- |
| `identity/avatar-description/current.yml` | 产品、页面、runtime | 最短的结构化分身描述：显示名、一句话、当前上下文、优势、边界、证据引用。 | 它是摘要，不是完整证据源。 |
| `identity/public-profile/profile.yml` | 普通用户、产品页面 | 公开身份资料和可展示字段。 | 只放 public-safe 信息。 |
| `identity/wenxin/WENXIN_REPORT.md` | 想理解公开定位的人 | “我是谁、站在哪、gap、未来路径、候选能力”。 | 当前是 evidence-limited，不等于完整人生档案。 |
| `identity/psp/anthony-fan/PSP.md` | AI、分身建模者 | 判断方式、表达方式、行为边界和人物模型。 | PSP 不是完整人格复刻。 |
| `SOUL.md` | AI、协作者 | 处事原则和运行方式的当前入口。 | Soul 从 PSP/证据中激活，不反过来当证据。 |
| `DESIGN.md` | 设计/表达相关协作者 | 全局审美、表达、视觉偏好。 | 项目级设计需求不能自动升级为长期偏好。 |

## 理解它能做什么

| 入口 | 能得到什么 | 当前状态 |
| --- | --- | --- |
| `capabilities/index.md` | 已沉淀稳定能力的总览。 | 当前只放已经形成边界的能力。 |
| `capabilities/engineering-everything/SKILL.md` | 工程化判断、项目、架构、流程、治理、验证的执行协议。 | 稳定能力。 |
| `capabilities/publication/public-narrative-system/SKILL.md` | 公开叙事、内容产品化、发布资产化的执行协议。 | 稳定能力。 |
| `runtime/runtime-skills/` | 运行中出现的临时/候选能力。 | 还不能直接等同于稳定能力。 |
| `identity/wenxin/skill-recommendations.yml` | Wenxin 根据材料推荐的候选能力。 | 候选，不是 capability 真相源。 |

## 理解它最近是否“活着”

| 入口 | 能得到什么 | 注意 |
| --- | --- | --- |
| `runtime/sessions/` | 任务、输入、动作、输出、观察和反馈的公开安全索引。 | Session 是生命活动源头。 |
| `runtime/runtime-lessons/` | 局部经验、教训、待复盘内容。 | Lesson 还不是能力。 |
| `runtime/memory/working-lessons/` | 当前活动记忆和 working lessons。 | 需要 IPO/owner alignment 才能升级。 |
| `runtime/runtime-profile/` | 本地运行期画像占位：当前上下文、限制、adapter 状态。 | 不是人格真相源。 |
| `runtime/profiles/` | 给 OpenClaw、Hermes 等外部系统使用的运行版本。 | 是外部适配版本，不是真相源。 |

## 理解它如何进化

| 入口 | 能得到什么 |
| --- | --- |
| `evolution/index.md` | 进化层总览。 |
| `evolution/organ-systems/` | Wenxin、PSP、IPO Reverse、Cognitive Alignment 等能力生产系统。 |
| `evolution/ipo/` | 从 session、runtime skill、runtime lesson 到 capability 的复盘和升级路径。 |
| `evolution/alignment/` | owner alignment 和认知对齐过程。 |
| `evolution/mutations/` | 结构或能力变化的候选记录。 |

## 理解材料从哪里来

| 入口 | 能得到什么 |
| --- | --- |
| `metabolism/inbox/` | 原始材料入口索引，例如 GitHub、Feishu、聊天、文档。 |
| `metabolism/processing/` | 材料处理、脱敏、first-read、evidence intake 状态。 |
| `metabolism/extracted/` | 已消化材料和可继续使用的 evidence packet。 |
| `integrations/data-sources.yml` | 外部数据源 authority 和绑定关系。 |

## 理解作品和展示

| 入口 | 能得到什么 | 注意 |
| --- | --- | --- |
| `work/index.md` | 工作产出入口。 | 只放 public-safe 指针和作品源文件。 |
| `work/apps/homepage/` | GitHub Pages 主页源码和公开素材。 | 构建产物不放这里。 |
| `work/avatar-page/view-model.yml` | 具体第三人称 avatar 页面应该消费哪些 LifeOS 字段。 | 展示模型，不是真相源。 |
| `docs/avatar-page-information-architecture.md` | 数字人页面的通用层级、字段、当前可产出物和缺口。 | 定义共同维度，不定义固定身份角色。 |

## 理解安全边界

| 入口 | 能得到什么 |
| --- | --- |
| `security/README.md` | 什么不能公开、不能提交、不能让 AI 使用。 |
| `security/permissions.yml` | 权限和公开策略。 |
| `docs/evidence-sufficiency.md` | 当前证据成熟度、材料缺口和可声明范围。 |

## 不建议普通用户优先看的内容

| 入口 | 为什么 |
| --- | --- |
| `docs/file-role-inventory.yml` | 文件级审计表，给维护者用。 |
| `docs/layer-file-review.md` | 层级审计摘要，给维护者用。 |
| `docs/schema-trim-completion-audit.md` | schema trim 验收记录，给维护者用。 |
| `legacy/` | 历史结构、旧产物、迁移记录，不是当前真相源。 |
| `evolution/organ-systems/*/references/` | 自我进化工具内部资料，普通用户不需要先读。 |

## 一句话记住

- 想认识 AnthonyHF：看 `README.md`、`identity/avatar-description/current.yml`、`identity/wenxin/WENXIN_REPORT.md`。
- 想让 AI 协作：看 `SKILL.md`、`artifacts/current.yml`、`identity/current.yml`。
- 想知道能力：看 `capabilities/index.md` 和具体 `capabilities/*/SKILL.md`。
- 想知道最近活动：看 `runtime/`。
- 想知道如何进化：看 `evolution/`。
- 想知道能不能公开：看 `security/` 和 `docs/evidence-sufficiency.md`。
