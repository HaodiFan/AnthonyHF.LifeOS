# InnerAtlas（问心）WENXIN_REPORT.xml · Canonical Output Contract

InnerAtlas（问心）的原始标准产物逻辑名只有一个：`WENXIN_REPORT.xml`。

Markdown、HTML、PDF、长图、简历、BP 和网页都只能是从 XML 派生的 presentation artifact，不是源产物。任何字段没有写进 XML，都视为没有完成。

## Artifact Root

产出物根目录必须可自定义。不要假设当前工作目录就是产出目录。

默认 root 是当前工作目录；用户或调用方可以指定任意 root，例如：

```bash
python scripts/inneratlas_doctor.py --root ./inneratlas-output
python scripts/inneratlas_doctor.py --root /path/to/person-artifacts
```

推荐布局：

```text
<artifact_root>/
  current/
    WENXIN_REPORT.xml
  versions/
    WENXIN_REPORT.20260606-191248.xml
    WENXIN_REPORT.20260607-101500.xml
  derived/
    report.md
    report.html
    report.pdf
  ARTIFACTS.xml
```

- `current/WENXIN_REPORT.xml` 是当前 active XML。
- `versions/WENXIN_REPORT.<version_id>.xml` 保存同名产物的不同版本。
- `derived/` 只能保存从 XML 派生的人类可读产物。
- `ARTIFACTS.xml` 可选，用于记录 current 指针、版本列表和派生物来源。

同名产物允许有多个版本，但必须通过 `version_id` 区分；不得覆盖历史版本。

## Completion Rule

`WENXIN_REPORT.xml` 必须跑 doctor。doctor 输出 `completion_percent`、缺失字段、证据不足字段和下一轮追问。

- `completion_percent = 100` 才算正式完成。
- 小于 100 时，只能输出临时画像或中间报告。
- agent 必须根据 doctor 的 `next_questions` 继续多轮对话获取材料，再更新 XML，再重跑 doctor。
- 用户明确拒绝回答的字段也不能静默跳过；写入 XML 的 `missing_information`，状态标为 `user_skipped`，并由 doctor 判断是否允许作为 completion exception。

## Canonical XML Skeleton

