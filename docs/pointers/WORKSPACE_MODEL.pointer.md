# Workspace Model Pointer

Workspace is a sovereign runtime entity under `core` authority.

## Ownership

- `core` owns workspace lifecycle/state truth.
- execution and cognition attach under governance (`exec`, `brain`).
- CLI/SDK consume state; they do not own runtime truth.

## Binding precedence

1. explicit `--ws-id`
2. current binding
3. deterministic error

## Alias note

Historical references to `root/kernel` are legacy aliases.
Primary semantics are `core` workspace sovereignty.
