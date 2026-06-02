# Lessons

## 2026-05-23: 系列编号服从真实发布顺序

- Context: `生命系统实验日记` 第一条正式口播被误排成 `#002`，因为 agent 预先把一个系列开场稿占成了 `#001`。
- Correction: 用户明确指出今天这条是第一集。
- Rule: 内容系统里的 episode number 是发布事实，不是叙事地图占位。开场稿、预告稿、置顶说明或世界观稿在未确认发布前只能进入 backlog / prelude candidate，不能自动占用正式编号。
- Apply to: RedNote、小红书、公众号、视频系列、产品叙事系列和任何跨渠道公开内容系列。

## 2026-05-23: 借鉴小红书 skill 时只吸收机制，不吸收人格

- Context: 用户要求参考 `OnePieceLwc/xiaohongshu-skill` 优化当前公开叙事系统。
- Useful mechanism: 标题池、正文、标签、互动、CTA、风险检查应该作为 RedNote 发布包的一部分。
- Rejected style: “爆款”“宝子”“扣 111”“亲测有效”“被大数据拯救”等表达会让 Anthony 的工程师叙事失真。
- Rule: 渠道增长机制可以落到 channel prompt 和 checker；人格、判断方式、产品叙事边界仍由 `public-narrative-system`、`voice.md` 和 `claims-policy.md` 控制。

## 2026-05-23: 渠道技巧应按 channel reference 组织

- Context: 用户指出 `public-narrative-system` 可以按照不同渠道组织各自技巧，当前场景应迭代 RedNote 部分。
- Correction: 主 `SKILL.md` 不应该长期堆 RedNote 细节，否则会把 meta skill 写成渠道文案 skill。
- Rule: 主 skill 负责跨渠道叙事闭环和路由；RedNote、公众号、官网、朋友圈、路演等技巧放在 `references/channels/<channel>.md`。当前先建立 `references/channels/rednote.md`。

## 2026-05-23: 首发内容不要把产品矩阵列成清单

- Context: `生命系统实验日记` 第一集一度把 BaseBuilder、openLifeOS、Cowdy Studio 以清单形式露出。
- Correction: 用户希望主线是“正在搞数字生命 / openLifeOS / 复刻自己 / 再理解公司”，而不是生硬列举产品。
- Rule: RedNote 首发应先建立真实实验和认知钩子。产品只能作为实验系统名、承载层或自然结果出现；产品矩阵要在连续内容里逐步长出来。

## 2026-05-23: Anthony 第一人称公开内容必须接 PSP 语气层

- Context: 用户指出当前稿子“语气不像我”，并建议 publication skill 借鉴 Anthony 的 PSP。
- Root cause: `public-narrative-system` 只读了 `voice.md` 和 channel reference，保证了不营销号，但没有使用 PSP 的判断方式、语言指纹和工作表达节奏。
- Rule: Anthony 第一人称口播、文章、公开身份表达必须先读 `identity/psp/anthony-fan/PSP.md` 和 `references/psp-voice-adapter.md`，再做 RedNote/公众号等渠道化包装。PSP 只用于公开/工作场景语气适配，不把原文和私密证据复制进 publication repo。

## 2026-05-23: Anthony 的 RedNote 钩子可以是高抽象战略问题

- Context: 用户不喜欢“数字分身不能从 prompt 开始”作为钩子，认为它不是足够强的反常识。
- Correction: 第一集钩子改为“你们公司的 moat 是什么？”，核心判断是“moat 是动态势能而非静态资产”，后文再解释为 second derivative 的工程类比。
- Rule: 对 Anthony 来说，强钩子可以是战略问题 + 高抽象判断，不必强行做普通平台反常识。但必须在正文后半段完成解释和 fact-check，避免只留下玄学感。

## 2026-05-23: Anthony 口播要直接给问题和判断

- Context: `生命系统实验日记` 第一集仍使用了“最近有人问我一个问题”“我越来越觉得”这类铺垫式表达。
- Correction: 用户明确要求开头直接炸：第一句就是问题，不要先说“最近有人问”；核心观点用“我认为...”直接给结论，然后再略微展开。
- Rule: Anthony 第一人称公开表达应遵循“问题/判断直出 -> 结论先行 -> 机制解释 -> 边界说明”。避免把核心观点藏在背景后面，也避免用“我越来越觉得”承担主判断。

## 2026-05-24: Anthony 理论型口播只走正向链路

- Context: `Second Derivative Moat` 口播一度把传统 moat 定义、静态优势会衰减、以及“这不是金融学标准定义”的边界说明放进正文主链路。
- Correction: 用户明确不喜欢这段，要求直接给结论并开始解释，只走正向链路。
- Rule: Anthony 的高抽象理论内容应按“结论 -> 核心变量 / 函数 -> 变量如何互相放大 -> 真实实验 -> 边界”推进。传统定义、反驳、免责声明和 fact-check 可以放在发布边界、脚注或 risk scan，不要抢占口播主叙事。

## 2026-05-24: 外部观点不能改写成 Anthony 的理解

