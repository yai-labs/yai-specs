# BINDING_CLI

## 1) Scope
CLI command schema and command-surface traceability/governance linkage.

## 2) Source-of-truth pointers
- `law/normative/invariants/I-001-traceability.md`
- `law/normative/invariants/I-002-determinism.md`
- `law/normative/invariants/I-003-governance.md`

## 3) Invariants covered
- `I-001-traceability`
- `I-002-determinism`
- `I-003-governance`

## 4) Spec artifacts
- `law/abi/registry/commands.v1.json`
- `law/abi/schema/commands.v1.schema.json`
- `law/surfaces/cli/notes/CLI_PUBLIC_INTERFACE.md`

## 5) Test vectors
- `vectors/transport_vectors.json`
- `vectors/auth_vectors.json`

## 6) Formal model linkage
- NOT YET: no dedicated CLI-level TLA module.
- Current relation is indirect via protocol/control formal guards in `formal/tla/YAI_KERNEL.tla`.

## 7) Known gaps / TODO
- NOT YET: command-schema to formal-action mapping table.
