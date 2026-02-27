# I-002 — Determinism and Reproducibility (Normative)

## Summary
Determinism and reproducibility are structural invariants of YAI.

Determinism is required to preserve traceability (I-001).
Reproducibility is required to preserve authority and governance (I-003).

A system that cannot be deterministically reasoned about within declared scope is not a valid instance of YAI.

## Definitions
**Determinism**: given the same initial conditions and constraints, the system produces equivalent outcomes within a defined execution scope.

**Reproducibility**: the ability to re-execute or reconstruct a run and obtain behaviorally equivalent results within that scope.

Determinism in YAI is about reconstructing past behavior, not predicting future behavior.

## Scope
Applies to any execution surface that:
- evaluates authority/policy and produces decisions
- performs state transitions (kernel/engine/mind/session/memory)
- produces artifacts intended for verification

Determinism is always **scope-defined** and **boundary-aware**.

## Normative requirements (MUST/SHOULD)

1) **Scope declaration**
- Each Run MUST declare (explicitly or via referenced config) the scope under which determinism is claimed (inputs, constraints, and boundaries).

2) **Deterministic evaluation**
- Given identical inputs and the same policy/baseline material, governance evaluation MUST produce equivalent outcomes (allow/deny/error) and equivalent reason codes.

3) **Bounded nondeterminism**
- Any nondeterminism MUST be explicitly bounded and declared (e.g. randomness only in proposal/inference, not in governed execution), and MUST NOT leak into unverifiable outcomes.

4) **Reconstruction requirement**
- The evidence set MUST allow reconstruction of *why* an outcome occurred within the declared scope (inputs, constraints, decision basis).

5) **Seed / configuration stability**
- If a seed is used, it MUST be recorded and bound to the Run metadata.
- If environment/toolchain affects behavior, an environment fingerprint SHOULD be recorded.

6) **Concurrency / distribution**
- Scaling, concurrency, and distribution MUST NOT violate determinism guarantees within the declared scope.  
  (Internal traces may differ; invariant-level outcomes must remain equivalent.)

7) **Verification offline**
- A verifier MUST be able to validate determinism and reproducibility claims offline using only bundle contents and schemas (no network).

## ABI anchors

### Primitives used (conceptual ABI)
- `S-034 Seed`
- `S-017 Fingerprint`
- `S-009 Clock` (ordering constraints)
- `S-010 Record`
- `S-011 Timeline`
- `S-004 Hash`
- `S-008 Validate`
- `T-006 Policy`
- `T-007 Decision`
- `T-008 Outcome`
- `T-009 ReasonCode`
- `T-012 Run`
- `T-013 Wave`
- `T-014 Bundle`
- `T-015 Verification`

### Required artifact roles (v1)
- `policy` (policy material + hash)
- `decision_record` (outcomes + reason codes)
- `bundle_manifest` (integrity + selection)
- `evidence_index` (inventory + hashes)
- `verification_report` (PASS/FAIL + findings)

Recommended (when available):
- `containment_metrics` (aggregations useful for stability budgets)
- environment fingerprint artifact if you later standardize one (not yet in v1 roles)

### Commands involved (if any)
System-wide invariant. At minimum, enforcement MUST be exercised by:
- `yai.verify.verify`

Other commands that produce runs SHOULD preserve determinism metadata (seed/env/policy hash) when applicable.

## Verification procedure (offline)
A verifier MUST be able to check the following without re-running the system:

1) **Integrity & immutability**
- `bundle_manifest` hashes match actual files.
- `evidence_index` covers required roles.

2) **Policy determinism basis**
- `policy.policy_hash` exists and is consistent with the policy referenced inside decisions.

3) **Decision equivalence basis**
- `decision_record` lines include:
  - policy hash/pointer
  - baseline reference (when applicable)
  - outcome + reason_code
  - stable identity/authority references when relevant

4) **Reproducibility prerequisites**
- If the run declares or uses a seed, that seed MUST be present in run metadata (either in decision records or associated run evidence).
- If environment fingerprinting is enabled, fingerprint MUST be present and stable within the bundle.

5) **Report**
- `verification_report` MUST include findings for determinism preconditions (missing seed when required, missing policy hash, inconsistent policy material, etc.)

## Violation signal (non-exhaustive)
Determinism/reproducibility is violated if:
- identical inputs + identical policy material can yield different outcomes/reason codes without declared bounded nondeterminism
- decisions omit policy hash/pointer or reason codes (cannot reconstruct basis)
- seeds/config/environment dependencies exist but are not recorded
- scaling/concurrency changes invariant-level outcomes within the declared scope
- verification cannot reconstruct why an outcome occurred within scope

Violations are structural: the system is non-compliant regardless of performance or “intelligence”.

## Non-goals
This invariant does not prescribe:
- scheduling algorithms
- concurrency models
- RNG implementation
- replay tooling specifics
- testing strategy design

Downstream implementations may choose any mechanism, but MUST preserve the guarantees above.