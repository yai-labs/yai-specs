# Docs Architecture Pointer

Defines documentation authority boundaries across repositories.

## Authority classes

1. `normative` (primary: `yai-law`)
2. `programmatic` (primary: `yai-sdk`)
3. `operational` (primary: `yai-cli`)
4. `runtime_procedural` (primary: `yai`)
5. `intro_navigational` (support only)

## Rule

Resolve conflicts by class precedence:
`normative > programmatic > operational > runtime_procedural > intro_navigational`.

## Ontology policy

Normative docs must use primary ontology (`core/exec/brain` + cross-cutting layers).
Historical runtime labels are migration aliases only.
