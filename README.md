# AnthonyHF.Skill

AnthonyHF.Skill is Anthony Fan's personal engineer avatar and work/life operating context.

This repository is not a generic personal-brand package. It is the top-level skill entry for using Anthony Fan's current engineering identity, engineering judgment, and durable work/life memory. The long-lived knowledge base stays in AF-wiki, and reusable engineering methodology stays in Engineering Everything.

## Current Shape

| Layer | Path | Role |
| --- | --- | --- |
| Root skill | `SKILL.md` | Entry point for Anthony Fan's engineer avatar and context-routing rules. |
| Person model | `people/anthony-fan/PSP.md` | Low-confidence PSP scaffold for the current engineer slice only. |
| Work/life memory | `knowledge/af-wiki` | Submodule for AF-wiki, the durable work/life second brain. |
| Engineering method | `skills/engineering-everything` | Submodule for engineering judgment and project execution routing. |

## Explicit Boundary

Wenxin Skill is intentionally not a submodule here.

AnthonyHF.Skill should not mix in personal positioning, personal BP, or writing-style extraction from Wenxin by default. Those workflows can live in their own repository or installed skill. This repository is the work/life and engineer-avatar carrier.

## Usage

Clone with submodules:

```bash
git clone --recurse-submodules https://github.com/HaodiFan/AnthonyHF.Skill.git
```

For an existing checkout:

```bash
git submodule update --init --recursive
```

When an agent uses this skill:

1. Read `SKILL.md`.
2. If the request is about Anthony's current work/life context, route into `knowledge/af-wiki/START-HERE.md`.
3. If the request is about engineering judgment, project execution, architecture, SOP, or AI/agent workflow, use `skills/engineering-everything/SKILL.md`.
4. If the request is about Anthony's personal avatar, read `people/anthony-fan/PSP.md`, but treat it as incomplete unless more raw materials have been added.

