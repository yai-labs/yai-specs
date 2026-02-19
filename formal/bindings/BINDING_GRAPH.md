# BINDING_GRAPH

## 1) Scope
Graph schema linkage and deterministic governance posture for graph surfaces.

## 2) Source-of-truth pointers
- `contracts/invariants/I-002-determinism.md`
- `contracts/invariants/I-003-governance.md`
- `contracts/invariants/I-005-abstract-cost-accountability.md`

## 3) Invariants covered
- `I-002-determinism`
- `I-003-governance`
- `I-005-abstract-cost-accountability`

## 4) Spec artifacts
- `specs/graph/schema/graph.v1.json`
- `specs/graph/notes/GRAPH_V1.md`

## 5) Test vectors
- `vectors/audit_vectors.json`

## 6) Formal model linkage
- NOT YET: graph-specific module/properties.
- Current relation is indirect via `formal/tla/YAI_KERNEL.tla` governance guards.

## 7) Known gaps / TODO
- NOT YET: explicit graph-state transition model in TLA.
- NOT YET: graph-specific vectors for formal replay alignment.
