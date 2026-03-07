# Formal / Registry / Schema Realignment

## Scope

This phase aligns `formal/`, `registry/`, and `schema/` to the new ontology without breaking public compatibility lines.

## YAI_KERNEL strategy

Adopted strategy: **staged transition**.

- Keep current artifact IDs and file names: `YAI_KERNEL.*`.
- Reinterpret semantics as current ontology (`core` sovereignty, `exec` effects, `brain` governed cognition).
- Mark names as historical artifact identity.
- Prepare later rename/deprecation window only when tooling and traceability are ready.

## Traceability realignment

`formal/traceability.v1.json` remains the canonical matrix.
It must track ontology semantics separately from artifact historical names.
No silent equivalence between artifact name and runtime ontology is allowed.

## Registry realignment posture

- Keep command IDs and compatibility surfaces stable.
- Update registry guidance to treat legacy runtime names as aliases.
- Prioritize semantic interpretation over cosmetic renames.

## Schema realignment posture

- Keep stable schema file lines where valid.
- Update descriptions/usages to avoid hidden legacy ontology.
- Avoid unnecessary schema churn that breaks consumers.

## Follow-up

Next phase should perform deeper file-by-file normalization of:
- legacy `layer` metadata values in command registries
- residual legacy references in formal artifacts and traceability entries
- top-level docs (`README`, `FOUNDATION`, `SPEC_MAP`, `REGISTRY`)
