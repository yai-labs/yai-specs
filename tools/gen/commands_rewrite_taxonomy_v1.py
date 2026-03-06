#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[2]
COMMANDS_PATH = ROOT / "registry" / "commands.v1.json"
SURFACE_PATH = ROOT / "registry" / "commands.surface.v1.json"
TOPICS_PATH = ROOT / "registry" / "commands.topics.v1.json"
REPORT_PATH = ROOT / "tools" / "out" / "taxonomy_report.md"
REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

ENTRYPOINT_ORDER = {
    "ws": 1,
    "run": 2,
    "gov": 3,
    "verify": 4,
    "inspect": 5,
    "bundle": 6,
    "config": 7,
    "doctor": 8,
    "watch": 9,
    "help": 10,
    "version": 11,
}

# Deterministic small user surface (operator-facing)
USER_STABLE_IDS = {
    "yai.lifecycle.up",
    "yai.lifecycle.down",
    "yai.lifecycle.restart",
    "yai.root.ping",
    "yai.kernel.ping",
    "yai.kernel.ws",
    "yai.kernel.ws_status",
    "yai.kernel.ws_list",
    "yai.root.handshake_status",
    "yai.root.router_status",
    "yai.root.session_status",
    "yai.root.authority_status",
    "yai.root.envelope_validate",
    "yai.boot.status",
    "yai.boot.runtime_status",
    "yai.boot.health_status",
    "yai.boot.service_status",
    "yai.boot.node_status",
}

USER_ENTRYPOINTS = {"ws", "run", "gov", "verify", "inspect", "bundle", "config", "doctor", "watch", "help", "version"}
RUNTIME_GROUPS = {"boot", "root", "kernel", "engine", "mind", "substrate", "orch", "lifecycle", "memory", "control"}


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, obj: Dict[str, Any]) -> None:
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def layer_from_boundaries(cmd: Dict[str, Any], group: str) -> str:
    boundaries = cmd.get("law_boundaries") or []
    if isinstance(boundaries, list):
        if any(str(b).startswith("L3") for b in boundaries):
            return "mind"
        if any(str(b).startswith("L2") for b in boundaries):
            return "engine"
        if any(str(b).startswith("L1") for b in boundaries):
            return "kernel"
        if any(str(b).startswith("Lx-docs") for b in boundaries):
            return "docs"
    m = {
        "boot": "boot", "root": "root", "kernel": "kernel", "engine": "engine", "mind": "mind",
        "memory": "mind", "substrate": "substrate", "orch": "orch", "lifecycle": "root",
        "governance": "kernel", "verify": "kernel", "bundle": "kernel", "inspect": "kernel", "control": "root",
    }
    return m.get(group, "root")


def domain_from_group(cmd: Dict[str, Any], group: str, name: str) -> str:
    lower = name.lower()
    if group == "governance":
        return "governance"
    if group == "bundle":
        return "bundle"
    if group == "inspect":
        return "inspection"
    if group == "verify":
        return "verification"
    if group == "lifecycle":
        return "runtime"
    if "policy" in lower or group == "policy":
        return "policy"
    if group == "kernel" and (lower.startswith("ws") or lower.startswith("workspace")):
        return "workspace"
    if group in RUNTIME_GROUPS:
        return "runtime"
    if group in {"doctor", "diagnostics"}:
        return "diagnostics"
    if "rpc_call" in set(cmd.get("side_effects") or []):
        return "runtime"
    return "dev"


def entrypoint_from_domain(domain: str, group: str, name: str) -> str:
    if domain == "workspace":
        return "ws"
    if domain == "governance":
        return "gov"
    if domain == "policy":
        return "config"
    if domain == "bundle":
        return "bundle"
    if domain == "inspection":
        return "inspect"
    if domain == "verification":
        return "verify"
    if domain == "diagnostics":
        return "doctor"
    if group == "lifecycle":
        return "run"
    if name in {"help", "version"}:
        return name
    if domain == "runtime":
        return "run"
    return "config"


def split_topic_op(name: str) -> Tuple[str, str]:
    tokens = [t for t in name.split("_") if t]
    if not tokens:
        return "command", "run"
    if len(tokens) == 1:
        return "general", tokens[0]
    return tokens[0], "_".join(tokens[1:])


def surface_from_cmd(cmd_id: str, group: str, entrypoint: str) -> str:
    if cmd_id in USER_STABLE_IDS:
        return "user"
    if entrypoint in {"doctor", "verify", "inspect", "bundle", "watch", "config"} and group not in RUNTIME_GROUPS:
        return "tool"
    if group in {"verify", "inspect", "bundle"}:
        return "tool"
    if group in RUNTIME_GROUPS:
        return "internal"
    return "tool"


def stability_from_cmd(cmd_id: str, surface: str) -> str:
    if cmd_id in USER_STABLE_IDS:
        return "stable"
    if surface == "user":
        return "beta"
    return "experimental"


