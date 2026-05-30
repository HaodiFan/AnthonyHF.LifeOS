# Engineering Everything

`Engineering Everything` 是 Anthony 自己起的名字。

它不是说所有事情都要写代码，也不是把所有问题都变成软件工程问题。它的核心含义是：

> 很多构建类型的事情，都可以用工程化方式思考。

## What It Means

当一个任务涉及构建、交付、组织、产品、流程、判断或复盘时，Anthony 倾向于先问：

- 真相源是什么？
- 目标和边界是什么？
- 当前阶段是什么？
- 任务如何拆解？
- 谁负责，什么时候交付？
- 风险、阻塞和依赖在哪里？
- 验收标准是什么？
- 这次经验能不能沉淀成 SOP、Skill、模板或系统能力？

这是一种 meta skill：它提供判断框架和路由原则，不直接保存项目事实。

## Relationship To The Skill

- Skill entrypoint: `skills/engineering-everything/SKILL.md`
- Wenxin summary: `identity/wenxin/skill-summaries/engineering-everything.md`

AnthonyHF.LifeOS 中的 `SKILL.md` 是本地可路由入口；本文件是问心侧能力总结，负责说明它为什么存在、如何归类、什么时候使用。

## When To Use

Use this meta skill when the task is about:

- 软件工程、系统架构、代码审查、技术选型。
- 企业 AI 落地、agent workflow、数据链路、验证门禁。
- 产品定义、PRD、GTM、客户交付、实施路径。
- 组织机制、培训、SOP、项目治理、复盘。
- 把一次任务沉淀成可复用流程、skill、模板或方法论。

## Not For

- 私人事实存储。
- 原始会议/聊天/文档正文。
- Anthony 身份、履历或 PSP 结论。
- 直接替代 Wenxin、PSP、IPO Reverse 或 Cognitive Alignment。

事实和长期上下文应通过 `memory/wiki-repo.yml`、`memory/` tiers 或 `cognition/skill-bindings/data-sources.yml` 查询。

## Operating Gate

进入 Engineering Everything 时，agent 应先给出工程路由判断：

1. 当前任务属于 coding、产品、组织、流程、交付、研究、复盘还是 skill 沉淀。
2. 主抓手是什么。
3. 需要哪些输入和真相源。
4. 产出物写到哪里。
5. 验证 gate 是什么。

如果任务需要 Anthony-specific 状态，再按 `memory/wiki-repo.yml` 查询配置的 memory wiki；不要把事实硬写进本 meta skill。
