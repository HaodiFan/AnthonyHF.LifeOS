# AnthonyHF.Skill

AnthonyHF.Skill is Anthony Fan's personal avatar skill matrix.

It is designed as the top-level index for reusable skills that encode Anthony Fan's working style, judgment patterns, and domain playbooks. Each skill can evolve independently, while this repository keeps the personal skill system discoverable and composable.

## Skill Matrix

| Skill | Path | Role |
| --- | --- | --- |
| Wenxin Skill | `skills/wenxin-skill` | Personal writing, thinking, and expression layer. |
| Engineering Everything | `skills/engineering-everything` | Engineering judgment router for software, organizations, SOPs, projects, and AI/agent workflows. |

## Repository Shape

- `matrix.yml` is the machine-readable skill index.
- `skills/` contains git submodules for independently maintained skills.
- Each submodule remains the source of truth for its own `SKILL.md`, references, scripts, and release flow.

## Clone

```bash
git clone --recurse-submodules git@github.com:HaodiFan/AnthonyHF.Skill.git
```

For an existing checkout:

```bash
git submodule update --init --recursive
```

