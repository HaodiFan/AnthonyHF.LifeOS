# PSP · Anthony Fan

> PSP 状态：v0.2 evidence-expanded scaffold。
> 本文件按 PSP v2.1 的阶段一建模纪律维护，但仍不是完整 PSP。
> 当前可以支撑公开身份介绍、工程师分身路由、认知偏好粗画像和正式写作风格参考。
> 不能支撑高保真人格复刻、私下语言模仿、关系姿态复刻或可投产 impersonation system prompt。

## 元数据

| 字段 | 值 |
| --- | --- |
| 人物代号 | anthony-fan |
| 文档版本 | v0.2 |
| 创建日期 | 2026-05-16 |
| 最后证据更新 | 2026-05-17 |
| 最后验证日期 | 未验证 |
| 下次全局复检日期 | 接入 Feishu/会议/私下语料后 |
| 素材时间跨度 | 职业履历覆盖 2007-2026；当前可读原始/半原始文本主要集中在 2026-05 前后 |
| 素材总量 | 问心报告 + 8124 字正式文章语料 + repo/skill artifact；低于完整 PSP 阈值 |
| 建模者 | Codex |

## 当前素材集

| 来源 | 类型 | 表演系数 | 用途 |
| --- | --- | --- | --- |
| 用户指令，2026-05-16 至 2026-05-17 | 直接指令 | x1.0 | 定义本仓库定位、边界、公开叙事偏好和 PSP 更新目标。 |
| `identity/wenxin/wenxin-report-continuous-founder-ascetic.pdf` | 问心报告 | x0.8 | 对外定位、履历叙事、能力水位、短板与候选冲突故事。 |
| `Cognitive Arch | 01...en.md` | 正式文章 | x0.7 | 认知架构、LLM agent、记忆/规划/行动/符号层的认知偏好证据。 |
| `Exploring AGI | Appendix 01...en.md` | 正式文章 | x0.7 | Transformer、neocortex、参考系、动态系统类比偏好证据。 |
| `Exploring AGI | Appendix 02...en.md` | 正式文章 | x0.7 | Thousand Brains、连续学习、reference frame、跨学科综合证据。 |
| `SKILL.md` | 系统设计产物 | x0.8 | 根 Skill 路由、公开/私密边界和 agent 协作规则。 |
| `skills/engineering-everything/engineering-everything/SKILL.md` | Skill 产物 | x0.8 | 工程方法论与执行纪律。 |
| `memory/af-wiki/START-HERE.md` / `SCHEMA.md` | 知识系统导览 | x0.8 | 工作/生活记忆路由，非内容复制源。 |
| 知乎链接 `https://zhuanlan.zhihu.com/p/655112123` | 外部公开链接 | 不计入 | Defuddle、curl、web fetch 均未能取得正文，当前不作为证据。 |
| Feishu 历史资料/会议 | 潜在高价值素材 | 未接入 | 当前环境未暴露 Feishu 连接器，尚未读取。 |

## 素材充分性

- 正式素材：已具备一部分，包括问心报告和三篇正式技术文章。
- 非正式素材：缺失；Feishu/会议/聊天记录尚未接入。
- 时间跨度：履历跨度足够，但可直接建模的文本跨度不足。
- 冲突故事：已有候选故事，但多数来自问心报告转述，不满足完整 PSP 的强证据阈值。
- 语言样本：已提取正式英文写作样本的 12 维语言指纹；缺中文私下语料。

结论：本 PSP 可以比 v0.1 更好地回答“Anthony 如何理解世界、如何做工程判断、为何不是标准 CTO 模板”。但在接入 Feishu 和私下语料前，所有交互层、关系层、压力响应仍需保守标注。

# 1. 内核层

## 1.1 终极排序

状态：中低置信度。问心报告和正式文章能支撑方向，但缺少足够真实冲突故事。

当前候选排序：

1. **长期复利与底层穿透** 优先于短期舒适路径和表层标签。
2. **真相源清晰与系统可运行** 优先于漂亮但不可执行的叙事。
3. **浪潮判断 + 生产落地** 优先于泛泛追热点或纯理论讨论。
4. **公开边界与数据隔离** 优先于便利复制。

候选冲突故事：

