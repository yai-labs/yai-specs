#!/usr/bin/env python3
"""Generate a compact Reply Architecture report from exec_reply schema."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "contracts" / "control" / "schema" / "exec_reply.v1.json"
OUT = ROOT / "tools" / "out" / "reply_architecture_report.md"


def main() -> int:
    obj = json.loads(SCHEMA.read_text(encoding="utf-8"))
    required = obj.get("required", [])
    props = obj.get("properties", {})
    status_values = props.get("status", {}).get("enum", [])
    code_values = props.get("code", {}).get("enum", [])

    lines = [
        "# Reply Architecture Report v1",
        "",
        f"- required_fields: {len(required)}",
        f"- status_values: {len(status_values)}",
        f"- code_values: {len(code_values)}",
        "",
        "## Required Fields",
    ]
    for name in required:
        lines.append(f"- `{name}`")

    lines.append("")
    lines.append("## Status Values")
    for v in status_values:
        lines.append(f"- `{v}`")

    lines.append("")
    lines.append("## Code Values")
    for v in code_values:
        lines.append(f"- `{v}`")

    lines.append("")
    lines.append("## Notes")
    lines.append("- `summary` and `hints` are human-facing fields.")
    lines.append("- `reason` remains the canonical internal cause token.")
    lines.append("- `details` and `data` carry diagnostic and machine payloads.")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[reply] wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

