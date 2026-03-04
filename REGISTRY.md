# YAI Law Registry

This registry defines the canonical locations of machine-readable law artifacts and the rules for allocating and evolving identifiers across the YAI law surface.

It is the reference index for canonical registries, schemas, headers, and published packs consumed by downstream implementations and validation tooling.

## 1) ID registry

The authoritative protocol and surface ID registry lives in:

- `contracts/protocol/include/yai_protocol_ids.h`

Rules:

- IDs are never reused
- Reserved ranges remain reserved until explicitly reclassified
- New IDs require a corresponding contract change and a `CHANGELOG.md` entry
- Any addition, removal, or reclassification of IDs must be reviewed for compatibility impact

## 2) Canonical registries

These files define the machine-readable registries consumed by tooling and implementations.

- `registry/primitives.v1.json`
- `registry/commands.v1.json`
- `registry/artifacts.v1.json`

Associated registry schemas:

- `registry/schema/primitives.v1.schema.json`
- `registry/schema/commands.v1.schema.json`
- `registry/schema/artifacts.v1.schema.json`

## 3) Canonical transversal schemas

These schemas define repository-wide artifact and policy payloads.

- `schema/bundle_manifest.v1.schema.json`
- `schema/containment_metrics.v1.schema.json`
- `schema/decision_record.v1.schema.json`
- `schema/evidence_index.v1.schema.json`
- `schema/policy.v1.schema.json`
- `schema/verification_report.v1.schema.json`
- `schema/compliance.context.v1.json`
- `schema/retention.policy.v1.json`

## 4) Canonical contract schemas

These schemas define public interface surfaces.

- `contracts/control/schema/control_plane.v1.json`
- `contracts/control/schema/control_call.v1.json`
- `contracts/control/schema/authority.json`
- `contracts/providers/schema/providers.v1.json`
- `contracts/vault/schema/vault_abi.json`
- `runtime/engine/schema/engine_cortex.v1.json`
- `runtime/mind/graph/schema/graph.v1.json`

## 5) Canonical headers

These headers define normative C-facing law surfaces.

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

## 6) Published normative packs

These published overlays remain part of the canonical law surface when referenced by compatibility and compliance workflows.

- `packs/compliance/gdpr-eu/2026Q1/pack.meta.json`
- `packs/compliance/gdpr-eu/2026Q1/retention.defaults.json`
- `packs/compliance/gdpr-eu/2026Q1/taxonomy.data_classes.json`
- `packs/compliance/gdpr-eu/2026Q1/taxonomy.legal_basis.json`
- `packs/compliance/gdpr-eu/2026Q1/taxonomy.purposes.json`

## 7) Conformance vectors

Vectors are informative validation artifacts. They do not override normative contracts, but they should be updated whenever normative behavior changes in a way that affects validation expectations.

- `vectors/transport_vectors.json`
- `vectors/auth_vectors.json`
- `vectors/audit_vectors.json`
## Registry scale

Current command registry target is **200 command_id per group** across 14 groups (total 2800 IDs).
This profile is a **registry-scale stress and coverage surface**, not a final product taxonomy.
Expansion is generated via `tools/gen/commands_expand_v1.py` and validated via `make validate-law-registry`.
