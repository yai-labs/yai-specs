# Registry

This registry defines the canonical location of normative artifacts and the rules for allocating IDs.

## ID Registry

The authoritative ID registry lives in `law/surfaces/protocol/include/yai_protocol_ids.h`.

Rules:
- IDs are never reused.
- Reserved ranges must remain reserved and documented in the header.
- New IDs require a corresponding spec change and a `CHANGELOG.md` entry.
- Any change that adds or reclassifies IDs must be reviewed for compatibility impact.

## Normative JSON Contracts

- `law/abi/registry/commands.v1.json`
- `law/abi/schema/commands.v1.schema.json`
- `compliance/compliance.context.v1.json`
- `compliance/retention.policy.v1.json`
- `law/packs/compliance/gdpr-eu/2026Q1/pack.meta.json`
- `law/packs/compliance/gdpr-eu/2026Q1/retention.defaults.json`
- `law/packs/compliance/gdpr-eu/2026Q1/taxonomy.data_classes.json`
- `law/packs/compliance/gdpr-eu/2026Q1/taxonomy.legal_basis.json`
- `law/packs/compliance/gdpr-eu/2026Q1/taxonomy.purposes.json`
- `law/surfaces/control/schema/control_plane.v1.json`
- `law/surfaces/control/schema/authority.json`
- `law/surfaces/engine/schema/engine_cortex.v1.json`
- `law/surfaces/graph/schema/graph.v1.json`
- `law/surfaces/providers/schema/providers.v1.json`
- `law/surfaces/vault/schema/vault_abi.json`

## Normative C Headers

- `law/surfaces/protocol/include/protocol.h`
- `law/surfaces/protocol/include/transport.h`
- `law/surfaces/protocol/include/yai_protocol_ids.h`
- `law/surfaces/protocol/include/errors.h`
- `law/surfaces/protocol/include/auth.h`
- `law/surfaces/protocol/include/roles.h`
- `law/surfaces/protocol/include/session.h`
- `law/surfaces/protocol/include/audit.h`
- `law/surfaces/protocol/runtime/include/rpc_runtime.h`
- `law/surfaces/vault/include/yai_vault_abi.h`

## Conformance Vectors

Vectors are informative but should be updated when normative behavior changes.

- `vectors/transport_vectors.json`
- `vectors/auth_vectors.json`
- `vectors/audit_vectors.json`
