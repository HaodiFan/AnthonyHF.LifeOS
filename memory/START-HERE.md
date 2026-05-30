# Memory Start Here

This file routes agents to AnthonyHF's approved long-term context surfaces and configured memory wiki.

## Areas

- `memory-wiki`: `object_type=area-index`, `visibility=private`, `authority=memory/wiki-repo.yml`, `configured_instance=AF-wiki`, `public_mirror=index-only`, `collaboration_mode=private-pr-or-owner-approved-extract`, `lifecycle_state=linked`.
- `work-context`: `object_type=area-index`, `visibility=private`, `authority=configured memory wiki or memory/long-term approved summaries`, `public_mirror=approved-derived`, `collaboration_mode=owner-approved-extract`, `lifecycle_state=linked`.
- `knowledge-context`: `object_type=area-index`, `visibility=private`, `authority=configured memory wiki, memory/distilled-knowledge summaries, and source manifests`, `public_mirror=index-only`, `collaboration_mode=owner-approved-extract`, `lifecycle_state=linked`.
- `psp-evidence`: `object_type=source-artifact`, `visibility=public`, `authority=identity/psp/anthony-fan/PSP.md`, `public_mirror=approved-derived`, `collaboration_mode=owner-reviewed-update`, `lifecycle_state=linked`.
- `skill-candidates`: `object_type=skill-upgrade-candidate`, `visibility=public`, `authority=identity/wenxin and IPO Reverse outputs`, `public_mirror=approved-derived`, `collaboration_mode=owner-reviewed-update`, `lifecycle_state=triaged`.

## Access Rules

- AF-wiki is AnthonyHF's configured memory wiki. Do not treat it as the openLifeOS default for other LifeOS repos.
- Public memory is a derived surface; private or local-only bodies can only move upward as approved facts, redacted summaries, or abstracted non-reversible conclusions.
- If an area is private, state the access boundary and ask the owner for approved extracts.
- Read `memory/wiki-repo.yml` before assuming which memory wiki is configured.
- If the configured memory wiki is unavailable, use only this repo's approved summaries or user-provided evidence.
- Prefer latest memory source over older PSP facts for time-sensitive work context.
- Treat unprocessed thought intake as provisional, not stable fact.
- Raw private memory bodies stay outside the public surface unless the owner explicitly provides an approved extract.
