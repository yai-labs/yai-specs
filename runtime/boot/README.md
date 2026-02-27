# Boot

`runtime/boot/` contains the canonical boot-layer law surface of `yai-law`.

This directory represents boot as the bring-up and initialization layer of the YAI runtime model. It defines how early runtime establishment, pre-runtime assumptions, and initialization-facing authority constraints are understood within YAI law.

This directory does not contain the boot implementation itself.
It defines the law-facing interpretation of the boot layer.

## Scope

The boot layer covers:

* runtime bring-up posture
* initialization and pre-runtime establishment assumptions
* early-stage authority constraints before lower runtime layers are fully active
* alignment of bring-up behavior with the canonical YAI law model

## Normative role

Artifacts under `runtime/boot/` are normative where they define canonical boot-layer constraints, bindings, or explanatory law notes.

They must remain aligned with:

* `foundation/axioms/` for basic runtime and authority premises
* `foundation/invariants/` for determinism, governance, and traceability expectations within declared scope
* `foundation/boundaries/` for layer separation and authority discipline
* `registry/` for canonical machine-readable references where boot-facing identifiers or roles are relevant
* `formal/` where initialization-facing behavior is traced indirectly through the runtime model

If boot behavior diverges from the canonical law defined here and in the foundational layer, it is non-conforming.

## Relationship to other runtime layers

The boot layer precedes operational runtime layers, but it does not create an exception to law.

It must remain consistent with:

* `runtime/root/` for root-layer coordination posture
* `runtime/kernel/` for governed runtime enforcement once active
* the foundational law surface for all authority and compatibility-sensitive behavior

Boot may establish runtime conditions, but it must not introduce hidden authority, hidden state assumptions, or untracked compatibility drift.

## Formal and traceability alignment

Where boot-layer behavior affects governed execution assumptions, it should remain traceable through the repository’s formal and traceability artifacts.

Relevant supporting artifacts include:

* `formal/traceability.v1.json`
* `formal/tla/YAI_KERNEL.tla`

These artifacts support rigor, but normative primacy remains with the foundational law.

## Change discipline

Any boot-layer law change that affects bring-up assumptions, initialization posture, runtime establishment rules, or compatibility expectations must update, as applicable:

* canonical artifacts under `runtime/boot/`
* relevant foundational artifacts
* relevant formal or traceability artifacts
* `REGISTRY.md`
* `SPEC_MAP.md`
* `CHANGELOG.md`

Silent drift between boot behavior and canonical boot-layer law is non-compliant by definition.
