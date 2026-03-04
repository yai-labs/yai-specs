# Runtime Bindings

`runtime/` contains the runtime-layer binding surfaces of `yai-law`.

These documents attach foundational YAI law to concrete runtime layers and runtime-adjacent surfaces. They are human-readable normative mappings, but they remain subordinate to canonical machine-readable artifacts, canonical headers, and formal traceability references.

Bindings do not originate law.
They explain how foundational law attaches to concrete runtime behavior and how that attachment is verified.

## Platform relevance

Runtime bindings are the normative bridge between law and implementation stacks consumed by:
- `yai` (runtime implementation)
- `yai-sdk` (contract client abstraction)
- `yai-cli` (operator command surface)
- `yai-ops` (evidence and verification context)

## Scope

Runtime bindings connect foundational law to runtime-layer surfaces such as:

- boot
- root
- kernel
- engine
- mind-facing surfaces where explicitly modeled

Where a layer includes a dedicated binding artifact, that artifact must remain aligned with canonical sources listed below.

## Canonical sources

### Machine-readable authority

- Primitives ABI: `registry/primitives.v1.json`
- Commands surface: `registry/commands.v1.json`
- Artifact roles ABI: `registry/artifacts.v1.json`
- Registry schemas: `registry/schema/*.v1.schema.json`
- Transversal artifact schemas: `schema/*.json`

### Foundational law

- Axioms: `foundation/axioms/`
- Invariants: `foundation/invariants/`
- Boundaries: `foundation/boundaries/`
- Compliance extensions: `foundation/extensions/`

### Formal authority

- Traceability matrix: `formal/traceability.v1.json`
- Kernel model: `formal/tla/YAI_KERNEL.tla`
- Formal configs: `formal/configs/*`

## Binding contract

A binding document must:

1. Declare scope and covered surfaces.
2. Reference relevant foundational law artifacts.
3. Reference canonical registries and schemas it depends on.
4. Identify required artifact roles used to verify the binding.
5. Provide verification hooks, including offline and formal references where applicable.
6. Record known gaps as explicit TODO or limitation statements.

Silent drift between runtime behavior and attached law surface is non-compliant by definition.

## Relationship to the rest of the repository

Bindings are subordinate to:

- `foundation/` for normative primacy
- `contracts/` for public interface authority
- `registry/` and `schema/` for machine-readable canonical references
- `formal/` for traceability and proof-support alignment

If a binding conflicts with a canonical contract, registry, schema, or foundational artifact, the canonical artifact prevails.
