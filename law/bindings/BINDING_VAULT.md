# BINDING_VAULT

## 1) Scope
Vault ABI and state/authority alignment at the L0 boundary.

## 2) Source-of-truth pointers
- `law/normative/axioms/A-003-state.md`
- `law/normative/boundaries/L0-vault.md`
- `law/normative/invariants/I-002-determinism.md`
- `law/normative/invariants/I-003-governance.md`

## 3) Invariants covered
- `I-002-determinism`
- `I-003-governance`

## 4) Spec artifacts
- `law/surfaces/vault/include/yai_vault_abi.h`
- `law/surfaces/vault/schema/vault_abi.json`
- `law/surfaces/protocol/include/yai_protocol_ids.h`

## 5) Test vectors
- `vectors/audit_vectors.json`

## 6) Formal model linkage
- Module: `formal/tla/YAI_KERNEL.tla`
- Config: `formal/configs/YAI_KERNEL.quick.cfg`
- Properties:
  - `VaultAbiVersionOk`
  - `TypeInvariant`

## 7) Known gaps / TODO
- NOT YET: dedicated vault-focused TLA module beyond kernel-level abstraction.
