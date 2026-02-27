# Binding — CLI (Normative)

## 1) Scope
CLI command surface: command taxonomy, argument surface, and its governance/traceability obligations.

This binding defines how CLI commands relate to:
- law invariants (traceability/determinism/governance)
- primitives used by commands
- required proof artifacts for verification

## 2) Canonical sources
- Commands registry: `registry/commands.v1.json`
- Commands schema: `registry/schema/commands.v1.schema.json`
- Primitives registry: `registry/primitives.v1.json`
- Artifact roles registry: `registry/artifacts.v1.json`
- CLI notes: `contracts/cli/notes/CLI_PUBLIC_INTERFACE.md`

## 3) Invariants covered
- `I-001-traceability`
- `I-002-determinism`
- `I-003-governance`

## 4) Command surface contract (normative)
- Every command MUST have a canonical command id `yai.<group>.<name>` in `commands.v1.json`.
- Commands that emit or consume proof artifacts MUST declare artifact roles using `artifacts.v1.json`.
- Commands that rely on governance MUST declare primitives via `uses_primitives` (IDs from `primitives.v1.json`).

## 5) Required artifact roles (v1)
At minimum, CLI verification MUST be able to reference:
- `verification_report`
- `bundle_manifest`
- `evidence_index`

Commands that participate in governed execution SHOULD also reference:
- `decision_record`
- `policy`
- `containment_metrics` (recommended)

## 6) Verification hooks
- Offline validation is performed by: `yai.verify.verify` (command id: `yai.verify.verify`)
- Registry linkage is enforced by: `tools/validate/validate_registry.py` (CI gate)

## 7) Formal linkage
No dedicated CLI TLA module yet.
CLI compliance is currently indirect via protocol/control/kernel constraints modeled in `formal/tla/YAI_KERNEL.tla`.

## 8) Known gaps / TODO
- Introduce a command → formal-action mapping table (optional) if/when CLI becomes part of TLC harness.