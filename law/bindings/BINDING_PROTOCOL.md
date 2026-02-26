# BINDING_PROTOCOL

## 1) Scope
Protocol envelope, transport, session/auth semantics, and protocol-level determinism/traceability constraints.

## 2) Source-of-truth pointers
- `law/normative/invariants/I-001-traceability.md`
- `law/normative/invariants/I-002-determinism.md`
- `law/normative/invariants/I-003-governance.md`
- `law/normative/invariants/I-006-external-effect-boundary.md`
- `law/normative/invariants/I-007-compliance-context-required.md`

## 3) Invariants covered
- `I-001-traceability`
- `I-002-determinism`
- `I-003-governance`
- `I-006-external-effect-boundary`
- `I-007-compliance-context-required`

## 4) Spec artifacts
- `law/surfaces/protocol/include/protocol.h`
- `law/surfaces/protocol/include/transport.h`
- `law/surfaces/protocol/include/auth.h`
- `law/surfaces/protocol/include/errors.h`
- `law/surfaces/protocol/include/roles.h`
- `law/surfaces/protocol/include/session.h`
- `law/surfaces/protocol/runtime/include/rpc_runtime.h`

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
