# registry/

`registry/` contains canonical machine-readable registries.

## Ontology policy

Registry metadata must reflect primary ontology:
- `core`
- `exec`
- `brain`
- `protocol/platform/support` as cross-cutting layers

Historical labels may remain only as compatibility metadata or migration aliases.
They must not be interpreted as primary runtime ontology.

## Scope

- `primitives.v1.json`
- `commands.v1.json`
- `commands.surface.v1.json`
- `commands.topics.v1.json`
- `artifacts.v1.json`
- `schema/*.v1.schema.json`

## Compatibility

Command IDs and existing schema lines are kept stable unless explicit breaking migration is approved.
Semantic interpretation can be realigned without renaming stable public IDs.
