# Compliance Contract Surface

`contracts/compliance/` defines the canonical compliance-facing contract surface of `yai-law`.

This surface binds compliance context, retention governance, and authority-facing enforcement expectations to public runtime law.
It does not replace foundational compliance law, schema contracts, or published compliance packs.

## Scope

This surface governs:
- compliance-context linkage to governed execution decisions
- retention-governance linkage to external-effect boundaries
- authority-facing compliance obligations
- verification expectations for compliance-sensitive execution paths

## Normative support set

This surface is normatively supported by:
- `foundation/extensions/compliance/`
- `foundation/invariants/I-006-external-effect-boundary.md`
- `foundation/invariants/I-007-compliance-context-required.md`
- `schema/compliance.context.v1.json`
- `schema/retention.policy.v1.json`
- `contracts/control/schema/authority.json`

## Normative role

`contracts/compliance/` is normative where it specifies how compliance requirements attach to public control and enforcement surfaces.

It must stay aligned with:
- foundational compliance law (`foundation/extensions/compliance/`)
- invariant constraints (`foundation/invariants/`)
- canonical schema payloads (`schema/`)
- authority control posture (`contracts/control/`)
- machine-readable references (`registry/`)
- formal linkage and traceability (`formal/`)

Conflict with these canonical domains is non-conformance.

## Relationship to adjacent compliance layers

- `foundation/extensions/compliance/`: normative compliance law
- `schema/`: canonical payload structures
- `packs/compliance/`: scoped published overlays
- `contracts/compliance/`: contract attachment to public enforcement surfaces

These layers are complementary and non-interchangeable.

## Evidence and verification expectations

Compliance-sensitive execution should provide evidence for:
- decision-time compliance-context validity
- policy-governed enforcement posture
- traceability across execution and authority boundaries
- schema compatibility for compliance payloads

Typical artifact roles:
- `decision_record`
- `policy`
- `evidence_index`
- `bundle_manifest`
- `verification_report`

## Formal linkage

Formal artifacts supporting this surface include:
- `formal/tla/YAI_KERNEL.tla`
- `formal/configs/YAI_KERNEL.quick.cfg`
- `formal/traceability.v1.json`

Notably, `YAI_KERNEL.tla` encodes external-effect and compliance-context guards that reinforce this contract surface.

## Change discipline

Any change affecting compliance-context interpretation, retention governance, authority-facing enforcement, or compatibility-sensitive behavior must update, where applicable:
- canonical compliance-facing artifacts
- foundational compliance extensions
- affected schemas and packs
- formal/traceability artifacts
- `REGISTRY.md`
- `SPEC_MAP.md`
- `CHANGELOG.md`

Silent drift is non-compliant by definition.
