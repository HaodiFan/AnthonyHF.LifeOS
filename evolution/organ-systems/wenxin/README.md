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
git clone https://github.com/MetaInFLow/inneratlas.git ~/.codex/skills/inneratlas
```

安装后，重新启动 Codex 或刷新 skills，即可使用 `inneratlas` Skill。

兼容说明：历史 LifeOS 产物和下游协议仍使用 `WENXIN_REPORT.md`、`schema: wenxin-report` 和 `identity/wenxin/` 作为稳定 artifact/protocol 名称。`wenxin` 是 legacy protocol id；`InnerAtlas` 是当前英文 repo/product name。

## 内容

- `SKILL.md`: Skill 主说明和工作流
- `references/`: 问心方法论、题库、报告协议和领域校准材料
- `assets/`: 输出模板
- `scripts/`: 辅助脚本

## License

This project is source-available under the PolyForm Noncommercial License 1.0.0. Noncommercial use is allowed; commercial use requires separate permission.
