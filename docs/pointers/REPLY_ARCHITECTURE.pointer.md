# Reply Architecture v1

This pointer defines the canonical reply model used across runtime, SDK, and CLI.

## Scope

- Normative envelope: `contracts/control/schema/exec_reply.v1.json`
- Runtime emits the envelope.
- SDK maps and exposes the envelope.
- CLI renders the envelope without inventing semantic meaning.

## Reply Dimensions

Every reply is classified by these dimensions:

- Envelope identity: `type` (must be `yai.exec.reply.v1`)
- Outcome identity: `status`, `code`
- Command binding: `command_id`, `target_plane`
- Traceability: `trace_id`
- Human support: `summary`, `hints`
- Machine payload: `data`
- Diagnostics: `details`, `meta`

## Human vs Machine Separation

- `reason` is the canonical internal cause token.
- `summary` is the human-readable sentence for operators.
- `hints` provides actionable next steps.
- `data` and `details` are for machine and diagnostics channels.

## Outcome Classes

- `ok` + `OK`
- `nyi` + `NOT_IMPLEMENTED`
- `error` + governed error codes (`BAD_ARGS`, `UNAUTHORIZED`, `DENIED`, `RUNTIME_NOT_READY`, `SERVER_UNAVAILABLE`, `PROTOCOL_ERROR`, `INTERNAL_ERROR`, `NOT_FOUND`, `CONFLICT`, `INVALID_STATE`, `INVALID_TARGET`)

## Exit Mapping Guidance (CLI)

- `OK` -> `0`
- `NOT_IMPLEMENTED` -> `10`
- `BAD_ARGS` -> `20`
- `UNAUTHORIZED` / `DENIED` -> `30`
- `RUNTIME_NOT_READY` / `SERVER_UNAVAILABLE` -> `40`
- `PROTOCOL_ERROR` / `INTERNAL_ERROR` / `INVALID_TARGET` / `NOT_FOUND` / `CONFLICT` / `INVALID_STATE` -> `50`

## Rendering Guidance

- Default human rendering prioritizes `summary` and `hints`.
- Verbose rendering may include `reason`, `details`, and trace metadata.
- JSON mode emits the raw reply envelope.

