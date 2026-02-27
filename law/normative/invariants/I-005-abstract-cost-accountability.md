# I-005 — Abstract Cost Accountability (Structural Invariant, Normative)

## Summary
Abstract cost accountability is a structural invariant: every valid transition MUST be attachable to one or more cost attributes within a declared, versioned metric space.

YAI does not treat cost as business logic or billing. Cost accountability exists to keep execution governable and claims defensible (efficiency, risk, resource usage) without speculation.

A system that allows valid transitions that cannot be cost-accounted is not a valid instance of YAI.

## Definitions
**Abstract cost accountability**: the property by which every valid transition can be associated with one or more abstract cost attributes within a declared metric space.

**Metric space**: a named, versioned taxonomy of cost dimensions (e.g., time/compute/memory/I/O/tokens/energy/risk) with declared units or ordering semantics.

Cost accountability requires attachability and interpretability, not monetary units.

## Scope
Applies to:
- any governed transition that mutates state or produces effects
- any transition that crosses the external effect boundary (I-006)

This invariant is non-bypassable and applies uniformly across components.

## Normative requirements (MUST/SHOULD)

1) **Declared metric space**
- Each Run (or bundle context) MUST declare an active cost metric space identifier and version (e.g., `yai.cost.v1`).
- The metric space MUST define its dimensions and units/ordering semantics.

2) **Per-transition attachability**
- Every valid governed transition MUST be linkable to one or more cost attributes in the declared metric space.
- Cost attribution MUST NOT be ambiguous within the YAI conceptual model.

3) **Traceability linkage**
- Cost attribution MUST be traceably linkable to a specific transition (I-001), not only aggregated at run-level.
- At minimum, cost attribution MUST be joinable to decisions/events by stable identifiers (e.g., decision_id, event_id, run_id).

4) **Governance compatibility**
- Cost attribution MUST remain compatible with determinism/reproducibility constraints (I-002): reconstruction of “what cost was attributed and why” MUST be possible within declared bounds.

5) **External-effect risk dimension**
- Transitions crossing the external effect boundary MUST include a risk dimension (or equivalent) in the declared metric space.
- External effects without explicit risk attribution are invalid transitions.

6) **Completeness**
- The system MUST NOT allow classes of governed transitions that are exempt from cost accountability.

7) **Verification offline**
- A verifier MUST be able to validate cost-accountability evidence offline using bundle contents and schemas.

## ABI anchors

### Primitives used (conceptual ABI)
- `T-001 Event`
- `T-002 Identity`
- `T-003 Authority`
- `T-007 Decision`
- `T-010 Effect`
- `T-011 Evidence`
- `T-012 Run`
- `T-014 Bundle`
- `T-015 Verification`
- `S-004 Hash`
- `S-008 Validate`
- `S-011 Timeline`
- `S-013 Index`

(Conceptual mapping: cost accountability is a governed, traceable annotation of transitions and effects within a declared metric space.)

### Required artifact roles (v1)
To prove cost accountability offline, bundles MUST provide:

- `decision_record` (per-transition linkage anchor)
- `containment_metrics` (cost dimensions as metric entries, with units)
- `evidence_index` (inventory + hashes)
- `bundle_manifest` (sealed inventory)
- `verification_report` (PASS/FAIL findings)

Recommended:
- `policy` (when cost constraints are policy-governed)

### Commands involved (if any)
System-wide invariant. Enforcement MUST be exercised at minimum by:
- `yai.verify.verify`

Commands that create/execute transitions SHOULD preserve cost attribution evidence when applicable (e.g., run/test/wave drivers).

## Verification procedure (offline)
A verifier MUST be able to validate:

1) **Integrity**
- `bundle_manifest` hashes match real files.
- `evidence_index` covers required roles.

2) **Metric space declaration**
- Evidence set includes a declared metric space identifier/version (may be embedded in metrics metadata, run metadata, or policy context).
- Dimensions in `containment_metrics` are interpretable (unit present for each metric entry).

3) **Per-transition linkage**
- There exists a defensible linkage from cost entries to governed transitions:
  - either explicit identifiers (decision_id/event_id) in metrics entries,
  - or a deterministic join path via run_id + timeline + event/decision references.
- Purely run-level aggregate without any link to transitions is insufficient for compliance.

4) **External-effect risk**
- For any external-effect class present, there MUST be a corresponding risk dimension entry (or equivalent) attributable within the metric space.

5) **Report**
- `verification_report` MUST surface FAIL findings for:
  - missing metric space declaration
  - missing units/interpretability
  - lack of per-transition linkage
  - external effects without risk attribution

## Invalid patterns (non-exhaustive)
- valid transitions without cost attribution
- attribution that cannot be linked to a specific transition
- metric space not declared or not versioned
- partial attribution (some components exempt)
- only run-level aggregates with no per-transition joinability
- external-effect transitions without risk dimension

## Violation signal
If violated:
- cost cannot be attributed defensibly
- efficiency/risk claims become speculative
- governance cannot defend resource and risk decisions

Violations are structural: the system is non-compliant regardless of correctness or performance.

## Non-goals
This invariant does not prescribe:
- telemetry/instrumentation mechanisms
- dashboards/reporting tooling
- KPI taxonomies or economic formulas
- optimization objectives or scheduling strategies

Downstream implementations MAY vary, but MUST preserve the guarantees above.