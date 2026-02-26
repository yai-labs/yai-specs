# BINDING_COMPLIANCE

## 1) Scope
Compliance context and retention governance linkage to authority/effect boundaries.

## 2) Source-of-truth pointers
- `law/normative/extensions/compliance/C-001-compliance-context.md`
- `law/normative/extensions/compliance/C-003-retention-governance.md`
- `law/normative/invariants/I-006-external-effect-boundary.md`
- `law/normative/invariants/I-007-compliance-context-required.md`

## 3) Invariants covered
- `I-006-external-effect-boundary`
- `I-007-compliance-context-required`

## 4) Spec artifacts
- `law/packs/schema/compliance.context.v1.json`
- `law/packs/schema/retention.policy.v1.json`
- `law/surfaces/control/schema/authority.json`

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
