# Repo Identity Rewrite

## Scope

This rewrite updates identity/navigation surfaces to the current normative model.

Updated identity surfaces:
- `README.md`
- `FOUNDATION.md`
- `SPEC_MAP.md`
- `REGISTRY.md`
- `docs/README.md`
- `docs/pointers/*` (primary pointer set)

## Model shift

Primary ontology is now explicit:
- `core`
- `exec`
- `brain`
- `protocol/platform/support` (cross-cutting)

Historical labels (`boot/root/kernel/engine/mind`) are documented only as migration aliases or artifact-history labels.

## Usage guidance

- Use `README.md` for top-level role and ontology.
- Use `FOUNDATION.md` for foundational model entry.
- Use `SPEC_MAP.md` for normative navigation.
- Use `REGISTRY.md` for registry substrate interpretation.
- Use pointers for fast cross-surface orientation, not as normative source replacement.

## Deferred to hardening/closeout

- deeper cleanup of residual alias metadata in large generated registries
- final deprecation scheduling for historical artifact names
