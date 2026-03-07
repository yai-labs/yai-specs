# Runtime Bindings

`runtime/` is the law-level runtime interpretation layer.

Primary runtime ontology:
- `core` (sovereign authority and lifecycle)
- `exec` (execution and external-effect plane)
- `brain` (governed cognitive plane)
- cross-cutting layers: `protocol`, `platform`, `support`

Historical package identities are not primary ontology.
Where retained, they are explicit compatibility aliases only.

## Current runtime surfaces

- `runtime/kernel/` -> sovereign `core` semantics (historical alias path)
- `runtime/engine/` -> `exec` semantics (historical alias path)
- `runtime/mind/` -> `brain` semantics (historical alias path)

Legacy standalone boot/root runtime documentation was removed.
Its valid semantics are absorbed into `core` lifecycle and dispatch law.

## Conformance

A runtime artifact is non-conforming when it treats legacy naming as primary ontology.
A runtime artifact is conforming when compatibility naming is retained only as alias and semantics remain aligned to `core/exec/brain`.
