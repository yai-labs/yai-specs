# YAI Law Documentation (Informative Layer)

`docs/` is the informative documentation layer for `yai-law`.
It is designed for enterprise-grade navigation, interpretation, and onboarding of law consumers.

`docs/` does not originate or redefine normative authority.

## Purpose

Artifacts in this directory exist to:
- explain how to consume law safely and consistently
- provide navigation pointers to canonical indexes
- support generated documentation and policy interpretation
- improve traceable onboarding across contracts, runtime constraints, compliance, and formal assets

## Interpretation rule

If a document in `docs/` conflicts with canonical artifacts outside `docs/`, canonical artifacts prevail.

## Canonical indexes (root)

- `../SPEC_MAP.md`
- `../REGISTRY.md`
- `../VERSIONING.md`
- `../COMPATIBILITY.md`
- `../CHANGELOG.md`

## Primary documents in this directory

- `C_MAINPAGE.md` - doxygen/documentation entry page
- `pointers/SPEC_MAP.pointer.md` - pointer to canonical structure map
- `policy/README.md` - documentation policy and governance rules

## Normative source domains (outside `docs/`)

- `../authority/`
- `../foundation/`
- `../runtime/`
- `../contracts/`
- `../registry/`
- `../schema/`
- `../formal/`
- `../packs/`
- `../vectors/`

## Platform alignment note

Consumers in `yai-sdk`, `yai-cli`, `yai`, and `yai-ops` should reference this directory as informative support only.
Normative references must always target canonical law domains.
