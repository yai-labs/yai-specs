# Formal Coverage Map

This page describes formal coverage status by area.
It is the human landing page for what is currently modeled vs not yet modeled.

Coverage labels:
- `none`: no explicit formal properties for this area
- `smoke`: area linked to model indirectly via shared kernel properties
- `modeled`: explicit model variables/properties exist for area concerns

| Area | contracts | specs | vectors | formal | Gaps |
|---|---|---|---|---|---|
| Protocol | yes (`foundation/invariants/I-001-traceability.md`, `I-002`, `I-003`, `I-006`, `I-007`) | yes (`contracts/protocol/include/*`, `contracts/protocol/runtime/include/rpc_runtime.h`) | yes (`vectors/transport_vectors.json`, `vectors/auth_vectors.json`, `vectors/audit_vectors.json`) | modeled (`formal/tla/YAI_KERNEL.tla`, `formal/configs/YAI_KERNEL.quick.cfg`) | Field-level transport properties (`magic/version/payload`) not yet explicit as named TLA properties |
| Vault | yes (`foundation/boundaries/L0-vault.md`, `foundation/invariants/I-002-determinism.md`, `I-003`) | yes (`contracts/vault/include/yai_vault_abi.h`, `contracts/vault/schema/vault_abi.json`) | partial (`vectors/audit_vectors.json`) | smoke (`VaultAbiVersionOk` in `formal/tla/YAI_KERNEL.tla`) | No dedicated vault module |
| Graph | yes (`foundation/invariants/I-002-determinism.md`, `I-003`, `I-005`) | yes (`runtime/mind/graph/schema/graph.v1.json`, `runtime/mind/graph/notes/GRAPH_V1.md`) | partial (`vectors/audit_vectors.json`) | none | Graph transitions are not yet modeled |
| Control | yes (`foundation/axioms/A-002-authority.md`, `foundation/invariants/I-003`, `I-006`, `I-007`) | yes (`contracts/control/schema/control_plane.v1.json`, `contracts/control/schema/authority.json`) | yes (`vectors/audit_vectors.json`, `vectors/auth_vectors.json`) | modeled (`ExternalEffectGuard`, `[](external_effect => compliance_context_valid)` in `formal/tla/YAI_KERNEL.tla`) | Need command taxonomy-specific formalization |
| Compliance | yes (`foundation/extensions/compliance/C-001-compliance-context.md`, `C-003`) | yes (`schema/compliance.context.v1.json`, `schema/retention.policy.v1.json`) | partial (`vectors/audit_vectors.json`) | smoke | Retention temporal guarantees not yet modeled |
| CLI | yes (`foundation/invariants/I-001-traceability.md`, `I-002`, `I-003`) | yes (`registry/commands.v1.json`, `registry/schema/commands.v1.schema.json`) | partial (`vectors/transport_vectors.json`) | none | No direct CLI formal model |
