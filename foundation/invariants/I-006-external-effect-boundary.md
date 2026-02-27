# I-006 — External Effect Boundary (Structural Invariant, Normative)

## Summary
The external effect boundary is a structural invariant: YAI MUST distinguish between:
- **internal transitions** whose effects remain confined to YAI-controlled state and are isolatable/reversible in the execution model, and
- **external-effect transitions** that produce effects outside YAI-controlled state that are irreversible or not reliably reversible.

External effects are highest-consequence transitions and MUST be subject to stronger authority and evidence constraints.

Without an explicit external effect boundary, YAI cannot remain governable where it matters most.

## Definitions
**Internal transition**: a valid transition whose effects remain confined to YAI-controlled state (isolatable/reversible within the model).

**External-effect transition**: a valid transition that produces effects outside YAI-controlled state that are irreversible or not reliably reversible.

**External effect boundary predicate**: a classification function evaluated at decision time:
`ExternalEffect(t) ∈ {true, false}` for a candidate transition `t`.

## Scope
Applies to any execution surface capable of:
- network egress
- filesystem writes outside controlled stores
- provider calls / remote APIs
- actuators / side-channel outputs
- any other non-YAI-controlled effect surface

The boundary MUST be enforced wherever the effect is attempted (non-bypassable).

## Normative requirements (MUST/SHOULD)

1) **Pre-execution classification**
- The external effect classification MUST be determinable **before** executing the effect.
- If a candidate transition cannot be classified at decision time, it MUST NOT be treated as valid.

2) **Declared effect surfaces**
- Classification MUST be derived from declared effect surfaces (providers, OS calls, network, filesystem, remote APIs).
- Classification is semantic-by-consequence, not “a list of APIs”.

3) **Strengthened authority on external effects**
- If `ExternalEffect(t)=true`, the system MUST apply strengthened authority appropriate to scope and impact.

4) **Augmented semantic evidence**
For any external-effect transition, the evidence set MUST include at minimum:
- target identity / target_ref
- effect class / effect_type
- irreversibility justification (or “not reliably reversible” basis)
- authority reference
- declared intent/purpose reference
- risk attribution (I-005)
- mitigation/rollback note (may be “none”)

5) **Non-bypassability**
- No component MAY execute external effects outside the boundary predicate and governance constraints.
- Side-channels (plugins, shell access, filesystem writes, provider calls) MUST NOT bypass enforcement.

6) **Compliance extension (context required)**
For every external-effect transition:
`ExternalEffect => HasAuthority AND HasComplianceContext`

- A valid compliance context MUST be present and auditable at decision time.
- The binding MUST be enforceable at the authority layer and verifiable offline.

(Implementation note: compliance schemas are under `schema/` and domain packs under `packs/compliance/`.)

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
- `S-029 Sandbox` (boundary enforcement)
- `S-030 Capability` (prevent side-channel bypass)
- `S-004 Hash`
- `S-008 Validate`
- `S-011 Timeline`
- `S-013 Index`

### Required artifact roles (v1)
To prove boundary enforcement offline, bundles MUST provide:

- `decision_record` (must include effect classification and authority outcome)
- `policy` (authorization basis for external effects)
- `evidence_index` (inventory + hashes)
- `bundle_manifest` (sealed inventory)
- `verification_report` (PASS/FAIL findings)

Recommended:
- `containment_metrics` (risk/cost dimensions, I-005)

### Commands involved (if any)
System-wide invariant. Enforcement MUST be exercised at minimum by:
- `yai.verify.verify`

Commands that are likely to drive or expose effect surfaces SHOULD preserve boundary evidence when applicable (examples from current CLI surface):
- `yai.control.shell` (high-risk surface; MUST NOT bypass boundary)
- `yai.control.kernel`
- `yai.lifecycle.up` / `yai.lifecycle.restart` / `yai.lifecycle.down`

(See canonical command IDs in `registry/commands.v1.json`.)

## Verification procedure (offline)
A verifier MUST be able to validate boundary compliance without network access:

1) **Integrity**
- `bundle_manifest` hashes match actual files.
- `evidence_index` covers required roles.

2) **Decision precedes external effect**
- For any recorded external effect attempt/applied, there MUST exist a preceding decision record.

3) **Classification evidence**
- `decision_record` MUST indicate whether the candidate transition was classified as external-effect (directly or by effect_type mapping) and MUST include:
  - authority reference
  - policy hash/pointer
  - outcome + reason_code
  - target_ref/effect_type for external effects

4) **Augmented evidence completeness**
- For external effects, ensure required semantic fields are present (target/effect class/irreversibility basis/intent/risk/mitigation note).

5) **Compliance context**
- For external effects, verify presence of a compliance context reference/serialization that validates against `schema/compliance.context.v1.json` (and applicable pack constraints where relevant).

6) **Report**
- `verification_report` MUST produce FAIL findings for:
  - post-hoc classification
  - effects without decisions
  - missing augmented evidence fields
  - missing compliance context on external effects
  - bypass indications (side-channel evidence inconsistent with decisions)

## Invalid patterns (non-exhaustive)
- external effects treated as internal transitions
- classification performed post-hoc (after effect execution)
- effect surfaces not declared/auditable
- external effects without risk attribution (I-005)
- external effects without compliance context
- bypass via side-channels (plugins/shell/fs writes/provider calls outside boundary predicate)

## Violation signal
If violated:
- high-impact actions may occur under weak constraints
- authority may be exercised out of scope
- evidence becomes insufficient for audit
- governance cannot defend responsibility

Violations are structural: the system is non-compliant regardless of performance or correctness.

## Non-goals
This invariant does not prescribe:
- provider-specific classification mechanisms
- enforcement architecture or UI patterns
- policy engines or confirmation workflows

Downstream implementations MAY vary, but MUST preserve the guarantees above.