def canonical_tokens(entrypoint: str, topic: str, op: str) -> List[str]:
    return [entrypoint, topic, op]


def classify(cmd: Dict[str, Any]) -> Dict[str, Any]:
    cmd_id = str(cmd.get("id", ""))
    group = str(cmd.get("group", "dev"))
    name = str(cmd.get("name", "op"))
    domain = domain_from_group(cmd, group, name)
    layer = layer_from_boundaries(cmd, group)
    entrypoint = entrypoint_from_domain(domain, group, name)
    topic, op = split_topic_op(name)

    # Runtime internals become run/<group>/<op-like> for discoverability without top-level clutter
    if group in RUNTIME_GROUPS:
        topic = group
        op = name

    tokens = canonical_tokens(entrypoint, topic, op)
    canonical_path = " ".join(tokens)

    surface = surface_from_cmd(cmd_id, group, entrypoint)
    stability = stability_from_cmd(cmd_id, surface)

    aliases = list(cmd.get("aliases") or [])
    aliases.append(f"{group}-{name}")

    cmd["domain"] = domain
    cmd["layer"] = layer
    cmd["entrypoint"] = entrypoint
    cmd["topic"] = topic
    cmd["op"] = op
    cmd["surface"] = surface
    cmd["stability"] = stability
    cmd["help_order"] = ENTRYPOINT_ORDER.get(entrypoint, 99)
    cmd["command_path_tokens"] = tokens
    cmd["canonical_path"] = canonical_path
    cmd["aliases"] = sorted(set(a for a in aliases if isinstance(a, str) and a))
    return cmd


def build_topics(commands: List[Dict[str, Any]]) -> Dict[str, Any]:
    tree: Dict[str, Dict[str, List[str]]] = defaultdict(lambda: defaultdict(list))
    for c in commands:
        toks = c.get("command_path_tokens") or []
        if not isinstance(toks, list) or len(toks) < 3:
            continue
        ep, topic, op = toks[0], toks[1], toks[2]
        if op not in tree[ep][topic]:
            tree[ep][topic].append(op)

    out = {"version": "1.0", "topics": []}
    for ep in sorted(tree.keys(), key=lambda x: ENTRYPOINT_ORDER.get(x, 999)):
        topics = []
        for topic in sorted(tree[ep].keys()):
            topics.append({"topic": topic, "ops": sorted(tree[ep][topic])})
        out["topics"].append({"entrypoint": ep, "topics": topics})
    return out


def write_report(commands: List[Dict[str, Any]]) -> None:
    by_surface = defaultdict(int)
    by_domain = defaultdict(int)
    by_layer = defaultdict(int)
    by_stability = defaultdict(int)
    surface_eps = set()
    fallback = []
    for c in commands:
        by_surface[c["surface"]] += 1
        by_domain[c["domain"]] += 1
        by_layer[c["layer"]] += 1
        by_stability[c["stability"]] += 1
        if c["surface"] == "user":
            surface_eps.add(c["entrypoint"])
        if c["domain"] == "dev" and c["surface"] == "internal":
            fallback.append(c["id"])

    lines = [
        "# Command Taxonomy Report v1",
        "",
        f"- total_commands: {len(commands)}",
        f"- surface_entrypoints: {len(surface_eps)}",
        "",
        "## By Surface",
    ]
    for k in sorted(by_surface):
        lines.append(f"- {k}: {by_surface[k]}")
    lines += ["", "## By Domain"]
    for k in sorted(by_domain):
        lines.append(f"- {k}: {by_domain[k]}")
    lines += ["", "## By Layer"]
    for k in sorted(by_layer):
        lines.append(f"- {k}: {by_layer[k]}")
    lines += ["", "## By Stability"]
    for k in sorted(by_stability):
        lines.append(f"- {k}: {by_stability[k]}")
    lines += ["", "## Fallback (dev/internal)", f"- count: {len(fallback)}"]
    lines += [f"- {cid}" for cid in fallback[:50]]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    data = load_json(COMMANDS_PATH)
    commands = data.get("commands", [])
    if not isinstance(commands, list):
        raise SystemExit("commands.v1.json: commands must be array")

    out_cmds = [classify(dict(c)) for c in commands if isinstance(c, dict)]
    out_cmds.sort(key=lambda c: c.get("id", ""))
    data["commands"] = out_cmds
    dump_json(COMMANDS_PATH, data)

    surface = {
        "version": data.get("version", "1.0"),
        "binary": data.get("binary", "yai"),
        "commands": [c for c in out_cmds if c.get("surface") == "user"],
    }
    dump_json(SURFACE_PATH, surface)
    dump_json(TOPICS_PATH, build_topics(out_cmds))
    write_report(out_cmds)
    print("taxonomy rewrite completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
