# YAI CLI Help Taxonomy v1

This note defines the normative navigation model for operator help.

## Model

- `entrypoint`: first token after `yai`
- `topic`: second token (noun)
- `op`: third token (verb, optional when topic is directly executable)

Canonical shape:

`yai <entrypoint> <topic> [op] [args...]`

## Surface classes

- `user`: default operator surface shown by `yai help`
- `tool`: auxiliary/diagnostic surface shown by `yai help --all`
- `internal`: plumbing/runtime internals shown by `yai help --all`

## Layer metadata

`layer` tracks runtime boundary impact and is independent from entrypoint:

- `boot`, `root`, `kernel`, `engine`, `mind`, `substrate`, `orch`, `docs`

## Rules

- Runtime internals (`boot/root/kernel/engine/mind/substrate/orch/lifecycle/memory`) are not top-level operator groups in default help.
- They are represented as `topic/layer` under stable entrypoints (typically `run`).
- Help ordering is deterministic and registry-driven.

