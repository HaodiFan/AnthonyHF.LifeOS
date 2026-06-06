# InnerAtlas（问心）Skill

InnerAtlas，中文名「问心」，是一个用于个人定位、自我认知、职业经历重构和个人 BP 输出的 Codex/Agent Skill。

它的核心目标是帮助用户绕过学历、公司、title 等外部标签，从具体经历、行为痕迹、元认知水位和领域覆盖度出发，回答四个问题：

- 我是谁
- 我现在站在哪
- 我离所在领域的完整版还差多少
- 我该往哪走

## 目录结构

```text
.
├── SKILL.md
├── assets/
├── references/
└── scripts/
```

## 安装

将本仓库克隆到 Codex skills 目录中的 `inneratlas` 子目录：

```bash
git clone https://github.com/MetaInFLow/innerAtlas-skill.git ~/.codex/skills/inneratlas
```

安装后，重新启动 Codex 或刷新 skills，即可使用 `inneratlas` Skill。

兼容说明：历史 LifeOS 产物和下游协议仍可能使用 `WENXIN_REPORT.md`、`schema: wenxin-report` 和 `identity/wenxin/`。`wenxin` 是 legacy protocol id；`InnerAtlas` 是当前英文 repo/product name。新的 source-of-truth 产物必须写入 `WENXIN_REPORT.xml`。

## 标准产出物

InnerAtlas 的标准交付物是 `WENXIN_REPORT.xml`，协议版本从 `1.2` 起必须固定输出这些关键信息，并通过 doctor 达到 100% completion：

- `metadata`：评估模式、工作流状态、artifact root、current/version 路径。
- `source_discovery`：启动时扫描本机可用于寻找基础资料的 CLI，例如 `larkcli`、`gh`、`git`、`rg`、`mdfind`；只发现入口，用户授权后才取材。
- `身份层`：外号、一句话定位、对外主线、对内主线、稀缺性判断。
- `interaction_review`：完整模式下的矛盾点、异常点、重点产出确认或模拟场景确认。
- `显式分析结果`：MBTI 处理结果与变化轨迹、Big Five/行为维度、硬实力水位、元认知水位、领域覆盖图、完成度百分比、Gap 分析、Skill 候选、不能判断项。
- `雷达图`：5-7 个动态维度、参照人物、水位、证据和整体形状判断。
- `核心壁垒`：3-5 个壁垒，每个包含来源、稀缺性、证据和 AI 时代耐受性。
- `里程碑`：按时间顺序记录关键经历及其意义。
- `卖点三段`：ta 是谁、ta 凭什么、ta 能给你什么。
- `软实力质地`：4-7 条带证据的行为模式句。
- `presentation_plan`：每个部分的推荐呈现形式，例如 source inventory、文本、x out of 5 评分、L0-L5 评分表、百分比、雷达图、卡片、时间线、模式句列表。
- `missing_information`：doctor 发现的缺失字段、原因和下一轮追问。
- `持续迭代记录`：append-only 更新历史。

产出物 root 可自定义。推荐布局：

```text
<artifact_root>/
  current/WENXIN_REPORT.xml
  versions/WENXIN_REPORT.<version_id>.xml
  derived/
```

同名产物通过 `version_id` 区分版本，不覆盖历史版本。doctor 支持：

```bash
python scripts/inneratlas_doctor.py --root <artifact_root>
python scripts/inneratlas_doctor.py --root <artifact_root> --version-id <version_id>
```

启动扫描支持：

```bash
python scripts/inneratlas_source_scan.py
python scripts/inneratlas_source_scan.py --xml-snippet
python scripts/inneratlas_source_scan.py --json
```

扫描脚本只检查 `PATH` 中可用的资料入口 CLI，不读取本地文件、不枚举仓库、不调用账号 API。后续使用任何来源前必须让用户明确授权来源和范围。

运行模式：

- 快速模式：基于用户全部原始输入直接推理完整 XML；所有猜测必须写猜测依据；doctor 不满 100% 时只补问缺失项。
- 完整模式：先推理完整 XML draft，再围绕矛盾点、异常点、重点产出确认点进行交互；交互记录必须写入 `interaction_review`。

状态写入 `metadata/workflow_state`，只有 doctor 达到 100% 才能进入 `complete`。

## 内容

- `SKILL.md`: Skill 主说明和工作流
- `references/`: 问心方法论、题库、报告协议和领域校准材料
  - `interaction_templates.md`: 快速/完整模式、状态更新、矛盾点、异常点、重点确认和模拟场景模板
- `assets/`: 输出模板
- `scripts/`: 辅助脚本
  - `inneratlas_doctor.py`: 检查 artifact root 中的 `current/WENXIN_REPORT.xml` 或指定版本是否达到 100% completion
  - `inneratlas_source_scan.py`: 启动时扫描本机可用的资料入口 CLI，并输出可写入 XML 的 `source_discovery`

## License

This project is source-available under the PolyForm Noncommercial License 1.0.0. Noncommercial use is allowed; commercial use requires separate permission.
