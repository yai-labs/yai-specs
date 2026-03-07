# CLI Contracts

`contracts/cli/` defines CLI-facing contract notes and binding constraints.

The CLI surface remains stable even when internal runtime packaging changes.

## Alignment rule

- Public command surface stability is prioritized.
- Internal topology migration (`core/exec/brain`) must not force unnecessary CLI breakage.
- Legacy runtime names may appear as command topics during migration, but are not ontology-defining.
