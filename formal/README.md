# formal/

`formal/` contains formal continuity artifacts for the current law ontology.

Primary ontology:
- `core`
- `exec`
- `brain`
- cross-cutting `protocol/platform/support`

## Artifact identity vs ontology

Formal artifact names can be historical while semantics are current.

Current policy for `YAI_KERNEL.*` artifacts:
- strategy: staged transition
- artifact identity: kept for continuity
- semantic meaning: sovereign `core` model with `exec/brain` governed relations
- status: historical name, active semantics

## Scope

- TLA+ modules and TLC configs
- formal traceability matrix and schema
- retained formal state artifacts

## Conformance rule

A formal artifact is non-conforming if it forces legacy package topology as primary ontology.
A formal artifact is conforming if it preserves continuity while expressing current law semantics.
