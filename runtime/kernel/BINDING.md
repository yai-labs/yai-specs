# Binding — Sovereign Core (Historical Alias: Kernel)

This binding maps sovereign runtime behavior to foundational law.
The primary semantic target is `core`; `kernel` is a retained historical alias.

## Canonical sources

Law:
- `foundation/axioms/A-002-authority.md`
- `foundation/axioms/A-003-state.md`
- `foundation/invariants/I-001-traceability.md`
- `foundation/invariants/I-003-governance.md`
- `foundation/invariants/I-006-external-effect-boundary.md`
- `foundation/invariants/I-007-compliance-context-required.md`
- `foundation/boundaries/L0-vault.md`
- `foundation/boundaries/L1-kernel.md`

Control contracts:
- `contracts/control/schema/control_plane.v1.json`
- `contracts/control/schema/control_call.v1.json`
- `contracts/control/schema/exec_reply.v1.json`

Formal continuity:
- `formal/tla/YAI_KERNEL.tla`
- `formal/configs/YAI_KERNEL.quick.cfg`

## Binding obligations

- Sovereign authority is a `core` concern.
- External effects are admitted only through explicit governance guards.
- Compliance context is mandatory for effectful transitions.
- Traceability must remain joinable across control, protocol, and evidence artifacts.

## Compatibility note

Artifact name `YAI_KERNEL.*` remains for continuity only.
It does not reintroduce kernel-centric ontology.
