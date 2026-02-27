# I-007 — Compliance Context Required for External Effects (Structural Invariant, Normative)

## Summary
For any external-effect transition, a valid compliance context is a mandatory authority precondition.

If an external effect occurs (or is attempted as external-effect class), the system MUST enforce:
- compliance context validity, and
- non-null explicit authority (no “NONE” authority)

A transition that crosses the external effect boundary without valid compliance context is invalid and MUST be denied.

## Invariant statement (normative)
For every candidate transition `t`:

1) `ExternalEffect(t) => compliance_context_valid = TRUE`
2) `ExternalEffect(t) => authority != "NONE"`

## Scope
This invariant applies only to authority checks for external effects (I-006).  
It does not define DSAR workflows, retention execution, or legal interpretation (those belong to compliance packs/workflows).

## Runtime model binding (formal)
The formal kernel model binds this invariant through:

- variable: `compliance_context_valid`
- guard: `ExternalEffectGuard`
- theorem: `[](external_effect => compliance_context_valid)`

(See `formal/tla/YAI_KERNEL.tla` and `formal/configs/YAI_KERNEL.quick.cfg`.)

## Normative requirements (MUST/SHOULD)

1) **Precondition at decision time**
- Compliance context validity MUST be evaluated at decision time for external effects (not post-hoc).

2) **Non-bypassability**
- There MUST exist no bypass path allowing external effects without compliance context validation.

3) **Evidence requirement**
- Evidence MUST be sufficient to prove offline that:
  - the transition was classified as external-effect, and
  - compliance context was present and valid at the time of decision.

4) **Consequence**
- If compliance context is missing or invalid for an external-effect transition, the outcome MUST be deny (or error if verification fails) and MUST produce an auditable reason code.

## ABI anchors

### Primitives used (conceptual ABI)
- `T-003 Authority`
- `T-006 Policy`
- `T-007 Decision`
- `T-008 Outcome`
- `T-009 ReasonCode`
- `T-010 Effect`
- `T-011 Evidence`
- `T-015 Verification`
- `S-008 Validate`
- `S-013 Index`
- `S-014 Manifest`

### Required artifact roles (v1)
To prove this invariant offline, bundles MUST provide:
- `decision_record` (authority outcome + reason_code, with external-effect classification)
- `evidence_index`
- `bundle_manifest`
- `verification_report`

Required supporting schema (compliance):
- `law/packs/schema/compliance.context.v1.json` (the compliance context serialization)

Recommended:
- `policy` (when the compliance context requirement is policy-governed per domain pack)

### Commands involved (if any)
System-wide invariant. Enforcement MUST be exercised at minimum by:
- `yai.verify.verify`

## Verification procedure (offline)
A verifier MUST be able to validate:

1) **Integrity**
- `bundle_manifest` hashes match actual files.
- `evidence_index` covers required roles.

2) **External-effect classification**
- Identify transitions/effects classified as external-effect (via decision/effect evidence).

3) **Compliance context present + valid**
- For each external-effect decision:
  - compliance context must be present in evidence and validate against `law/packs/schema/compliance.context.v1.json`
  - decision evidence must indicate `compliance_context_valid = TRUE` at decision time

4) **Authority not NONE**
- For each external-effect decision, authority reference must be non-null and explicit.

5) **Report**
- `verification_report` MUST produce FAIL findings if any external-effect transition lacks valid compliance context or explicit authority.

## Violation signal
Violation occurs if:
- `external_effect = TRUE` without valid compliance context
- external effects can be produced without compliance validation (bypass)
- evidence cannot prove compliance validation happened at decision time

Violations are structural: the system is non-compliant regardless of runtime behavior.

## Non-goals
This invariant does not define:
- DSAR workflow details
- retention policy execution
- legal interpretation

Those are downstream compliance workflows built on top of this authority invariant.