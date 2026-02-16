# YAI Specs

`yai-specs` is the canonical, normative contract repository for YAI.
It is the single source of truth for protocols, schemas, policy specs, and formal law.
Consumers MUST pin a specific revision when integrating these specs.

## Normative vs Informative

Normative artifacts define contracts and are binding:
- JSON contracts (`*.json`)
- Protocol/ABI headers (`protocol/*.h`, `vault/yai_vault_abi.h`)
- Formal law artifacts (`contracts/**`)
- Compliance policy specs and packs (`compliance/**`)

Informative artifacts explain or guide:
- Markdown documentation (`*.md`)
- Runbooks or explanatory notes

If there is a conflict, normative artifacts take precedence.

## Repository Structure

- `compliance/` - machine-readable policy specs and packs
- `contracts/` - normative law, axioms, invariants, boundaries, formal proofs
- `protocol/` - wire/ABI headers and protocol IDs
- `control/` - control-plane schemas
- `cli/` - CLI command schemas
- `engine/` - engine contract surface
- `graph/` - graph schema
- `providers/` - provider-facing schema
- `vault/` - vault ABI contract
- `vectors/` - test vectors for conformance

## Canonical Indexes

- `SPEC_MAP.md` - authoritative table of contents for all specs
- `REGISTRY.md` - normative artifact registry and ID allocation rules
- `VERSIONING.md` - versioning and compatibility policy
- `COMPATIBILITY.md` - consumer compatibility matrix
- `CHANGELOG.md` - contract change log
- `SECURITY.md` - security and disclosure policy
- API Reference (Doxygen): https://francescomaiomascio.github.io/yai-specs/

## Consumption Model

- Treat this repo as a pinned dependency (submodule or snapshot).
- Upgrades are deliberate and validated against `VERSIONING.md` and `COMPATIBILITY.md`.
- Do not copy specs into downstream repos; link and pin instead.
