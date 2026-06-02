# AnthonyHF.LifeOS 文件夹结构说明

生成范围：`output/meta/AnthonyHF.LifeOS`。

说明：已排除 `.git`、`node_modules`、`.DS_Store`；每行 `#` 后是一句话作用说明，控制在 20 字内。

```text
AnthonyHF.LifeOS/ # LifeOS实例根
├── integrations/agents/ # Agent配置
│   └── openai.yaml # OpenAI配置
├── work/apps/ # 应用入口
│   └── homepage/ # 主页应用
│       ├── components/ # 组件目录
│       │   └── ui/ # UI组件
│       │       └── story-scroll.tsx # 故事滚动组件
│       ├── dist/ # 构建产物
│       │   ├── assets/ # 静态资产
│       │   │   ├── hardware/ # 硬件图片
│       │   │   │   ├── jetson-orin.png # 图片资产
│       │   │   │   └── jetson-xavier-clean.png # 图片资产
│       │   │   ├── logos/ # 品牌标识
│       │   │   │   ├── grainedai-logo-clean.png # 图片资产
│       │   │   │   ├── grainedai.svg # 矢量标识
│       │   │   │   ├── metainflow-logo.png # 图片资产
│       │   │   │   ├── metainflow.svg # 矢量标识
│       │   │   │   ├── nvidia-logo-clean.png # 图片资产
│       │   │   │   ├── nvidia.svg # 矢量标识
│       │   │   │   ├── shellprobe-logo.jpg # 图片资产
│       │   │   │   └── snapanthony-logo.png # 图片资产
│       │   │   ├── personal/ # 个人图片
│       │   │   │   ├── anthonyhf-readme-cover.png # 封面图片
│       │   │   │   └── selfie.jpg # 图片资产
│       │   │   ├── products/ # 产品图片
│       │   │   │   ├── shellprobe-product.jpg # 图片资产
│       │   │   │   └── snapanthony-product.png # 图片资产
│       │   │   ├── index-BnLsZEj6.js # 文件
│       │   │   ├── index-uaf-mR80.css # 样式文件
│       │   │   └── README.md # 目录说明
│       │   └── index.html # 页面入口
│       ├── lib/ # 工具函数
│       │   └── utils.ts # 工具函数
│       ├── public/ # 公共资源
│       │   └── assets/ # 静态资产
│       │       ├── hardware/ # 硬件图片
│       │       │   ├── jetson-orin.png # 图片资产
│       │       │   └── jetson-xavier-clean.png # 图片资产
│       │       ├── logos/ # 品牌标识
│       │       │   ├── grainedai-logo-clean.png # 图片资产
│       │       │   ├── grainedai.svg # 矢量标识
│       │       │   ├── metainflow-logo.png # 图片资产
│       │       │   ├── metainflow.svg # 矢量标识
│       │       │   ├── nvidia-logo-clean.png # 图片资产
│       │       │   ├── nvidia.svg # 矢量标识
│       │       │   ├── shellprobe-logo.jpg # 图片资产
│       │       │   └── snapanthony-logo.png # 图片资产
│       │       ├── personal/ # 个人图片
│       │       │   ├── anthonyhf-readme-cover.png # 封面图片
│       │       │   └── selfie.jpg # 图片资产
│       │       ├── products/ # 产品图片
│       │       │   ├── shellprobe-product.jpg # 图片资产
│       │       │   └── snapanthony-product.png # 图片资产
│       │       └── README.md # 目录说明
│       ├── src/ # 源码目录
│       │   ├── App.tsx # 主页组件
│       │   ├── index.css # 主页样式
│       │   ├── main.tsx # React入口
│       │   └── vite-env.d.ts # Vite类型
│       ├── components.json # 组件配置
│       ├── DESIGN.md # 审美入口
│       ├── index.html # 页面入口
│       ├── package-lock.json # 依赖锁定
│       ├── package.json # 前端包配置
│       ├── tsconfig.app.json # 应用TS配置
│       ├── tsconfig.json # TS总配置
│       ├── tsconfig.node.json # NodeTS配置
│       └── vite.config.ts # Vite配置
├── artifacts/ # 产物索引
│   ├── current.yml # 当前指针
│   └── README.md # 目录说明
├── cognition/ # 认知契约
│   ├── skill-bindings/ # Skill绑定
│   │   ├── data-sources.yml # 数据源声明
│   │   └── README.md # 目录说明
│   ├── data-contracts.yml # 数据契约
│   ├── object-taxonomy.yml # 对象分类
│   └── README.md # 目录说明
├── identity/design/ # 审美系统
│   ├── changelog.md # 变更记录
│   ├── DESIGN-20260530-235550.md # 说明文档
│   ├── README.md # 目录说明
│   └── versions.yml # 版本台账
├── docs/ # 说明文档
│   ├── assets/ # 静态资产
│   │   └── anthonyhf-readme-cover.png # 封面图片
│   ├── evidence-metabolism/inbox/ # 证据摄入
│   │   ├── external-drive-afelite-20260530.md # 说明文档
│   │   ├── external-drive-next-pass-20260530.md # 说明文档
│   │   ├── external-drive-project-first-read-20260530.md # 说明文档
│   │   └── feishu-first-read-20260530.md # 说明文档
│   ├── migration/ # 迁移记录
│   │   ├── anthonyhf-skill-import-report.md # Skill导入报告
│   │   ├── information-retention-audit-20260530.md # 信息保留审计
│   │   ├── platform-migration-instructions.md # 平台迁移说明
│   │   └── source-inventory.yml # 来源清单
│   ├── skill-system/ # 能力系统
│   │   └── runtime-skill-candidates.md # 运行Skill候选
│   ├── avatar-description-eval.md # 分身评估
│   ├── evidence-sufficiency.md # 证据成熟度
│   ├── lifeos-content-review.md # 内容审查
│   ├── README.md # 目录说明
│   └── self-evolution-output-standards.md # 自进化标准
├── identity/ # 身份系统
│   ├── avatar-description/ # 分身描述
│   │   ├── changelog.md # 变更记录
│   │   ├── current.yml # 当前指针
│   │   ├── README.md # 目录说明
│   │   └── versions.yml # 版本台账
│   ├── psp/ # 人物模型
│   │   ├── anthony-fan/ # Anthony模型
│   │   │   ├── analysis/ # 分析材料
│   │   │   │   ├── conflict_stories.md # 冲突故事
│   │   │   │   ├── feishu_private_evidence_summary.md # 飞书证据摘要
│   │   │   │   ├── feishu_writing_first_read_20260530.md # 飞书写作初读
│   │   │   │   ├── linguistic_fingerprint.json # 语言指纹
│   │   │   │   └── pattern_observations.md # 模式观察
│   │   │   ├── raw_materials/ # 原料占位
│   │   │   │   ├── chat_logs/ # 聊天占位
│   │   │   │   │   └── .gitkeep # 保留空目录
│   │   │   │   ├── emails/ # 邮件占位
│   │   │   │   │   └── .gitkeep # 保留空目录
│   │   │   │   ├── interviews/ # 访谈占位
│   │   │   │   │   └── .gitkeep # 保留空目录
│   │   │   │   ├── speeches/ # 演讲占位
│   │   │   │   │   └── .gitkeep # 保留空目录
│   │   │   │   ├── meta.json # 原料元数据
│   │   │   │   └── README.md # 目录说明
│   │   │   ├── validation/ # 验证材料
│   │   │   │   ├── test_samples/ # 测试样本
│   │   │   │   │   ├── ai_outputs/ # AI输出样本
│   │   │   │   │   │   └── .gitkeep # 保留空目录
│   │   │   │   │   └── human_samples/ # 真人样本
│   │   │   │   │       └── .gitkeep # 保留空目录
│   │   │   │   └── validation_report.md # 验证报告
│   │   │   ├── changelog.md # 变更记录
│   │   │   ├── current.yml # 当前指针
│   │   │   ├── INITIALIZATION.md # 初始化记录
│   │   │   ├── PSP-00000000-openlifeos.md # PSP初始版
│   │   │   ├── PSP-20260530-171725.md # PSP版本快照
│   │   │   ├── PSP.html # PSP结构页
│   │   │   ├── PSP.md # PSP旧入口
│   │   │   ├── PSP.xml # PSP机器版
│   │   │   ├── SOUL-20260530-235550.md # Soul版本快照
│   │   │   ├── system_prompt.txt # 系统提示草稿
│   │   │   ├── update-log-20260530-171725.md # PSP更新日志
│   │   │   └── versions.yml # 版本台账
│   │   └── README.md # 目录说明
│   ├── public-profile/ # 公开档案
│   │   ├── profile.yml # 公开档案
│   │   └── README.md # 目录说明
│   ├── wenxin/ # 问心产物
│   │   ├── project-evidence/ # 项目证据
│   │   │   ├── computer-use-datasets-20260530.md # 数据集证据
│   │   │   ├── feishu-project-ops-20260530.md # 飞书项目证据
│   │   │   ├── qcanything-platform-20260530.md # QC平台证据
│   │   │   ├── README.md # 目录说明
│   │   │   └── webtwin-20260530.md # WebTwin证据
│   │   ├── skill-summaries/ # Skill摘要
│   │   │   ├── engineering-everything.md # 工程能力摘要
│   │   │   └── README.md # 目录说明
│   │   ├── changelog.md # 变更记录
│   │   ├── project-evidence-external-drive-20260530.md # 外盘项目证据
│   │   ├── public-positioning.md # 公开定位
│   │   ├── README.md # 目录说明
│   │   ├── skill-recommendations.yml # Skill推荐
│   │   ├── versions.yml # 版本台账
│   │   ├── WENXIN-20260530-235550.md # 问心版本快照
│   │   ├── wenxin-report-continuous-founder-ascetic.pdf # 问心原PDF
│   │   ├── WENXIN_REPORT.html # 问心结构页
│   │   ├── WENXIN_REPORT.md # 问心旧入口
│   │   └── WENXIN_REPORT.xml # 问心机器版
│   ├── current.yml # 当前指针
│   └── README.md # 目录说明
├── integrations/ # 外部集成
│   ├── skill-sources/ # Skill来源
│   │   └── default-skills/ # 默认Skill源
│   │       ├── README.md # 目录说明
│   │       ├── self-evolution.md # 自进化说明
│   │       └── skill-updates.yml # Skill更新配置
│   ├── data-sources.yml # 数据源声明
│   ├── feishu.yml # 飞书集成
│   ├── github.yml # GitHub集成
│   ├── hermes-sync-log.md # Hermes同步日志
│   ├── hermes.yml # Hermes集成
│   └── README.md # 目录说明
├── memory/ # 长期记忆
│   ├── af-wiki/ # AF记忆库
│   ├── distilled-knowledge/ # 蒸馏知识
│   │   └── README.md # 目录说明
│   ├── long-term/ # 长期记忆
│   │   └── README.md # 目录说明
│   ├── working-lessons/ # 工作教训
│   │   └── README.md # 目录说明
│   ├── README.md # 目录说明
│   ├── START-HERE.md # 记忆入口
│   └── wiki-repo.yml # Wiki指针
├── runtime/profiles/ # 运行投影
│   ├── hermes/ # Hermes投影
│   │   └── anthonyhf/ # Anthony投影
│   │       ├── learning_queue/ # 学习队列
│   │       │   ├── skill-recommendations.yml # Skill推荐
│   │       │   └── working-lessons.README.md # 教训队列说明
│   │       ├── memories/ # 记忆种子
│   │       │   └── seed.md # 记忆种子
│   │       ├── config.yaml # 运行配置
│   │       ├── coverage-report.yml # 覆盖报告
│   │       ├── profile.manifest.yml # 投影清单
│   │       ├── PROFILE.md # 运行档案
│   │       ├── README.md # 目录说明
│   │       ├── SOUL.md # 处事方法
│   │       └── translation.review.md # 投影审查
│   └── openclaw/ # OpenClaw投影
│       └── anthonyhf/ # Anthony投影
│           ├── learning_queue/ # 学习队列
│           │   ├── skill-recommendations.yml # Skill推荐
│           │   └── working-lessons.README.md # 教训队列说明
│           ├── skills/ # 能力目录
│           │   ├── _source-links/ # 源链接
│           │   │   ├── engineering-everything/ # 工程MetaSkill
│           │   │   │   ├── integrations/agents/ # Agent配置
│           │   │   │   │   └── openai.yaml # OpenAI配置
│           │   │   │   ├── data/ # 配置数据
│           │   │   │   │   ├── review_roles.yaml # Review角色
│           │   │   │   │   ├── routes.yaml # 路由数据
│           │   │   │   │   └── validation_commands.yaml # 验证命令
│           │   │   │   ├── references/ # 参考资料
│           │   │   │   │   ├── agent-operating-standards.md # Agent执行标准
│           │   │   │   │   ├── architecture-cases-ai.md # AI架构案例
│           │   │   │   │   ├── architecture-cases.md # 架构案例
│           │   │   │   │   ├── checklists.md # 检查清单
│           │   │   │   │   ├── code-review-standards.md # 代码审查标准
│           │   │   │   │   ├── engineering-scenario-map.md # 工程场景地图
│           │   │   │   │   ├── engineering-scenarios.md # 工程扩展场景
│           │   │   │   │   ├── execution-pipeline.md # 执行流水线
│           │   │   │   │   ├── inheriting-projects.md # 接手项目指南
│           │   │   │   │   ├── lessons.md # 纠偏记录
│           │   │   │   │   ├── memory-bank-guide.md # 记忆库指南
│           │   │   │   │   ├── patterns-skill.md # 模式库
│           │   │   │   │   ├── project-blueprints.md # 项目蓝图
│           │   │   │   │   ├── prompts-guide.md # 提示词指南
│           │   │   │   │   ├── psps-framework.md # PSPS框架
│           │   │   │   │   ├── refactoring-rules.md # 重构规则
│           │   │   │   │   ├── scenario-playbooks.md # 场景手册
│           │   │   │   │   ├── spec-templates.md # 规格模板
│           │   │   │   │   ├── stage-playbook.md # 阶段手册
│           │   │   │   │   ├── templates-core.md # 核心模板
│           │   │   │   │   ├── templates-governance.md # 治理模板
│           │   │   │   │   └── templates-specs.md # 规格模板集
│           │   │   │   ├── schemas/ # 数据模式
│           │   │   │   │   ├── lesson.schema.json # Lesson模式
│           │   │   │   │   └── pattern.schema.json # Pattern模式
│           │   │   │   ├── scripts/ # 脚本目录
│           │   │   │   │   ├── install.py # 安装脚本
│           │   │   │   │   ├── lesson.py # Lesson脚本
│           │   │   │   │   └── skill_doctor.py # Skill体检脚本
│           │   │   │   ├── .git # 文件
│           │   │   │   ├── README.md # 目录说明
│           │   │   │   ├── SKILL.md # Skill入口
│           │   │   │   └── SKILLS-CATALOG.html # 场景地图
│           │   │   ├── ipo-reverse/ # IPO逆向
│           │   │   │   ├── evals/ # 评测数据
│           │   │   │   │   └── evals.json # 评测配置
│           │   │   │   ├── examples/ # 示例材料
│           │   │   │   │   ├── business-proposal-reverse.md # 商业逆向示例
│           │   │   │   │   ├── conversation-to-sop.md # 对话转SOP示例
│           │   │   │   │   └── skill-reverse.md # Skill逆向示例
│           │   │   │   ├── references/ # 参考资料
│           │   │   │   │   ├── active-inference-rules.md # 主动推理规则
│           │   │   │   │   ├── evidence-ladder.md # 证据阶梯
│           │   │   │   │   ├── ipo-output-template.md # IPO输出模板
│           │   │   │   │   ├── methodology-map.md # 方法论地图
│           │   │   │   │   ├── middle-layer-artifacts.md # 中间层产物
│           │   │   │   │   └── questioning-strategies.md # 提问策略
│           │   │   │   ├── .openlifeos-skill-source.yml # Skill来源声明
│           │   │   │   ├── ipo-reverse-spec.md # IPO规格
│           │   │   │   ├── ipo-reverse-v2-upgrade-spec.md # IPO升级规格
│           │   │   │   ├── LICENSE # 许可证
│           │   │   │   ├── README.md # 目录说明
│           │   │   │   └── SKILL.md # Skill入口
│           │   │   ├── lifeos-skills/ # 目录
│           │   │   │   ├── content/ # 内容能力
│           │   │   │   │   └── public-narrative-system/ # 公开叙事
│           │   │   │   │       ├── references/ # 参考资料
│           │   │   │   │       │   ├── channels/ # 渠道资料
│           │   │   │   │       │   │   └── rednote.md # 小红书规则
│           │   │   │   │       │   ├── humanizer-zh-adapter.md # 去AI腔规则
│           │   │   │   │       │   ├── lessons.md # 纠偏记录
│           │   │   │   │       │   ├── psp-voice-adapter.md # PSP语气适配
│           │   │   │   │       │   └── publication-repo-map.md # 发布仓库地图
│           │   │   │   │       ├── SKILL.md # Skill入口
│           │   │   │   │       └── SKILLS-CATALOG.html # 场景地图
│           │   │   │   ├── engineering-everything/ # 工程MetaSkill
│           │   │   │   │   ├── integrations/agents/ # Agent配置
│           │   │   │   │   │   └── openai.yaml # OpenAI配置
│           │   │   │   │   ├── data/ # 配置数据
│           │   │   │   │   │   ├── review_roles.yaml # Review角色
│           │   │   │   │   │   ├── routes.yaml # 路由数据
│           │   │   │   │   │   └── validation_commands.yaml # 验证命令
│           │   │   │   │   ├── references/ # 参考资料
│           │   │   │   │   │   ├── agent-operating-standards.md # Agent执行标准
│           │   │   │   │   │   ├── architecture-cases-ai.md # AI架构案例
│           │   │   │   │   │   ├── architecture-cases.md # 架构案例
│           │   │   │   │   │   ├── checklists.md # 检查清单
│           │   │   │   │   │   ├── code-review-standards.md # 代码审查标准
│           │   │   │   │   │   ├── engineering-scenario-map.md # 工程场景地图
│           │   │   │   │   │   ├── engineering-scenarios.md # 工程扩展场景
│           │   │   │   │   │   ├── execution-pipeline.md # 执行流水线
│           │   │   │   │   │   ├── inheriting-projects.md # 接手项目指南
│           │   │   │   │   │   ├── lessons.md # 纠偏记录
│           │   │   │   │   │   ├── memory-bank-guide.md # 记忆库指南
│           │   │   │   │   │   ├── patterns-skill.md # 模式库
│           │   │   │   │   │   ├── project-blueprints.md # 项目蓝图
│           │   │   │   │   │   ├── prompts-guide.md # 提示词指南
│           │   │   │   │   │   ├── psps-framework.md # PSPS框架
│           │   │   │   │   │   ├── refactoring-rules.md # 重构规则
│           │   │   │   │   │   ├── scenario-playbooks.md # 场景手册
│           │   │   │   │   │   ├── spec-templates.md # 规格模板
│           │   │   │   │   │   ├── stage-playbook.md # 阶段手册
│           │   │   │   │   │   ├── templates-core.md # 核心模板
│           │   │   │   │   │   ├── templates-governance.md # 治理模板
│           │   │   │   │   │   └── templates-specs.md # 规格模板集
│           │   │   │   │   ├── schemas/ # 数据模式
│           │   │   │   │   │   ├── lesson.schema.json # Lesson模式
│           │   │   │   │   │   └── pattern.schema.json # Pattern模式
│           │   │   │   │   ├── scripts/ # 脚本目录
│           │   │   │   │   │   ├── install.py # 安装脚本
│           │   │   │   │   │   ├── lesson.py # Lesson脚本
│           │   │   │   │   │   └── skill_doctor.py # Skill体检脚本
│           │   │   │   │   ├── .git # 文件
│           │   │   │   │   ├── README.md # 目录说明
│           │   │   │   │   ├── SKILL.md # Skill入口
│           │   │   │   │   └── SKILLS-CATALOG.html # 场景地图
│           │   │   │   ├── publication/ # 发布能力
│           │   │   │   ├── self-evolution/ # 自进化Skill
│           │   │   │   │   ├── cognitive-alignment/ # 认知对齐
│           │   │   │   │   │   └── SKILL.md # Skill入口
│           │   │   │   │   ├── ipo-reverse/ # IPO逆向
│           │   │   │   │   │   ├── evals/ # 评测数据
│           │   │   │   │   │   │   └── evals.json # 评测配置
│           │   │   │   │   │   ├── examples/ # 示例材料
│           │   │   │   │   │   │   ├── business-proposal-reverse.md # 商业逆向示例
│           │   │   │   │   │   │   ├── conversation-to-sop.md # 对话转SOP示例
│           │   │   │   │   │   │   └── skill-reverse.md # Skill逆向示例
│           │   │   │   │   │   ├── references/ # 参考资料
│           │   │   │   │   │   │   ├── active-inference-rules.md # 主动推理规则
│           │   │   │   │   │   │   ├── evidence-ladder.md # 证据阶梯
│           │   │   │   │   │   │   ├── ipo-output-template.md # IPO输出模板
│           │   │   │   │   │   │   ├── methodology-map.md # 方法论地图
│           │   │   │   │   │   │   ├── middle-layer-artifacts.md # 中间层产物
│           │   │   │   │   │   │   └── questioning-strategies.md # 提问策略
│           │   │   │   │   │   ├── .openlifeos-skill-source.yml # Skill来源声明
│           │   │   │   │   │   ├── ipo-reverse-spec.md # IPO规格
│           │   │   │   │   │   ├── ipo-reverse-v2-upgrade-spec.md # IPO升级规格
│           │   │   │   │   │   ├── LICENSE # 许可证
│           │   │   │   │   │   ├── README.md # 目录说明
│           │   │   │   │   │   └── SKILL.md # Skill入口
│           │   │   │   │   ├── psp/ # 人物模型
│           │   │   │   │   │   ├── references/ # 参考资料
│           │   │   │   │   │   │   ├── anti_blunting_rules.md # 反钝化规则
│           │   │   │   │   │   │   ├── extraction_protocol.md # 提取协议
│           │   │   │   │   │   │   ├── PSP_v2.1_full.md # PSP协议全文
│           │   │   │   │   │   │   ├── scoring_rules.md # 评分规则
│           │   │   │   │   │   │   └── system_prompt_structure.md # 提示结构
│           │   │   │   │   │   ├── scripts/ # 脚本目录
│           │   │   │   │   │   │   ├── blind_eval_prep.py # 盲评准备脚本
│           │   │   │   │   │   │   ├── consistency_scan.py # 一致性扫描
│           │   │   │   │   │   │   ├── extract_fingerprint.py # 指纹提取脚本
│           │   │   │   │   │   │   └── init_person.sh # 人物初始化脚本
│           │   │   │   │   │   ├── templates/ # 模板目录
│           │   │   │   │   │   │   ├── anti_blunting_template.md # 反钝化模板
│           │   │   │   │   │   │   ├── judgment_test_template.md # 判断测试模板
│           │   │   │   │   │   │   ├── PSP_template.md # PSP模板
│           │   │   │   │   │   │   ├── system_prompt_template.md # 系统提示模板
│           │   │   │   │   │   │   └── validation_report_template.md # 验证报告模板
│           │   │   │   │   │   ├── .gitignore # Git忽略规则
│           │   │   │   │   │   ├── .openlifeos-skill-source.yml # Skill来源声明
│           │   │   │   │   │   ├── LICENSE # 许可证
│           │   │   │   │   │   ├── README.md # 目录说明
│           │   │   │   │   │   └── SKILL.md # Skill入口
│           │   │   │   │   └── wenxin/ # 问心产物
│           │   │   │   │       ├── assets/ # 静态资产
│           │   │   │   │       │   └── output_template.md # 问心输出模板
│           │   │   │   │       ├── references/ # 参考资料
│           │   │   │   │       │   ├── domain_question_banks/ # 领域题库
│           │   │   │   │       │   │   ├── _template.md # 通用模板
│           │   │   │   │       │   │   ├── ecommerce.md # 电商题库
│           │   │   │   │       │   │   └── README.md # 目录说明
│           │   │   │   │       │   ├── knowledge_probes/ # 知识探针
│           │   │   │   │       │   │   ├── _template.md # 通用模板
│           │   │   │   │       │   │   ├── gpu_soc_architecture.md # GPU架构探针
│           │   │   │   │       │   │   └── README.md # 目录说明
│           │   │   │   │       │   ├── bp_reconstruction.md # BP重建方法
│           │   │   │   │       │   ├── coverage_assessment.md # 覆盖评估
│           │   │   │   │       │   ├── integration_with_web_design.md # 网页设计集成
│           │   │   │   │       │   ├── mbti_assessment.md # MBTI评估
│           │   │   │   │       │   ├── methodology_sources.md # 方法论来源
│           │   │   │   │       │   ├── questionnaire_bank.md # 问卷题库
│           │   │   │   │       │   ├── reference_person_matching.md # 参考人匹配
│           │   │   │   │       │   ├── update_logic.md # 更新逻辑
│           │   │   │   │       │   └── wenxin_report_protocol.md # 问心报告协议
│           │   │   │   │       ├── scripts/ # 脚本目录
│           │   │   │   │       │   ├── compare_versions.py # 版本对比脚本
│           │   │   │   │       │   └── generate_questionnaire.py # 问卷生成脚本
│           │   │   │   │       ├── .gitignore # Git忽略规则
│           │   │   │   │       ├── .openlifeos-skill-source.yml # Skill来源声明
│           │   │   │   │       ├── LICENSE # 许可证
│           │   │   │   │       ├── README.md # 目录说明
│           │   │   │   │       └── SKILL.md # Skill入口
│           │   │   │   ├── README.md # 目录说明
│           │   │   │   └── SKILLS-CATALOG.html # 场景地图
│           │   │   ├── migration-docs/ # 目录
│           │   │   │   ├── anthonyhf-skill-import-report.md # Skill导入报告
│           │   │   │   ├── information-retention-audit-20260530.md # 信息保留审计
│           │   │   │   ├── platform-migration-instructions.md # 平台迁移说明
│           │   │   │   └── source-inventory.yml # 来源清单
│           │   │   ├── self-evolution/ # 自进化Skill
│           │   │   │   ├── cognitive-alignment/ # 认知对齐
│           │   │   │   │   └── SKILL.md # Skill入口
│           │   │   │   ├── ipo-reverse/ # IPO逆向
│           │   │   │   │   ├── evals/ # 评测数据
│           │   │   │   │   │   └── evals.json # 评测配置
│           │   │   │   │   ├── examples/ # 示例材料
│           │   │   │   │   │   ├── business-proposal-reverse.md # 商业逆向示例
│           │   │   │   │   │   ├── conversation-to-sop.md # 对话转SOP示例
│           │   │   │   │   │   └── skill-reverse.md # Skill逆向示例
│           │   │   │   │   ├── references/ # 参考资料
│           │   │   │   │   │   ├── active-inference-rules.md # 主动推理规则
│           │   │   │   │   │   ├── evidence-ladder.md # 证据阶梯
│           │   │   │   │   │   ├── ipo-output-template.md # IPO输出模板
│           │   │   │   │   │   ├── methodology-map.md # 方法论地图
│           │   │   │   │   │   ├── middle-layer-artifacts.md # 中间层产物
│           │   │   │   │   │   └── questioning-strategies.md # 提问策略
│           │   │   │   │   ├── .openlifeos-skill-source.yml # Skill来源声明
│           │   │   │   │   ├── ipo-reverse-spec.md # IPO规格
│           │   │   │   │   ├── ipo-reverse-v2-upgrade-spec.md # IPO升级规格
│           │   │   │   │   ├── LICENSE # 许可证
│           │   │   │   │   ├── README.md # 目录说明
│           │   │   │   │   └── SKILL.md # Skill入口
│           │   │   │   ├── psp/ # 人物模型
│           │   │   │   │   ├── references/ # 参考资料
│           │   │   │   │   │   ├── anti_blunting_rules.md # 反钝化规则
│           │   │   │   │   │   ├── extraction_protocol.md # 提取协议
│           │   │   │   │   │   ├── PSP_v2.1_full.md # PSP协议全文
│           │   │   │   │   │   ├── scoring_rules.md # 评分规则
│           │   │   │   │   │   └── system_prompt_structure.md # 提示结构
│           │   │   │   │   ├── scripts/ # 脚本目录
│           │   │   │   │   │   ├── blind_eval_prep.py # 盲评准备脚本
│           │   │   │   │   │   ├── consistency_scan.py # 一致性扫描
│           │   │   │   │   │   ├── extract_fingerprint.py # 指纹提取脚本
│           │   │   │   │   │   └── init_person.sh # 人物初始化脚本
│           │   │   │   │   ├── templates/ # 模板目录
│           │   │   │   │   │   ├── anti_blunting_template.md # 反钝化模板
│           │   │   │   │   │   ├── judgment_test_template.md # 判断测试模板
│           │   │   │   │   │   ├── PSP_template.md # PSP模板
│           │   │   │   │   │   ├── system_prompt_template.md # 系统提示模板
│           │   │   │   │   │   └── validation_report_template.md # 验证报告模板
│           │   │   │   │   ├── .gitignore # Git忽略规则
│           │   │   │   │   ├── .openlifeos-skill-source.yml # Skill来源声明
│           │   │   │   │   ├── LICENSE # 许可证
│           │   │   │   │   ├── README.md # 目录说明
│           │   │   │   │   └── SKILL.md # Skill入口
│           │   │   │   └── wenxin/ # 问心产物
│           │   │   │       ├── assets/ # 静态资产
│           │   │   │       │   └── output_template.md # 问心输出模板
│           │   │   │       ├── references/ # 参考资料
│           │   │   │       │   ├── domain_question_banks/ # 领域题库
│           │   │   │       │   │   ├── _template.md # 通用模板
│           │   │   │       │   │   ├── ecommerce.md # 电商题库
│           │   │   │       │   │   └── README.md # 目录说明
│           │   │   │       │   ├── knowledge_probes/ # 知识探针
│           │   │   │       │   │   ├── _template.md # 通用模板
│           │   │   │       │   │   ├── gpu_soc_architecture.md # GPU架构探针
│           │   │   │       │   │   └── README.md # 目录说明
│           │   │   │       │   ├── bp_reconstruction.md # BP重建方法
│           │   │   │       │   ├── coverage_assessment.md # 覆盖评估
│           │   │   │       │   ├── integration_with_web_design.md # 网页设计集成
│           │   │   │       │   ├── mbti_assessment.md # MBTI评估
│           │   │   │       │   ├── methodology_sources.md # 方法论来源
│           │   │   │       │   ├── questionnaire_bank.md # 问卷题库
│           │   │   │       │   ├── reference_person_matching.md # 参考人匹配
│           │   │   │       │   ├── update_logic.md # 更新逻辑
│           │   │   │       │   └── wenxin_report_protocol.md # 问心报告协议
│           │   │   │       ├── scripts/ # 脚本目录
│           │   │   │       │   ├── compare_versions.py # 版本对比脚本
│           │   │   │       │   └── generate_questionnaire.py # 问卷生成脚本
│           │   │   │       ├── .gitignore # Git忽略规则
│           │   │   │       ├── .openlifeos-skill-source.yml # Skill来源声明
│           │   │   │       ├── LICENSE # 许可证
│           │   │   │       ├── README.md # 目录说明
│           │   │   │       └── SKILL.md # Skill入口
│           │   │   └── root-skill # 文件
│           │   ├── anthonyhf-root/ # 根Skill投影
│           │   │   └── SKILL.md # Skill入口
│           │   ├── engineering-everything/ # 工程MetaSkill
│           │   │   └── SKILL.md # Skill入口
│           │   ├── openlifeos-migration/ # 迁移Skill
│           │   │   └── SKILL.md # Skill入口
│           │   ├── self-evolution/ # 自进化Skill
│           │   │   ├── cognitive-alignment/ # 认知对齐
│           │   │   │   └── SKILL.md # Skill入口
│           │   │   ├── ipo-reverse/ # IPO逆向
│           │   │   │   └── SKILL.md # Skill入口
│           │   │   ├── psp/ # 人物模型
│           │   │   │   └── SKILL.md # Skill入口
│           │   │   └── wenxin/ # 问心产物
│           │   │       └── SKILL.md # Skill入口
│           │   └── _source-links.md # 源链接索引
│           ├── AGENTS.md # Agent规则
│           ├── coverage-report.yml # 覆盖报告
│           ├── IDENTITY.md # 身份投影
│           ├── profile.manifest.yml # 投影清单
│           ├── README.md # 目录说明
│           ├── SOUL.md # 处事方法
│           ├── TOOLS.md # 工具投影
│           ├── translation.review.md # 投影审查
│           └── USER.md # 用户上下文
├── scripts/ # 脚本目录
│   └── update_default_skills.py # 更新默认Skill
├── security/ # 安全边界
│   ├── permissions.yml # 权限边界
│   └── README.md # 目录说明
├── skills/ # 能力目录
│   ├── content/ # 内容能力
│   │   └── public-narrative-system/ # 公开叙事
│   │       ├── references/ # 参考资料
│   │       │   ├── channels/ # 渠道资料
│   │       │   │   └── rednote.md # 小红书规则
│   │       │   ├── humanizer-zh-adapter.md # 去AI腔规则
│   │       │   ├── lessons.md # 纠偏记录
│   │       │   ├── psp-voice-adapter.md # PSP语气适配
│   │       │   └── publication-repo-map.md # 发布仓库地图
│   │       ├── SKILL.md # Skill入口
│   │       └── SKILLS-CATALOG.html # 场景地图
│   ├── engineering-everything/ # 工程MetaSkill
│   │   ├── integrations/agents/ # Agent配置
│   │   │   └── openai.yaml # OpenAI配置
│   │   ├── data/ # 配置数据
│   │   │   ├── review_roles.yaml # Review角色
│   │   │   ├── routes.yaml # 路由数据
│   │   │   └── validation_commands.yaml # 验证命令
│   │   ├── references/ # 参考资料
│   │   │   ├── agent-operating-standards.md # Agent执行标准
│   │   │   ├── architecture-cases-ai.md # AI架构案例
│   │   │   ├── architecture-cases.md # 架构案例
│   │   │   ├── checklists.md # 检查清单
│   │   │   ├── code-review-standards.md # 代码审查标准
│   │   │   ├── engineering-scenario-map.md # 工程场景地图
│   │   │   ├── engineering-scenarios.md # 工程扩展场景
│   │   │   ├── execution-pipeline.md # 执行流水线
│   │   │   ├── inheriting-projects.md # 接手项目指南
│   │   │   ├── lessons.md # 纠偏记录
│   │   │   ├── memory-bank-guide.md # 记忆库指南
│   │   │   ├── patterns-skill.md # 模式库
│   │   │   ├── project-blueprints.md # 项目蓝图
│   │   │   ├── prompts-guide.md # 提示词指南
│   │   │   ├── psps-framework.md # PSPS框架
│   │   │   ├── refactoring-rules.md # 重构规则
│   │   │   ├── scenario-playbooks.md # 场景手册
│   │   │   ├── spec-templates.md # 规格模板
│   │   │   ├── stage-playbook.md # 阶段手册
│   │   │   ├── templates-core.md # 核心模板
│   │   │   ├── templates-governance.md # 治理模板
│   │   │   └── templates-specs.md # 规格模板集
│   │   ├── schemas/ # 数据模式
│   │   │   ├── lesson.schema.json # Lesson模式
│   │   │   └── pattern.schema.json # Pattern模式
│   │   ├── scripts/ # 脚本目录
│   │   │   ├── install.py # 安装脚本
│   │   │   ├── lesson.py # Lesson脚本
│   │   │   └── skill_doctor.py # Skill体检脚本
│   │   ├── .git # 文件
│   │   ├── README.md # 目录说明
│   │   ├── SKILL.md # Skill入口
│   │   └── SKILLS-CATALOG.html # 场景地图
│   ├── publication/ # 发布能力
│   ├── self-evolution/ # 自进化Skill
│   │   ├── cognitive-alignment/ # 认知对齐
│   │   │   └── SKILL.md # Skill入口
│   │   ├── ipo-reverse/ # IPO逆向
│   │   │   ├── evals/ # 评测数据
│   │   │   │   └── evals.json # 评测配置
│   │   │   ├── examples/ # 示例材料
│   │   │   │   ├── business-proposal-reverse.md # 商业逆向示例
│   │   │   │   ├── conversation-to-sop.md # 对话转SOP示例
│   │   │   │   └── skill-reverse.md # Skill逆向示例
│   │   │   ├── references/ # 参考资料
│   │   │   │   ├── active-inference-rules.md # 主动推理规则
│   │   │   │   ├── evidence-ladder.md # 证据阶梯
│   │   │   │   ├── ipo-output-template.md # IPO输出模板
│   │   │   │   ├── methodology-map.md # 方法论地图
│   │   │   │   ├── middle-layer-artifacts.md # 中间层产物
│   │   │   │   └── questioning-strategies.md # 提问策略
│   │   │   ├── .openlifeos-skill-source.yml # Skill来源声明
│   │   │   ├── ipo-reverse-spec.md # IPO规格
│   │   │   ├── ipo-reverse-v2-upgrade-spec.md # IPO升级规格
│   │   │   ├── LICENSE # 许可证
│   │   │   ├── README.md # 目录说明
│   │   │   └── SKILL.md # Skill入口
│   │   ├── psp/ # 人物模型
│   │   │   ├── references/ # 参考资料
│   │   │   │   ├── anti_blunting_rules.md # 反钝化规则
│   │   │   │   ├── extraction_protocol.md # 提取协议
│   │   │   │   ├── PSP_v2.1_full.md # PSP协议全文
│   │   │   │   ├── scoring_rules.md # 评分规则
│   │   │   │   └── system_prompt_structure.md # 提示结构
│   │   │   ├── scripts/ # 脚本目录
│   │   │   │   ├── blind_eval_prep.py # 盲评准备脚本
│   │   │   │   ├── consistency_scan.py # 一致性扫描
│   │   │   │   ├── extract_fingerprint.py # 指纹提取脚本
│   │   │   │   └── init_person.sh # 人物初始化脚本
│   │   │   ├── templates/ # 模板目录
│   │   │   │   ├── anti_blunting_template.md # 反钝化模板
│   │   │   │   ├── judgment_test_template.md # 判断测试模板
│   │   │   │   ├── PSP_template.md # PSP模板
│   │   │   │   ├── system_prompt_template.md # 系统提示模板
│   │   │   │   └── validation_report_template.md # 验证报告模板
│   │   │   ├── .gitignore # Git忽略规则
│   │   │   ├── .openlifeos-skill-source.yml # Skill来源声明
│   │   │   ├── LICENSE # 许可证
│   │   │   ├── README.md # 目录说明
│   │   │   └── SKILL.md # Skill入口
│   │   └── wenxin/ # 问心产物
│   │       ├── assets/ # 静态资产
│   │       │   └── output_template.md # 问心输出模板
│   │       ├── references/ # 参考资料
│   │       │   ├── domain_question_banks/ # 领域题库
│   │       │   │   ├── _template.md # 通用模板
│   │       │   │   ├── ecommerce.md # 电商题库
│   │       │   │   └── README.md # 目录说明
│   │       │   ├── knowledge_probes/ # 知识探针
│   │       │   │   ├── _template.md # 通用模板
│   │       │   │   ├── gpu_soc_architecture.md # GPU架构探针
│   │       │   │   └── README.md # 目录说明
│   │       │   ├── bp_reconstruction.md # BP重建方法
│   │       │   ├── coverage_assessment.md # 覆盖评估
│   │       │   ├── integration_with_web_design.md # 网页设计集成
│   │       │   ├── mbti_assessment.md # MBTI评估
│   │       │   ├── methodology_sources.md # 方法论来源
│   │       │   ├── questionnaire_bank.md # 问卷题库
│   │       │   ├── reference_person_matching.md # 参考人匹配
│   │       │   ├── update_logic.md # 更新逻辑
│   │       │   └── wenxin_report_protocol.md # 问心报告协议
│   │       ├── scripts/ # 脚本目录
│   │       │   ├── compare_versions.py # 版本对比脚本
│   │       │   └── generate_questionnaire.py # 问卷生成脚本
│   │       ├── .gitignore # Git忽略规则
│   │       ├── .openlifeos-skill-source.yml # Skill来源声明
│   │       ├── LICENSE # 许可证
│   │       ├── README.md # 目录说明
│   │       └── SKILL.md # Skill入口
│   ├── README.md # 目录说明
│   └── SKILLS-CATALOG.html # 场景地图
├── .gitignore # Git忽略规则
├── .gitmodules # 子模块声明
├── DELIVERY.md # 交付说明
├── DESIGN.md # 审美入口
├── LIFEOS_STATUS.yml # 状态真相源
├── matrix.yml # 能力矩阵
├── README.md # 目录说明
├── replicateme.yml # 配置指针
├── SKILL.md # Skill入口
└── SOUL.md # 处事方法
```

## 读法

- `identity/` 是身份真相源。
- `skills/` 是可执行或可路由能力。
- `memory/` 是长期记忆入口。
- `runtime/profiles/` 是运行时投影，不是真相源。
- `work/apps/homepage/` 是展示页面源码和构建产物。

