#!/usr/bin/env python3
"""Plan owner-reviewed updates for built-in openLifeOS default Skills.

This script intentionally does not overwrite Skills automatically. It reads
`skills/default-skills/skill-updates.yml` and prints the configured sources so an agent
or owner can fetch, diff, review, and then apply updates deliberately.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "skills" / "default-skills" / "skill-updates.yml"
SETUP_CONFIG = ROOT / "replicateme.yml"


def read_process_log_language() -> str:
    if not SETUP_CONFIG.exists():
        return "zh-CN"
    config: dict[str, str] = {}
    for raw_line in SETUP_CONFIG.read_text(encoding="utf-8").splitlines():
        if ":" not in raw_line or raw_line.startswith((" ", "\t", "-")):
            continue
        key, value = raw_line.split(":", 1)
        config[key.strip()] = value.strip().strip('"').strip("'")
    return config.get("process_log_language") or config.get("language") or "zh-CN"


def main() -> int:
    if not CONFIG.exists():
        raise SystemExit(f"Missing update config: {CONFIG}")
    zh = read_process_log_language() == "zh-CN"
    print("当前阶段：Default Skill Update Plan / 内置 Skill 更新计划" if zh else "Stage: Default Skill Update Plan")
    print("这是计划门禁，不会自动覆盖本地 Skill。" if zh else "This is a planning gate, not an automatic overwrite.")
    print()
    print(CONFIG.read_text(encoding="utf-8"))
    print(
        "下一步：把选定 GitHub ref 拉到临时目录，与 local_path 生成 diff，经 owner 确认后再应用。"
        if zh
        else "Next: fetch the selected GitHub ref into a temp directory, diff against local_path, then ask owner before applying."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
