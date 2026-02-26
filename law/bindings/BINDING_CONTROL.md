# BINDING_CONTROL

## 1) Scope
Authority/control-plane semantics and compliance context requirement for effectful transitions.

## 2) Source-of-truth pointers
- `law/normative/axioms/A-002-authority.md`
- `law/normative/invariants/I-003-governance.md`
- `law/normative/invariants/I-006-external-effect-boundary.md`
- `law/normative/invariants/I-007-compliance-context-required.md`
- `law/normative/extensions/compliance/C-001-compliance-context.md`

## 3) Invariants covered
- `I-003-governance`
- `I-006-external-effect-boundary`
- `I-007-compliance-context-required`

## 4) Spec artifacts
- `law/surfaces/control/schema/control_plane.v1.json`
- `law/surfaces/control/schema/authority.json`
- `law/packs/schema/compliance.context.v1.json`
- `law/packs/schema/retention.policy.v1.json`

## 5) Test vectors
- `vectors/audit_vectors.json`
- `vectors/auth_vectors.json`

## 6) Formal model linkage
- Module: `formal/tla/YAI_KERNEL.tla`
- Config: `formal/configs/YAI_KERNEL.quick.cfg`
- Properties:
  - `ExternalEffectGuard`
  - `[](external_effect => compliance_context_valid)`

## 7) Known gaps / TODO
- NOT YET: dedicated control-plane TLA module with command taxonomy semantics.
