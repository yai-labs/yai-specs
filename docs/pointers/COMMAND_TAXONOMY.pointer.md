# Command Taxonomy Pointer

Canonical sources:
- `registry/commands.v1.json`
- `registry/commands.surface.v1.json`
- `registry/commands.topics.v1.json`
- `registry/schema/commands.v1.schema.json`

Validation hooks:
- `tools/validate/validate_registry.py`

## Taxonomy note

Command taxonomy is a compatibility surface.
It may retain historical labels in metadata during migration.
Primary ontology for semantic interpretation remains:
- `core`
- `exec`
- `brain`
- `protocol/platform/support` as cross-cutting layers

Do not infer primary runtime architecture from legacy taxonomy tokens alone.
