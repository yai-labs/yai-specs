# BINDING_COMPLIANCE

## 1) Scope
Compliance context and retention governance linkage to authority/effect boundaries.

## 2) Source-of-truth pointers
- `contracts/extensions/compliance/C-001-compliance-context.md`
- `contracts/extensions/compliance/C-003-retention-governance.md`
- `contracts/invariants/I-006-external-effect-boundary.md`
- `contracts/invariants/I-007-compliance-context-required.md`

## 3) Invariants covered
- `I-006-external-effect-boundary`
- `I-007-compliance-context-required`

## 4) Spec artifacts
- `compliance/schema/compliance.context.v1.json`
- `compliance/schema/retention.policy.v1.json`
- `specs/control/schema/authority.json`

## 5) Test vectors
- `vectors/audit_vectors.json`

## 6) Formal model linkage
- Module: `formal/tla/YAI_KERNEL.tla`
- Config: `formal/configs/YAI_KERNEL.quick.cfg`
- Properties:
  - `ExternalEffectGuard`
  - `[](external_effect => compliance_context_valid)`

## 7) Known gaps / TODO
- NOT YET: retention-specific temporal properties in separate TLA module.
