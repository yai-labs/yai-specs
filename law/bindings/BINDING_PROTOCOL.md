# BINDING_PROTOCOL

## 1) Scope
Protocol envelope, transport, session/auth semantics, and protocol-level determinism/traceability constraints.

## 2) Source-of-truth pointers
- `contracts/invariants/I-001-traceability.md`
- `contracts/invariants/I-002-determinism.md`
- `contracts/invariants/I-003-governance.md`
- `contracts/invariants/I-006-external-effect-boundary.md`
- `contracts/invariants/I-007-compliance-context-required.md`

## 3) Invariants covered
- `I-001-traceability`
- `I-002-determinism`
- `I-003-governance`
- `I-006-external-effect-boundary`
- `I-007-compliance-context-required`

## 4) Spec artifacts
- `specs/protocol/include/protocol.h`
- `specs/protocol/include/transport.h`
- `specs/protocol/include/auth.h`
- `specs/protocol/include/errors.h`
- `specs/protocol/include/roles.h`
- `specs/protocol/include/session.h`
- `specs/protocol/runtime/include/rpc_runtime.h`

## 5) Test vectors
- `vectors/transport_vectors.json`
- `vectors/auth_vectors.json`
- `vectors/audit_vectors.json`

## 6) Formal model linkage
- Module: `formal/tla/YAI_KERNEL.tla`
- Configs:
  - `formal/configs/YAI_KERNEL.quick.cfg`
  - `formal/configs/YAI_KERNEL.deep.cfg`
- Properties currently represented in model:
  - `TypeInvariant`
  - `AuthorityRequired`
  - `ExternalEffectGuard`
  - `[](external_effect => compliance_context_valid)`

## 7) Known gaps / TODO
- NOT YET: explicit TLA property name for all protocol header fields (`magic`, `version`, payload semantics).
- NOT YET: transport vector replay integrated into TLC harness.
