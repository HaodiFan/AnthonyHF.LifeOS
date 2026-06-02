# Skills 能力层

这一层回答：“AnthonyHF 什么时候调用什么能力？”

根层场景地图：`SKILLS-CATALOG.html`。它回答可插拔 meta skill 分别在什么场景下使用；不要在里面写“当前有几个 skill”这类会随新增/删除变化的数量声明。具体 skill 内部能力地图分别见：

- `engineering-everything/SKILLS-CATALOG.html`
- `content/public-narrative-system/SKILLS-CATALOG.html`

`skills/` 只放真正的 Skill 包。每个可执行或可路由能力最终都必须有一个 `SKILL.md` 入口。不是 Skill 的推荐列表、总结、数据绑定、source metadata、候选说明和 runtime 投影不要放在这里。

## Skill 类型

AnthonyHF.LifeOS 里有三类能力：

| 类型 | 作用 | 放在哪里 |
| --- | --- | --- |
| Meta Skill | 长期可复用的判断框架、路由原则、方法论和 review gate。 | `skills/<skill-id>/SKILL.md` 或 `identity/wenxin/skill-summaries/` 中的候选说明 |
| Runtime Skill | 执行具体任务，产生任务结果、run log、验证结果和候选经验。 | 独立 runtime skill repo，或未来的 `skills/runtime/<skill-id>/SKILL.md` |
| Self-evolution Skill | 更新 AnthonyHF 自己的 identity、PSP、Soul、Design、memory、skill roadmap 和对齐规则。 | `skills/self-evolution/<skill-id>/SKILL.md` |

`Engineering Everything` 是 Anthony 对“构建系统”这件事的 meta skill：它不是把所有事情都写成代码，而是把软件、产品、组织、SOP、企业机制、交付、复盘和 Skill 沉淀这些构建型任务，用工程化方式思考。

`Public Narrative System` 是 Anthony 对“公开表达和措辞”这件事的 meta skill：写文章、发公告、改措辞、产品叙事或去人机味时，用它把草稿改成更像 Anthony 的公开/工作表达。

## 当前 Skill

| Skill | 类型 | 什么时候用 |
| --- | --- | --- |
| `engineering-everything/SKILL.md` | Meta Skill / 构建型工程判断 | 做项目、写代码、架构、产品定义、GTM、组织机制、SOP、培训、交付、治理、复盘、构建企业或把经验沉淀成系统能力时。 |
| `content/public-narrative-system/SKILL.md` | Meta Skill / 公开叙事与措辞 | 写文章、发公告、改措辞、公开说明、产品叙事、社媒/公众号/官网/路演文本，或把 AI 草稿去人机味、改成更像 Anthony 说话时。 |
| `self-evolution/cognitive-alignment/SKILL.md` | Self-evolution Skill | 用户要求“讲出你的判断”“和我认知对齐”，或指出“不对”“不是我想要的”“这个 skill 不全面”，需要复盘 agent 与 Anthony 判断差异时。 |
| `self-evolution/wenxin/SKILL.md` | Self-evolution Skill | 处理“我是谁”“我站在哪”“个人定位”“公开介绍”“履历叙事”“个人 BP”“能力地图”“未来路径”时。 |
| `self-evolution/psp/SKILL.md` | Self-evolution Skill | 构建或更新 Anthony 的人物模型、数字分身边界、语言指纹、判断方式、system prompt 或保真验证时。 |
| `self-evolution/ipo-reverse/SKILL.md` | Self-evolution Skill | 从已经完成的文档、方案、代码、对话或系统设计里反推证据、隐性认知任务、中间思考资产和可复用 IPO，用于 SOP、培训和 Skill 蓝图。 |

## 路由规则

优先按任务对象路由：

