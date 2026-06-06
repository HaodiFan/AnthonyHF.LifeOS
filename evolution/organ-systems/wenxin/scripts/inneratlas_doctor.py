#!/usr/bin/env python3
"""Doctor for InnerAtlas canonical WENXIN_REPORT.xml outputs."""

from __future__ import annotations

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


PLACEHOLDERS = {
    "",
    "todo",
    "tbd",
    "unknown",
    "n/a",
    "na",
    "未知",
    "证据不足",
    "用户选择跳过",
    "待补充",
    "未判断",
}


@dataclass(frozen=True)
class Check:
    path: str
    label: str
    question: str
    attr: str | None = None
    min_count: int = 1


CHECKS = [
    Check(".", "artifact_name", "这个 XML 的逻辑产物名必须是 WENXIN_REPORT.xml。", attr="artifact_name"),
    Check(".", "version_id", "这个 XML 需要一个稳定 version_id，例如 20260606-191248。", attr="version_id"),
    Check("./metadata/generated_at", "生成时间", "这次 InnerAtlas 报告是什么日期生成的？"),
    Check("./metadata/last_updated", "最近更新时间", "这次报告最后更新时间是什么？"),
    Check("./metadata/artifact_root", "产物根目录", "这份报告的 artifact root 在哪里？"),
    Check("./metadata/current_path", "当前版本路径", "current XML 相对 artifact root 的路径是什么？"),
    Check("./metadata/version_path", "版本路径", "这个版本 XML 相对 artifact root 的路径是什么？"),
    Check("./metadata/subject_display_name", "对象显示名", "这份报告分析的是谁？可以用真实名、化名或公开名。"),
    Check("./metadata/assessment_mode", "评估模式", "请选择 quick 或 complete，并写入 metadata/assessment_mode。"),
    Check("./metadata/workflow_state", "工作流状态", "当前流程状态是什么？例如 mode_selected、interaction_needed、doctor_blocked 或 complete。"),
    Check("./metadata/report_status", "报告状态", "这份报告当前是 draft 还是 complete？"),
    Check("./source_discovery/scanned_at", "本地资料入口扫描时间", "启动时是否已扫描本机可用于寻找基础资料的 CLI？扫描时间是什么？"),
    Check("./source_discovery/scan_status", "本地资料入口扫描状态", "本地 CLI source discovery 是否已完成？"),
    Check("./source_discovery/discovery_policy", "资料发现授权策略", "请写明只发现入口、不自动读取私有资料，后续取材必须经用户授权。"),
    Check("./source_discovery/cli_candidates/cli_candidate", "资料入口 CLI 候选", "本机发现了哪些可用于寻找基础资料的 CLI？例如 larkcli、gh、git、rg、mdfind；没有发现也要记录 none。"),
    Check("./identity_layer/nickname_plain", "接地气外号", "用一句容易记住的中文外号概括这个人，会是什么？"),
    Check("./identity_layer/nickname_serious", "严肃版外号", "更正式、可放简历或 BP 的定位名是什么？"),
    Check("./identity_layer/one_line_positioning", "一句话定位", "用 30-60 字说明这个人是谁、稀缺在哪里。"),
    Check("./identity_layer/public_mainline", "对外主线", "对外介绍时，最适合使用哪条人物主线？"),
    Check("./identity_layer/private_mainline", "对内主线", "只给本人看的真实驱动主线是什么？"),
    Check("./identity_layer/why_nickname_fits", "外号成立理由", "这个外号压缩了哪些经历、能力或稀缺组合？"),
    Check("./identity_layer/scarcity_judgment", "稀缺性判断", "这个人的组合稀缺性是 ordinary、rare_local、rare_national 还是 rare_global？"),
    Check("./identity_layer/evidence", "身份层证据", "有哪些具体经历或行为证据支撑身份层判断？"),
    Check("./interaction_review/contradiction", "矛盾点复盘", "完整模式下，需要记录发现的矛盾点、影响字段和用户澄清。"),
    Check("./interaction_review/anomaly", "异常点复盘", "完整模式下，需要记录异常信号、解释假设和用户回应。"),
    Check("./interaction_review/confirmation", "重点产出确认", "完整模式下，需要记录重点产出字段的二次确认或模拟场景确认。"),
    Check("./explicit_analysis/mbti/method", "MBTI 处理方式", "MBTI 是已知、简化测试、用户跳过，还是证据不足？"),
    Check("./explicit_analysis/mbti/current_judgment", "MBTI 当前判断", "不要只写类型，四个维度目前分别如何倾向？"),
    Check("./explicit_analysis/mbti/dimension", "MBTI 四维", "E/I、S/N、T/F、J/P 四维分别是什么倾向、分数和证据？", min_count=4),
    Check("./explicit_analysis/mbti/change_trajectory", "MBTI 变化轨迹", "MBTI 或人格倾向过去到现在发生过什么变化？发生在什么阶段？"),
    Check("./explicit_analysis/mbti/evidence", "MBTI 证据", "哪些行为、测试或自述支撑人格维度判断？"),
    Check("./explicit_analysis/big_five/trait", "Big Five 五维", "Big Five 五个维度分别打几分、证据是什么？", min_count=5),
    Check("./explicit_analysis/capability_levels/capability", "能力水位", "至少列出一个关键能力领域，给实现层 L0-L5、元认知 L0-L5、覆盖度和证据。"),
    Check("./explicit_analysis/field_coverage/strength_zone", "优势区", "这个人的优势区有哪些？证据是什么？"),
    Check("./explicit_analysis/field_coverage/touched_zone", "触及区", "这个人触及但没有形成优势的领域有哪些？"),
    Check("./explicit_analysis/field_coverage/blank_zone", "空白区", "对目标方向重要但目前为空白的领域有哪些？"),
    Check("./explicit_analysis/gap_analysis/advantage_area", "Gap 分析", "至少选一个优势区，定义 100% 完整版、当前完成度、必须补和可不补。"),
    Check("./radar/dimension", "雷达图维度", "需要 5-7 个雷达图维度，每个有参照人物、分数、定义和证据。", min_count=5),
    Check("./radar/overall_shape", "雷达图整体形状", "雷达图整体形状是什么？钉子型、锯齿型、平衡型还是其他？"),
    Check("./barriers/barrier", "核心壁垒", "至少列出 3 个核心壁垒，每个要有来源、稀缺性、证据和 AI 时代耐受性。", min_count=3),
    Check("./milestones/milestone", "里程碑", "至少列出 3 个关键里程碑，每个要有事件、意义和证据。", min_count=3),
    Check("./pitch/who_they_are", "ta 是谁", "卖点三段第一段：ta 是谁？"),
    Check("./pitch/why_they_are_credible", "ta 凭什么", "卖点三段第二段：ta 凭什么？"),
    Check("./pitch/what_value_they_create", "ta 能给什么", "卖点三段第三段：ta 能给别人什么价值？"),
    Check("./soft_texture/pattern_sentence", "软实力质地", "需要 4-7 条条件、行为、证据组成的模式句。", min_count=4),
    Check("./skill_recommendations/recommended_skill", "Skill 推荐", "推荐这个人可以沉淀的稀缺元能力 Skill 或重复/岗位必需 workflow Skill。"),
    Check("./presentation_plan/section", "呈现形式定义", "每个产出部分要声明推荐呈现形式，例如 source inventory、text、x out of 5、radar chart、timeline。", min_count=13),
    Check("./missing_information/status", "缺失信息状态", "请明确当前是否还有不能判断或缺失信息；没有缺失也要写 no_missing_required_fields。"),
    Check("./iteration_log/entry", "迭代记录", "至少保留一个 append-only 迭代记录入口。"),
]


