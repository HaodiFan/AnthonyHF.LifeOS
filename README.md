# AnthonyHF.Skill

AnthonyHF.Skill 是 Anthony Fan 的个人工程师分身与工作/生活上下文入口。

这个仓库不是泛化的个人品牌包装，也不是简历/个人 BP 工具。它的职责是承载 Anthony 当前的工程师身份、工程化判断方式、长期工作/生活记忆入口，以及可复用的工程方法论。

长期知识库放在 AF-wiki；工程方法论放在 Engineering Everything；本仓库只做顶层入口、路由和个人分身的轻量建模。

## 当前结构

| 层级 | 路径 | 作用 |
| --- | --- | --- |
| 根 Skill | `SKILL.md` | AnthonyHF 的触发入口、上下文路由和边界规则。 |
| 人物模型 | `people/anthony-fan/PSP.md` | 低置信度 PSP 骨架，目前只覆盖工程师身份切片。 |
| 工作/生活记忆 | `knowledge/af-wiki` | AF-wiki submodule，承载持续更新的 work/life second brain。 |
| 工程方法论 | `skills/engineering-everything` | Engineering Everything submodule，承载工程判断、项目执行和验证门禁。 |

## 明确边界

Wenxin Skill 不作为本仓库的 submodule。

AnthonyHF.Skill 默认不混入 Wenxin 式个人定位、个人 BP、简历包装或写作风格提炼。那些流程可以独立存在于自己的仓库或已安装 Skill 中。本仓库只负责 Anthony 的工程师分身、工作/生活上下文和工程化判断入口。

## 使用方式

克隆时拉取 submodule：

```bash
git clone --recurse-submodules https://github.com/HaodiFan/AnthonyHF.Skill.git
```

已有 checkout 初始化 submodule：

```bash
git submodule update --init --recursive
```

Agent 使用本仓库时：

1. 先读 `SKILL.md`。
2. 如果任务涉及 Anthony 当前工作/生活上下文，进入 `knowledge/af-wiki/START-HERE.md`。
3. 如果任务涉及工程判断、项目执行、架构、SOP 或 AI/Agent workflow，使用 `skills/engineering-everything/SKILL.md`。
4. 如果任务涉及 Anthony 的个人分身，读取 `people/anthony-fan/PSP.md`，但在补足原始素材前必须视为不完整模型。
