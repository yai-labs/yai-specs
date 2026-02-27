# Changelog

This file records notable changes to normative contracts and their documentation.

## Principles

- Keep entries short and factual.
- Note compatibility impact (MAJOR/MINOR/PATCH).
- Include date and scope when a change affects consumers.

## Unreleased

- MAJOR (contract root): replace `deps/yai-specs` with `deps/yai-law` as the single pinned law source for `yai-cli`.
- MAJOR (path surface): contract pointers moved to Law v2 canonical layout:
  - Commands: `deps/yai-law/registry/commands.v1.json`
  - Primitives: `deps/yai-law/registry/primitives.v1.json`
  - Artifacts: `deps/yai-law/registry/artifacts.v1.json`
  - Protocol/Vault/Control surfaces: `deps/yai-law/contracts/**`
  - Compliance schemas/packs: `deps/yai-law/packs/**`
- PATCH (docs/tooling): consumer documentation and tooling updated to reference `yai-law` (no legacy `yai-specs` paths).

## [0.1.0] - 2026-02-17

- MAJOR (API line): `SPECS_API_VERSION` established as `v1` for current canonical contracts.
- PATCH: Public hardening baseline (licensing, governance, security, registry/index consistency).
- PATCH: Canonical repository structure stabilized for pinning by `yai` and `yai-cli`.
