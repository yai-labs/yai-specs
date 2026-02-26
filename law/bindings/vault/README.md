# Binding — Vault (L0) (Normative)

## 1) Scope
Vault ABI and state/authority alignment at the L0 boundary.

## 2) Canonical sources
Law:
- `law/normative/axioms/A-003-state.md`
- `law/normative/boundaries/L0-vault.md`
- `law/normative/invariants/I-002-determinism.md`
- `law/normative/invariants/I-003-governance.md`

Surfaces:
- `law/surfaces/vault/include/yai_vault_abi.h`
- `law/surfaces/vault/schema/vault_abi.json`
- `law/surfaces/protocol/include/yai_protocol_ids.h`

ABI registries:
- `law/abi/registry/primitives.v1.json`
- `law/abi/registry/artifacts.v1.json`

## 3) Invariants covered
- `I-002-determinism`
- `I-003-governance`

## 4) Required artifact roles (v1)
Vault-level transitions MUST support:
- `decision_record` (when vault gates effectful transitions)
- `evidence_index`
- `bundle_manifest`
- `verification_report`

## 5) Formal model linkage
- Module: `formal/tla/YAI_KERNEL.tla`
- Config: `formal/configs/YAI_KERNEL.quick.cfg`
- Properties:
  - `VaultAbiVersionOk`
  - `TypeInvariant`

## 6) Known gaps / TODO
- Dedicated vault-focused TLA module beyond kernel-level abstraction (optional).