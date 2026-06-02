# File Structure Policy

这个文件定义 AnthonyHF.LifeOS 的文件级结构，避免 `.md` 文件重复和散乱。

## Source Of Truth

| File | Role |
| --- | --- |
| `artifacts/current.yml` | 全局 latest registry，声明当前核心产物入口。 |
| `identity/current.yml` | identity active registry，声明当前 Wenxin、PSP、Soul 等入口。 |
| `matrix.yml` | 机器可读结构索引。 |
| `docs/file-role-inventory.yml` | 当前文件级审计表；只解释文件角色，不替代任何内容真相源。 |
| `docs/layer-file-review.md` | 当前层级审计摘要；汇总 trim 决策，不替代 schema 或 registry。 |
| `docs/schema-trim-completion-audit.md` | schema trim 完成审计；记录验证证据，不替代 current registry。 |
| `docs/avatar-page-information-architecture.md` | 第三人称 avatar 页面信息架构；定义展示层消费哪些 LifeOS 产物。 |

`SOUL.md`、`DESIGN.md`、`SKILL.md` 是当前入口，不是完整证据源。

## Markdown File Classes

| Class | Allowed Location | Rule |
| --- | --- | --- |
| current entrypoint | root, `identity/*/current` | 给用户或 agent 快速读取当前版本。 |
| versioned artifact | `identity/wenxin/`, `identity/psp/*/`, `identity/design/` | 保留历史版本，不能替代 current registry。 |
| evidence intake | `metabolism/inbox/`, `metabolism/processing/`, `metabolism/extracted/` | 记录材料进入、处理、抽取，不放在 `docs/`。 |
| runtime projection | `runtime/profiles/*` | 目标 runtime 的生成投影，不是真源。 |
| runtime local profile | `runtime/runtime-profile/` | 本 LifeOS 的运行期画像占位，记录当前上下文/限制/adapter 状态，不是真源。 |
| runtime skill binding | `runtime/runtime-skills/*/manifest.yml` | 可调用或待验证 runtime skill 的本地/外部 repo 绑定、输入输出和升级门。 |
| capability reference | `capabilities/*/references/` | 能力内部知识库，归能力所有。 |
| organ-system reference | `evolution/organ-systems/*` | Wenxin/PSP/IPO 等生产系统自带文件。 |
| app source | `work/apps/*` | 可运行作品源码、配置和公开素材；不放构建产物。 |
| build output | `legacy/build-output/*` | 历史构建产物或发布包，保留但不参与当前 schema 语义。 |
| human docs | `docs/` | 只放标准、review、migration、说明，不放 evidence intake。 |
| legacy | `legacy/` | 旧结构说明、历史导入报告、无法分类材料。 |

## Trim Rules

- 不删除 versioned artifact；只通过 registry 激活当前版本。
- 不把 runtime projection 当 LifeOS 真源。
- 不把 evidence intake 放在 `docs/`。
- 不在 root 新增 Markdown 入口，除非它是 schema required root file。
- 旧结构说明进入 `legacy/docs-v1/`。

## Current Known Buckets

- `metabolism/processing/evidence-intake/`: 外部硬盘、Feishu、first-read 等摄入处理记录。
- `identity/psp/anthony-fan/analysis/`: PSP 分析证据，非最终 PSP。
- `runtime/profiles/`: OpenClaw/Hermes projection。
- `runtime/runtime-profile/`: 本地运行期画像占位，不等同于 runtime projection。
- `runtime/runtime-skills/snapaf/`: 外部 runtime skill repo 绑定样本。
- `capabilities/*/references/`: 能力本体内部资料。
- `work/apps/homepage/`: homepage 源码和公开素材。
- `legacy/build-output/homepage-dist-20260602/`: homepage 历史 Vite build output。

## Schema V2 Structure

| Layer | Keeps | Does Not Keep |
| --- | --- | --- |
| `identity/` | Wenxin、PSP、Soul、cognition、memories、public profile、design。 | session 过程、临时 lesson、应用源码。 |
| `metabolism/` | inbox、processing、extracted 的材料消化过程。 | 已形成的身份结论和能力。 |
| `runtime/` | sessions、runtime-skills、runtime-lessons、runtime profiles、working memory。 | 长期人格真相源和稳定能力本体。 |
| `capabilities/` | 经 IPO/owner alignment 后沉淀的稳定能力。 | Wenxin/PSP/IPO 生产系统本身。 |
| `evolution/` | IPO、alignment、mutations、organ-systems。 | runtime projection 和工作产物。 |
| `identities/` | founder、teacher、author 等社会身份投影。 | 人格核心和 PSP。 |
| `work/` | projects、apps、reports、publications 等作品源文件和索引。 | build output、私密原文、长期记忆。 |
| `legacy/` | v1/v1.5 历史、无法归类材料、历史构建产物。 | 当前 schema 真相源。 |

## Duplicate Policy

- Exact duplicate build output moves to `legacy/build-output/`.
- Runtime profile duplicates are allowed only when they are generated projections with a manifest or coverage report.
- External runtime skills are represented by manifest only unless explicitly vendored; do not copy them into `capabilities/`.
- Capability reference files and organ-system reference files are not duplicates across layers; they belong to different owners.
- Public app assets may duplicate documentation assets only when the app needs a web-served copy; document the reason in the app asset README.
