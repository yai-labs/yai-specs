# I-003 — Governance (Structural Invariant, Normative)

## Summary
Governance is a structural invariant: YAI MUST remain permanently constrained such that:
- authority is exercised only within explicit bounds
- execution remains accountable over time
- violations are detectable and consequential
- governance is non-bypassable

A system that cannot maintain governance structurally is not a valid instance of YAI.

## Definitions
**Governance**: the structural property that ensures authority, execution, and responsibility remain enforceable continuously and non-bypassably over time.

Governance implies:
- an explicit authority model (who/what can authorize)
- an enforcement boundary (where authorization is checked)
- a consequence model (what happens on violation)

Governance is not “policy content”; it is the existence of enforceable constraints.

## Scope
Applies to any path that can:
- evaluate or assert authority
- produce a decision
- perform a state transition
- produce an external effect
- package or publish evidence for verification

Governance MUST hold across normal operation, restarts, upgrades, recovery, and degraded modes.

## Normative requirements (MUST/SHOULD)

1) **Authority-bound execution**
- No governed transition and no external effect MAY occur without explicit authority evaluation and a recorded decision.

2) **Non-bypassability**
- There MUST exist no execution path (intentional or accidental) by which a component can produce external effects outside governance constraints.
- Governance enforcement MUST be on the execution boundary, not downstream of it.

3) **Continuity over time**
- Governance MUST remain enforceable across:
  - long-running execution
  - restart/recovery
  - upgrades/reconfiguration
  - partial failures and degraded modes

4) **Detectability**
- Attempts to bypass governance or to produce unauthorized effects MUST be detectable in a structurally meaningful way (i.e., evidence artifacts allow a verifier to prove violation).

5) **Consequentiality**
- Violations MUST have defined consequences that preserve system integrity (e.g., deny, suspend, contain, escalate).
- A system that can observe violations but cannot respond is not governed.

6) **Implementation independence**
- Tooling, UI, and workflows MUST NOT be treated as the source of truth for governance.
- Governance guarantees MUST be enforceable by the system regardless of operator trust.

## ABI anchors

### Primitives used (conceptual ABI)
- `T-003 Authority`
- `T-004 Contract`
- `T-005 Baseline`
- `T-006 Policy`
- `T-007 Decision`
- `T-008 Outcome`
- `T-009 ReasonCode`
- `T-010 Effect`
- `T-011 Evidence`
- `T-014 Bundle`
- `T-015 Verification`
- `T-019 Invariant` (checking)
- `T-022 Finding`
- `S-004 Hash`
- `S-008 Validate`
- `S-011 Timeline`
- `S-013 Index`
- `S-014 Manifest`
- `S-029 Sandbox` (boundary enforcement)
- `S-030 Capability` (can-do vs should-do separation)

### Required artifact roles (v1)
To prove governance offline, bundles MUST provide:

- `decision_record` (authority evaluation + outcome + reason_code)
- `policy` (material + hash)
- `bundle_manifest` (sealed inventory and hashes)
- `evidence_index` (artifact inventory for verification)
- `verification_report` (PASS/FAIL + findings)

Recommended when available:
- `containment_metrics` (useful for consequence modeling and trend detection)

### Commands involved (if any)
System-wide invariant. Enforcement MUST be exercised at minimum by:
- `yai.verify.verify`

Commands that drive control-plane/execution boundaries SHOULD preserve governance evidence, including:
- `yai.control.kernel`
- `yai.control.root`
- `yai.lifecycle.up`
- `yai.lifecycle.down`
- `yai.lifecycle.restart`

(Exact command set may evolve; command IDs are canonical in `law/abi/registry/commands.v1.json`.)

## Verification procedure (offline)
A verifier MUST be able to validate governance properties offline:

1) **Integrity**
- `bundle_manifest` hashes match real files.
- `evidence_index` covers required roles.

2) **Decision precedes effect**
- Using `decision_record` (and optional effect fields), verify:
  - external effects are preceded by decisions
  - denies imply effects are not applied (where measurable)
  - decisions include authority reference and policy hash/pointer

3) **Policy binding**
- `policy.policy_hash` exists and matches what decisions cite.
- baseline/contract references are present where applicable.

4) **Non-bypassability evidence**
- The evidence set MUST not permit “effects without decisions”.
- Violations (attempts or successes) MUST surface as FAIL findings in `verification_report`.

5) **Consequences**
- Verify that unauthorized attempts produce deterministic outcomes (deny/error) and corresponding reason codes.

## Violation signal (non-exhaustive)
Governance is violated if:
- execution or external effects occur without explicit authority evaluation/decision
- an execution path can bypass enforcement boundaries
- violations cannot be detected or cannot be made consequential
- governance holds only in normal operation but collapses under restart, failure, upgrade, or degraded mode
- governance depends primarily on trust, convention, or external supervision

Violations are structural: the system may continue running, but it is no longer YAI-compliant.

## Non-goals
This invariant does not prescribe:
- policy languages / rule engines
- ACL tooling / dashboards
- human approval workflows
- access control products
- a specific runtime mechanism

Downstream implementations MAY add mechanisms, but MUST NOT weaken the invariant.