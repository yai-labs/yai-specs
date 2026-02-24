# YAI Law - Canonical Contracts and Constraints

YAI = "YAI Ain't Intelligence"  
Law is where intelligence becomes governable.

`yai-law` is the normative contract repository for the YAI ecosystem: protocols, schemas, ABI surfaces, policy packs, and formal artifacts that define what the runtime must do.

This repo is not documentation. It is the source of authority that every consumer pins, audits, and upgrades deliberately.

---

## 1) What this repository is

YAI Law is the single source of truth for:

- Wire and transport contracts (envelopes, IDs, routing semantics)
- Vault ABI and low-level invariants
- Control-plane schemas (commands, governance surfaces)
- Graph / events / providers schemas
- Formal law artifacts (axioms, invariants, boundaries, proofs)
- Compliance packs (machine-readable, versioned)

If a runtime or client diverges from this law, the implementation is wrong.

---

## 2) What this repository is not

- Not a playground for product experiments
- Not a best-effort reference
- Not something you copy/paste downstream

Consumers pin a revision and integrate it as a dependency.

---

## 3) Normative vs Informative

Normative artifacts are binding (contracts you must implement/validate):

- JSON schemas and contracts (`*.json`)
- Protocol and ABI headers (`specs/protocol/include/*.h`, `specs/vault/include/*.h`)
- Formal contracts and proofs (`contracts/**`)
- Compliance packs (`compliance/**`)
- Test vectors (`vectors/**`)

Informative artifacts explain the system (help you interpret the law):

- Markdown guides and notes (`*.md`, where not explicitly marked normative)

If there is a conflict, normative wins.

---

## How to consume (pinning model)

Treat this repo as a pinned dependency:

- Git submodule (preferred for auditability), or
- Vendored snapshot with a recorded commit hash

Upgrades are deliberate: read `VERSIONING.md`, check `COMPATIBILITY.md`, then validate with your conformance gates.

---

## Canonical indexes

- `SPEC_MAP.md` - authoritative table of contents
- `REGISTRY.md` - artifact registry + ID allocation rules
- `VERSIONING.md` - versioning and compatibility policy
- `COMPATIBILITY.md` - consumer compatibility matrix
- `CHANGELOG.md` - contract change log
- `SECURITY.md` - disclosure and security policy