NESTED_REQUIREMENTS = {
    "./explicit_analysis/mbti/dimension": ["tendency", "score_out_of_100", "confidence"],
    "./explicit_analysis/big_five/trait": ["score_out_of_5", "confidence"],
    "./explicit_analysis/capability_levels/capability": [
        "name",
        "implementation_level",
        "metacognition_level",
        "coverage_percent",
        "confidence",
    ],
    "./radar/dimension": ["name", "reference_person", "score_out_of_100"],
    "./barriers/barrier": ["name"],
    "./milestones/milestone": ["date"],
    "./skill_recommendations/recommended_skill": ["name", "type", "recommend"],
    "./presentation_plan/section": ["name", "recommended_form"],
    "./source_discovery/cli_candidates/cli_candidate": ["name", "status", "source_type", "approval_required"],
}


CONTENT_NOT_REQUIRED = {
    "./explicit_analysis/mbti/dimension",
    "./presentation_plan/section",
}


def is_filled(value: str | None) -> bool:
    if value is None:
        return False
    normalized = " ".join(value.strip().lower().split())
    if normalized in PLACEHOLDERS:
        return False
    if normalized.startswith("[") and normalized.endswith("]"):
        return False
    return bool(normalized)


def element_has_content(element: ET.Element) -> bool:
    if is_filled(element.text):
        return True
    for child in list(element):
        if element_has_content(child):
            return True
    return False


