#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[2]
COMMANDS_PATH = ROOT / "registry" / "commands.v1.json"
REPORT_PATH = ROOT / "tools" / "out" / "command_architecture_report.md"

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

MUTATING_VERBS = {
    "create", "destroy", "set", "update", "publish", "reconcile", "clear", "attach", "detach",
    "start", "stop", "restart", "up", "down", "lock", "unlock", "bootstrap", "apply", "record",
    "claim", "approve", "deny", "waive", "restore", "import", "export",
}

EFFECTFUL_SIDE_EFFECTS = {
    "rpc_call", "network", "external_effect", "spawn_process", "invoke_provider",
}

MUTATING_SIDE_EFFECTS = {
    "write_files", "delete_files", "mutate_state",
}

DOMAIN_BY_ENTRYPOINT = {
    "ws": "workspace",
    "run": "runtime",
    "gov": "governance",
    "verify": "verification",
    "inspect": "inspection",
    "bundle": "bundle",
    "config": "configuration",
    "doctor": "diagnostics",
    "watch": "diagnostics",
    "help": "help",
    "version": "help",
}


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def boundary_to_layer(boundaries: List[str], group: str) -> str:
    b = boundaries or []
    for it in b:
        if it == "L1-kernel":
            return "kernel"
        if it == "L2-engine":
            return "engine"
        if it == "L3-mind":
            return "mind"
        if it == "Lx-docs":
            return "docs"
    group_layer = {
        "boot": "boot",
        "root": "root",
        "kernel": "kernel",
        "engine": "engine",
        "mind": "mind",
        "substrate": "substrate",
        "orch": "orch",
    }
    return group_layer.get(group, "root")


def map_entrypoint(group: str, name: str) -> str:
    g = (group or "").strip()
    n = (name or "").strip()
    if g in {"workspace", "ws"}:
        return "ws"
    if g == "governance":
        return "gov"
    if g == "verify":
        return "verify"
    if g == "inspect":
        return "inspect"
    if g == "bundle":
        return "bundle"
    if g in {"config", "configuration"}:
        return "config"
    if g in {"doctor", "diagnostics"}:
        return "doctor"
    if g == "watch":
        return "watch"
    if g == "help":
        return "help"
    if g == "version":
        return "version"
    if g == "kernel" and (n == "ws" or n.startswith("ws_")):
        return "ws"
    if g in {"boot", "root", "kernel", "engine", "mind", "substrate", "orch", "lifecycle", "memory", "control"}:
        return "run"
    return "config"


def split_topic_op(group: str, name: str, entrypoint: str) -> Tuple[str, str]:
    g = (group or "").strip() or "runtime"
    n = (name or "").strip() or "run"

    if entrypoint == "help":
        return ("help", n)
    if entrypoint == "version":
        return ("version", "show")
    if entrypoint == "ws":
        if n == "ws":
            return ("workspace", "manage")
        if n.startswith("ws_"):
            op = n[3:] if len(n) > 3 else "status"
            return ("workspace", op)
        parts = n.split("_", 1)
        if len(parts) == 2:
            return (parts[0], parts[1])
        return ("workspace", n)

    if g in {"boot", "root", "kernel", "engine", "mind", "substrate", "orch", "lifecycle", "memory", "control"}:
        if "_" in n:
            subtopic, op = n.split("_", 1)
            topic = f"{g}_{subtopic}" if subtopic else g
            return (topic, op or "run")
        return (g, n)

    if "_" in n:
        topic, op = n.split("_", 1)
        return (topic or g, op or "run")
    return (n, "run")


def derive_surface(group: str, entrypoint: str) -> str:
    if group in {"substrate", "orch", "memory", "control"}:
        return "plumbing"
    if group in {"boot", "root", "kernel", "engine", "mind", "lifecycle"}:
        return "ancillary"
    if entrypoint in SURFACE_ENTRYPOINTS:
        return "surface"
    return "ancillary"


def derive_effect_class(side_effects: List[str], op: str) -> str:
    se = {x for x in (side_effects or []) if isinstance(x, str)}
    if se & EFFECTFUL_SIDE_EFFECTS:
        return "effectful"
    if se & MUTATING_SIDE_EFFECTS:
        return "mutating"
    if op in MUTATING_VERBS:
        return "mutating"
    return "read_only"


def derive_scope(group: str, entrypoint: str, args: List[Dict[str, Any]]) -> str:
    has_ws_arg = False
    for a in args or []:
        if not isinstance(a, dict):
            continue
        nm = str(a.get("name", ""))
        fg = str(a.get("flag", ""))
        if nm == "ws" or fg == "--ws":
            has_ws_arg = True
            break
    if has_ws_arg:
        return "workspace"
    if entrypoint == "ws":
        return "workspace"
    if group in {"kernel", "engine", "mind", "governance", "bundle", "inspect"}:
        return "workspace"
    if group in {"lifecycle", "boot", "root", "control"}:
        return "runtime"
    return "global"


