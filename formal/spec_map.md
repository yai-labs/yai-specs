# Formal Coverage Map

This page describes formal coverage status by area.
It is the human landing page for what is currently modeled vs not yet modeled.

Coverage labels:
- `none`: no explicit formal properties for this area
- `smoke`: area linked to model indirectly via shared kernel properties
- `modeled`: explicit model variables/properties exist for area concerns

| Area | contracts | specs | vectors | formal | Gaps |
|---|---|---|---|---|---|
| Protocol | yes (`law/normative/invariants/I-001-traceability.md`, `I-002`, `I-003`, `I-006`, `I-007`) | yes (`law/surfaces/protocol/include/*`, `law/surfaces/protocol/runtime/include/rpc_runtime.h`) | yes (`vectors/transport_vectors.json`, `vectors/auth_vectors.json`, `vectors/audit_vectors.json`) | modeled (`formal/tla/YAI_KERNEL.tla`, `formal/configs/YAI_KERNEL.quick.cfg`) | Field-level transport properties (`magic/version/payload`) not yet explicit as named TLA properties |
| Vault | yes (`law/normative/boundaries/L0-vault.md`, `law/normative/invariants/I-002-determinism.md`, `I-003`) | yes (`law/surfaces/vault/include/yai_vault_abi.h`, `law/surfaces/vault/schema/vault_abi.json`) | partial (`vectors/audit_vectors.json`) | smoke (`VaultAbiVersionOk` in `formal/tla/YAI_KERNEL.tla`) | No dedicated vault module |
| Graph | yes (`law/normative/invariants/I-002-determinism.md`, `I-003`, `I-005`) | yes (`law/surfaces/graph/schema/graph.v1.json`, `law/surfaces/graph/notes/GRAPH_V1.md`) | partial (`vectors/audit_vectors.json`) | none | Graph transitions are not yet modeled |
| Control | yes (`law/normative/axioms/A-002-authority.md`, `law/normative/invariants/I-003`, `I-006`, `I-007`) | yes (`law/surfaces/control/schema/control_plane.v1.json`, `law/surfaces/control/schema/authority.json`) | yes (`vectors/audit_vectors.json`, `vectors/auth_vectors.json`) | modeled (`ExternalEffectGuard`, `[](external_effect => compliance_context_valid)` in `formal/tla/YAI_KERNEL.tla`) | Need command taxonomy-specific formalization |
| Compliance | yes (`law/normative/extensions/compliance/C-001-compliance-context.md`, `C-003`) | yes (`law/packs/schema/compliance.context.v1.json`, `law/packs/schema/retention.policy.v1.json`) | partial (`vectors/audit_vectors.json`) | smoke | Retention temporal guarantees not yet modeled |
| CLI | yes (`law/normative/invariants/I-001-traceability.md`, `I-002`, `I-003`) | yes (`law/abi/registry/commands.v1.json`, `law/abi/schema/commands.v1.schema.json`) | partial (`vectors/transport_vectors.json`) | none | No direct CLI formal model |
