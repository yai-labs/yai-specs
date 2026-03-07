# YAI Law

`yai-law` is the normative source repository for YAI.
It defines the law surfaces consumed by:
- `yai` (runtime implementation)
- `yai-cli` (operator surface)
- `yai-sdk` (programmatic surface)

This repository is not runtime code.
It defines what conforming runtime code must satisfy.

## Primary normative ontology

Primary runtime ontology used by `yai-law`:
- `core`: sovereign authority, workspace sovereignty, lifecycle, dispatch, enforcement baseline
- `exec`: execution and external-effect plane under governance
- `brain`: governed cognitive plane
- cross-cutting layers: `protocol`, `platform`, `support`

Historical labels (`boot`, `root`, `kernel`, `engine`, `mind`) may appear only as:
- historical aliases
- migration notes
- compatibility references

They are not primary normative ontology.

## Repository law surfaces

- `foundation/`: axioms, invariants, boundaries, terminology, extensions
- `runtime/`: runtime interpretation bindings aligned to `core/exec/brain`
- `contracts/`: public contract surfaces (control, protocol, cli, providers, vault)
- `registry/`: machine-readable registries (`primitives`, `commands`, `artifacts`)
- `schema/`: transversal payload schemas
- `formal/`: formal continuity artifacts and traceability matrix
- `packs/`: normative overlays
- `vectors/`: validation vectors

## Canonical entry docs

- `FOUNDATION.md`
- `SPEC_MAP.md`
- `REGISTRY.md`
- `docs/README.md`

## Interpretation rule

If informative text conflicts with normative artifacts, normative artifacts prevail.