```xml
<inneratlas_report schema="inneratlas-report" version="1.2" artifact_name="WENXIN_REPORT.xml" version_id="20260606-191248" language="zh-CN">
  <metadata>
    <generated_at>2026-06-06</generated_at>
    <last_updated>2026-06-06</last_updated>
    <artifact_root></artifact_root>
    <current_path>current/WENXIN_REPORT.xml</current_path>
    <version_path>versions/WENXIN_REPORT.20260606-191248.xml</version_path>
    <subject_display_name></subject_display_name>
    <assessment_mode>quick|complete</assessment_mode>
    <workflow_state>mode_selected|input_ingested|initial_inference_done|interaction_needed|interaction_done|xml_draft_written|doctor_running|doctor_blocked|complete</workflow_state>
    <report_status>draft|complete</report_status>
    <completion_percent>0</completion_percent>
  </metadata>

  <source_discovery presentation="source_inventory">
    <scanned_at></scanned_at>
    <scan_status>completed|skipped|failed</scan_status>
    <path_entries_scanned></path_entries_scanned>
    <total_executables_seen></total_executables_seen>
    <discovery_policy>Discovery only. Do not ingest local, private, remote, or account-bound material without explicit user approval.</discovery_policy>
    <cli_candidates>
      <cli_candidate name="gh" status="available|not_found" source_type="github_repos_issues_prs" approval_required="true">
        <matched_aliases></matched_aliases>
        <command_path></command_path>
        <suggested_use></suggested_use>
        <user_approval>pending|approved|denied</user_approval>
        <approved_scope></approved_scope>
      </cli_candidate>
    </cli_candidates>
  </source_discovery>

  <interaction_review required_for_mode="complete" presentation="review_log">
    <contradiction>
      <signal></signal>
      <why_it_matters></why_it_matters>
      <user_resolution></user_resolution>
    </contradiction>
    <anomaly>
      <signal></signal>
      <hypothesis></hypothesis>
      <user_response></user_response>
    </anomaly>
    <confirmation>
      <target_field></target_field>
      <why_confirm></why_confirm>
      <question_or_simulated_scenario></question_or_simulated_scenario>
      <answer></answer>
    </confirmation>
  </interaction_review>

  <identity_layer presentation="short_text">
    <nickname_plain></nickname_plain>
    <nickname_serious></nickname_serious>
    <one_line_positioning></one_line_positioning>
    <public_mainline></public_mainline>
    <private_mainline></private_mainline>
    <why_nickname_fits></why_nickname_fits>
    <scarcity_judgment scale="ordinary|rare_local|rare_national|rare_global"></scarcity_judgment>
    <evidence></evidence>
  </identity_layer>

  <explicit_analysis presentation="mixed">
    <mbti presentation="dimension_scores">
      <method>known_type|short_test|user_skipped|insufficient_evidence</method>
      <current_judgment></current_judgment>
      <dimension code="E/I" tendency="" score_out_of_100="" confidence=""></dimension>
      <dimension code="S/N" tendency="" score_out_of_100="" confidence=""></dimension>
      <dimension code="T/F" tendency="" score_out_of_100="" confidence=""></dimension>
      <dimension code="J/P" tendency="" score_out_of_100="" confidence=""></dimension>
      <change_trajectory></change_trajectory>
      <evidence></evidence>
    </mbti>

    <big_five presentation="score_table">
      <trait name="openness" score_out_of_5="" confidence=""><evidence></evidence></trait>
      <trait name="conscientiousness" score_out_of_5="" confidence=""><evidence></evidence></trait>
      <trait name="extraversion" score_out_of_5="" confidence=""><evidence></evidence></trait>
      <trait name="agreeableness" score_out_of_5="" confidence=""><evidence></evidence></trait>
      <trait name="emotional_stability" score_out_of_5="" confidence=""><evidence></evidence></trait>
    </big_five>

    <capability_levels presentation="score_table">
      <capability name="" implementation_level="L0-L5" metacognition_level="L0-L5" coverage_percent="" confidence="">
        <evidence></evidence>
      </capability>
    </capability_levels>

    <field_coverage presentation="coverage_map">
      <strength_zone></strength_zone>
      <touched_zone></touched_zone>
      <blank_zone></blank_zone>
    </field_coverage>

    <gap_analysis presentation="score_plus_text">
      <advantage_area name="" completion_percent="">
        <full_version_definition></full_version_definition>
        <must_improve></must_improve>
        <optional_to_ignore></optional_to_ignore>
        <thousand_hour_advice></thousand_hour_advice>
      </advantage_area>
    </gap_analysis>
  </explicit_analysis>

  <radar presentation="radar_chart">
    <dimension name="" reference_person="" score_out_of_100="">
      <definition></definition>
      <evidence></evidence>
    </dimension>
    <overall_shape></overall_shape>
  </radar>

  <barriers presentation="cards">
    <barrier name="">
      <source_experience></source_experience>
      <scarcity></scarcity>
      <evidence></evidence>
      <ai_era_resilience>strengthened|neutral|weakened</ai_era_resilience>
    </barrier>
  </barriers>

  <milestones presentation="timeline">
    <milestone date="">
      <event></event>
      <meaning></meaning>
      <evidence></evidence>
    </milestone>
  </milestones>

  <pitch presentation="three_text_blocks">
    <who_they_are></who_they_are>
    <why_they_are_credible></why_they_are_credible>
    <what_value_they_create></what_value_they_create>
  </pitch>

  <soft_texture presentation="pattern_sentences">
    <pattern_sentence>
      <condition></condition>
      <behavior></behavior>
      <evidence></evidence>
    </pattern_sentence>
  </soft_texture>

  <skill_recommendations presentation="skill_cards">
    <recommended_skill name="" type="scarce_meta_capability|repeated_workflow|role_required_workflow" recommend="yes|no">
      <why_recommended></why_recommended>
      <scarcity_basis></scarcity_basis>
      <repetition_basis></repetition_basis>
      <role_requirement_basis></role_requirement_basis>
      <inputs></inputs>
      <process></process>
      <outputs></outputs>
      <acceptance_criteria></acceptance_criteria>
      <evidence></evidence>
    </recommended_skill>
  </skill_recommendations>

  <presentation_plan presentation="rendering_contract">
    <section name="source_discovery" recommended_form="source_inventory"></section>
    <section name="identity_layer" recommended_form="short_text"></section>
    <section name="mbti" recommended_form="dimension_scores"></section>
    <section name="big_five" recommended_form="x_out_of_5_score_table"></section>
    <section name="capability_levels" recommended_form="L0-L5_score_table"></section>
    <section name="field_coverage" recommended_form="coverage_map"></section>
    <section name="gap_analysis" recommended_form="percent_score_plus_text"></section>
    <section name="radar" recommended_form="radar_chart"></section>
    <section name="barriers" recommended_form="cards"></section>
    <section name="milestones" recommended_form="timeline"></section>
    <section name="pitch" recommended_form="three_text_blocks"></section>
    <section name="soft_texture" recommended_form="pattern_sentence_list"></section>
    <section name="skill_recommendations" recommended_form="skill_cards"></section>
  </presentation_plan>

  <missing_information presentation="doctor_queue">
    <status>has_missing_required_fields|no_missing_required_fields</status>
    <missing field="" status="unknown|insufficient_evidence|user_skipped" required_for_100="true">
      <why_needed></why_needed>
      <next_question></next_question>
    </missing>
  </missing_information>

  <iteration_log presentation="append_only">
    <entry date="">
      <trigger></trigger>
      <changes></changes>
    </entry>
  </iteration_log>
</inneratlas_report>
```

