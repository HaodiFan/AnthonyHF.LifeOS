# Artifacts Registry

This directory records the current active openLifeOS process artifacts.

`current.yml` is the machine-readable latest registry. It points agents to the current Wenxin, PSP, Soul, design, skill recommendations, and evidence maturity entrypoints without making runtime projections the source of truth.

Update rule:

1. Write a timestamped artifact first.
2. Update the human-readable current entrypoint.
3. Update the artifact's `versions.yml` and `changelog.md`.
4. Update `identity/current.yml` when the artifact is identity-related.
5. Update `artifacts/current.yml`.

Raw private materials never belong in this registry.
