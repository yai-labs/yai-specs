# Command Taxonomy v1 Pointer

Normative sources for command taxonomy:

- `registry/commands.v1.json` (per-command taxonomy fields)
- `registry/commands.surface.v1.json` (surface-only view)
- `registry/commands.topics.v1.json` (entrypoint/topic/op map)
- `registry/schema/commands.v1.schema.json` (field shape and enums)
- `tools/gen/commands_rewrite_taxonomy_v1.py` (idempotent normalizer)
- `tools/validate/validate_registry.py` (taxonomy guardrails)

Taxonomy fields:

- `surface`: `surface | ancillary | plumbing`
- `domain`: `workspace | runtime | governance | policy | bundle | inspection | verification | diagnostics | dev`
- `layer`: `boot | root | kernel | engine | mind | substrate | orch | docs`
- `stability`: `stable | experimental | planned | deprecated`
- `entrypoint`: canonical short UX entrypoint
- `help_order`: stable ordering weight for help rendering
- `command_path_tokens`: canonical hierarchical path tokens
- `canonical_path`: stable joined path string
