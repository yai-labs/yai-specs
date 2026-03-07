# Runtime and Contracts Realignment

## Purpose

This phase realigns `runtime/` and `contracts/` to the primary ontology:
- `core`
- `exec`
- `brain`

while preserving stable compatibility surfaces for `yai-cli` and `yai-sdk`.

## Runtime reinterpretation

- `runtime/kernel/` interpreted as sovereign `core` binding (historical path alias).
- `runtime/engine/` interpreted as `exec` runtime binding.
- `runtime/mind/` interpreted as `brain` runtime binding.
- `runtime/boot/` and `runtime/root/` removed as standalone runtime docs.

## Control contracts

`contracts/control/` is now explicitly `core` authority plane.
`exec_reply.v1` and `control_call.v1` now accept primary plane labels (`core/exec/brain`) and retained legacy aliases for compatibility.

## Protocol contracts

`contracts/protocol/` is explicitly documented as cross-cutting layer.
Header comments were aligned without C-ABI symbol renaming.

## CLI/providers/vault posture

- CLI: kept stable; ontology text aligned; no forced public break.
- Providers: aligned to `brain` cognitive trust semantics under `core` governance.
- Vault: treated conservatively as stable L0 boundary.

## Legacy naming status

Retained aliases: `kernel`, `engine`, `mind`, `root`, `boot`.
Removed runtime doc roots: `runtime/boot`, `runtime/root`.

## Next phase handoff

Next phase must complete deep realignment in:
- `formal/`
- `registry/`
- `schema/`
with hard checks against residual legacy semantics.