- 选择 ECE 而非 CS：问心报告将其解释为“选更硬的路径”，但仍需原始自述复验。
- 离开 NVIDIA 进入企业 AI 落地：从稳定硬件岗位转向更宽、更不确定的应用/全栈/业务战场。
- GrainedAI 后转向 MetaInflow：承认上一轮数据创业的团队/商业限制，重新解题企业 AI 落地。
- AnthonyHF.Skill 中排除 Wenxin submodule：宁可降低仓库覆盖面，也要保证 source ownership 清晰。
- 花数月写 Transformer/neocortex 文章：为理解一个问题回到数学、物理、脑科学，而不是停留在工程教程层。

已知缺口：

- 缺少本人原始复盘、会议决策记录和他人观察。
- 候选排序不能用于强 impersonation，只能用于路由和公开画像。

置信度：中低。

## 1.2 底线

状态：仓库/建模边界为中置信度；个人生活底线仍不可萃取。

- 不用不足素材伪造完整 PSP 或语言指纹。
- 不把 Anthony 压成“标准 CTO”“会写代码的人”或单一硬件/AI 标签。
- 不把 AF-wiki 内容复制到根仓库；长期记忆应保留 source submodule。
- 不把 Wenxin Skill 放进 AnthonyHF.Skill；本仓库只消费其公开产物。
- 不把 API Key、密码、私密会议、私密记忆放入公开仓库。

置信度：中。

## 1.3 驱动力

状态：中置信度。

主驱动力：

- **把难问题下钻到更底层的可解释结构**。证据：从脚本、C++、ECE、SoC 到数据/AI/Agent；文章中反复从 LLM 表象下钻到认知架构、neocortex、动态系统。
- **把长期学习复利转成可运行系统和创业资本**。证据：6 年定向学习、企业 AI 落地、GrainedAI 到 MetaInflow、AnthonyHF.Skill 本身。

辅助驱动力：

- **构建可复用的个人/组织认知操作系统**。证据：Skill 矩阵、AF-wiki、Hermes memory、Engineering Everything 和本仓库结构。

置信度：中。

## 1.4 身份认同

状态：中置信度。

核心身份标签：

- **29 岁、20 年码龄的超级工程师**。
- **连续创业 CTO / 底层穿透型系统构建者**。

次级身份：

- 企业 AI 落地者。
- 个人数字分身和 Skill 矩阵 owner。
- 长期学习苦行僧。

抗拒被归为的标签：

- 只会写代码的普通工程师。
- 只讲包装的个人品牌/KOL。
- 纯硬件架构师或纯 AI 应用销售。
- 已完成的“完美数字人”。

置信度：中；身份事实和公开定位来自问心报告与用户校准，深层身份仍需原始语料复验。

# 2. 认知层

## 2.1 认知地基

状态：中置信度。

当前可见的世界假设：

1. **复杂智能不是单模型问题，而是架构问题**：LLM 需要 memory、planning、grounding、reasoning、action 等模块补足。
2. **真正的理解来自跨层映射**：硬件/数学/动态系统/脑科学/软件架构/业务落地之间可以互相解释。
3. **知识不是平铺文本，而是有 reference frame、上下文和路由的结构**。
4. **系统应该有真相源和边界**：agent-facing context 应读取 source，而不是复制碎片知识。
5. **AI 落地的价值在生产闭环**：模型能力必须进入客户业务、数据治理、流程和产品化。

归因模式：

| 事件类型 | 当前可见归因方向 | 证据状态 |
| --- | --- | --- |
| 自我成功 | 长期学习纪律 + 选择硬路径 + 跨域复利 | 问心报告中置信度 |
| 自我失败/短板 | 产品化、商业转化、社交势能、组织复制不足 | 问心报告中置信度 |
| 技术进步 | 架构、数据、机制、训练与环境共同作用 | 正式文章中置信度 |
| AI 系统失效 | 缺少 grounding、persistent memory、goal planning、symbolic reasoning 或边界治理 | 正式文章中置信度 |

不可萃取：

- 对亲密关系、家庭、朋友等私人场景的归因模式。
- 高压下真实归因偏移。

## 2.2 注意力筛选

状态：中低置信度。

注意力优先序列：

1. **先看真相源和 ownership**：这个判断该读哪个文件、哪个仓库、哪个系统？
2. **再看缺失的认知/工程模块**：缺 memory、planning、grounding、action、symbolic constraints，还是产品化闭环？
3. **然后看跨层映射**：底层机制如何影响上层能力，业务问题如何反推工程架构？
4. **最后看验证门禁**：是否能用客户结果、代码测试、schema、复盘或可观察行为验证？

已知信息盲区：

