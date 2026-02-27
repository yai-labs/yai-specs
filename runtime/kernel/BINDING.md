# Binding — Kernel ↔ Law (Normative)

This binding defines the normative mapping between YAI Law constraints and the kernel runtime model.
Kernel behavior MUST conform to these mappings.

## Canonical sources
Law:
- `foundation/axioms/*`
- `foundation/invariants/*`
- `foundation/boundaries/L0-vault.md`
- `foundation/boundaries/L1-kernel.md`

Formal:
- `formal/tla/YAI_KERNEL.tla`
- `formal/configs/YAI_KERNEL.quick.cfg`

ABI registries:
- `registry/primitives.v1.json`
- `registry/artifacts.v1.json`

## Variable binding map (conceptual)
This section describes expected correspondences. Runtime symbols may evolve; the mapping MUST be kept aligned.

- Traceability (I-001): kernel MUST preserve a trace identifier and/or logical clock sufficient to join decisions/effects to a run timeline.
- Authority (A-002, I-003): kernel MUST gate effectful transitions on explicit authority state (no implicit escalation).
- External effect boundary (I-006): kernel MUST participate in non-bypassable gating for external effects (classification + enforcement path).
- Compliance context (I-007): external effects MUST require compliance context validity.

## Transition binding (high-level)
Kernel state-machine transitions MUST remain consistent with formal model transitions (TLA module), especially for:
- suspension/resumption boundaries
- invalidation / reconfiguration gates
- error and reset handling

## Guard / enforcement binding
The following guards MUST remain aligned:
- Authority required
- External effect guard
- Compliance context validity guard
- Determinism constraints within declared scope

## Required artifact roles (v1)
Kernel-level evidence MUST allow offline verification of:
- `decision_record`
- `bundle_manifest`
- `evidence_index`
- `verification_report`

## Change control
Any change to kernel state machine, guards, or vault layout MUST update:
- `formal/tla/YAI_KERNEL.tla`
- this binding document
- the relevant runtime implementation

Silent drift is non-compliant by definition.