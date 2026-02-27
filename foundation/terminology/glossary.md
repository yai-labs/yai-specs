# YAI Law — Glossary (Normative, ABI-anchored)

This glossary defines the controlled terminology of YAI Law.

It is **normative**: the meaning of terms here is authoritative within YAI Law.
Downstream projects MAY extend vocabulary, but MUST NOT redefine terms.

This glossary is **ABI-anchored**: when a concept has a canonical primitive, command surface, or artifact role, this document points to the canonical registry.

## Canonical sources (source of truth)

The authoritative machine-readable registries are:

- Primitives (conceptual ABI): `registry/primitives.v1.json`
- Commands (CLI surface): `registry/commands.v1.json`
- Artifact roles (proof ABI): `registry/artifacts.v1.json`
- Artifact schemas (normative): `schema/*.v1.schema.json`

Normative contracts live under:

- `foundation/axioms/`
- `foundation/invariants/`
- `foundation/boundaries/`

## Scope

Included:
- foundational concepts used by axioms, invariants, and boundaries
- governance concepts: authority, decision, traceability, determinism
- proof concepts: evidence, bundle, verification

Excluded:
- implementation-specific names (frameworks, libraries)
- runtime-specific operational details not bound to a registry
- domain-specific extensions (these belong in packs)

## Registry conventions

- Primitive IDs use `S-###` (Substrate), `T-###` (Governance), `O-###` (Orchestration).
- Commands are canonically identified as `yai.<group>.<name>`.
- Artifact roles are canonically identified by `artifacts.v1.json` (example: `decision_record`, `bundle_manifest`).

---

# Core Law Concepts

## Law
The conceptual layer that defines axioms, structural invariants, epistemic boundaries, and authoritative meaning.

The Law defines meaning and authority, not runtime behavior.

## Axiom
A foundational assumption taken as true by definition and not derived from lower-level mechanisms.

Axioms constrain what YAI is allowed to mean.

## Structural Invariant
A non-negotiable constraint that MUST always hold for a system to be considered a valid instance of YAI.

Structural invariants derive authority from axioms and make them enforceable over time.

## Boundary
An explicit conceptual separation defining what the Law does and does not govern with respect to other domains.

Boundaries prevent semantic overreach.

## Execution
The act of causing state transitions within the system.

Execution implies consequence and accountability.

## Runtime
The domain responsible for executing actions, managing lifecycle, and enforcing constraints during operation.

The Runtime implements behavior within limits defined by the Law.

## Intent
A proposed, declarative request for execution (command candidates).

Intent is not authority and cannot cause execution without control.

## Inference
The process of deriving conclusions, intentions, or proposals from information.

Inference may inform decisions but never grants authority to act.

---

# Governance Concepts (ABI-anchored)

These terms map directly to governance primitives in `primitives.v1.json`.

## Event (Primitive: `T-001 Event`)
A recorded occurrence eligible to enter governance evaluation.

Events are append-only once recorded.

## Identity (Primitive: `T-002 Identity`)
A stable identifier for an actor/component/workload participating in events and decisions.

Identity MUST be present in decision records (as subject/ref).

## Authority (Primitive: `T-003 Authority`)
The right to request or enact an effect within a defined boundary.

Authority MUST be explicit and auditable (no implicit escalation).

## Contract (Primitive: `T-004 Contract`)
A normative statement of allowed/required behavior, expressed as versioned inputs to governance.

Contracts SHOULD be testable via qualification.

## Baseline (Primitive: `T-005 Baseline`)
A named, versioned operational profile derived from a Contract used as an evaluation starting point.

Baselines used in published bundles MUST be immutable.

## Policy (Primitive: `T-006 Policy`, Artifact role: `policy`)
A concrete, machine-readable enforcement configuration derived from Contract + Baseline.

Policy material MUST be hash-identifiable and reproducible.

## Decision (Primitive: `T-007 Decision`, Artifact role: `decision_record`)
The formal result of evaluating an Event under Authority + Policy.

Every governed external effect MUST be preceded by a Decision.

## Outcome (Primitive: `T-008 Outcome`)
A constrained result class for Decisions: `allow | deny | error`.

## ReasonCode (Primitive: `T-009 ReasonCode`)
A stable, namespaced code explaining the outcome in an auditable and aggregatable way.

ReasonCodes MUST NOT change meaning once published.

## Effect (Primitive: `T-010 Effect`)
A state change or external action that crosses a defined boundary (network call, write, publish, mutation).

External effects MUST be measurable when possible (attempted/applied).

## Scope (Primitive: `T-021 Scope`)
The explicit perimeter of application for authority/policy/claims (resources/actions).

---

# Proof & Verification Concepts (ABI-anchored)

## Evidence (Primitive: `T-011 Evidence`, Artifact role: `evidence_index`)
A curated set of artifacts proving what happened (or did not happen), sufficient to verify claims without re-running the system.

Evidence MUST be integrity-protected (hashes) and self-descriptive (index).

## Run (Primitive: `T-012 Run`)
A single execution instance that emits records and artifacts.

A Run MUST be uniquely addressable within a Bundle.

## Wave (Primitive: `T-013 Wave`)
An orchestrated set of Runs under one scenario.

A Wave SHOULD produce a publishable Bundle.

## Bundle (Primitive: `T-014 Bundle`, Artifact role: `bundle_manifest`)
A portable, auditable package containing curated evidence, policies, and a manifest.

Bundles MUST be verifiable offline (no network required).

## Verification (Primitive: `T-015 Verification`, Artifact role: `verification_report`)
A deterministic procedure that checks bundle integrity and claim consistency.

Verification MUST NOT require network access.

## Traceability (Invariant: `I-001-traceability`)
The property by which actions, decisions, and transitions can be attributed, reconstructed, and reasoned about after execution.

Traceability is a structural invariant and MUST be supported by evidence artifacts.

## Determinism (Invariant: `I-002-determinism`)
Given the same inputs and constraints, behavior produces equivalent outcomes within a defined scope.

Determinism enables reconstruction, not prediction.

## Reproducibility
The ability to re-execute or reconstruct system behavior and obtain behaviorally equivalent results.

Reproducibility is required for governance and accountability.

## Governance (Invariant: `I-003-governance`)
The invariant by which authority, responsibility, and control remain enforceable over time, across system evolution.

Governance is structural, not procedural.

---

# Cognitive Layer Concepts (Conceptual, boundary-anchored)

These terms are conceptual and scoped by L3 boundaries. They MUST NOT be used to bypass governance primitives.

## Mind
The domain responsible for intent formation, routing, and orchestration under L3 constraints.

Mind proposes; it does not execute.

## Cognitive Adaptability
The capability by which a system explicitly suspends execution and reorganizes its cognitive configuration when observed reality invalidates current assumptions.

Cognitive adaptability does not imply autonomy.

## Cognitive Configuration
The explicit set of assumptions, constraints, priorities, goals, and contextual validity under which execution may proceed.

## Cognitive Validity / Invalidation
Validity: the configuration remains consistent with observed reality.
Invalidation: explicit detection that it no longer supports valid execution.

## Cognitive Reconfiguration
An explicit, authority-bound transition from one configuration to another performed in response to invalidation.

A reconfiguration MUST be traceable and MUST NOT be conflated with state.

---

# Terminology governance

- Terms defined here MUST NOT be redefined downstream.
- New foundational terms require explicit inclusion here (or in an approved extension pack).
- When a term maps to a registry entry (primitive, command id, artifact role), the registry is authoritative for identifiers and schema expectations.

Terminology changes are conceptual changes and MUST follow VERSIONING / COMPATIBILITY rules.