# SPEC_MAP

Canonical map of normative surfaces in `yai-law`.

## 1) Foundation truth

- `foundation/axioms/`
- `foundation/invariants/`
- `foundation/boundaries/`
- `foundation/terminology/`
- `foundation/extensions/`

## 2) Runtime interpretation bindings

Runtime bindings are interpreted with primary ontology `core/exec/brain`:
- `runtime/kernel/` (historical alias path for sovereign/core binding)
- `runtime/engine/` (historical alias path for exec binding)
- `runtime/mind/` (historical alias path for brain binding)

Canonical runtime schemas currently in-scope:
- `runtime/engine/schema/engine_cortex.v1.json`
- `runtime/mind/graph/schema/graph.v1.json`

## 3) Contract surfaces

- Control: `contracts/control/schema/*.json`
- Protocol: `contracts/protocol/include/*`, `contracts/protocol/runtime/include/rpc_runtime.h`
- Providers: `contracts/providers/schema/providers.v1.json`
- Vault: `contracts/vault/schema/vault_abi.json`, `contracts/vault/include/yai_vault_abi.h`
- CLI bindings/notes: `contracts/cli/*`

## 4) Registry substrate

- `registry/primitives.v1.json`
- `registry/commands.v1.json`
- `registry/commands.surface.v1.json`
- `registry/commands.topics.v1.json`
- `registry/artifacts.v1.json`
- `registry/schema/*.v1.schema.json`

## 5) Transversal schemas

- `schema/bundle_manifest.v1.schema.json`
- `schema/containment_metrics.v1.schema.json`
- `schema/decision_record.v1.schema.json`
- `schema/evidence_index.v1.schema.json`
- `schema/policy.v1.schema.json`
- `schema/verification_report.v1.schema.json`
- `schema/compliance.context.v1.json`
- `schema/retention.policy.v1.json`

## 6) Formal continuity

- `formal/traceability.v1.json`
- `formal/schema/traceability.v1.schema.json`
- `formal/tla/LAW_IDS.tla`
- `formal/tla/YAI_KERNEL.tla` (historical artifact name, ontology-aligned semantics)
- `formal/configs/YAI_KERNEL*.cfg`

## 7) Packs and vectors

- `packs/compliance/*`
- `vectors/*.json`

## 8) Historical alias policy

Historical runtime names are retained only where needed for continuity.
They must not be used as primary ontology in new law text.
