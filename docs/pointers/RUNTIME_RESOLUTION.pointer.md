# Runtime Resolution Pointer

Defines runtime/path resolution concepts used across YAI repositories.

## Primary concepts

- `runtime_home`
- `install_root`
- `workspace_root`
- `control_endpoint`
- `deploy_mode`

## Binary identity

Primary runtime binaries are:
- `yai`
- `yai-core`

Historical binary overrides (boot/root/kernel/engine) are legacy compatibility knobs only and must not be treated as primary model.

## Resolution precedence

1. explicit CLI/config override
2. environment override
3. canonical resolver defaults
4. deterministic failure

## Binding

Programmatic resolver behavior is owned by `yai-sdk`.
Normative semantic constraints are owned by `yai-law`.