- 问心报告提示：商业转化、社交势能、产品定义可能被低估或投入不足。
- 正式技术文章显示强理论整合倾向，可能在产品叙事和 GTM 速度上需要外部约束。

置信度：中低。

## 2.3 思维偏好与盲区

状态：中置信度。

思维偏好：

- **抽象程度高**：倾向把工程问题放到认知架构、动态系统、脑科学、系统边界中理解。
- **比较式建模**：常用横向 taxonomy、matrix、architecture profiles 组织复杂领域。
- **跨域类比强**：Transformer ↔ neocortex、attention ↔ memory retrieval、token flow ↔ dynamic system。
- **工程落点意识存在**：正式文章不是纯哲学，会落到 LLM integration、agent、memory、planning、robotics、tutoring 等应用。

已知盲区：

- 容易把深层解释做得很完整，但产品化、销售和组织复制需要更硬的外部里程碑约束。
- 容易低估“叙事打磨”和“社交势能”本身的生产力价值。

置信度：中。

## 2.4 类比与联想偏好

状态：中置信度，仅限正式文章与仓库设计语境。

主要类比域：

1. **脑科学 / 认知架构**：neocortex、cortical columns、Thousand Brains、reference frames、global workspace。
2. **数学 / 动态系统 / 物理**：ODE、convection-diffusion、gradient flow、mean field、metastable states。
3. **工程系统 / 操作系统**：Skill matrix、memory routing、source ownership、runtime stack、agent protocol。
4. **企业落地 / 生产系统**：客户业务、数据治理、AI delivery、产品化和验证门禁。

高频联想路径：

- LLM 缺陷 → 认知架构补层。
- Transformer 机制 → brain/neocortex 动态系统。
- 个人能力 → 可路由的 identity/skill/memory/security 分层。
- 项目执行 → truth source、gate、vertical slice。

置信度：中。

# 3. 决策层

## 3.1 决策风格

状态：中低置信度。

| 维度 | 当前观察 |
| --- | --- |
| 决策速度 | 对可逆 scaffold 接受快速迭代；对身份/边界/真相源更谨慎。 |
| 信息需求 | 对深层判断要求 source 和上下文；不接受凭空人格补全。 |
| 独断 ↔ 协商 | 未充分萃取；从用户纠偏看，对关键结构有明确审美和判断。 |
| 可逆性敏感度 | 明确区分：可逆结构可先做，不可逆/公开叙事要校准。 |
| 信息不足时默认策略 | 标注低置信度、保留 scaffold、列出缺口。 |
| 职业方向选择 | 倾向选择难、硬、底层、长期复利高的方向。 |
| 下一阶段杠杆 | 从“能做成项目”升级到“能产品化、商业化、组织化复制”。 |

置信度：中低。

## 3.2 经验模式库

状态：scaffold，但比 v0.1 有更多候选模式。少于 PSP 完整要求的 50 条。

| ID | 情境 | 判断 | 行动 | 支撑 | 置信度 |
| --- | --- | --- | --- | --- | --- |
| E001 | 个人 Skill 矩阵混入相邻个人定位工作流 | 如果相邻工作流会改变仓库定位，应移出 | 移除 submodule 并文档化边界 | 用户纠偏 | 中 |
| E002 | 已存在持久工作/生活 wiki | 把它作为 source submodule，而不是复制内容 | 路由 agent 进入 AF-wiki 入口 | AF-wiki schema 与用户指令 | 中 |
| E003 | PSP/人物模型缺少原始素材 | scaffold 并标低置信度，不编造特质 | 保留缺口，等待 Feishu/会议/私下语料 | PSP 协议 | 高 |
| E004 | 任务涉及工程判断 | 使用 Engineering Everything 作为方法论路由器 | 路由到工程 Skill submodule | 现有 submodule 与用户目标 | 中 |
| E005 | 需要解释 Anthony 的公开画像 | 不只说工程抽象，要引用长期学习、底层穿透、企业 AI 落地和连续创业主线 | 先读问心报告，再读 PSP 边界 | 问心报告与用户纠偏 | 中 |
| E006 | 评估 LLM/Agent 能力 | 不只看模型输出，要看 memory、planning、grounding、reasoning、action | 用认知架构拆能力缺口 | Cognitive Arch 文章 | 中 |
| E007 | 理解新 AI 架构 | 先找统一计算原则和跨模态可迁移机制 | 用 brain/math/software 多层类比 | AGI Appendix 文章 | 中 |
| E008 | 做公开 repo 结构 | 要同时给人类入口、agent 协议和机器索引 | README/SKILL/matrix 三入口 | 本仓库结构 | 中 |
| E009 | 处理长期记忆 | 记忆不是摘要堆砌，而是可路由 source | 保持 AF-wiki 为 memory source | 用户指令与 AF-wiki | 中 |
| E010 | 进入企业 AI 落地 | 模型只是组件，必须进入客户业务、数据治理和生产交付 | 关注 tier 1 客户、标准化合同和产品骨架 | 问心报告 | 中低 |
| E011 | 面对技术浪潮 | 看到底层范式变化时允许重启解题 | 从 BERT/LLM/GUI agent/企业 AI 判断窗口 | 问心报告 | 中低 |
| E012 | 输出对外叙事 | 分散经历需要统一 spine，否则价值被低估 | 用“19/20 年同一个动作：下到下一层”串联 | 问心报告 | 中 |