- Context: `Second Derivative Moat` 口播把“没有真正的 moat，快就是 moat”写成了“我当时对这句话的理解”。
- Correction: 用户明确指出这不是他的理解，而是当时听来的观点。
- Rule: 引用外部分享、老师观点、行业判断时，必须区分“听来的观点”和“Anthony 当前判断”。不要为了叙事顺滑把外部观点内化成 Anthony 的理解；正确结构是“当时听到的观点 -> 我现在往前推一层 -> 我的判断”。

## 2026-05-24: 理论变量不能写成机械清单

- Context: `Second Derivative Moat` 口播把公司系统写成“每一次工作进入 memory / 每一次错误进入 reflection / 每一次判断进入 alignment...”的逐项变量清单。
- Correction: 用户明确不喜欢这段。
- Rule: Anthony 的理论口播不能只是逐条念变量。变量要被翻译成系统状态变化，尤其是“上一轮工作是否改变下一轮工作的起点”。优先表达变量之间如何造成下一次任务更少解释、更少人工介入、更稳定判断，而不是把 `memory/reflection/alignment/skill` 逐项排队。

## 2026-05-24: Second Derivative Moat 的操作初衷

- Context: 用户补充 `Second Derivative Moat` 的真实初衷：想让每做一次正确的产出，下次都比上次少花一点时间，直到之后能够不需要本人来产出。
- Correction: 口播应把理论变量落到“正确产出降低下一次同类产出的时间成本和人工介入”。
- Rule: 讲组织自进化时，核心不是“工作进入 memory”这类存储动作，而是“正确产出是否改变下一次产出的成本结构”。理想状态不是人越来越快，而是同类产出逐渐由系统自主完成。

## 2026-05-24: 不把“不是 X，而是 Y”作为默认句式

- Context: `Second Derivative Moat` 口播和 voice adapter 多次使用“不是 X，而是 Y”的对比句式。
- Correction: 用户明确要求不要用这种语言习惯。
- Rule: Anthony 公开表达要优先使用正向定义、因果链、目标函数和系统状态变化。需要做区分时，也不要把“不是 X，而是 Y”变成主节奏；可改为“核心是...”“真正看...”“目标函数是...”“这个变化来自...”。

## 2026-05-24: 融合 Humanizer-zh 为 Anthony humanizer pass

- Context: 用户要求借鉴 `op7418/Humanizer-zh.git`，把相关提示词融合到 publication workflow。
- Source: `https://github.com/op7418/Humanizer-zh` at commit `91f3d39`, MIT license.
- Rule: 只吸收适合 Anthony 的去 AI 腔机制：删填充、查真实归因、去机械对比、去三段式、把变量清单改成系统状态变化、去宣传腔。不能把 Anthony 的工程密度改成泛口语，也不能为了“自然”牺牲判断精度。

## 2026-05-24: Second Derivative Moat 的正确展开起点

- Context: Agent 把 `Second Derivative Moat` 第一集从 openLifeOS 个人实验场景展开，用户指出没有理解真正结构。
- Correction: 正确起点是“面对公司壁垒是什么的灵魂拷问”，创业将近两年反复思考这个问题，然后从“企业是杠杆的载体”切入，讲工业时代、互联网时代、AI-native 时代的杠杆变化，再拆组织生产力变量，最后由一次斜率推到二次求导。
- Rule: 讲 `Second Derivative Moat` 时，主线顺序应是：公司 moat 问题 -> 企业是杠杆载体 -> 历史杠杆迁移 -> 组织生产力函数 -> 认知/价值/能力斜率 -> 二阶导 moat。openLifeOS 只能作为后续实验例子，不应作为理论展开的第一入口。
- Wording: 必须保留用户给出的关键名词，如“灵魂拷问”“企业是杠杆的载体”“工厂”“资本杠杆”“劳动力杠杆”“基础设施杠杆”“AI 杠杆”。工业时期要说清楚工厂作为组织形态；互联网时代要说清楚互联网大厂通过组织管理、人效管理、SOP 和基础设施利用杠杆；AI-native 时代要说清楚 AI 杠杆体现在 Agent 能力层和组织自进化层。

## 2026-05-24: Anthony 旧创业复盘口吻样本

- Context: 用户提供一段过去创业半年复盘文，说明“这是我的语言风格”。
- Source: `red-note/metabolism/inbox/2026-05-24-anthony-old-founder-style-sample.md`
- Rule: Anthony 的公开内容不要全程端成理论稿。生活/创业复盘可以保留具体日常细节、阶段变化、轻微自嘲和括号尾巴。理论内容可吸收这种具体质感，但不能把旧事实当成当前事实复用，也不能把轻松朋友圈语气直接套到高抽象口播。

## 2026-05-24: Anthony 创业燃尽与锚点口吻样本

- Context: 用户提供一段“创业九个月有感 - 心态进化”旧文。
- Source: `red-note/metabolism/inbox/2026-05-24-anthony-founder-burnout-anchor-style-sample.md`
- Rule: 创业心态复盘可以写真实压力体感和个人锚点：context switch、燃尽、期待周末、不快乐、盘核桃、喝茶、健身。可以保留自然中英混杂。核心结构是“真实业务压力 -> 身体/情绪体感 -> 找到稳定锚点 -> 抽象成系统机制”。避免把脆弱写成卖惨，也不要把具体旧项目事实当作当前公开事实复用。
