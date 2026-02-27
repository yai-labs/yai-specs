# Binding — Compliance (Normative)

## 1) Scope
Compliance context and retention governance linkage to authority and external-effect boundaries.

## 2) Canonical sources
Law:
- `foundation/extensions/compliance/C-001-compliance-context.md`
- `foundation/extensions/compliance/C-003-retention-governance.md`
- `foundation/invariants/I-006-external-effect-boundary.md`
- `foundation/invariants/I-007-compliance-context-required.md`

Packs / schemas:
- `schema/compliance.context.v1.json`
- `schema/retention.policy.v1.json`

Surface:
- `contracts/control/schema/authority.json`

ABI registries:
- `registry/artifacts.v1.json`
- `registry/primitives.v1.json`

## 3) Invariants covered
- `I-006-external-effect-boundary`
- `I-007-compliance-context-required`

## 4) Required artifact roles (v1)
Compliance enforcement MUST be verifiable via:
- `decision_record` (must show compliance context validity at decision time for external effects)
- `policy` (when compliance is policy-governed)
- `evidence_index`
- `bundle_manifest`
- `verification_report`

## 5) Formal model linkage
- Module: `formal/tla/YAI_KERNEL.tla`
- Config: `formal/configs/YAI_KERNEL.quick.cfg`
- Properties:
  - `ExternalEffectGuard`
  - `[](external_effect => compliance_context_valid)`

## 6) Known gaps / TODO
- Retention-specific temporal properties in a separate TLA module (optional).