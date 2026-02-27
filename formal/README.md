# formal/

`formal/` contains the formal verification and traceability layer of `yai-law`.

These artifacts strengthen the rigor of the canonical law surface through formal models, traceability mappings, schemas, and model-checking configurations. They are authoritative for the formalization layer of the repository, but they do not replace the normative primacy of `foundation/`, `contracts/`, `registry/`, or `schema/`.

## Scope

Artifacts under `formal/` include:

* TLA+ specifications
* TLC configuration files
* formal traceability artifacts
* formal-support schemas
* optional model-checking outputs retained for review

## Contents

* `tla/YAI_KERNEL.tla` — primary TLA+ model
* `tla/LAW_IDS.tla` — identifier-oriented formal definitions
* `configs/YAI_KERNEL.cfg` — standard TLC configuration
* `configs/YAI_KERNEL.quick.cfg` — reduced or faster validation configuration
* `configs/YAI_KERNEL.deep.cfg` — deeper validation configuration
* `traceability.v1.json` — canonical traceability matrix linking invariants, contracts, bindings, vectors, and formal references
* `schema/traceability.v1.schema.json` — schema for validating the traceability matrix
* `spec_map.md` — formal coverage map
* `artifacts/` — optional retained outputs and review artifacts

## Normative role

Artifacts under `formal/` are authoritative for the formal model and formal traceability layer.

They do not create an independent law surface.
They formalize, validate, and strengthen the law defined elsewhere in the repository.

In case of conflict:

* `foundation/` remains the normative core
* `contracts/`, `registry/`, and `schema/` remain canonical implementation-facing law surfaces
* `formal/` must be updated to restore alignment

## Running and review

Model checking may be run using the provided `.cfg` files, depending on the required depth and review purpose.

* use `YAI_KERNEL.quick.cfg` for lighter validation
* use `YAI_KERNEL.cfg` for standard validation
* use `YAI_KERNEL.deep.cfg` for deeper review where appropriate

Optional outputs may be retained under `artifacts/` when needed for audit, review, or reproducibility.

## Binding and alignment

The formal layer must remain aligned with:

* `foundation/` for axioms, invariants, and boundaries
* `contracts/protocol/` for transport and protocol-facing law surfaces
* `contracts/control/` where authority and external-effect constraints are modeled
* `registry/` and `schema/` for machine-readable canonical references

The canonical alignment artifact is `traceability.v1.json`.
Silent drift between the formal model and the canonical law surface is non-compliant by definition.

## Formal coverage map

This section summarizes current formal coverage by area.

Coverage labels:

* `none` — no explicit formal properties for this area
* `partial` — some supporting vectors or indirect coverage exist, but not a dedicated formal treatment
* `smoke` — the area is linked indirectly through shared runtime or kernel properties
* `modeled` — explicit variables, properties, or constraints exist for the area

| Area       | law                                                                                              | canonical surfaces                                                                                | vectors                                                                                           | formal                                                                                                            | Gaps                                                                                                    |
| ---------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Protocol   | yes (`foundation/invariants/I-001-traceability.md`, `I-002`, `I-003`, `I-006`, `I-007`)          | yes (`contracts/protocol/include/*`, `contracts/protocol/runtime/include/rpc_runtime.h`)          | yes (`vectors/transport_vectors.json`, `vectors/auth_vectors.json`, `vectors/audit_vectors.json`) | modeled (`formal/tla/YAI_KERNEL.tla`, `formal/configs/YAI_KERNEL.quick.cfg`)                                      | Field-level transport properties (`magic/version/payload`) are not yet explicit as named TLA properties |
| Vault      | yes (`foundation/boundaries/L0-vault.md`, `foundation/invariants/I-002-determinism.md`, `I-003`) | yes (`contracts/vault/include/yai_vault_abi.h`, `contracts/vault/schema/vault_abi.json`)          | partial (`vectors/audit_vectors.json`)                                                            | smoke (`VaultAbiVersionOk` in `formal/tla/YAI_KERNEL.tla`)                                                        | No dedicated vault module                                                                               |
| Graph      | yes (`foundation/invariants/I-002-determinism.md`, `I-003`, `I-005`)                             | yes (`runtime/mind/graph/schema/graph.v1.json`, `runtime/mind/graph/notes/GRAPH_V1.md`)           | partial (`vectors/audit_vectors.json`)                                                            | none                                                                                                              | Graph transitions are not yet modeled                                                                   |
| Control    | yes (`foundation/axioms/A-002-authority.md`, `foundation/invariants/I-003`, `I-006`, `I-007`)    | yes (`contracts/control/schema/control_plane.v1.json`, `contracts/control/schema/authority.json`) | yes (`vectors/audit_vectors.json`, `vectors/auth_vectors.json`)                                   | modeled (`ExternalEffectGuard`, `[](external_effect => compliance_context_valid)` in `formal/tla/YAI_KERNEL.tla`) | Command-taxonomy-specific formalization is still missing                                                |
| Compliance | yes (`foundation/extensions/compliance/C-001-compliance-context.md`, `C-003`)                    | yes (`schema/compliance.context.v1.json`, `schema/retention.policy.v1.json`)                      | partial (`vectors/audit_vectors.json`)                                                            | smoke                                                                                                             | Retention-specific temporal guarantees are not yet modeled                                              |
| CLI        | yes (`foundation/invariants/I-001-traceability.md`, `I-002`, `I-003`)                            | yes (`registry/commands.v1.json`, `registry/schema/commands.v1.schema.json`)                      | partial (`vectors/transport_vectors.json`)                                                        | none                                                                                                              | No direct CLI formal model                                                                              |
