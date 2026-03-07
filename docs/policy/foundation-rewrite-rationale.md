# Foundation Rewrite Rationale

## Why this rewrite was required
The prior foundation corpus mixed valid governance semantics with obsolete runtime ontology labels (`kernel/engine/mind`) as primary structure.
The runtime primary ontology is now `core/exec/brain` with `protocol/platform/support` as cross-cutting layers.
Without rewrite, foundation law would continue to drift from runtime reality.

## Rewrite strategy
- keep stable IDs for continuity (`A-*`, `I-*`, `L*`)
- rewrite content to primary ontology
- declass historical labels to migration aliases
- preserve valid core concepts: authority discipline, traceability, determinism, governance, external-effect control

## Files kept with same ID but rewritten
- Axioms: `A-001..A-004`
- Invariants: `I-001..I-007`
- Boundaries: `L0`, `L1`, `L2`, `L3`, `Lx`

## Boundary model decisions
- `L0-vault`: retained as foundational low-level boundary
- `L1-kernel`: rewritten as **Sovereign Core Boundary**, `kernel` retained only as legacy alias
- `L2-engine`: rewritten as **Execution Boundary**, `engine` retained only as legacy alias
- `L3-mind`: rewritten as **Cognitive Boundary**, `mind` retained only as legacy alias
- `Lx-docs`: rewritten to enforce normative vs explanatory separation with ontology alignment rule

## Historical term declassification
Declassified as primary normative terms:
- `boot`, `root`, `kernel`, `engine`, `mind`

They remain allowed only for:
- migration notes
- compatibility pointers
- formal continuity where pending realignment

## What stayed stable
- authority cannot emerge from inference
- execution must remain governed and attributable
- external effects require strengthened control and evidence
- compliance context is mandatory for external effects

## What this rewrite intentionally did not do
- no runtime folder rewrite
- no contracts rewrite
- no formal artifact rewrite
- no registry/schema rewrite
- no top-level doc rewrite (`README.md`, `FOUNDATION.md`, `SPEC_MAP.md`, `REGISTRY.md`)

## Next required wave
Use this rewritten foundation to drive:
1. runtime/contracts realignment
2. formal/registry/schema realignment
3. top-level narrative convergence
