#!/usr/bin/env python3
"""Discover local CLI tools that may help find InnerAtlas source materials.

This scanner is intentionally discovery-only. It checks command availability
from PATH and does not fetch private content, enumerate repositories, or call
remote APIs. Any ingestion must be explicitly approved by the user later.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape


@dataclass(frozen=True)
class Candidate:
    command: str
    aliases: tuple[str, ...]
    source_type: str
    suggested_use: str
    approval_required: str = "true"


@dataclass(frozen=True)
class DiscoveryResult:
    scanned_at: str
    path_entries_scanned: int
    total_executables_seen: int
    candidates: list[dict]
    policy: str


CANDIDATES = [
    Candidate(
        command="larkcli",
        aliases=("larkcli", "lark", "feishu"),
        source_type="lark_docs_messages",
        suggested_use="Locate user-approved Feishu/Lark docs, profiles, meeting notes, or work traces.",
    ),
    Candidate(
        command="gh",
        aliases=("gh",),
        source_type="github_repos_issues_prs",
        suggested_use="Locate user-approved GitHub repositories, issues, pull requests, and public contribution traces.",
    ),
    Candidate(
        command="git",
        aliases=("git",),
        source_type="local_git_history",
        suggested_use="Locate user-approved local repositories and inspect commit/project history.",
    ),
    Candidate(
        command="rg",
        aliases=("rg", "ripgrep"),
        source_type="local_files_text_search",
        suggested_use="Search user-approved local folders for resumes, bios, notes, project records, and prior reports.",
    ),
    Candidate(
        command="fd",
        aliases=("fd", "fdfind"),
        source_type="local_files_path_search",
        suggested_use="Find user-approved local files and folders by filename patterns.",
    ),
    Candidate(
        command="mdfind",
        aliases=("mdfind",),
        source_type="macos_spotlight_index",
        suggested_use="Find user-approved local documents through macOS Spotlight metadata.",
    ),
    Candidate(
        command="obsidian",
        aliases=("obsidian",),
        source_type="obsidian_vaults",
        suggested_use="Open or locate user-approved Obsidian vault material; direct reading still requires approval.",
    ),
    Candidate(
        command="notion",
        aliases=("notion", "notion-cli"),
        source_type="notion_pages",
        suggested_use="Locate user-approved Notion pages or databases if a local Notion CLI is configured.",
    ),
    Candidate(
        command="gcloud",
        aliases=("gcloud",),
        source_type="cloud_project_metadata",
        suggested_use="Locate user-approved cloud project metadata that may evidence shipped systems.",
    ),
    Candidate(
        command="aws",
        aliases=("aws",),
        source_type="cloud_project_metadata",
        suggested_use="Locate user-approved cloud project metadata that may evidence shipped systems.",
    ),
]


def list_path_executables() -> set[str]:
    executables: set[str] = set()
    for path_entry in os.environ.get("PATH", "").split(os.pathsep):
        if not path_entry:
            continue
        path = Path(path_entry)
        if not path.is_dir():
            continue
        try:
            for child in path.iterdir():
                if child.is_file() and os.access(child, os.X_OK):
                    executables.add(child.name)
        except OSError:
            continue
    return executables


def discover() -> DiscoveryResult:
    executables = list_path_executables()
    discovered = []

    for candidate in CANDIDATES:
        matches = []
        command_path = None
        for alias in candidate.aliases:
            resolved = shutil.which(alias)
            if resolved:
                matches.append(alias)
                command_path = command_path or resolved

        if not matches:
            continue

        discovered.append(
            {
                "name": candidate.command,
                "matched_aliases": matches,
                "path": command_path,
                "status": "available",
                "source_type": candidate.source_type,
                "suggested_use": candidate.suggested_use,
                "approval_required": candidate.approval_required,
            }
        )

    if not discovered:
        discovered.append(
            {
                "name": "none",
                "matched_aliases": [],
                "path": "",
                "status": "not_found",
                "source_type": "none",
                "suggested_use": "No known source-discovery CLI was found in PATH; ask the user to provide raw materials manually.",
                "approval_required": "false",
            }
        )

    return DiscoveryResult(
        scanned_at=datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        path_entries_scanned=len([entry for entry in os.environ.get("PATH", "").split(os.pathsep) if entry]),
        total_executables_seen=len(executables),
        candidates=discovered,
        policy="Discovery only. Do not ingest local, private, remote, or account-bound material without explicit user approval.",
    )


def emit_xml_snippet(result: DiscoveryResult) -> str:
    def x(value: object) -> str:
        return escape(str(value), {'"': "&quot;"})

    lines = [
        '<source_discovery presentation="source_inventory">',
        f"  <scanned_at>{x(result.scanned_at)}</scanned_at>",
        "  <scan_status>completed</scan_status>",
        f"  <path_entries_scanned>{x(result.path_entries_scanned)}</path_entries_scanned>",
        f"  <total_executables_seen>{x(result.total_executables_seen)}</total_executables_seen>",
        f"  <discovery_policy>{x(result.policy)}</discovery_policy>",
        "  <cli_candidates>",
    ]
    for candidate in result.candidates:
        aliases = ",".join(candidate["matched_aliases"])
        lines.extend(
            [
                (
                    f'    <cli_candidate name="{x(candidate["name"])}" '
                    f'status="{x(candidate["status"])}" source_type="{x(candidate["source_type"])}" '
                    f'approval_required="{x(candidate["approval_required"])}">'
                ),
                f"      <matched_aliases>{x(aliases)}</matched_aliases>",
                f"      <command_path>{x(candidate['path'])}</command_path>",
                f"      <suggested_use>{x(candidate['suggested_use'])}</suggested_use>",
                "    </cli_candidate>",
            ]
        )
    lines.extend(["  </cli_candidates>", "</source_discovery>"])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan PATH for InnerAtlas source-discovery CLIs.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a text summary")
    parser.add_argument("--xml-snippet", action="store_true", help="Emit a source_discovery XML snippet")
    args = parser.parse_args()

    result = discover()
    if args.json:
        print(json.dumps(asdict(result), ensure_ascii=False, indent=2))
        return 0
    if args.xml_snippet:
        print(emit_xml_snippet(result))
        return 0

    print(f"scanned_at: {result.scanned_at}")
    print(f"path_entries_scanned: {result.path_entries_scanned}")
    print(f"total_executables_seen: {result.total_executables_seen}")
    print("policy: " + result.policy)
    print("\ncli_candidates:")
    for candidate in result.candidates:
        print(
            f"- {candidate['name']} [{candidate['status']}] "
            f"{candidate['source_type']} -> {candidate['suggested_use']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
