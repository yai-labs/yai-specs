# YAI Law — Canonical Governance Substrate for the YAI Platform

YAI = "YAI Ain't Intelligence".

`yai-law` is the canonical normative repository for the YAI platform.
It defines the contract surface that governs runtime behavior, operator control, SDK compatibility, compliance posture, and formal verification boundaries.

This repository is authority-first, not narrative-first.
Downstream repositories consume it as a pinned dependency and must prove conformance.

---

## 1) Platform role

`yai-law` is the legal-technical root of the platform stack:

`yai-law` -> `yai-sdk` -> `yai-cli` -> `yai` -> `yai-ops`

- `yai-law`: canonical normative source of truth
- `yai-sdk`: law-constrained client abstraction
- `yai-cli`: governed operator surface over SDK + law
- `yai`: runtime and program implementation constrained by law
- `yai-ops`: operational evidence and validation against law-defined expectations

If any consumer diverges from law-defined contracts, the consumer is non-conforming.

---

## 2) What this repository defines

- Canonical protocol, control, and vault contract surfaces
- Runtime-layer constraints across Boot, Root, Kernel, Engine, and Mind-facing domains
- Foundational law (axioms, invariants, boundaries, terminology, extensions)
- Canonical machine-readable registries and schemas
- Formal models and traceability artifacts
- Published normative packs (including compliance overlays)
- Validation vectors and release verification surfaces

Law authority originates here; implementation authority does not.

---

## 3) Normative vs informative

### Normative artifacts
Normative artifacts are binding and enforceable.

Examples:
- `registry/**`
- `registry/schema/**`, `schema/**`
- `contracts/protocol/include/*.h`, `contracts/vault/include/*.h`
- `foundation/**`
- `runtime/**`
- `packs/**`
- `vectors/**`

### Informative artifacts
Informative artifacts explain and navigate normative law but do not override it.

Examples:
- section-level README files
- explanatory notes
- navigation maps not explicitly declared normative

Conflict rule: normative artifacts always prevail.

---

## 4) Repository structure

- `authority/` - publication status, compatibility posture, deprecation policy
- `foundation/` - axioms, invariants, boundaries, terminology, normative extensions
- `runtime/` - canonical runtime-layer constraints (including Mind-facing surfaces)
- `contracts/` - public cross-layer contract interfaces and bindings
- `registry/` - canonical machine-readable registries and registry-bound schemas
- `schema/` - transversal schemas for policy and artifact payloads
- `formal/` - formal models, configs, proofs, traceability assets
- `packs/` - versioned normative overlays, including compliance packs
- `vectors/` - validation vectors
- `tools/` - verification and release tooling
- `docs/` - informative navigation and policy documentation

---

## 5) Consumption model (pinning is mandatory)

Consumers must treat `yai-law` as a pinned dependency:

- Prefer submodule pinning for auditability, or
- Vendor a snapshot with an explicit commit reference

Upgrade process is deliberate:
1. Read `VERSIONING.md`
2. Check `COMPATIBILITY.md`
3. Review `CHANGELOG.md`
4. Execute conformance gates before adoption

Consumers do not redefine law locally.
They pin, integrate, validate, and promote only with evidence.

---

## 6) Canonical indexes

- `SPEC_MAP.md` - authoritative structure and navigation map
- `REGISTRY.md` - canonical registries and allocation rules
- `VERSIONING.md` - versioning and compatibility contract
- `COMPATIBILITY.md` - consumer compatibility expectations
- `CHANGELOG.md` - contract/surface evolution log
- `SECURITY.md` - disclosure and security policy

---

## 7) Formal and compliance linkage

Compliance-sensitive and authority-sensitive behavior must remain aligned across:
- foundational compliance law (`foundation/extensions/compliance/`)
- compliance schemas (`schema/compliance.context.v1.json`, `schema/retention.policy.v1.json`)
- control authority surfaces (`contracts/control/schema/authority.json`)
- formal governance properties (`formal/tla/YAI_KERNEL.tla`)

This includes governance for external effects, compliance-context validity, and traceability.

---

## 8) Status and publication rule

Unless explicitly marked otherwise, published artifacts in this repository are canonical public law for their corresponding platform surfaces.

This repository is the normative foundation for enterprise-grade governed execution across the YAI platform.