def check_nested(element: ET.Element, attrs: list[str], require_content: bool = True) -> list[str]:
    missing = []
    for attr in attrs:
        if not is_filled(element.attrib.get(attr)):
            missing.append(f"@{attr}")
    if require_content and not element_has_content(element):
        missing.append("content")
    return missing


def run_doctor(path: Path) -> dict:
    if not path.exists():
        return {
            "status": "error",
            "completion_percent": 0,
            "error": f"File not found: {path}",
            "missing_fields": [],
            "next_questions": [f"请先生成 canonical XML: {path}"],
        }

    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        return {
            "status": "error",
            "completion_percent": 0,
            "error": f"Invalid XML: {exc}",
            "missing_fields": [],
            "next_questions": ["请先修复 WENXIN_REPORT.xml 的 XML 语法。"],
        }

    total = 0
    passed = 0
    missing_fields = []
    next_questions = []

    for check in CHECKS:
        mode = root.findtext("./metadata/assessment_mode", default="").strip().lower()
        if mode == "quick" and check.path.startswith("./interaction_review/"):
            continue
        total += 1
        elements = root.findall(check.path)
        valid_elements = []
        for element in elements:
            nested_missing = check_nested(
                element,
                NESTED_REQUIREMENTS.get(check.path, []),
                require_content=check.path not in CONTENT_NOT_REQUIRED,
            )
            if check.attr and not is_filled(element.attrib.get(check.attr)):
                nested_missing.append(f"@{check.attr}")
            has_required_content = check.path in CONTENT_NOT_REQUIRED or element_has_content(element)
            if not nested_missing and has_required_content:
                valid_elements.append(element)

        if len(valid_elements) >= check.min_count:
            passed += 1
            continue

        missing_fields.append(
            {
                "path": check.path,
                "label": check.label,
                "required_count": check.min_count,
                "current_valid_count": len(valid_elements),
            }
        )
        next_questions.append(check.question)

    completion_percent = round((passed / total) * 100) if total else 0
    status = "complete" if completion_percent == 100 else "incomplete"

    return {
        "status": status,
        "completion_percent": completion_percent,
        "report_path": str(path),
        "passed_checks": passed,
        "total_checks": total,
        "missing_fields": missing_fields,
        "next_questions": next_questions,
    }


def resolve_report_path(
    report: Path | None,
    root: Path | None,
    artifact_name: str,
    version_id: str | None,
) -> Path:
    if report is not None:
        return report

    artifact_root = root or Path.cwd()
    if version_id:
        return artifact_root / "versions" / f"{artifact_name.removesuffix('.xml')}.{version_id}.xml"
    return artifact_root / "current" / artifact_name


def print_text(result: dict) -> None:
    print(f"status: {result['status']}")
    print(f"completion_percent: {result['completion_percent']}")
    if result.get("error"):
        print(f"error: {result['error']}")
    if result["missing_fields"]:
        print("\nmissing_fields:")
        for field in result["missing_fields"]:
            print(
                f"- {field['label']} ({field['path']}): "
                f"{field['current_valid_count']}/{field['required_count']}"
            )
    if result["next_questions"]:
        print("\nnext_questions:")
        for question in result["next_questions"]:
            print(f"- {question}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Doctor InnerAtlas WENXIN_REPORT.xml completeness.")
    parser.add_argument("report", type=Path, nargs="?", help="Path to WENXIN_REPORT.xml")
    parser.add_argument("--root", type=Path, help="Artifact root containing current/ and versions/")
    parser.add_argument("--artifact-name", default="WENXIN_REPORT.xml", help="Logical artifact name")
    parser.add_argument("--version-id", help="Check versions/WENXIN_REPORT.<version_id>.xml instead of current")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    report_path = resolve_report_path(args.report, args.root, args.artifact_name, args.version_id)
    result = run_doctor(report_path)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_text(result)
    return 0 if result["status"] == "complete" else 1


if __name__ == "__main__":
    sys.exit(main())
