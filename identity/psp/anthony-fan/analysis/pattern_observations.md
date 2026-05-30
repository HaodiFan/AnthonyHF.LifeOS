# 模式观察 · Anthony Fan

状态：v0.4 chatgpt-export-enriched scaffold。

隐私规则：Feishu/Miaoji 原始转写和完整 ChatGPT export 不进入公开仓库。下表只保留跨场景稳定模式和公开可用的抽象结论。

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
| P021 | 把公司理解为 AI-native 杠杆机器：不是“一个人 + 一堆 AI”，而是 skill、SOP、角色、培训和 workflow 的组合。 | ChatGPT export：AI Native 创业公司、年度规划讨论。 | 高 |
| P022 | 当前身份从“做产品的工程师”推进到“企业自进化系统工程师”。 | ChatGPT export：AI Native 创业公司。 | 中高 |
| P023 | 产品机会研究先承认不确定性，再找公司/项目/论文/开源/客户场景证据。 | ChatGPT export：agent_data tools idea、Agent RL environment、GEO。 | 高 |
| P024 | 当产品清晰度是瓶颈时，明确要求 PRD / detailed PRD / design doc，而不是直接写代码。 | ChatGPT export 多场景短指令统计。 | 高 |
| P025 | 工程 runtime 倾向可检查、可续跑、数据库持久化和 Occam's Razor，不喜欢中间过程只散落成 JSON。 | ChatGPT export：Flow Orchestration、repo coding prompt。 | 高 |
| P026 | UI 结构跟生命周期、scope、对象层级、角色权限和 service blueprint 走。 | ChatGPT export：生命周期与 UI 布局。 | 高 |
| P027 | 创业复盘不只列产品，还追问交付吞吐、SOP 蒸馏、外部势能、软实力和个人价值点。 | ChatGPT export：GrainedAI 创业经验分析。 | 高 |
| P028 | ChatGPT 协作语言是高频短指令 + 强纠偏：先定义目标和边界，再持续修正误解。 | ChatGPT export 用户侧统计。 | 中高 |
| P029 | 工作 notes 倾向用 done / in-progress / issue / solution / next-plan 管理执行，关注具体 failure mode 和下一步修复。 | 外部硬盘 Feishu first read：Daily Notes redacted summary，作者/上下文待确认。 | 低 |
| P030 | 数据生产和交付中会把问题拆到截图时机、bbox 漂移、脏 OCR、key 判断、磁盘空间、限流、上传/下载速度等可操作变量。 | 外部硬盘 Feishu first read：Daily Notes、WebAgent 生产复盘 redacted summary。 | 中低 |
| P031 | Feishu 材料常混合正文、代码、凭证上下文、客户/项目记录，进入 PSP 前必须先做 redaction-first summary。 | 外部硬盘 Feishu first read 安全边界。 | 高 |

提升规则：同一观察至少有 3 个独立支撑场景后，才能提升为稳定 PSP pattern。
