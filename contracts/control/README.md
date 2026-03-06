# Control

`contracts/control/` contains the canonical control-plane schemas of `yai-law`.

These artifacts define the authority-facing and control-plane payloads used to model YAI control surfaces.

## Scope

The control surface covers:

* control-plane structure
* authority-related payload definitions
* schema-level constraints for control-facing interactions

## Normative artifacts

Canonical schemas:

* `schema/control_plane.v1.json`
* `schema/control_call.v1.json`
* `schema/exec_reply.v1.json`
* `schema/authority.v1.json`
* `schema/authority.json`

Execution reply policy:

* `schema/exec_reply.v1.json` is the single execution envelope for SDK↔runtime calls.
* Runtime `control.call` responses must always conform to `yai.exec.reply.v1`.
* `status` + `code` are deterministic for the same input.
* `summary` and `hints` carry human-facing guidance; `reason` remains the canonical internal token.
* `data` and `details` are the machine/diagnostic payload channels.
* `schema/authority.v1.json` is the normative authority schema.
* `schema/authority.json` is a deprecated compatibility alias.

Supporting material:

* `notes/CONTROL_PLANE.md`

## Normative role

Artifacts in this directory are normative where they define canonical schema structure.

They must remain aligned with:

* `foundation/axioms/` and `foundation/invariants/` for authority and governance rules
* `foundation/extensions/compliance/` where compliance context affects control behavior
* `registry/` for machine-readable canonical references
* `formal/` where authority and external-effect constraints are modeled

If a consumer interprets control behavior in a way that conflicts with these schemas, the consumer is non-conforming.

## Versioning and compatibility rules

* File names encode schema major versions where applicable
* Breaking schema changes require a new major schema line and compatibility review
* Additive compatible changes require repository version review and `CHANGELOG.md` coverage
* Changes that affect authority interpretation must be treated as compatibility-sensitive even when the file name remains stable

## Consumers

Typical consumers include:

* `yai`
* `yai-cli`
* `yai-yx`
* validation and governance tooling that consumes canonical control-plane schemas

## Change discipline

A control-surface change must update, as applicable:

* canonical schemas in this directory
* `REGISTRY.md`
* `SPEC_MAP.md`
* `CHANGELOG.md`
* related formal and validation artifacts when semantics change

Silent drift between control-plane behavior and canonical authority schemas is non-compliant by definition.