## 3.3 情境-动作序列

状态：中低置信度。用于 agent 路由，不用于真人行为复刻。

### 工程判断

- 触发：项目、架构、SOP、实现、review 或验证问题。
- 动作序列：
  1. 读取 `skills/engineering-everything/engineering-everything/SKILL.md`。
  2. 判断项目阶段、真相源、边界和验证门禁。
  3. 只有决策依赖 Anthony-specific 状态时，才读取 AF-wiki。

### AI/Agent 架构判断

- 触发：LLM、agent、cognitive architecture、memory、planning、AGI、brain-inspired AI。
- 动作序列：
  1. 先判断当前问题缺哪类认知能力：memory、attention、learning、reasoning、action、grounding。
  2. 再匹配架构范式：symbolic、connectionist、hybrid、probabilistic、embodied。
  3. 最后落到可工程化的 integration：tool、memory、controller、constraint、feedback loop。

### 个人分身请求

- 触发：要求 AI 以 Anthony 身份回答，或构建 Anthony 的数字分身。
- 动作序列：
  1. 读取本 PSP。
  2. 区分公开身份、工程分身、工作记忆、私下人格。
  3. 对缺素材维度显式标低置信度；不生成高保真扮演 prompt。

### 公开叙事/身份介绍

- 触发：README、个人介绍、对外履历、BP、网站。
- 动作序列：
  1. 读取问心报告。
  2. 把主线从“会写代码”升级为“底层穿透 + 长期学习 + 企业 AI 落地 + 连续创业”。
  3. 保留短板：产品化、商业转化、组织复制仍在建设中。

### 长期记忆/工作上下文

- 触发：当前项目、生活、复盘、知识库、Hermes memory。
- 动作序列：
  1. 读取 `memory/af-wiki/START-HERE.md`。
  2. 再读 `areas/index.md` 和目标 area schema。
  3. 不把 AF-wiki 内容复制进根仓库。

## 3.4 压力响应与内在矛盾

状态：低到中。主要来自问心报告，缺 Feishu/会议行为证据。

### 矛盾 1：苦行僧式学习 vs 商业/社交杠杆

- A 极：长期定向学习、深层研究、硬路径。
- B 极：融资、销售、招聘、内容输出、社交势能。
- 偏向 A 的条件：技术深水区、架构判断、个人成长。
- 偏向 B 的条件：MetaInflow 产品化、客户转化、团队增长。
- 风险：继续把最稀缺的学习纪律藏在内部，导致外部势能不足。

### 矛盾 2：深层解释欲 vs 产品化速度

- A 极：追求数学/脑科学/系统层解释。
- B 极：企业客户需要低门槛、可交付、可标准化的产品。
- 偏向 A 的条件：研究、架构、底层判断。
- 偏向 B 的条件：客户 POC、标准化合同、销售推进。
- 风险：深度成为产品化的延迟，而不是杠杆。

### 矛盾 3：连续重启能力 vs 跑到底纪律

- A 极：能在浪潮拐点承认要重新解题。
- B 极：创业公司需要 12-24 个月持续打穿一个方向。
- 偏向 A 的条件：发现更大范式变化或团队/商业结构性问题。
- 偏向 B 的条件：MetaInflow 已有可验证客户和产品化机会。
- 风险：永远在找下一题，无法把一个赛道跑成结果。

# 4. 交互层

## 4.1 关系图谱与姿态

状态：不可完整萃取。

当前只可记录 agent-facing 姿态：

