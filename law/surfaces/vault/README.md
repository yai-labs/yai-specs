# Vault

## What It Is

Normative vault ABI contracts and headers.

## Normative Artifacts

- `vault_abi.json`
- `yai_vault_abi.h`

## Versioning Rules

- ABI changes are compatibility-critical.
- Any breaking change requires a repo `MAJOR` bump.
- Additive fields require `MINOR` bump and `CHANGELOG.md` entry.

## Consumers

- `yai-core`
- `yai-cli`
- `yai-yx`

## Change Procedure

- Update the ABI contracts.
- Update `REGISTRY.md`, `SPEC_MAP.md`, and `CHANGELOG.md`.
- Update vectors/tests if behavior changes.
