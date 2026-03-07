# Post-Refactor Authoring Rules

## Primary terms (use by default)

- `core`
- `exec`
- `brain`
- `protocol`
- `platform`
- `support`

## Historical terms (restricted use)

`boot`, `root`, `kernel`, `engine`, `mind` may be used only when explicitly marked as:
- historical alias
- migration reference
- retained artifact identity

## Placement rules

- Constitutional truth -> `foundation/`
- Runtime interpretation binding -> `runtime/`
- Public contract surface -> `contracts/`
- Machine-readable allocation -> `registry/`
- Transversal payload structure -> `schema/`
- Formal continuity/traceability -> `formal/`
- Informative navigation -> `docs/`

## Drift prevention rules

- Do not infer ontology from historical filenames.
- Do not define authority semantics outside `foundation` + `contracts/control`.
- Do not treat `docs/` as normative override.
- Update mapping matrices when introducing/retaining aliases.

## Validation discipline

Before merge, run at minimum:
- `make check`
- `tools/validate/lint_normative_refs.sh`
- `tools/validate/check_links.sh`
- `tools/validate/validate_registry.py`
- `tools/formal/validate_traceability.py` (with `jsonschema` installed)
