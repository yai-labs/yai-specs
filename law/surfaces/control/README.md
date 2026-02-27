# Control

## What It Is

Normative control-plane schemas and authority model for YAI control surfaces.

## Normative Artifacts

- `control_plane.v1.json`
- `authority.json`

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
