# Command Architecture v1 (Pointer)

This document defines the normative command architecture model consumed by `yai-sdk` and `yai-cli`.
It complements taxonomy metadata and closes command governance gaps across discovery, help exposure, and lifecycle transitions.

## 1. Command Identity

Each command record is identified by:

- `id` (canonical immutable identifier, `yai.<group>.<name>`)
- `canonical_path` (operator-facing path)
- `entrypoint`, `topic`, `op` (path decomposition)

`canonical_path` is the operator source of truth.
Legacy aliases can exist but must resolve to one canonical path.

## 2. Required Architecture Dimensions

Every command must be classified on these dimensions:

- Surface class: `surface | ancillary | plumbing`
- Lifecycle class: `stable | experimental | planned | deprecated`
- Scope class: `global | workspace | session | runtime`
- Effect class: `read_only | mutating | effectful`
- Visibility class: `public | advanced | internal | hidden`
- Authority class: `none | operator | elevated | policy_gated`
- Implementation status: `implemented | stubbed | nyi | planned`

## 3. Command Roots

Surface command roots (entrypoints) are:

- `ws`
- `run`
- `gov`
- `verify`
- `inspect`
- `bundle`
- `config`
- `doctor`
- `watch`
- `help`
- `version`

## 4. Core Rules

- `surface=surface` requires `visibility=public`.
- `command_scope=workspace` requires `requires_workspace=true`.
- `effect_class=effectful` requires `authority_class` not equal to `none`.
- `visibility=public` cannot be combined with `hidden=true`.
- `stability=deprecated` must include at least one of:
  - `deprecated_by`
  - `alias_of`
  - `replaced_by`
- `stability=stable` cannot be combined with `implementation_status` in `{nyi, planned}`.

## 5. Promotion Policy v1

Promotion from `planned -> experimental -> stable` requires:

- canonical path fixed and unique
- architecture dimensions fully classified
- output/reply contract defined
- implementation status coherent with lifecycle
- test evidence and discoverability in help/catalog
- no unresolved alias collisions

## 6. Deprecation Policy v1

Deprecated commands remain resolvable through aliases for compatibility windows.
CLI/SDK should emit a soft canonical-path hint when deprecated aliases are used.
Removal happens in later versions only after explicit compatibility notice.

## 7. Consumer Responsibilities

- `yai-sdk` must ingest all architecture fields and expose them in catalog/help query surfaces.
- `yai-cli` must apply architecture fields for default help filtering, `--all`, and plumbing exposure.
- No consumer may infer architecture class from local heuristics when the field is present in law.
