# tools/

`tools/` contains the local tooling surface of `yai-law`.

This directory groups the repository utilities used to validate, inspect, release, and operate the canonical law surface. Tooling here supports the repository authority model, but it does not replace the canonical artifacts defined elsewhere in the repository.

## Scope

Artifacts under `tools/` include:

* executable helper entrypoints
* validation utilities
* formal verification support utilities
* release helpers
* repository-local operational tooling

## Structure

* `bin/` — user-facing executable entrypoints and local helper commands
* `validate/` — repository validation and consistency checks
* `formal/` — formal-layer validation helpers
* `release/` — release and versioning support utilities

## Normative role

Artifacts under `tools/` are generally operational and supportive rather than normative.

They are authoritative only as repository tooling for validating and operating the law surface.
They do not supersede:

* `foundation/`
* `runtime/`
* `contracts/`
* `registry/`
* `schema/`
* `formal/`
* `packs/`

If tooling behavior conflicts with canonical law artifacts, the canonical law artifacts prevail and the tooling must be corrected.

## Usage posture

Tooling in this directory is intended to help maintain:

* path consistency
* registry integrity
* traceability alignment
* documentation consistency
* release discipline

Consumers may reuse these tools where useful, but downstream trust should remain pinned to canonical repository artifacts, not to unreviewed tool behavior alone.

## Current notable entrypoints

* `bin/yai-govern`
* validation helpers under `validate/`
* formal validation helpers under `formal/`
* release helpers under `release/`

## Change discipline

Any tool change that affects repository validation, traceability checks, registry checks, or release discipline should be reviewed for downstream workflow impact and kept aligned with the canonical law surfaces it operates on.
# tools/

`tools/` contains the local tooling surface of `yai-law`.

This directory groups the repository utilities used to validate, inspect, release, and operate the canonical law surface. Tooling here supports the repository authority model, but it does not replace the canonical artifacts defined elsewhere in the repository.

## Scope

Artifacts under `tools/` include:

* executable helper entrypoints
* validation utilities
* formal verification support utilities
* release helpers
* repository-local operational tooling

## Structure

* `bin/` — user-facing executable entrypoints and local helper commands
* `validate/` — repository validation and consistency checks
* `formal/` — formal-layer validation helpers
* `release/` — release and versioning support utilities

## Normative role

Artifacts under `tools/` are generally operational and supportive rather than normative.

They are authoritative only as repository tooling for validating and operating the law surface.
They do not supersede:

* `foundation/`
* `runtime/`
* `contracts/`
* `registry/`
* `schema/`
* `formal/`
* `packs/`

If tooling behavior conflicts with canonical law artifacts, the canonical law artifacts prevail and the tooling must be corrected.

## Usage posture

Tooling in this directory is intended to help maintain:

* path consistency
* registry integrity
* traceability alignment
* documentation consistency
* release discipline

Consumers may reuse these tools where useful, but downstream trust should remain pinned to canonical repository artifacts, not to unreviewed tool behavior alone.

## Current notable entrypoints

* `bin/yai-govern`
* validation helpers under `validate/`
* formal validation helpers under `formal/`
* release helpers under `release/`

## Change discipline

Any tool change that affects repository validation, traceability checks, registry checks, or release discipline should be reviewed for downstream workflow impact and kept aligned with the canonical law surfaces it operates on.
