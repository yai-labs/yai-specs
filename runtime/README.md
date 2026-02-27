# Law Bindings (Normative)

Bindings attach YAI Law to concrete surfaces (CLI, protocol, vault, kernel, control, graph, compliance).
They are human-readable but must remain verifiable via machine-readable registries and formal artifacts.

## Canonical sources (source of truth)
Machine registries:
- Primitives ABI: `registry/primitives.v1.json`
- Commands surface: `registry/commands.v1.json`
- Artifact roles ABI: `registry/artifacts.v1.json`
- Artifact schemas: `schema/*.v1.schema.json`

Normative law:
- Axioms: `foundation/axioms/`
- Invariants: `foundation/invariants/`
- Boundaries: `foundation/boundaries/`
- Compliance extensions: `foundation/extensions/`

Formal:
- Traceability matrix: `formal/traceability.v1.json`
- Kernel model: `formal/tla/YAI_KERNEL.tla`
- Configs: `formal/configs/*`

## Binding contract
A binding document MUST:
1) Declare scope and covered surfaces
2) Reference relevant law documents (axioms/invariants/boundaries)
3) Reference canonical registries (primitives/commands/artifacts)
4) List required artifact roles (v1) used to verify the binding
5) Provide verification hooks (offline / formal where applicable)
6) Track known gaps as explicit TODO (no implicit drift)

Silent drift between surface behavior and law is non-compliant by definition.