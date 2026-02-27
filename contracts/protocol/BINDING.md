# Binding — Protocol (Normative)

## 1) Scope
Protocol envelope, transport, session/auth semantics, and protocol-level determinism/traceability constraints.

## 2) Canonical sources
Law:
- `foundation/invariants/I-001-traceability.md`
- `foundation/invariants/I-002-determinism.md`
- `foundation/invariants/I-003-governance.md`
- `foundation/invariants/I-006-external-effect-boundary.md`
- `foundation/invariants/I-007-compliance-context-required.md`

Surfaces:
- `contracts/protocol/include/protocol.h`
- `contracts/protocol/include/transport.h`
- `contracts/protocol/include/auth.h`
- `contracts/protocol/include/errors.h`
- `contracts/protocol/include/roles.h`
- `contracts/protocol/include/session.h`
- `contracts/protocol/runtime/include/rpc_runtime.h`

ABI registries:
- `registry/primitives.v1.json`
- `registry/artifacts.v1.json`

## 3) Invariants covered
- `I-001-traceability`
- `I-002-determinism`
- `I-003-governance`
- `I-006-external-effect-boundary`
- `I-007-compliance-context-required`

## 4) Required artifact roles (v1)
Protocol surfaces MUST preserve evidence sufficient for:
- `decision_record`
- `evidence_index`
- `bundle_manifest`
- `verification_report`

## 5) Formal model linkage
- Module: `formal/tla/YAI_KERNEL.tla`
- Configs:
  - `formal/configs/YAI_KERNEL.quick.cfg`
  - `formal/configs/YAI_KERNEL.deep.cfg`
- Properties represented:
  - `TypeInvariant`
  - `AuthorityRequired`
  - `ExternalEffectGuard`
  - `[](external_effect => compliance_context_valid)`

## 6) Known gaps / TODO
- Make explicit formal properties for all protocol header fields (magic/version/payload invariants).
- Integrate transport vector replay into TLC harness (optional).