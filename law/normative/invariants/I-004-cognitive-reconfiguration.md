# I-004 — Governable Cognitive Reconfiguration (Structural Invariant, Normative)

## Summary
Governable cognitive reconfiguration is a structural invariant: when cognitive assumptions become invalid, execution MUST NOT continue under known invalid configurations.

Invalidation MUST cause suspension (default) or explicitly authorized constraint.
Reconfiguration MUST be explicit, inspectable, traceable, and authority-bound.
Resumption MUST require renewed authority.

A system that adapts implicitly or continues execution under invalid cognitive configurations is not a valid instance of YAI.

## Definitions
**Cognitive configuration**: the explicit set of assumptions, constraints, goals/priorities, and contextual validity under which execution may proceed.

**Cognitive invalidation**: an explicit, verifiable signal that the current configuration no longer supports valid execution.

**Cognitive reconfiguration**: an explicit, authority-bound transition from one cognitive configuration to another performed in response to invalidation.

Governable cognitive reconfiguration constrains **when** execution may proceed, not **how** adaptation is implemented.

## Scope
Applies to any execution surface that:
- proposes or selects intents (L3)
- routes, plans, or orchestrates under cognitive assumptions
- can trigger transitions that may cross the external effect boundary
- can mutate long-lived cognitive configuration

This invariant is system-wide, continuous, and non-bypassable.

## Normative requirements (MUST/SHOULD)

1) **Execution subordinated to cognitive validity**
- Execution MUST only proceed while the active cognitive configuration is valid within declared scope.

2) **Mandatory suspension on invalidation (default)**
- Upon detected invalidation, execution MUST be suspended by default.
- Constraint (instead of full suspension) MAY occur only when explicitly authorized and traceable.

3) **Invalidation must be verifiable**
- Invalidation MUST be based on verifiable internal signal or traceable evidence (I-001), not on un-auditable “model sentiment”.

4) **Explicit, inspectable transition**
- Reconfiguration MUST be represented as an explicit transition (not implicit drift).
- The system MUST preserve evidence sufficient to reconstruct:
  - what became invalid
  - what configuration was active before
  - what configuration became active after
  - the scope affected
  - the authority under which reconfiguration and resumption occurred

5) **Authority-bound resumption**
- Resuming execution after invalidation/reconfiguration MUST require renewed authority evaluation.
- Reconfiguration MUST NOT self-authorize.

6) **Non-bypassability**
- No component MAY ignore, override, or “skip” reconfiguration constraints to proceed with execution.
- Any attempt to bypass MUST be detectable and consequential (I-003).

7) **Determinism / reproducibility**
- Reconfiguration and its authorization basis MUST be reproducible within declared scope (I-002), sufficient to enforce responsibility over time.

## ABI anchors

### Primitives used (conceptual ABI)
- `T-001 Event` (invalidation trigger/event)
- `T-002 Identity`
- `T-003 Authority`
- `T-006 Policy` (authorization basis for constrain/resume)
- `T-007 Decision` (suspend/allow/deny transition gating)
- `T-008 Outcome`
- `T-009 ReasonCode`
- `T-010 Effect` (especially if resumption enables external effects)
- `T-011 Evidence`
- `T-012 Run`
- `T-015 Verification`
- `S-010 Record`
- `S-011 Timeline`
- `S-013 Index`
- `S-004 Hash`
- `S-008 Validate`

(Conceptual mapping: “reconfiguration” is an authority-bound transition recorded as events/decisions/evidence; a dedicated artifact role can be added later.)

### Required artifact roles (v1)
To prove governable reconfiguration offline, evidence MUST include (as applicable):

- `decision_record` (records suspension/constraint/resumption decisions and reason codes)
- `policy` (authorization basis)
- `evidence_index` (inventory + hashes)
- `bundle_manifest` (sealed inventory)
- `verification_report` (PASS/FAIL findings)

Optional (recommended when available):
- `containment_metrics` (to support consequence/stability analysis)

### Commands involved (if any)
This invariant is system-wide. Typical surfaces involved include:
- `yai.control.chat` (cognitive sessions)
- `yai.memory.graph` / `yai.memory.embed` (cognitive surfaces)
- `yai.control.kernel` (authority boundary and workspace lifecycle)
- `yai.verify.verify` (offline enforcement)

Command IDs are canonical in `law/abi/registry/commands.v1.json`.

## Verification procedure (offline)
A verifier MUST be able to validate, without network access:

1) **Evidence integrity**
- `bundle_manifest` hashes match actual files.
- `evidence_index` includes required roles.

2) **Invalidation → suspension/constraint**
- For any recorded invalidation event (domain-specific), there MUST exist a corresponding decision path resulting in suspension by default, or an explicitly authorized constrained mode.

3) **Resumption is authority-bound**
- Any return to normal execution after invalidation MUST be preceded by an authority evaluation and recorded decision(s).
- Decisions MUST include policy hash/pointer and reason codes indicating reconfiguration/resumption conditions.

4) **Non-bypassability signal**
- The evidence set MUST NOT allow “continued execution under invalidation without decision”.
- Any bypass attempt MUST surface as FAIL findings in `verification_report` (or be detectable by missing required decision/evidence).

## Violation signal (non-exhaustive)
This invariant is violated if:
- execution continues after known invalidation without suspension/authorized constraint
- reconfiguration occurs implicitly without inspectable evidence
- resumption occurs without renewed authority evaluation
- invalidation is based on un-verifiable sentiment and cannot be audited
- bypass is possible or not consequential

Violations are structural: the system is non-compliant regardless of observed usefulness.

## Non-goals
This invariant does not prescribe:
- learning algorithms or adaptation mechanisms
- invalidation detection strategy
- control architecture or enforcement mechanism
- storage/query/index implementation details

Downstream implementations MAY vary, but MUST preserve the guarantees above.