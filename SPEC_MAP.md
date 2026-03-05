# SPEC_MAP

Canonical map of the normative artifacts in `yai-law`.

This file is the authoritative navigation index for the public law surface of YAI. It groups canonical artifacts by authority area so consumers can identify the correct source for contracts, schemas, registries, runtime constraints, compliance overlays, and conformance vectors.

## 0) Consumption context

Cross-repo authority/consumption chain:

`yai-law` -> `yai-sdk` -> `yai-cli` -> `yai` -> `yai-ops`

Use this map to locate normative sources before changing implementation behavior, SDK/CLI behavior, or operational claims.

## 1) Foundation

Foundational law artifacts:

- `foundation/axioms/`
- `foundation/invariants/`
- `foundation/boundaries/`
- `foundation/terminology/`
- `foundation/extensions/`
- `foundation/extensions/compliance/`

## 2) Runtime layers

Canonical runtime-layer surfaces:

- `runtime/boot/`
- `runtime/root/`
- `runtime/kernel/`
- `runtime/engine/`
- `runtime/mind/`

Layer-specific canonical schemas:

- `runtime/engine/schema/engine_cortex.v1.json`
- `runtime/mind/graph/schema/graph.v1.json`

## 3) Protocol

Normative protocol and transport surfaces:

- `contracts/protocol/include/protocol.h`
- `contracts/protocol/include/transport.h`
- `contracts/protocol/include/yai_protocol_ids.h`
- `contracts/protocol/include/errors.h`
- `contracts/protocol/include/auth.h`
- `contracts/protocol/include/roles.h`
- `contracts/protocol/include/session.h`
- `contracts/protocol/include/audit.h`
- `contracts/protocol/runtime/include/rpc_runtime.h`

## 4) Control

Canonical control-plane schemas:

- `contracts/control/schema/control_plane.v1.json`
- `contracts/control/schema/control_call.v1.json`
- `contracts/control/schema/exec_reply.v1.json`
- `contracts/control/schema/authority.v1.json`
- `contracts/control/schema/authority.json`

Execution path rule:

- `exec_reply.v1.json` is the mandatory single envelope for command execution replies.

## 5) Vault

Canonical vault surfaces:

- `contracts/vault/schema/vault_abi.json`
- `contracts/vault/include/yai_vault_abi.h`

## 6) Providers

Canonical provider-facing schema surfaces:

- `contracts/providers/schema/providers.v1.json`

## 7) CLI and registries

Canonical machine-readable registries:

- `registry/primitives.v1.json`
- `registry/commands.v1.json`
- `registry/artifacts.v1.json`

Associated registry schemas:

- `registry/schema/primitives.v1.schema.json`
- `registry/schema/commands.v1.schema.json`
- `registry/schema/artifacts.v1.schema.json`

## 8) Transversal schemas

Canonical transversal artifact and policy schemas:

- `schema/bundle_manifest.v1.schema.json`
- `schema/containment_metrics.v1.schema.json`
- `schema/decision_record.v1.schema.json`
- `schema/evidence_index.v1.schema.json`
- `schema/policy.v1.schema.json`
- `schema/verification_report.v1.schema.json`
- `schema/compliance.context.v1.json`
- `schema/retention.policy.v1.json`

## 9) Compliance packs

Published compliance overlays:

- `packs/compliance/gdpr-eu/2026Q1/pack.meta.json`
- `packs/compliance/gdpr-eu/2026Q1/retention.defaults.json`
- `packs/compliance/gdpr-eu/2026Q1/taxonomy.data_classes.json`
- `packs/compliance/gdpr-eu/2026Q1/taxonomy.legal_basis.json`
- `packs/compliance/gdpr-eu/2026Q1/taxonomy.purposes.json`

## 10) Formal artifacts

Formal traceability and model artifacts:

- `formal/traceability.v1.json`
- `formal/schema/traceability.v1.schema.json`
- `formal/spec_map.md`
- `formal/tla/LAW_IDS.tla`
- `formal/tla/YAI_KERNEL.tla`
- `formal/configs/YAI_KERNEL.cfg`
- `formal/configs/YAI_KERNEL.quick.cfg`
- `formal/configs/YAI_KERNEL.deep.cfg`

## 11) Conformance vectors

Validation vectors are informative, but they are part of conformance discipline and should be updated whenever normative behavior changes.

- `vectors/transport_vectors.json`
- `vectors/auth_vectors.json`
- `vectors/audit_vectors.json`

## 12) Registry scale target

Command registry is maintained at 14 groups x 200 command_id (2800 total) through generator-driven expansion (`tools/gen/commands_expand_v1.py`).
This scale profile is intended to stress CLI/SDK/runtime contract paths while preserving deterministic semantics.
