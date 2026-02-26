# Protocol

## What It Is

Normative wire, envelope, and ID contracts shared across all consumers.
The `*.h` files are the canonical interface definitions.
`runtime/` contains protocol extensions used by runtime-bound transports.

## Normative Artifacts

- `protocol.h`
- `transport.h`
- `yai_protocol_ids.h`
- `errors.h`
- `auth.h`
- `roles.h`
- `session.h`
- `audit.h`
- `runtime/rpc_runtime.h`

## Versioning Rules

- Header constants and IDs are compatibility-critical.
- Any breaking change requires a repo `MAJOR` bump.
- New IDs require registry updates and a `CHANGELOG.md` entry.

## Consumers

- `yai-core`
- `yai-cli`
- `yai-yx`

## Change Procedure

- Update headers and ID registry.
- Update `REGISTRY.md`, `SPEC_MAP.md`, and `CHANGELOG.md`.
- Update vectors/tests if behavior changes.
