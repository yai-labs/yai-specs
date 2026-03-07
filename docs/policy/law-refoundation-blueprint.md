# Law Refoundation Blueprint for `yai-law`

## Executive Summary
`yai-law` must stop modeling runtime truth through the historical package topology (`boot/root/kernel/engine/mind`).
The normative primary model is now:
- sovereign plane: `core`
- execution plane: `exec`
- cognitive plane: `brain`
- cross-cutting layers: `protocol`, `platform`, `support`

This blueprint defines the target ontology, the migration bridge from historical roles, and the sequencing to refactor `yai-law` without breaking valid contracts or invariants.

## Why The Old Runtime Topology Is No Longer Primary
The `yai/` runtime no longer uses top-level legacy packages as authoritative structure.
`yai-core` composes runtime planes internally (`core + exec + brain`) and uses shared layers (`protocol/platform/support`).
If `yai-law` keeps old package names as the normative axis, contracts and formal artifacts drift from real runtime behavior.

## New Normative Ontology for YAI
Primary ontology:
- `core`: authority, workspace sovereignty, lifecycle, dispatch, enforcement baseline
- `exec`: external effects, resource and environment gates, execution-side runtime adaptation
- `brain`: cognition, memory, planning, cognitive provider usage, cognitive lifecycle

Cross-cutting ontology:
- `protocol`: transport and message contracts shared across planes
- `platform`: OS/FS/clock/UDS host abstractions
- `support`: neutral primitives (ids, errors, logging, paths/strings, shared alloc helpers)

## Primary Domains
### `core`
Normative center of authority and governance. Source for sovereignty constraints and lifecycle ordering.

### `exec`
Normative center of external effect boundaries and execution interaction rules. Not sovereign authority.

### `brain`
Normative center of cognitive behavior under governance. Not sovereign authority.

## Foundational Cross-Cutting Layers
### `protocol`
Defines wire/runtime contracts shared by planes; must not embed authority semantics.

### `platform`
Defines host bindings; must not define policy semantics.

### `support`
Defines reusable neutral primitives; must not encode runtime plane semantics.

## Historical Role Mapping
- `boot` -> historical startup role; now represented under `core` lifecycle semantics
- `root` -> historical control ingress role; now represented under `core` dispatch/authority semantics
- `kernel` -> historical sovereign runtime role; now split into `core` + shared `protocol/support` concerns
- `engine` -> historical execution role; now `exec`
- `mind` -> historical cognitive subsystem role; now `brain`

Historical terms are migration aliases, not primary ontology.

## What Remains Semantically Valid From The Old Model
- authority-first governance discipline
- vault boundary as low-level authority state anchor
- traceability and determinism requirements
- explicit external-effect controls
- protocol compatibility obligations where contracts are public

## What Must Be Rewritten
High-priority rewrite domains:
- `foundation/boundaries/*` where levels are anchored to kernel/engine/mind names
- `foundation/terminology/glossary.md` to establish primary vs historical terms
- `runtime/*` narrative modeled as legacy package hierarchy
- `contracts/control/*` semantics that still assume root/kernel topology as primary

## What Can Be Realigned (Not Demolished)
- `contracts/cli/*` (surface can remain stable with ontology notes)
- `contracts/providers/*` (semantic alignment to `brain` plane)
- `contracts/vault/*` (conservative alignment, preserve ABI stability)
- parts of `registry/*` and `schema/*` with stable primitives

## What Must Be Deprecated or Removed
- normative statements asserting `boot/root/kernel/engine/mind` as primary runtime ontology
- boundary narratives that map directly to removed package topology
- ambiguous wording where authority and execution are conflated

## Refoundation Sequencing for `yai-law`
1. **Blueprint (this wave)**
   Define ontology, mapping, placement rules.
2. **Foundation rewrite**
   Rewrite axioms, invariants, boundaries, terminology to the new ontology.
3. **Runtime/contracts realignment**
   Realign `runtime/` and `contracts/*` to `core/exec/brain` + shared layers.
4. **Formal/registry/schema realignment**
   Align formal artifacts and registries; keep compatibility where needed.
5. **Top-level doc convergence**
   Rewrite `README`, `FOUNDATION`, `SPEC_MAP`, `REGISTRY` to match final ontology.

## Risks of Semantic Drift
- formal artifacts keep `YAI_KERNEL` labels as if primary runtime identity
- `contracts/control` and `runtime/*` continue narrating legacy topology
- registry/schema lock old naming into machine-readable surfaces
- docs pointers continue exposing legacy terms without migration scope labels

## Bridge Notes Toward ADR/Runbook/Program Updates
This blueprint is normative preparation only.
Next updates must include:
- ADR-level articulation of plane and layer ontology
- runbook updates for operator workflows around `yai`/`yai-core`
- program and governance docs aligned to the same vocabulary
- explicit migration aliases catalog for historical terms
