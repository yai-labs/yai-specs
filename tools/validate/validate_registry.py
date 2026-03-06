#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Set

REPO_ROOT = Path(__file__).resolve().parents[2]

PRIMITIVES_REG = REPO_ROOT / "registry" / "primitives.v1.json"
PRIMITIVES_SCHEMA = REPO_ROOT / "registry" / "schema" / "primitives.v1.schema.json"

COMMANDS_REG = REPO_ROOT / "registry" / "commands.v1.json"
COMMANDS_SCHEMA = REPO_ROOT / "registry" / "schema" / "commands.v1.schema.json"

ARTIFACTS_REG = REPO_ROOT / "registry" / "artifacts.v1.json"
ARTIFACTS_SCHEMA = REPO_ROOT / "registry" / "schema" / "artifacts.v1.schema.json"

SURFACE_ENTRYPOINTS = {
    "ws",
    "run",
    "gov",
    "verify",
    "inspect",
    "bundle",
    "config",
    "doctor",
    "watch",
    "help",
    "version",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def validate_jsonschema(instance: Dict[str, Any], schema: Dict[str, Any]) -> List[str]:
    try:
        from jsonschema import Draft202012Validator
    except Exception as exc:
        print(f"[registry] WARN: jsonschema not installed, skipping schema validation ({exc})")
        return []

    errors: List[str] = []
    v = Draft202012Validator(schema)
    for err in sorted(v.iter_errors(instance), key=lambda e: e.path):
        where = "$." + ".".join(str(x) for x in err.path) if err.path else "$"
        errors.append(f"schema error at {where}: {err.message}")
    return errors


def primitives_id_set(primitives: Dict[str, Any]) -> Set[str]:
    out: Set[str] = set()
    for p in primitives.get("primitives", []):
        pid = p.get("id")
        if isinstance(pid, str) and pid:
            out.add(pid)
    return out


def artifacts_role_map(artifacts: Dict[str, Any]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for a in artifacts.get("artifacts", []):
        role = a.get("role")
        schema_ref = a.get("schema_ref")
        if isinstance(role, str) and role and isinstance(schema_ref, str) and schema_ref:
            out[role] = schema_ref
    return out


def ensure_file_exists(path_str: str) -> bool:
    if not isinstance(path_str, str) or not path_str.strip():
        return False
    p = (REPO_ROOT / path_str).resolve()
    return p.exists()


def validate_commands(commands: Dict[str, Any], prim_ids: Set[str], role_map: Dict[str, str]) -> List[str]:
    errors: List[str] = []

    cmd_list = commands.get("commands", [])
    if not isinstance(cmd_list, list):
        return ["commands.commands must be an array"]

    seen_ids: Set[str] = set()
    seen_paths: Dict[str, str] = {}
    surface_entrypoints: Set[str] = set()

    for c in cmd_list:
        if not isinstance(c, dict):
            errors.append("commands.commands[] must be objects")
            continue

        cid = c.get("id")
        if not isinstance(cid, str) or not cid:
            continue

        if cid in seen_ids:
            errors.append(f"duplicate command id: {cid}")
        seen_ids.add(cid)

        cpath = c.get("canonical_path")
        if not isinstance(cpath, str) or not cpath.strip():
            errors.append(f"{cid}: canonical_path missing or empty")
        else:
            owner = seen_paths.get(cpath)
            if owner and owner != cid:
                errors.append(f"canonical_path collision: '{cpath}' used by {owner} and {cid}")
            seen_paths[cpath] = cid

        surface = c.get("surface")
        entrypoint = c.get("entrypoint")
        stability = c.get("stability")
        aliases = c.get("aliases", [])

        if surface == "surface":
            if entrypoint not in SURFACE_ENTRYPOINTS:
                errors.append(f"{cid}: surface command has non-surface entrypoint '{entrypoint}'")
            if isinstance(entrypoint, str):
                surface_entrypoints.add(entrypoint)

        if stability == "deprecated":
            has_aliases = isinstance(aliases, list) and len(aliases) > 0
            replaced_by = c.get("replaced_by")
            if not has_aliases and not replaced_by:
                errors.append(f"{cid}: deprecated command must define aliases or replaced_by")

        uses = c.get("uses_primitives", [])
        if uses is None:
            uses = []
        if not isinstance(uses, list):
            errors.append(f"{cid}: uses_primitives must be an array")
        else:
            for pid in uses:
                if not isinstance(pid, str):
                    errors.append(f"{cid}: uses_primitives contains non-string value")
                    continue
                if pid not in prim_ids:
                    errors.append(f"{cid}: unknown primitive id referenced: {pid}")

        for field in ("emits_artifacts", "consumes_artifacts"):
            items = c.get(field, [])
            if items is None:
                items = []
            if not isinstance(items, list):
                errors.append(f"{cid}: {field} must be an array")
                continue

            for it in items:
                if not isinstance(it, dict):
                    errors.append(f"{cid}: {field} entries must be objects")
                    continue

                role = it.get("role")
                if not isinstance(role, str) or not role:
                    errors.append(f"{cid}: {field} entry missing role")
                    continue

                if role not in role_map:
                    errors.append(f"{cid}: {field} references unknown artifact role: {role}")
                    continue

                canonical_schema_ref = role_map[role]
                schema_ref = it.get("schema_ref")

                if isinstance(schema_ref, str) and schema_ref.strip():
                    if schema_ref != canonical_schema_ref:
                        errors.append(
                            f"{cid}: {field} role '{role}' schema_ref mismatch: got '{schema_ref}' expected '{canonical_schema_ref}'"
                        )
                    if not ensure_file_exists(schema_ref):
                        errors.append(f"{cid}: schema_ref not found: {schema_ref}")
                else:
                    if not ensure_file_exists(canonical_schema_ref):
                        errors.append(f"{cid}: canonical schema_ref not found for role '{role}': {canonical_schema_ref}")

    if len(surface_entrypoints) > 12:
        errors.append(f"surface entrypoints guardrail exceeded: {len(surface_entrypoints)} (> 12)")

    sorted_by_id = sorted(
        (c for c in cmd_list if isinstance(c, dict) and isinstance(c.get("id"), str)),
        key=lambda x: x["id"],
    )
    if [c.get("id") for c in cmd_list if isinstance(c, dict)] != [c["id"] for c in sorted_by_id]:
        errors.append("commands list is not stable-sorted by id")

    return errors


def main() -> int:
    required = [PRIMITIVES_REG, PRIMITIVES_SCHEMA, COMMANDS_REG, COMMANDS_SCHEMA, ARTIFACTS_REG, ARTIFACTS_SCHEMA]
    missing = [p for p in required if not p.exists()]
    if missing:
        print("[registry] ERROR: missing required files:")
        for p in missing:
            print(f"- {rel(p)}")
        return 2

    prim = load_json(PRIMITIVES_REG)
    prim_schema = load_json(PRIMITIVES_SCHEMA)
    cmd = load_json(COMMANDS_REG)
    cmd_schema = load_json(COMMANDS_SCHEMA)
    arts = load_json(ARTIFACTS_REG)
    arts_schema = load_json(ARTIFACTS_SCHEMA)

    errors: List[str] = []
    errors.extend(validate_jsonschema(prim, prim_schema))
    errors.extend(validate_jsonschema(cmd, cmd_schema))
    errors.extend(validate_jsonschema(arts, arts_schema))

    prim_ids = primitives_id_set(prim)
    if not prim_ids:
        errors.append("primitives registry contains no ids")

    role_map = artifacts_role_map(arts)
    if not role_map:
        errors.append("artifacts registry contains no roles")

    errors.extend(validate_commands(cmd, prim_ids, role_map))

    if errors:
        print("[registry] FAIL:")
        for e in errors:
            print(f"- {e}")
        return 1

    print("[registry] OK: primitives + commands + artifacts validated and links resolved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
