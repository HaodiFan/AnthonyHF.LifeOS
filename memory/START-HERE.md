# Memory Start Here

This file routes agents to AnthonyHF's long-term context sources.

## Areas

- `af-wiki`: `object_type=area-index`, `visibility=private`, `authority=memory/af-wiki submodule`, `public_mirror=index-only`, `collaboration_mode=private-pr-or-owner-approved-extract`, `lifecycle_state=linked`.
- `work-context`: `object_type=area-index`, `visibility=private`, `authority=AF-wiki areas/work`, `public_mirror=approved-derived`, `collaboration_mode=owner-approved-extract`, `lifecycle_state=linked`.
- `knowledge-context`: `object_type=area-index`, `visibility=private`, `authority=AF-wiki areas/knowledge and source manifests`, `public_mirror=index-only`, `collaboration_mode=owner-approved-extract`, `lifecycle_state=linked`.
- `psp-evidence`: `object_type=source-artifact`, `visibility=public`, `authority=identity/psp/anthony-fan/PSP.md`, `public_mirror=approved-derived`, `collaboration_mode=owner-reviewed-update`, `lifecycle_state=linked`.
- `skill-candidates`: `object_type=skill-upgrade-candidate`, `visibility=public`, `authority=identity/wenxin and IPO Reverse outputs`, `public_mirror=approved-derived`, `collaboration_mode=owner-reviewed-update`, `lifecycle_state=triaged`.

## Access Rules

- Do not copy private wiki content into this repo.
- Public memory is a derived surface; private or local-only bodies can only move upward as approved facts, redacted summaries, or abstracted non-reversible conclusions.
- If an area is private, state the access boundary and ask the owner for approved extracts.
- Read `memory/wiki-repo.yml` before assuming whether GitHub or server wiki is authoritative.
- If server wiki is authoritative, treat GitHub as a mirror/collaboration surface and prefer server state for facts.
- Prefer latest memory source over older PSP facts for time-sensitive work context.
- Treat unprocessed thought intake as provisional, not stable fact.
- Existing private memory authority is `memory/af-wiki`; this public surface only stores routing, approved summaries, and provenance.
