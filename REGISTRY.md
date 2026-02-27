# Registry

This registry defines the canonical location of normative artifacts and the rules for allocating IDs.

## ID Registry

The authoritative ID registry lives in `contracts/protocol/include/yai_protocol_ids.h`.

Rules:
- IDs are never reused.
- Reserved ranges must remain reserved and documented in the header.
- New IDs require a corresponding spec change and a `CHANGELOG.md` entry.
- Any change that adds or reclassifies IDs must be reviewed for compatibility impact.

## Normative JSON Contracts

- `registry/commands.v1.json`
- `registry/schema/commands.v1.schema.json`
- `compliance/compliance.context.v1.json`
- `compliance/retention.policy.v1.json`
- `packs/compliance/gdpr-eu/2026Q1/pack.meta.json`
- `packs/compliance/gdpr-eu/2026Q1/retention.defaults.json`
- `packs/compliance/gdpr-eu/2026Q1/taxonomy.data_classes.json`
- `packs/compliance/gdpr-eu/2026Q1/taxonomy.legal_basis.json`
- `packs/compliance/gdpr-eu/2026Q1/taxonomy.purposes.json`
- `contracts/control/schema/control_plane.v1.json`
- `contracts/control/schema/authority.json`
- `runtime/engine/schema/engine_cortex.v1.json`
- `runtime/mind/graph/schema/graph.v1.json`
- `contracts/providers/schema/providers.v1.json`
- `contracts/vault/schema/vault_abi.json`

## Normative C Headers

- `contracts/protocol/include/protocol.h`
- `contracts/protocol/include/transport.h`
- `contracts/protocol/include/yai_protocol_ids.h`
- `contracts/protocol/include/errors.h`
- `contracts/protocol/include/auth.h`
- `contracts/protocol/include/roles.h`
- `contracts/protocol/include/session.h`
- `contracts/protocol/include/audit.h`
- `contracts/protocol/runtime/include/rpc_runtime.h`
- `contracts/vault/include/yai_vault_abi.h`

## Conformance Vectors

Vectors are informative but should be updated when normative behavior changes.

- `vectors/transport_vectors.json`
- `vectors/auth_vectors.json`
- `vectors/audit_vectors.json`
