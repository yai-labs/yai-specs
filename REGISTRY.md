# REGISTRY

`REGISTRY.md` describes canonical machine-readable registries and their use.

## What registry is

Registry is the normative substrate for stable identifiers and structured law surfaces.
It is not a mirror of historical runtime packaging.

## Canonical registry artifacts

- `registry/primitives.v1.json`
- `registry/commands.v1.json`
- `registry/commands.surface.v1.json`
- `registry/commands.topics.v1.json`
- `registry/artifacts.v1.json`

Schemas:
- `registry/schema/primitives.v1.schema.json`
- `registry/schema/commands.v1.schema.json`
- `registry/schema/artifacts.v1.schema.json`

## How to read registry

- `primitives`: capability primitives and governance hooks
- `commands`: canonical command IDs and metadata
- `commands.surface`: exposure-oriented command view
- `commands.topics`: entrypoint/topic/op index
- `artifacts`: canonical artifact roles and schema links

## Registry relation to other surfaces

- `contracts/` defines public contract surfaces.
- `schema/` defines transversal payload schemas.
- `formal/traceability.v1.json` links invariants to artifacts.
- `foundation/` defines normative primacy.

Registry entries must be interpreted in current ontology (`core/exec/brain` + cross-cutting layers), even when compatibility aliases remain in metadata.

## Compatibility rule

Registry IDs are stability surfaces.
Semantic realignment is preferred over unnecessary ID churn.
