# Law Refoundation Placement Rules

## 1) Normative placement model
- `foundation/`: immutable normative core (axioms, invariants, boundaries, terminology)
- `runtime/`: runtime semantics and role-model interpretation layer
- `contracts/`: externally consumable contract surfaces (ABI/schema/binding)
- `registry/`: machine-readable catalogs of primitives/artifacts/commands
- `schema/`: cross-domain schemas not tied to a single contract package
- `formal/`: formal specifications and model-check artifacts

## 2) Primary ontology rule
All normative texts must use `core`, `exec`, `brain` as primary runtime planes.
`protocol`, `platform`, `support` are cross-cutting layers.
Historical labels (`boot/root/kernel/engine/mind`) are allowed only as migration aliases.

## 3) Axiom vs Invariant vs Boundary rules
Use an **axiom** when defining first-order system truth (authority model, execution model, state model, adaptability model).
Use an **invariant** for mandatory behavior constraints that must hold at runtime.
Use a **boundary** for separation surfaces between authority/execution/cognition/cross-cutting layers.

## 4) Contract placement rules
- Put stable public wire/ABI obligations under `contracts/`.
- `contracts/control/`: authority/control semantics owned by `core`.
- `contracts/protocol/`: protocol layer, no authority policy embedding.
- `contracts/providers/`: cognitive provider semantics under `brain` governance.
- `contracts/vault/`: low-level authority-state ABI anchor.
- `contracts/cli/`: command/UI-facing surface contracts; keep compatibility unless a normative break is intentional.

## 5) Registry and schema placement rules
- Put catalog indices under `registry/` (commands/primitives/artifacts).
- Put reusable schemas under `schema/` when not package-local.
- Registry entries must be ontology-neutral and must not encode obsolete package topology as primary semantics.

## 6) Formal placement rules
- Place TLA+/formal configs and traces under `formal/`.
- Formal names may temporarily preserve historical tokens for continuity, but each artifact must include an ontology-alignment note when terms diverge from primary vocabulary.

## 7) Historical naming rules
- Allowed as: migration alias, historical note, artifact compatibility label.
- Not allowed as: primary normative domain label.
- Every historical term in normative docs must have explicit mapping to `core`, `exec`, `brain`, or cross-cutting layers.

## 8) Deprecation rules
A concept is `deprecate` when:
- it is topology-historical and no longer authoritative,
- but still needed for migration readability or compatibility trace.
A concept is `remove` when:
- it has no remaining normative or compatibility value,
- and replacement mapping is complete.

## 9) Rewrite discipline
- Do not rename public contracts or schema IDs without compatibility rationale.
- Prefer semantic rewrite over filename churn.
- Keep IDs stable when possible (`A-*`, `I-*`, boundary levels) while rewriting content.

## 10) Mandatory metadata for refoundation edits
Each rewritten file in foundation/runtime/contracts phases must state:
- primary ontology domain (`core/exec/brain/protocol/platform/support`)
- compatibility impact (`none`, `doc-only`, `contract-breaking`)
- migration aliases used (if any)
