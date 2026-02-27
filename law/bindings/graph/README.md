# Binding — Graph (Normative)

## 1) Scope
Graph schema linkage and deterministic governance posture for graph surfaces.

## 2) Canonical sources
Law:
- `law/normative/invariants/I-002-determinism.md`
- `law/normative/invariants/I-003-governance.md`
- `law/normative/invariants/I-005-abstract-cost-accountability.md`

Surfaces:
- `law/surfaces/graph/schema/graph.v1.json`
- `law/surfaces/graph/notes/GRAPH_V1.md`

ABI registries:
- `law/abi/registry/primitives.v1.json`
- `law/abi/registry/artifacts.v1.json`
- `law/abi/registry/commands.v1.json`

## 3) Invariants covered
- `I-002-determinism`
- `I-003-governance`
- `I-005-abstract-cost-accountability`

## 4) Required artifact roles (v1)
When graph operations are part of governed execution, evidence SHOULD support:
- `decision_record`
- `containment_metrics` (cost dimensions for graph operations, when relevant)
- `evidence_index`
- `bundle_manifest`
- `verification_report`

## 5) Command surfaces (examples)
- `yai.memory.graph`
- `yai.control.chat` (if graph is used as backing store)

## 6) Formal model linkage
No dedicated graph-specific TLA module yet.
Current relation is indirect via kernel governance guards in `formal/tla/YAI_KERNEL.tla`.

## 7) Known gaps / TODO
- Graph-specific transition model in TLA (optional).
- Graph-specific vectors for formal replay alignment (optional).