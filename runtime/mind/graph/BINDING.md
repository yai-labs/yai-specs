# Binding — Graph ↔ Law (Normative)

This binding defines the normative mapping between the canonical graph surface and the foundational YAI law constraints that govern it.

Graph-facing behavior MUST conform to these mappings whenever graph operations participate in governed execution.

## 1) Scope

This binding covers:

* graph schema linkage
* governance posture for graph-facing operations
* determinism and accountability expectations for graph participation in governed execution
* evidence expectations where graph behavior contributes to a validated run or bundle

This document does not define the graph implementation itself.
It defines how the graph surface is attached to YAI law.

## 2) Canonical sources

### Foundational law

* `foundation/invariants/I-002-determinism.md`
* `foundation/invariants/I-003-governance.md`
* `foundation/invariants/I-005-abstract-cost-accountability.md`

### Graph surface artifacts

* `runtime/mind/graph/schema/graph.v1.json`
* `runtime/mind/graph/notes/GRAPH_V1.md`

### Canonical registries

* `registry/primitives.v1.json`
* `registry/artifacts.v1.json`
* `registry/commands.v1.json`

### Formal linkage

* `formal/traceability.v1.json`
* `formal/tla/YAI_KERNEL.tla`

## 3) Invariants covered

This binding is primarily attached to the following invariants:

* `I-002-determinism`
* `I-003-governance`
* `I-005-abstract-cost-accountability`

## 4) Binding expectations

### Determinism

Graph-facing behavior must preserve determinism within the declared scope of the operation.

Where replay, reconstruction, or verification is expected, graph-related state transitions and outputs must not introduce untracked ambiguity.

### Governance

Graph operations must remain subordinate to explicit governance constraints.

No graph-facing operation may be treated as outside the governed execution model when it participates in a YAI-controlled workflow.

### Accountability

Where graph operations consume resources, influence execution, or contribute to outcomes, they must remain accountable through the canonical evidence model and associated artifact roles.

## 5) Required artifact roles (v1)

When graph operations are part of governed execution, evidence SHOULD support, as applicable:

* `decision_record`
* `containment_metrics`
* `evidence_index`
* `bundle_manifest`
* `verification_report`

The exact required set may depend on the execution profile, but graph participation must not evade evidence expectations when it materially affects runtime behavior.

## 6) Command-surface examples

Examples of command surfaces that may rely on or interact with graph behavior include:

* `yai.memory.graph`
* `yai.control.chat` when graph is used as a backing or supporting store

These examples are illustrative.
Canonical command meaning remains defined by the command registry and related law artifacts.

## 7) Formal model linkage

There is currently no dedicated graph-specific TLA module.

The current formal relation is indirect, through shared runtime governance constraints and the traceability layer, including:

* `formal/tla/YAI_KERNEL.tla`
* `formal/traceability.v1.json`

This means graph law is already governed, but not yet modeled as an independent formal state-transition surface.

## 8) Known gaps

* Graph-specific transition modeling in TLA, where justified
* Graph-specific vectors for replay and formal-alignment workflows, where justified
* Stronger explicit linkage between graph command surfaces and artifact-role expectations, if the surface expands

## 9) Change control

Any change to graph schema structure, graph-facing governance interpretation, or graph evidence expectations MUST update, as applicable:

* this binding document
* `runtime/mind/graph/schema/graph.v1.json`
* relevant foundational artifacts
* relevant traceability or formal artifacts
* `REGISTRY.md`
* `SPEC_MAP.md`
* `CHANGELOG.md`

Silent drift between graph behavior and graph law is non-compliant by definition.
