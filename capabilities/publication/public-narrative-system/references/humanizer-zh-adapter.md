# Humanizer-zh Adapter For Anthony Public Narrative

This reference adapts useful checks from `op7418/Humanizer-zh` into AnthonyHF's public narrative workflow.

Source:

- Repo: `https://github.com/op7418/Humanizer-zh`
- Checked commit: `91f3d39`
- License: MIT

This is not a generic "make it casual" layer. It is a cleanup pass for AI writing traces while preserving Anthony's judgment density.

## When To Use

Use after PSP voice adaptation when:

- a draft sounds like generic AI writing;
- the user says the wording feels unlike Anthony;
- the draft has formulaic contrast, list-like variable exposition, promotional texture, or over-clean structure;
- the draft is intended for RedNote, WeChat, product pages, decks, or public narrative assets.

## Operating Principle

Anthony's public writing should not become smoother at the cost of being less precise.

Target:

```text
direct judgment
-> concrete mechanism
-> real attribution
-> system motion
-> explicit experimental boundary
```

Avoid:

```text
setup filler
-> generic contrast
-> three-part padding
-> vague authority
-> inspirational closing
```

## Anthony-Specific Humanizer Checks

### 1. Delete Setup Filler

Remove conversational filler inherited from chatbot answers:

- `今天想和大家聊聊`
- `最近有人问我一个问题`
- `我越来越觉得`
- `值得注意的是`
- `总的来说`
- `希望这对你有帮助`

Open with the question, judgment, or concrete scene.

### 2. Keep Attribution Honest

External ideas must remain external.

Correct structure:

```text
我当时听到一个观点...
我现在往前推一层...
我的判断是...
```

Wrong structure:

```text
我当时理解为...
行业专家认为...
很多人都说...
```

unless the source is explicit and public-safe.

### 3. Avoid Formulaic Contrast

Do not use `不是 X，而是 Y` as the default explanatory rhythm.

Also treat these as revision triggers, especially in openings and core claim paragraphs:

- consecutive defensive exclusions: `不是...也不是...`;
- soft defensive phrasing: `这不是...` / `也不是...` / `并不是...`;
- contrast bridges: `不是让...` / `不只是...而是...`;
- concept definition by negation: `数字生命不是...` / `数字分身不是...`.

These patterns can appear in notes or risk scans, but publish-facing口播 should usually convert them into positive definitions, target functions, or system-state claims.

Prefer:

- `核心是...`
- `真正看...`
- `目标函数是...`
- `这个变化来自...`
- `我的判断是...`
- `这个测试的对象是...`
- `我关心的变量是...`
- `数字生命在这里指...`
- `第一阶段先看...`

### 4. Convert Variable Lists Into State Change

If a draft lists terms like `memory / reflection / alignment / skill`, rewrite toward system motion:

```text
上一轮工作有没有改变下一轮工作的起点。
一次正确产出之后，下次同类产出的时间成本是否下降。
人工介入有没有减少。
判断是否更稳定。
```

### 5. Remove Promotional Texture

Watch for broad, shiny language:

- `革命`
- `颠覆`
- `无缝`
- `强大`
- `充满活力`
- `至关重要`
- `关键作用`
- `不断演变的格局`
- `开创性`
- `赋能`

Replace with observed behavior, mechanism, or constraint.

### 6. Break Mechanical Threes

Three-item phrasing is allowed when the three items are real. If it sounds like rhythm padding, compress or expand with actual structure.

### 7. Trust Dense Lines

Anthony can leave a sentence dense if the next line explains the mechanism.

Do not over-explain every metaphor or technical term immediately.

### 8. Preserve Friction

Humanized Anthony writing may still be compact and technical.

Keep:

- English technical terms when accurate;
- first-person judgment;
- unresolved experimental boundaries;
- direct corrections.

Remove:

- generic friendliness;
- explanatory over-service;
- polished marketing closure.

## Final Five-Point Check

Score 1-10:

- Directness: judgment appears early.
- Specificity: mechanisms replace slogans.
- Attribution: external ideas are separate from Anthony's own judgment.
- Rhythm: no formulaic contrast or mechanical variable list.
- Voice fidelity: sounds like Anthony, not a generic content creator.

Any score below 7 requires revision.
