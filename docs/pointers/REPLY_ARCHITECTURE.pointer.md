# Reply Architecture Pointer

Canonical envelope source:
- `contracts/control/schema/exec_reply.v1.json`

## Interpretation

- Reply contract is stable compatibility surface.
- `target_plane` now supports primary labels (`core/exec/brain`) with retained legacy aliases where declared.
- CLI/SDK must normalize and render deterministically.

## Separation

- `summary/hints`: human surface
- `data/details/meta`: machine and diagnostics surface
- `trace`: traceability surface
