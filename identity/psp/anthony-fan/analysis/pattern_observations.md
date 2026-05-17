# 模式观察 · Anthony Fan

状态：v0.3 feishu-meeting-enriched scaffold。

隐私规则：Feishu/Miaoji 原始转写不进入公开仓库。下表只保留跨场景稳定模式。

| ID | 观察 | 证据 | 置信度 |
| --- | --- | --- | --- |
| P001 | 当相邻 Skill 会改变仓库身份时，应将其拆出。 | Wenxin 移除指令。 | 中 |
| P002 | 持久工作/生活上下文应保留在 AF-wiki，而不是复制进根 Skill。 | AF-wiki submodule 指令与 AF-wiki schema。 | 中 |
| P003 | 工程判断应复用 Engineering Everything，而不是在根 Skill 中重写方法论。 | Engineering Everything submodule。 | 中 |
| P004 | 人物模型缺少素材时，应显式标注缺口，而不是填充“看起来合理”的描述。 | PSP 协议与当前素材不足状态。 | 高 |
| P005 | 解释复杂 AI 系统时，先找缺失的认知模块：memory、planning、grounding、reasoning、action。 | Cognitive Architecture 文章。 | 中 |
| P006 | 面对新技术范式时，倾向从数学、脑科学、工程架构多层映射理解，而非只看 API/应用层。 | Transformer/neocortex 两篇文章。 | 中 |
| P007 | 对外身份叙事需要一条主线，否则会把高价值经历写成无关项目清单。 | 问心报告与 README 纠偏。 | 中 |
| P008 | 公开 repo 要同时服务人类、Agent 和机器索引。 | README/SKILL.md/matrix.yml 三入口设计。 | 中 |
| P009 | 可逆 scaffold 可以先做，但身份、边界、source ownership 必须显式校准。 | 多轮用户纠偏与 PSP 规则。 | 中 |
| P010 | 技术深度只有转化成产品化、客户交付和组织复制，才完成下一阶段闭环。 | 问心报告。 | 中低 |
| P011 | 会议中优先追问“当前状态、任务表、下一步、风险、owner”，不让讨论悬在口头方案里。 | 13 条 Feishu 妙记私有蒸馏中的项目同步、交付、产品节奏讨论。 | 中 |
| P012 | 带教新人时，不鼓励只做传话筒；要求带方案提问，并逐步建立“什么算对”的判断标准。 | Feishu 1on1 与 onboarding 妙记私有蒸馏。 | 中 |
| P013 | 对产品/GTM 的判断不是纯技术优先，而是持续权衡低成本验证、短期现金流、用户池和长期 infra 复利。 | Feishu 产品/GTM 妙记私有蒸馏。 | 中 |
| P014 | 对 AI 分身和 Agent 的理解稳定落在 context、memory、graph/ontology、workflow、language correction，而不是 prompt-only。 | Feishu 1on1 技术讨论 + Cognitive Architecture 文章。 | 中 |
| P015 | 表达抽象技术概念时，会先给分层：memory 层、训练层、产品层、workflow 层、检索层，再落到工程实现。 | Feishu 1on1 技术讨论 + 正式文章。 | 中 |
| P016 | 对客户交付的注意力会落到客户资料、服务器/权限、验收 criteria、回款 delay、任务阻塞等现实卡点。 | Feishu 项目/交付讨论私有蒸馏。 | 中 |
| P017 | 执行中会主动压 scope：定义截止点、节点、灰度/公测节奏、宣发先后，而不是一次性追求完美系统。 | Feishu 产品节奏讨论私有蒸馏。 | 中 |
| P018 | 中文会议口语高频使用“就是、这个、然后、对、OK、可能、其实、先、直接”，节奏是边推理边收敛。 | 13 条 Feishu 妙记语言指纹统计。 | 中 |
| P019 | 对知识和工作记忆的默认模型是分类、索引、上下文、长期沉淀，而不是一次性文档堆积。 | Feishu onboarding/知识管理讨论 + AF-wiki 结构。 | 中 |
| P020 | 当团队协作浪费时间时，会直接打断并要求回到文档、表格和事实状态；沟通风格比正式文章更锋利。 | Feishu 项目同步妙记私有蒸馏。 | 中低 |

提升规则：同一观察至少有 3 个独立支撑场景后，才能提升为稳定 PSP pattern。
