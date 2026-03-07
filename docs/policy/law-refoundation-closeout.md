# Law Refoundation Closeout

## Completed

- Blueprint and placement rules established.
- Foundation rewritten (axioms/invariants/boundaries/terminology).
- Runtime and contracts semantically realigned.
- Formal/registry/schema realigned with continuity policy.
- Top-level identity/navigation surfaces rewritten.
- Legacy runtime docs `runtime/boot` and `runtime/root` removed.

## Authoritative ontology

Primary ontology is:
- `core`
- `exec`
- `brain`
- `protocol/platform/support` as cross-cutting layers

Historical labels remain only where explicitly declared as aliases.

## Residual legacy status

Residual legacy elements are limited to:
- historical path/file names retained for continuity (`runtime/kernel|engine|mind`, `YAI_KERNEL.*`, boundary filenames)
- compatibility metadata in generated command registries

All are tracked in `law-legacy-decommission-matrix.md`.

## Validate/hardening status

- `make check` is green.
- `make ci` requires `jsonschema` in local environment for formal coverage validation.
- validation scripts reviewed for ontology drift expectations.

## What remains out of scope

- ADR/runbook/program-document rewrite across other repositories.
- final large-scale renaming of historical artifact file paths.
- complete generated metadata cleanup in registry command layers.

## Operational rule going forward

New normative content must use primary ontology terms.
Historical terms require explicit alias/deprecation context.
