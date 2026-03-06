#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]

PRIMITIVES_REG = REPO_ROOT / "registry" / "primitives.v1.json"
PRIMITIVES_SCHEMA = REPO_ROOT / "registry" / "schema" / "primitives.v1.schema.json"

COMMANDS_REG = REPO_ROOT / "registry" / "commands.v1.json"
COMMANDS_SCHEMA = REPO_ROOT / "registry" / "schema" / "commands.v1.schema.json"

ARTIFACTS_REG = REPO_ROOT / "registry" / "artifacts.v1.json"
ARTIFACTS_SCHEMA = REPO_ROOT / "registry" / "schema" / "artifacts.v1.schema.json"


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def validate_jsonschema(instance: Dict[str, Any], schema: Dict[str, Any]) -> List[str]:
    try:
        from jsonschema import Draft202012Validator
    except Exception as exc:
        print(f"[registry] WARN: jsonschema dependency not available, schema validation skipped ({exc})")
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
    """
    Returns: role -> schema_ref
    """
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
    allowed_surface = {"surface", "ancillary", "plumbing"}
    allowed_stability = {"stable", "experimental", "planned", "deprecated"}
    allowed_scope = {"global", "workspace", "session", "runtime"}
    allowed_effect = {"read_only", "mutating", "effectful"}
    allowed_visibility = {"public", "advanced", "internal", "hidden"}
    allowed_authority = {"none", "operator", "elevated", "policy_gated"}
    allowed_impl = {"implemented", "stubbed", "nyi", "planned"}
    allowed_surface_entrypoints = {
        "ws", "run", "gov", "verify", "inspect", "bundle", "config", "doctor", "watch", "help", "version"
    }

    cmd_list = commands.get("commands", [])
    if not isinstance(cmd_list, list):
        return ["commands.commands must be an array"]

    # uniqueness of command IDs
    seen: Set[str] = set()
    for c in cmd_list:
        if not isinstance(c, dict):
            errors.append("commands.commands[] must be objects")
            continue
        cid = c.get("id")
        if not isinstance(cid, str) or not cid:
            # schema should catch this, but keep robust
            continue
        if cid in seen:
            errors.append(f"duplicate command id: {cid}")
        seen.add(cid)

    # validate per-command links
    seen_paths: Dict[str, str] = {}
    seen_aliases: Dict[str, str] = {}
    for c in cmd_list:
        if not isinstance(c, dict):
            continue

        cid = c.get("id") or f"{c.get('group','?')}.{c.get('name','?')}"
        canonical_path = c.get("canonical_path")
        if not isinstance(canonical_path, str) or not canonical_path.strip():
            errors.append(f"{cid}: canonical_path must be a non-empty string")
        else:
            owner = seen_paths.get(canonical_path)
            if owner and owner != cid:
                errors.append(f"{cid}: canonical_path collision with {owner}: {canonical_path}")
            else:
                seen_paths[canonical_path] = cid

        surface = c.get("surface")
        stability = c.get("stability")
        command_scope = c.get("command_scope")
        effect_class = c.get("effect_class")
        visibility = c.get("visibility")
        authority_class = c.get("authority_class")
        impl_status = c.get("implementation_status")
        entrypoint = c.get("entrypoint")
        hidden = bool(c.get("hidden", False))
        requires_workspace = bool(c.get("requires_workspace", False))

        if surface not in allowed_surface:
            errors.append(f"{cid}: invalid surface: {surface}")
        if stability not in allowed_stability:
            errors.append(f"{cid}: invalid stability: {stability}")
        if command_scope not in allowed_scope:
            errors.append(f"{cid}: invalid command_scope: {command_scope}")
        if effect_class not in allowed_effect:
            errors.append(f"{cid}: invalid effect_class: {effect_class}")
        if visibility not in allowed_visibility:
            errors.append(f"{cid}: invalid visibility: {visibility}")
        if authority_class not in allowed_authority:
            errors.append(f"{cid}: invalid authority_class: {authority_class}")
        if impl_status not in allowed_impl:
            errors.append(f"{cid}: invalid implementation_status: {impl_status}")
        if not isinstance(entrypoint, str) or not entrypoint:
            errors.append(f"{cid}: missing entrypoint")

        if surface == "surface" and visibility != "public":
            errors.append(f"{cid}: surface command must have visibility=public")
        if surface == "surface" and entrypoint not in allowed_surface_entrypoints:
            errors.append(f"{cid}: surface command entrypoint not allowed: {entrypoint}")
        if command_scope == "workspace" and not requires_workspace:
            errors.append(f"{cid}: workspace command must set requires_workspace=true")
        if effect_class == "effectful" and authority_class == "none":
            errors.append(f"{cid}: effectful command must not use authority_class=none")
        if visibility == "public" and hidden:
            errors.append(f"{cid}: public command cannot be hidden=true")
        if stability == "deprecated":
            if not c.get("deprecated_by") and not c.get("alias_of") and not c.get("replaced_by"):
                errors.append(f"{cid}: deprecated command requires deprecated_by/alias_of/replaced_by")
        if stability == "stable" and impl_status in {"nyi", "planned"}:
            errors.append(f"{cid}: stable command cannot have implementation_status={impl_status}")

        side_effects = c.get("side_effects", [])
        if not isinstance(side_effects, list):
            side_effects = []
        if effect_class == "read_only":
            incompatible = {"write_files", "delete_files", "network", "rpc_call", "external_effect"} & set(
                x for x in side_effects if isinstance(x, str)
            )
            if incompatible:
                errors.append(f"{cid}: read_only command has incompatible side_effects: {sorted(incompatible)}")

        aliases = c.get("aliases", [])
        if isinstance(aliases, list):
            for a in aliases:
                if not isinstance(a, str):
                    continue
                owner = seen_aliases.get(a)
                if owner and owner != cid:
                    errors.append(f"{cid}: alias collision for '{a}' (already used by {owner})")
                else:
                    seen_aliases[a] = cid

        # primitives linkage
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

        # artifacts linkage
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

                # If provided, it MUST match registry (hard mode)
                if isinstance(schema_ref, str) and schema_ref.strip():
                    if schema_ref != canonical_schema_ref:
                        errors.append(
                            f"{cid}: {field} role '{role}' schema_ref mismatch: "
                            f"got '{schema_ref}' expected '{canonical_schema_ref}'"
                        )
                    if not ensure_file_exists(schema_ref):
                        errors.append(f"{cid}: schema_ref not found: {schema_ref}")
                else:
                    # schema_ref omitted: accept, but still ensure canonical exists
                    if not ensure_file_exists(canonical_schema_ref):
                        errors.append(f"{cid}: canonical schema_ref not found for role '{role}': {canonical_schema_ref}")

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
