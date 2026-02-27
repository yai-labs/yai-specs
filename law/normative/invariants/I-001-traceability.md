# I-001 — Traceability (Normative)

## Summary
Traceability is non-negotiable. Any valid action, decision, or state transition in YAI MUST be attributable, reconstructable, and explainable within the YAI governance model.

A system that cannot preserve traceability cannot preserve authority, governance, or responsibility, and is therefore not a valid instance of YAI.

## Scope
This invariant applies to any component that can:
- produce an action or effect
- evaluate or enforce authority/policy
- mutate state (kernel/engine/mind/session/memory)
- emit evidence intended for verification

This invariant defines *what must be true*, not implementation mechanics.

## Normative requirements (MUST/SHOULD)

1) **Attribution**
- Every governed transition MUST reference an explicit identity and authority source.  
- Every governed transition MUST reference a declared intent (what was attempted).

2) **Authorization basis**
- If an action is allowed or denied, the system MUST preserve the policy/baseline context used for evaluation (at least by hash/pointer) and the reason code.

3) **Causal reconstruction**
- For every valid transition, the system MUST preserve enough semantic evidence to reconstruct:
  - inputs (what the transition acted upon)
  - outputs (what the transition produced)
  - effects (what changed, including external effects)
  - causal linkage (why this path occurred rather than alternatives)

4) **External effects**
- No external effect may occur without an attributable and explainable decision record.

5) **Semantic integrity**
- “Trace records” MUST remain semantically meaningful in the YAI model.  
  Timestamps alone are insufficient: authority + intent + conditions MUST be present.

6) **Completeness**
- Traceability MUST NOT be partial in a way that permits unaccountable execution.

## ABI anchors

### Primitives used (conceptual ABI)
- `T-001 Event`
- `T-002 Identity`
- `T-003 Authority`
- `T-006 Policy`
- `T-007 Decision`
- `T-008 Outcome`
- `T-009 ReasonCode`
- `T-010 Effect`
- `T-011 Evidence`
- `T-012 Run`
- `T-014 Bundle`
- `T-015 Verification`
- `S-010 Record`
- `S-011 Timeline`
- `S-013 Index`
- `S-014 Manifest`
- `S-004 Hash`
- `S-008 Validate`

### Required artifact roles (v1)
The following artifact roles MUST be sufficient to prove traceability claims offline (as applicable to the execution surface):

- `decision_record`
- `policy`
- `evidence_index`
- `bundle_manifest`
- `verification_report`

Optional (recommended when available):
- `containment_metrics` (to support accountability/aggregation, not required for attribution)

### Commands involved (if any)
This invariant is system-wide (not command-specific).  
However, at minimum, verification MUST be enforced by:

- `yai.verify.verify`

Other commands MAY emit traces/evidence, but MUST NOT weaken the invariant.

## Verification procedure (offline)
A verifier MUST be able to validate traceability without network access, using only bundle contents and schemas.

Minimum checks:
1) `bundle_manifest` exists and hashes resolve to actual files.
2) `evidence_index` exists and covers all required roles referenced by claims.
3) `decision_record` entries:
   - include identity/authority reference
   - include policy hash/pointer + baseline reference where applicable
   - include outcome + reason_code
   - if an external effect is present, it is linked to a decision (decision precedes effect)
4) `policy` material exists (or is referenced immutably) and its hash matches what appears in decisions.
5) `verification_report` reports PASS/FAIL for these checks.

## Violation signal (non-exhaustive)
Traceability is violated if any of the following hold:

- an action/effect exists without authority + identity attribution
- a governed transition exists without declared intent reference
- a decision exists without policy hash/pointer and reason code
- external effects can occur without an attributable decision
- trace artifacts exist but are semantically meaningless (timestamps without authority/intent/conditions)
- evidence inventory cannot reconstruct causal linkage for a transition

When violated: authority cannot be validated, governance cannot be enforced, responsibility cannot be assigned, and the system is non-compliant with YAI regardless of performance or correctness.

## Non-goals
This invariant does not prescribe:
- logging pipelines or observability frameworks
- storage/query/index implementation details
- metrics tooling

Downstream implementations may choose any mechanism, but MUST preserve the semantics above.