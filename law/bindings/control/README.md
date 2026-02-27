# Binding — Control Plane (Normative)

## 1) Scope
Authority/control-plane semantics and compliance-context requirement for effectful transitions.

## 2) Canonical sources
Law:
- `law/normative/axioms/A-002-authority.md`
- `law/normative/invariants/I-003-governance.md`
- `law/normative/invariants/I-006-external-effect-boundary.md`
- `law/normative/invariants/I-007-compliance-context-required.md`
- `law/normative/extensions/compliance/C-001-compliance-context.md`

Surfaces / schemas:
- `law/surfaces/control/schema/control_plane.v1.json`
- `law/surfaces/control/schema/authority.json`
- `law/packs/schema/compliance.context.v1.json`
- `law/packs/schema/retention.policy.v1.json`

ABI registries:
- `law/abi/registry/primitives.v1.json`
- `law/abi/registry/artifacts.v1.json`
- `law/abi/registry/commands.v1.json`

## 3) Invariants covered
- `I-003-governance`
- `I-006-external-effect-boundary`
- `I-007-compliance-context-required`

## 4) Required artifact roles (v1)
- `decision_record` (authority evaluation, effect classification, reason codes)
- `policy` (policy hash/material when applicable)
- `evidence_index`
- `bundle_manifest`
- `verification_report`

## 5) Formal model linkage
- Module: `formal/tla/YAI_KERNEL.tla`
- Config: `formal/configs/YAI_KERNEL.quick.cfg`
- Properties:
  - `ExternalEffectGuard`
  - `[](external_effect => compliance_context_valid)`
  - `AuthorityRequired` (where modeled)

## 6) Command surfaces (examples)
Command IDs involved (non-exhaustive; see `commands.v1.json`):
- `yai.control.kernel`
- `yai.control.root`
- `yai.control.shell` (high-risk surface; MUST NOT bypass boundary rules)

## 7) Known gaps / TODO
- Dedicated control-plane TLA module (optional) for command taxonomy semantics.