| 用户要做什么 | 先用哪个 Skill | 说明 |
| --- | --- | --- |
| 构建一个系统、项目、产品、组织机制、SOP 或交付方案 | `engineering-everything` | 这是 Anthony 的构建型 meta skill。先判断工程路由、阶段、真相源、产出物和验证 gate。 |
| 写代码、修 bug、做架构、review PR、设计技术方案 | `engineering-everything` | 软件工程只是它的一个子场景。 |
| 设计产品、PRD、GTM、客户交付、实施路径 | `engineering-everything` | 用工程方式处理业务闭环、交付链路、owner、风险和验收。 |
| 面试、入职培训、组织协同、公司运行机制 | `engineering-everything` | 组织和企业机制也按构建型系统处理。 |
| 写文章、发公告、改公开措辞、去人机味 | `public-narrative-system` | 先保留真实判断和公开边界，再调整结构、语气和措辞，让文本更像 Anthony 的公开/工作表达。 |
| 写产品叙事、官网文案、社媒/公众号/路演文本 | `public-narrative-system` | 如果涉及产品事实或交付承诺，先用 `engineering-everything` 判定事实和边界，再由 `public-narrative-system` 写表达。 |
| 解释 Anthony 是谁、对外怎么介绍、履历怎么讲 | `wenxin` | 需要人物边界或判断方式时再读 PSP。 |
| 更新数字分身、人物模型、语言风格、行为边界 | `psp` | PSP 是人物模型源产物；不要用它替代事实库。 |
| 用户纠偏 agent，或要求先讲清判断 | `cognitive-alignment` | 先解释 agent 当前判断和依据，再定位分歧，把可复用规则写回正确位置。 |
| 从一次完成的产出里沉淀方法论、SOP、Skill 蓝图 | `ipo-reverse` | IPO Reverse 处理“已完成产物”的逆向萃取；如果还没产出物，先走 Engineering Everything 做正向计划。 |

组合使用时按这个顺序：

1. 构建型任务先走 `engineering-everything`。
2. 公开表达、文章、公告、措辞和去人机味走 `public-narrative-system`。
3. 涉及 Anthony 当前身份、公开定位或人生阶段时，加读 `wenxin`。
4. 涉及分身行为、判断方式、语言保真或 impersonation 风险时，加读 `psp`。
5. 用户纠偏或需要对齐 Anthony 判断时，加读 `cognitive-alignment`。
6. 任务完成后要沉淀 SOP、培训材料或新 Skill 时，再走 `ipo-reverse`。

## 不要误用

- 不要把 `engineering-everything` 当成“所有事情都写代码”。它的核心是构建系统的工程化判断。
- 不要把 `public-narrative-system` 当成营销号文案工具。它的核心是公开表达保真、去人机味、真实归因和发布边界。
- 不要把 `wenxin` 当成简历润色工具；它回答个人定位、能力水位、gap 和未来路径。
- 不要把 `psp` 当成泛人格测试；它是人物模型和分身保真工程协议。
- 不要把 `cognitive-alignment` 当成泛用复盘模板；它处理 agent 与 Anthony 判断之间的分歧。
- 不要把 `ipo-reverse` 用在还没有完成产出物的正向规划上。

## 非 Skill 产物位置

- 推荐 Skill 列表：`identity/wenxin/skill-recommendations.yml`。
- Skill 总结和能力说明：`identity/wenxin/skill-summaries/`。
- Skill 读取 memory/wiki/source 的边界和依赖声明：`identity/cognition/skill-bindings/`。
- factory bridge / source update metadata：`integrations/skill-sources/`。
- 候选 runtime Skill 说明：`docs/skill-system/`。

## Placement Policy

- 新能力只有形成可执行或可路由的 `SKILL.md` 后才进入 `skills/<skill-id>/`。
- 新 Meta Skill 进入 `skills/<skill-id>/` 时，必须同时提供 `SKILLS-CATALOG.html`，说明它在什么场景下使用、输入/输出、边界和与其他 meta skill 的组合关系。
- 事实、偏好、长期上下文不写进 Skill；通过 `memory/`、配置的 memory wiki 或 `identity/cognition/skill-bindings/` 查询。
- 推荐、总结和证据门控先留在 Wenxin 层，经过 IPO Reverse、owner alignment 和 privacy review 后再提升为真实 Skill。
