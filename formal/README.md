# Formal

TLA+ specifications and configuration files for the normative law.
These artifacts are authoritative for the formal model.

## Contents

- `YAI_KERNEL.tla` - primary TLA+ spec
- `LAW_IDS.tla` - ID definitions
- `YAI_KERNEL.cfg` / `YAI_KERNEL.quick.cfg` / `YAI_KERNEL.deep.cfg` - TLC configurations
- `KERNEL_LAW_BINDING.md` - binding notes between law and spec
- `artifacts/` - optional TLC outputs (see `artifacts/README.md`)

## Running TLC (Conceptual)

- Use the `.cfg` files to select the model checking depth.
- Keep formal outputs in `artifacts/` when needed for review.

## Binding

The formal model must remain aligned with the normative law in `foundation/` and the surface definitions in `contracts/protocol/`.