def derive_stability(surface: str, entrypoint: str, op: str) -> str:
    if entrypoint in {"help", "version"}:
        return "stable"
    if surface == "plumbing":
        return "planned"
    if op in {"ping", "status", "list", "current", "use", "clear", "create", "destroy", "up", "down", "restart"}:
        return "stable"
    return "experimental"


def derive_impl_status(stability: str) -> str:
    if stability == "stable":
        return "implemented"
    if stability == "experimental":
        return "stubbed"
    if stability == "deprecated":
        return "nyi"
    return "planned"


def classify_command(c: Dict[str, Any]) -> Dict[str, Any]:
    group = str(c.get("group", ""))
    name = str(c.get("name", ""))
    args = c.get("args", []) if isinstance(c.get("args", []), list) else []
    side_effects = c.get("side_effects", []) if isinstance(c.get("side_effects", []), list) else []
    law_boundaries = c.get("law_boundaries", []) if isinstance(c.get("law_boundaries", []), list) else []

    entrypoint = map_entrypoint(group, name)
    topic, op = split_topic_op(group, name, entrypoint)
    canonical_path = " ".join([x for x in [entrypoint, topic, op] if x]).strip()
    domain = DOMAIN_BY_ENTRYPOINT.get(entrypoint, "internal")
    layer = boundary_to_layer(law_boundaries, group)
    surface = derive_surface(group, entrypoint)
    effect_class = derive_effect_class(side_effects, op)
    command_scope = derive_scope(group, entrypoint, args)
    visibility = {"surface": "public", "ancillary": "advanced", "plumbing": "internal"}[surface]
    authority_class = "policy_gated" if effect_class == "effectful" else ("operator" if effect_class == "mutating" else "none")
    stability = derive_stability(surface, entrypoint, op)
    if c.get("deprecated", False):
        stability = "deprecated"
    implementation_status = derive_impl_status(stability)

    hidden = bool(c.get("hidden", False))
    if visibility == "public":
        hidden = False
    if hidden:
        visibility = "hidden"

    c["surface"] = surface
    c["stability"] = stability
    c["entrypoint"] = entrypoint
    c["topic"] = topic
    c["op"] = op
    c["domain"] = domain
    c["layer"] = layer
    c["canonical_path"] = canonical_path

    c["command_scope"] = command_scope
    c["effect_class"] = effect_class
    c["visibility"] = visibility
    c["authority_class"] = authority_class
    c["implementation_status"] = implementation_status

    c["requires_workspace"] = command_scope == "workspace"
    c["requires_runtime"] = command_scope in {"workspace", "runtime"} or effect_class == "effectful"
    c["requires_authority"] = authority_class != "none"
    c["hidden"] = hidden

    if c.get("deprecated", False):
        if not c.get("deprecated_by") and c.get("replaced_by"):
            c["deprecated_by"] = c["replaced_by"]

    return c


def render_counter(title: str, ctr: Counter) -> str:
    lines = [f"## {title}"]
    for k in sorted(ctr):
        lines.append(f"- `{k}`: {ctr[k]}")
    lines.append("")
    return "\n".join(lines)


def build_report(commands: List[Dict[str, Any]]) -> str:
    by_surface = Counter()
    by_stability = Counter()
    by_scope = Counter()
    by_effect = Counter()
    by_visibility = Counter()
    by_authority = Counter()
    by_impl = Counter()
    path_map: Dict[str, List[str]] = defaultdict(list)

    for c in commands:
        by_surface[c["surface"]] += 1
        by_stability[c["stability"]] += 1
        by_scope[c["command_scope"]] += 1
        by_effect[c["effect_class"]] += 1
        by_visibility[c["visibility"]] += 1
        by_authority[c["authority_class"]] += 1
        by_impl[c["implementation_status"]] += 1
        path_map[c["canonical_path"]].append(c["id"])

    collisions = {p: ids for p, ids in path_map.items() if len(ids) > 1}
    lines = [
        "# Command Architecture Report v1",
        "",
        f"- commands_total: {len(commands)}",
        f"- canonical_path_collisions: {len(collisions)}",
        "",
        render_counter("Surface", by_surface),
        render_counter("Stability", by_stability),
        render_counter("Scope", by_scope),
        render_counter("Effect Class", by_effect),
        render_counter("Visibility", by_visibility),
        render_counter("Authority Class", by_authority),
        render_counter("Implementation Status", by_impl),
        "## Collisions",
    ]
    if not collisions:
        lines.append("- none")
    else:
        for path in sorted(collisions):
            lines.append(f"- `{path}` -> {', '.join(collisions[path])}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    data = load_json(COMMANDS_PATH)
    cmds = data.get("commands", [])
    if not isinstance(cmds, list):
        raise SystemExit("commands.v1.json: commands must be a list")

    normalized = [classify_command(dict(c)) for c in cmds if isinstance(c, dict)]
    data["commands"] = normalized
    write_json(COMMANDS_PATH, data)

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(build_report(normalized), encoding="utf-8")
    print(f"[arch] wrote {COMMANDS_PATH}")
    print(f"[arch] wrote {REPORT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
