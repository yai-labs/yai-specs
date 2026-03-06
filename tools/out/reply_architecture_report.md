# Reply Architecture Report v1

- required_fields: 8
- status_values: 3
- code_values: 13

## Required Fields
- `type`
- `status`
- `code`
- `reason`
- `summary`
- `command_id`
- `target_plane`
- `trace_id`

## Status Values
- `ok`
- `error`
- `nyi`

## Code Values
- `OK`
- `NOT_IMPLEMENTED`
- `BAD_ARGS`
- `UNAUTHORIZED`
- `DENIED`
- `INVALID_TARGET`
- `RUNTIME_NOT_READY`
- `SERVER_UNAVAILABLE`
- `PROTOCOL_ERROR`
- `INTERNAL_ERROR`
- `NOT_FOUND`
- `CONFLICT`
- `INVALID_STATE`

## Notes
- `summary` and `hints` are human-facing fields.
- `reason` remains the canonical internal cause token.
- `details` and `data` carry diagnostic and machine payloads.
