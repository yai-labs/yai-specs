# Root

`runtime/root/` contains the canonical root-layer law surface of `yai-law`.

This directory represents the root layer as a runtime authority surface. It defines how root-level coordination, top-level runtime control posture, and root-facing authority expectations are understood within the YAI law model.

This directory does not contain the root implementation itself.
It defines the law-facing interpretation of the root layer.

## Scope

The root layer covers:

* top-level runtime authority posture
* root-facing coordination of runtime bring-up and control flow
* root-layer responsibility for preserving governed execution boundaries
* alignment between root behavior and the foundational law surface

## Normative role

Artifacts under `runtime/root/` are normative where they define canonical root-layer constraints, bindings, or explanatory law notes.

They must remain aligned with:

* `foundation/boundaries/` for runtime-layer authority separation
* `foundation/invariants/` for governance, traceability, and external-effect constraints
* `foundation/axioms/` where explicit authority posture is relevant
* `registry/` for canonical machine-readable references
* `formal/` where root-relevant behavior is traced through the formal runtime model

If a root implementation or runtime entry posture diverges from the canonical law defined here and in the foundational layer, it is non-conforming.

## Relationship to other runtime layers

The root layer is upstream of lower runtime layers in the operational bring-up and coordination sense, but it is not above foundational law.

It must remain consistent with:

* `runtime/boot/` for bring-up and initialization posture
* `runtime/kernel/` for governed runtime enforcement
* `runtime/engine/` for engine-layer execution posture
* `runtime/mind/` for mind-facing runtime surfaces where applicable

The root layer may coordinate, but it must not bypass the authority boundaries defined elsewhere in the law.

## Formal and traceability alignment

The root layer must remain traceable within the formal and repository traceability model where applicable.

Relevant supporting artifacts include:

* `formal/traceability.v1.json`
* `formal/tla/YAI_KERNEL.tla`

Formal artifacts strengthen verification of root-aligned runtime behavior, but they do not replace the normative force of foundational law.

## Change discipline

Any root-layer law change that affects coordination, authority posture, execution boundaries, or compatibility expectations must update, as applicable:

* canonical artifacts under `runtime/root/`
* relevant foundational artifacts
* relevant formal or traceability artifacts
* `REGISTRY.md`
* `SPEC_MAP.md`
* `CHANGELOG.md`

Silent drift between root behavior and canonical root-layer law is non-compliant by definition.
