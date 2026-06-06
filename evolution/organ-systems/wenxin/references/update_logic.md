# InnerAtlas XML Update Logic

InnerAtlas 的持续迭代只更新 artifact root 下的 `current/WENXIN_REPORT.xml` 和 `versions/WENXIN_REPORT.<version_id>.xml`。所有人类可读报告都从 XML 派生，不在本规则中直接维护。

## Artifact Root

每次更新前先解析产物根目录：

- 用户指定 root 时使用用户给的 root。
- 未指定时使用当前工作目录。
- current 文件固定为 `<root>/current/WENXIN_REPORT.xml`。
- 版本文件固定为 `<root>/versions/WENXIN_REPORT.<version_id>.xml`。
- 不允许直接覆盖历史版本。

## Update Modes

每次进入首次评估或增量更新前，先运行：

```bash
python scripts/inneratlas_source_scan.py --xml-snippet
```

把结果写入 `source_discovery`。这一步只发现可用资料入口 CLI，不读取资料；后续使用任何本地目录、仓库、Lark/Feishu、GitHub 或云账号来源前，必须获得用户明确授权和范围限制。

### Mode A: Full Re-run

适用：

- 用户经历重大变化。
- 用户认为旧画像不准。
- doctor 缺失字段过多，局部补齐成本高。

流程：

1. 归档旧 XML 到 `versions/WENXIN_REPORT.<old_version_id>.xml`。
2. 按阶段 0-5 重新收集材料和生成判断。
3. 写入新的 `versions/WENXIN_REPORT.<new_version_id>.xml`。
4. 同步更新 `current/WENXIN_REPORT.xml`。
5. 追加 `iteration_log/entry`。
6. 运行 `python scripts/inneratlas_doctor.py --root <root>`。
7. 若 completion < 100，按 doctor 的 `next_questions` 继续追问。

### Mode B: Partial Update

适用：

- 用户只想更新某几个维度。
- 新信息只影响 MBTI 变化轨迹、能力水位、Gap、里程碑、Skill 推荐或外号。

流程：

1. 读取当前 XML。
2. 列出可更新维度，让用户选择。
3. 只追问被选择维度所需材料。
4. 更新对应 XML 节点。
5. 将受影响字段写入 `iteration_log/entry/changes`。
6. 跑 doctor：`python scripts/inneratlas_doctor.py --root <root>`。
7. doctor 未达 100 时继续补齐。

### Mode C: Milestone Append

适用：

- 用户报告一个新项目、新职位、新融资、新作品、新学习结果或关键失败。

流程：

1. 追加 `milestones/milestone`。
2. 判断是否影响 `capability_levels`、`radar`、`barriers`、`skill_recommendations` 或 `identity_layer`。
3. 只更新受影响节点。
4. 追加 `iteration_log/entry`。
5. 跑 doctor：`python scripts/inneratlas_doctor.py --root <root>`。

## Nickname Recheck

外号重大变化才改。

触发条件：

- 任一关键维度变化 >= 30%。
- `public_mainline` 或 `private_mainline` 发生根本变化。
- 用户主动要求重新审视外号。
- 增量更新累计 3 次但外号从未重审。

触发后必须更新：

- `identity_layer/nickname_plain`
- `identity_layer/nickname_serious`
- `identity_layer/why_nickname_fits`
- `identity_layer/scarcity_judgment`
- `iteration_log`

然后跑 doctor。

## Doctor Discipline

不能手动宣称完成。只有 doctor 返回 `completion_percent: 100` 时，InnerAtlas 才算正式完成。

若 completion < 100：

- 把缺失字段写入 `missing_information`。
- 逐轮询问 doctor 的 `next_questions`。
- 用户跳过的问题写成 `status="user_skipped"`，并说明为什么跳过会影响完成度。
- 更新 XML 后继续跑 doctor。
