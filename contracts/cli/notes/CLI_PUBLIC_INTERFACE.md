# YAI CLI Public Interface (v1)

This surface is normative for public command compatibility.

## Compatibility principle

Public CLI shape can remain stable while internal runtime topology converges to:
- `core` (sovereign control)
- `exec` (execution plane)
- `brain` (cognitive plane)

## Boundary rule

CLI is a client surface.
It must not redefine authority semantics or bypass `contracts/control/` and `contracts/protocol/`.

## Historical aliases

Legacy command group names may remain temporarily for compatibility.
They are interpreted as aliases, not ontology primitives.