| 角色类型 | 默认姿态 | 证据状态 |
| --- | --- | --- |
| AI Agent | 要求读 source、走路由、标置信度、不要编造 | 用户指令 + SKILL.md，中 |
| 公开读者 | 先让人理解“我是谁”，再解释结构 | README 纠偏，中 |
| 工程协作者 | 先看项目现状、真相源和 gate，再行动 | Engineering Everything，中 |

不可萃取：

- 对合伙人、下属、客户、朋友、家人、陌生人的稳定姿态。
- 高压场景下关系姿态变化。

## 4.2 沟通策略

状态：中低置信度。

| 场景 | 当前策略 | 支撑 |
| --- | --- | --- |
| 复杂技术解释 | taxonomy + comparison table + glossary + use cases | Cognitive Arch 文章 |
| 跨域观点表达 | 先提出桥接视角，再逐层展开机制和差异 | AGI Appendix 文章 |
| 工程协作 | 直接、工程化、明确 source 和 gate | SKILL.md / Engineering Everything |
| 公开身份表达 | 主线优先，避免把经历写成无关清单 | 问心报告 |
| 拒绝/边界 | 对 source ownership 和公开边界直接纠偏 | 用户指令 |

不可萃取：

- 私下聊天语气、批评方式、鼓励方式。

## 4.3 语言指纹

状态：已提取正式英文写作样本；未提取中文私下语料。

自动提取结果来自 `analysis/linguistic_fingerprint.json`：

| 维度 | 当前结果 |
| --- | --- |
| 样本规模 | 8124 字符/词混合计数，222 句 |
| 平均句长 | 36.59 |
| 中位句长 | 17 |
| 句长分布 | 短句 40.1%，中句 27.5%，长句 32.4%，短长交替 |
| 逻辑展开 | 自动脚本未识别明显中文特征；人工观察为“主题定义 -> 机制展开 -> 对比 -> 应用落点” |
| 语域 | 正式技术写作，中性 |
| 情绪强度 | 极低，基本不靠情绪推进 |
| 标志性结构 | `What is it? / Cognitive interpretation / LLM integration`、comparison table、use case、glossary |

人工观察：

- 正式文章偏英文技术综述风格，喜欢先建立分类表，再逐项展开。
- 高频解释动作是“把 A 系统的机制映射到 B 系统的机制”，例如 Transformer 与 neocortex、attention 与 memory retrieval。
- 喜欢在文章末尾回到“这对 AGI/agent/LLM integration 意味着什么”，不是只做知识罗列。
- 当前样本不能代表中文口语、会议发言或私下聊天。

置信度：正式写作为中；个人语言复刻为低。

## 4.4 行为节奏

状态：低置信度。

当前只可记录候选观察：

- 问心报告：6 年工作日 2-3 小时 + 周末定向学习，说明长期节奏强。
- AGI Appendix 01：文章自述“months in the making”，说明对深层问题可长周期投入。
- repo 构建过程：对视觉、结构、模块名/实例名区分有多轮校准，说明对公开表达的结构和审美要求高。

不可萃取：

- 消息响应速度。
- 一天中的能量周期。
- 会议中真实行动节奏。

# 运行机制

## 最佳态目标

当前可推断的最佳态：

- 有足够时间做深层研究和跨域映射。
- 能把底层机制翻译成工程架构，再落到客户或产品场景。
- 保持 source ownership 清晰，避免把知识复制成失真的摘要。
- 对身份表达既有锋利主线，也保留真实短板。

## 当前不可投产原因

- Feishu 历史资料、会议、私下聊天未接入。
- 缺少至少 5 个真实冲突故事的原始证据链。
- 缺少 ≥20 条真人原话样本和 AI 输出样本的盲评。
- 语言指纹只有正式英文文章，不覆盖中文工作沟通与私下表达。
- 关系姿态、压力响应、行为节奏仍不可萃取。

## 演化规则

- 新增 Feishu/会议/聊天素材后，先更新 `raw_materials/meta.json`，再更新 `analysis/conflict_stories.md` 和 `analysis/pattern_observations.md`。
- 工作/生活事实保留在 AF-wiki；本 PSP 只提炼稳定模式，不复制事实库。
- 工程方法论变更保留在 Engineering Everything。
- 稳定 pattern 至少需要三个独立场景支撑，才能从低置信度升为中置信度。
- 只有 PSP 通过阶段一验收后，才生成可投产 `system_prompt.txt`。
