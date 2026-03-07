# YAI Law

YAI Law is the canonical rule system of the YAI platform.

It defines the contracts, constraints, invariants, formal boundaries, and machine-readable surfaces that govern how YAI is built, exposed, validated, and operated.

This repository is normative by design.  
Downstream systems do not reinterpret it. They consume it, pin it, and prove conformance against it.

## Platform position

YAI Law anchors the platform chain:

`yai-law` → `yai-sdk` → `yai-cli` → `yai` → `yai-ops`

That chain is a discipline, not a diagram.  
Law defines the rules. Interfaces carry them forward. Systems implement them. Operations verify them.

## What this repository defines

YAI Law defines the canonical surfaces of the platform, including:

- foundational law: axioms, invariants, boundaries, terminology, and normative extensions
- contracts for protocol, control, providers, vault, and related system surfaces
- runtime constraints across the governed platform model
- machine-readable registries, schemas, and allocation rules
- formal models, traceability structures, and verification linkage
- normative packs, overlays, and validation vectors
- publication, compatibility, and deprecation posture for law surfaces

Law authority originates here.  
Implementation authority does not.

## Normative posture

This repository distinguishes between artifacts that bind the platform and artifacts that explain it.

### Normative artifacts

Normative artifacts are binding platform law.

Examples include:

- `foundation/**`
- `contracts/**`
- `runtime/**`
- `registry/**`
- `registry/schema/**`
- `schema/**`
- `formal/**`
- `packs/**`
- `vectors/**`

### Informative artifacts

Informative artifacts support navigation, explanation, and adoption, but do not override law.

Examples include:

- section-level `README.md` files
- explanatory notes
- pointer documents
- informative maps not explicitly declared normative

Where informative and normative content diverge, normative artifacts prevail.

## Repository structure

- `authority/` — publication status, compatibility posture, and deprecation discipline
- `foundation/` — axioms, invariants, boundaries, terminology, and extensions
- `contracts/` — canonical contract surfaces and bindings
- `runtime/` — platform runtime constraints and governed operating model
- `registry/` — machine-readable registries and registry-bound schemas
- `schema/` — transversal schemas for policy, evidence, and structured payloads
- `formal/` — formal models, configs, artifacts, and traceability assets
- `packs/` — published normative overlays, including compliance packs
- `vectors/` — validation vectors
- `tools/` — validation and release tooling
- `docs/` — informative navigation and supporting documentation

## Consumption model

Consumers must treat YAI Law as a pinned dependency.

Recommended approaches include:

- submodule pinning for auditability, or
- vendored snapshots with explicit commit references

Adoption is deliberate:

1. review `VERSIONING.md`
2. check `COMPATIBILITY.md`
3. read `CHANGELOG.md`
4. execute conformance gates before promotion

Consumers do not redefine law locally.  
They pin it, integrate it, validate it, and promote it with evidence.

## Canonical references

- `SPEC_MAP.md` — authoritative structure and navigation map
- `REGISTRY.md` — canonical registries and allocation rules
- `VERSIONING.md` — versioning and compatibility contract
- `COMPATIBILITY.md` — consumer compatibility expectations
- `CHANGELOG.md` — contract and surface evolution log
- `SECURITY.md` — disclosure and security policy

## Formal and compliance alignment

Compliance-sensitive and authority-sensitive behavior must remain aligned across:

- foundational law
- contract surfaces
- runtime constraints
- registry and schema definitions
- formal models and traceability assets
- compliance packs and validation vectors

This includes alignment for governance of external effects, compliance context validity, traceability, and operational proof.

## Status

Published artifacts in this repository are canonical law for their corresponding YAI platform surfaces unless explicitly marked otherwise.

YAI Law is the normative foundation of the platform.