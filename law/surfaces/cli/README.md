# CLI

## What It Is

Normative command and schema contracts for the YAI CLI surface.

## Normative Artifacts

- `commands.v1.json`
- `commands.schema.json`

## Versioning Rules

- File names encode the major version (`v1`).
- Any breaking change requires a new major file and a repo `MAJOR` bump.
- Additive changes require `MINOR` bump and `CHANGELOG.md` entry.

## Consumers

- `yai-core`
- `yai-cli`
- `yai-yx`

## Change Procedure

- Update the JSON contracts.
- Update `REGISTRY.md`, `SPEC_MAP.md`, and `CHANGELOG.md`.
- Update vectors/tests if behavior changes.