## Required Sections

Doctor must verify these top-level sections:

| Section | Required content | Recommended presentation |
|---|---|---|
| `source_discovery` | startup scan time, scan status, source-discovery policy, CLI candidates, user approval state | source inventory |
| `identity_layer` | nickname, one-line positioning, public/private mainline, scarcity judgment, evidence | short text |
| `interaction_review` | contradictions, anomalies, and confirmations in complete mode | review log |
| `explicit_analysis/mbti` | method, current judgment, E/I, S/N, T/F, J/P, change trajectory, evidence | dimension scores |
| `explicit_analysis/big_five` | five traits with `score_out_of_5`, confidence, evidence | x out of 5 score table |
| `explicit_analysis/capability_levels` | capabilities with implementation L0-L5, metacognition L0-L5, coverage %, evidence | score table |
| `explicit_analysis/field_coverage` | strength, touched, blank zones | coverage map |
| `explicit_analysis/gap_analysis` | full-version definition, completion %, must-improve, optional-to-ignore, 1000-hour advice | percent score plus text |
| `radar` | 5-7 dimensions, reference person, score, evidence, overall shape | radar chart |
| `barriers` | 3-5 barriers with source, scarcity, evidence, AI-era resilience | cards |
| `milestones` | dated events, meaning, evidence | timeline |
| `pitch` | who they are, why credible, what value they create | three text blocks |
| `soft_texture` | 4-7 condition-behavior-evidence pattern sentences | pattern sentence list |
| `skill_recommendations` | scarce meta-capability or repeated/role-required workflow candidates | skill cards |
| `presentation_plan` | recommended rendering form for each section | rendering contract |
| `missing_information` | every unresolved required field and next question | doctor queue |
| `iteration_log` | append-only change history | append-only log |

## Skill Recommendation Rules

`skill_recommendations` is a required output section.

InnerAtlas must recommend candidate personal skills when either condition is met:

1. **Scarce meta-capability**: evidence suggests the person has a rare, high-percentile meta ability. This should combine scarcity, experience, repeated judgment, and evidence. It does not need to be a conventional job skill.
2. **Repeated or role-required workflow**: the person repeatedly faces a workflow because of their role, even if they are not industry-top in it. Examples: sales people need sales workflow skills; founders need fundraising, hiring, customer discovery, and narrative skills; engineering leads need review, architecture, prioritization, incident response.

Every recommended skill must include:

- `type`: `scarce_meta_capability`, `repeated_workflow`, or `role_required_workflow`
- why it is recommended
- scarcity basis, repetition basis, or role requirement basis
- inputs
- process
- outputs
- acceptance criteria
- evidence

If evidence is insufficient, recommend `no` and add the missing field to `missing_information`.

## Modes

