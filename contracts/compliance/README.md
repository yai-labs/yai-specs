# Compliance

`contracts/compliance/` contains the canonical compliance-facing contract surface of `yai-law`.

This directory defines how compliance context, retention governance, and related enforcement expectations attach to the public law surface of YAI. It does not replace the foundational compliance extensions or the published compliance packs; it binds them to runtime-facing authority and verification expectations.

## Scope

The compliance surface covers:

* compliance-context linkage to governed execution
* retention-governance linkage to external-effect control
* authority-facing compliance requirements
* verification expectations for compliance-sensitive execution paths

## Normative artifacts

Primary artifact in this directory:

* `README.md` — compliance-facing contract surface definition

This surface is normatively supported by canonical artifacts elsewhere in the repository, especially:

* `foundation/extensions/compliance/`
* `foundation/invariants/I-006-external-effect-boundary.md`
* `foundation/invariants/I-007-compliance-context-required.md`
* `schema/compliance.context.v1.json`
* `schema/retention.policy.v1.json`
* `contracts/control/schema/authority.json`

## Normative role

`contracts/compliance/` is normative where it defines how compliance-related law attaches to public control and enforcement surfaces.

It must remain aligned with:

* `foundation/extensions/compliance/` for normative compliance law
* `foundation/invariants/` for external-effect and compliance-context requirements
* `schema/` for canonical policy and compliance payload structure
* `contracts/control/` for authority-facing enforcement posture
* `registry/` for canonical machine-readable references
* `formal/` where compliance-sensitive constraints are modeled or traced

If a consumer or runtime treats compliance behavior in a way that conflicts with these canonical law surfaces, it is non-conforming.

## Relationship to other compliance layers

The compliance surface in this directory is distinct from the other compliance-related layers in the repository:

* `foundation/extensions/compliance/` defines the normative compliance law
* `schema/` defines canonical compliance-related payload structure
* `packs/compliance/` publishes scoped compliance overlays
* `contracts/compliance/` defines how those compliance requirements attach to public law-facing enforcement surfaces

These layers are complementary, not interchangeable.

## Evidence and verification expectations

Where compliance-sensitive execution participates in governed runtime behavior, verification should be able to demonstrate, as applicable:

* decision-time compliance context validity
* policy-governed enforcement posture
* evidence traceability across the execution path
* compatibility between compliance payloads and canonical schema expectations

Typical artifact roles may include:

* `decision_record`
* `policy`
* `evidence_index`
* `bundle_manifest`
* `verification_report`

## Formal linkage

Compliance-facing law may be linked formally through shared runtime governance properties and the canonical traceability layer.

Relevant supporting artifacts include:

* `formal/tla/YAI_KERNEL.tla`
* `formal/configs/YAI_KERNEL.quick.cfg`
* `formal/traceability.v1.json`

Formal support strengthens validation, but it does not replace the normative force of the foundational compliance law.

## Change discipline

Any compliance-surface change that affects compliance-context interpretation, retention-governance expectations, authority-facing enforcement, or compatibility-sensitive behavior must update, as applicable:

* canonical compliance-facing artifacts
* relevant foundational compliance extensions
* relevant schemas and published packs
* relevant formal or traceability artifacts
* `REGISTRY.md`
* `SPEC_MAP.md`
* `CHANGELOG.md`

Silent drift between compliance-sensitive behavior and canonical compliance law is non-compliant by definition.