At the beginning, InnerAtlas must ask the user to choose:

```text
你想用哪种模式？
A. 快速模式：我基于你已经给的全部原始输入直接推理并出 XML 报告。猜测会写明猜测依据。
B. 完整模式：我先基于输入推理所有方面，再围绕矛盾点、异常点、重点产出点和确认点继续多轮交互，直到 doctor 达到 100%。
```

After mode selection and before ingesting additional material, InnerAtlas must run local source discovery:

```bash
python scripts/inneratlas_source_scan.py --xml-snippet
```

The scan only detects CLI availability from `PATH`. It must not fetch Lark/Feishu content, enumerate GitHub data, search local folders, inspect repositories, or call account-bound APIs. Write the result to `source_discovery`, show the candidate entrances to the user, and ask which sources are approved and what scope is allowed. Without approval, use only material already provided by the user.

### Quick Mode

Quick mode still writes every required XML field and runs doctor. It may fill uncertain fields with clearly marked inference, but every inference must include evidence or reasoning in the relevant `<evidence>` node.

Quick mode can finish only when doctor reaches 100%. If doctor finds missing fields, ask targeted follow-up questions even in quick mode; otherwise the result is only a draft.

### Complete Mode

Complete mode must include `interaction_review`.

The interaction must focus on:

1. **Contradictions**: claims, timelines, self-descriptions, or evidence that conflict.
2. **Anomalies**: unusually dense capability jumps, rare outcomes, suspiciously smooth stories, missing failure evidence, over-strong labels.
3. **Second confirmation of key outputs**: nickname, public/private mainline, MBTI trajectory, key capability levels, scarcity judgment, barriers, future paths, and skill recommendations.
4. **Simulated scenario confirmation**: when direct self-report is weak, ask a situation-based question that tests the inferred pattern.

Complete mode cannot finish until:

- each important contradiction has either a resolution or an explicit unknown;
- each important anomaly has a hypothesis and user response;
- every key output has been confirmed or marked as evidence-insufficient;
- doctor reaches 100%.

## Doctor Loop

Use `scripts/inneratlas_doctor.py`:

```bash
python scripts/inneratlas_doctor.py WENXIN_REPORT.xml
python scripts/inneratlas_doctor.py --root ./inneratlas-output
python scripts/inneratlas_doctor.py --root ./inneratlas-output --version-id 20260606-191248
python scripts/inneratlas_doctor.py WENXIN_REPORT.xml --json
```

Doctor behavior:

1. Resolve target XML from explicit path, `--root current/WENXIN_REPORT.xml`, or `--root versions/WENXIN_REPORT.<version_id>.xml`.
2. Parse XML.
3. Check required sections and required fields.
4. Count filled fields vs required fields.
5. Treat placeholder text, empty tags, `未知`, `证据不足`, `TODO`, and `TBD` as incomplete unless the field is explicitly allowed as a completion exception.
6. Emit `completion_percent`.
7. Emit `missing_fields`.
8. Emit `next_questions`.
9. If completion is below 100, agent must continue asking targeted questions and update XML before claiming completion.

## Versioning Rules

When updating a report:

1. Resolve artifact root.
2. Read `current/WENXIN_REPORT.xml` if it exists.
3. Before modifying current, copy it to `versions/WENXIN_REPORT.<old_version_id>.xml` if that exact version does not already exist.
4. Write the new version to `versions/WENXIN_REPORT.<new_version_id>.xml`.
5. Update `current/WENXIN_REPORT.xml` to the same XML content as the new version.
6. Set root attributes:
   - `artifact_name="WENXIN_REPORT.xml"`
   - `version_id="<new_version_id>"`
7. Set metadata paths:
   - `metadata/artifact_root`
   - `metadata/current_path`
   - `metadata/version_path`
8. Run doctor against the current file.

Version IDs should be timestamp-like and stable, e.g. `YYYYMMDD-HHMMSS`. If a user supplies a semantic version label, normalize it into a filesystem-safe suffix.

## Compatibility

Legacy names remain accepted as compatibility aliases:

- `identity/wenxin/`
- `schema: wenxin-report`
- `WENXIN_REPORT.md`

But new source-of-truth outputs must be written to `WENXIN_REPORT.xml`.
