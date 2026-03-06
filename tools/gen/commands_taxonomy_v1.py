#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
COMMANDS_PATH = REPO_ROOT / "registry" / "commands.v1.json"
SURFACE_OUT_PATH = REPO_ROOT / "registry" / "commands.surface.v1.json"
TOPICS_OUT_PATH = REPO_ROOT / "registry" / "commands.topics.v1.json"
REPORT_PATH = REPO_ROOT / "tools" / "out" / "taxonomy_report.md"

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

DOMAIN_ENUM = {
    "workspace",
    "runtime",
    "governance",
    "policy",
    "bundle",
    "inspection",
    "verification",
    "diagnostics",
    "configuration",
    "help",
    "internal",
}

LAYER_ENUM = {
    "boot",
    "root",
    "kernel",
    "engine",
    "mind",
    "substrate",
    "orch",
    "docs",
}

RUNTIME_GROUPS = {
    "boot",
    "control",
    "engine",
    "kernel",
    "lifecycle",
    "memory",
    "mind",
    "orch",
    "root",
    "substrate",
}

GOV_TOPICS_SURFACE = {
    "decision",
    "evidence",
    "event",
    "effect",
    "disclosure",
    "controlset",
    "policy",
    "claim",
    "scope",
}

INSPECT_TOPICS_SURFACE = {"status", "events", "logs", "monitor"}

WS_OPS_SURFACE = {"create", "destroy", "status", "list", "reset", "open", "select"}
RUN_CORE = {
    ("lifecycle", "up"),
    ("lifecycle", "down"),
    ("lifecycle", "restart"),
    ("root", "ping"),
    ("kernel", "ping"),
    ("engine", "ping"),
    ("mind", "ping"),
    ("boot", "status"),
}

INFORMATIVE_OPS = {
    "status",
    "trace",
    "list",
    "validate",
    "check",
    "health",
    "audit",
    "report",
    "review",
    "scope",
    "lock",
    "unlock",
}


def _split_name(name: str) -> Tuple[str, Optional[str]]:
    if "_" not in name:
        return name, None
    head, tail = name.split("_", 1)
    return head, tail if tail else None


def _normalize_token(value: str) -> str:
    out = []
    for ch in value.lower().strip():
        if ch.isalnum() or ch in {"_", "-"}:
            out.append(ch)
        elif ch in {" ", "/", "."}:
            out.append("-")
    token = "".join(out).strip("-")
    return token or "unknown"


def _layer_from_boundaries(boundaries: List[str]) -> Optional[str]:
    bset = set(boundaries)
    if "L3-mind" in bset:
        return "mind"
    if "L2-engine" in bset:
        return "engine"
    if "L1-kernel" in bset:
        return "kernel"
    if "Lx-docs" in bset:
        return "docs"
    return None


def classify_domain(group: str, cid: str, name: str) -> str:
    gid = cid.lower()
    g = group.lower()
    n = name.lower()

    if g == "governance" or gid.startswith("yai.governance."):
        return "governance"
    if g == "verify" or gid.startswith("yai.verify."):
        return "verification"
    if g == "inspect" or gid.startswith("yai.inspect."):
        return "inspection"
    if g == "bundle" or gid.startswith("yai.bundle."):
        return "bundle"
    if g in {"kernel"} and (n.startswith("ws") or n == "ws"):
        return "workspace"
    if g in {"config"}:
        return "configuration"
    if g in {"doctor", "diagnostics"}:
        return "diagnostics"
    if g in {"help", "version"}:
        return "help"
    if g in RUNTIME_GROUPS:
        return "runtime"
    return "internal"


def classify_layer(group: str, boundaries: List[str], cid: str) -> str:
    inferred = _layer_from_boundaries(boundaries)
    if inferred:
        return inferred

    g = group.lower()
    if g in LAYER_ENUM:
        return g
    if g == "lifecycle":
        return "root"
    if g == "control":
        return "root"
    if g in {"verify", "inspect", "bundle", "governance"}:
        return "docs"

    gid = cid.lower()
    for layer in ("boot", "root", "kernel", "engine", "mind", "substrate", "orch"):
        if f"yai.{layer}." in gid:
            return layer
    return "root"


@dataclass
class PathParts:
    entrypoint: str
    topic: str
    op: Optional[str]


def classify_path(group: str, name: str, domain: str) -> PathParts:
    g = group.lower()
    n = name.lower()

    if g == "kernel" and (n == "ws" or n.startswith("ws_")):
        _, op = _split_name(n)
        if n == "ws":
            return PathParts("ws", "workspace", "open")
        return PathParts("ws", "workspace", _normalize_token(op or "status"))

    if g == "governance":
        topic, op = _split_name(n)
        return PathParts("gov", _normalize_token(topic), _normalize_token(op) if op else None)

    if g == "verify":
        topic, op = _split_name(n)
        return PathParts("verify", _normalize_token(topic), _normalize_token(op) if op else None)

    if g == "inspect":
        topic, op = _split_name(n)
        return PathParts("inspect", _normalize_token(topic), _normalize_token(op) if op else None)

    if g == "bundle":
        topic, op = _split_name(n)
        return PathParts("bundle", _normalize_token(topic), _normalize_token(op) if op else None)

    if g in RUNTIME_GROUPS:
        # Keep runtime planes as topic namespace to avoid cross-plane path collisions.
        return PathParts("run", _normalize_token(g), _normalize_token(n))

    if domain == "workspace":
        topic, op = _split_name(n)
        return PathParts("ws", _normalize_token(topic), _normalize_token(op) if op else None)
    if domain == "configuration":
        topic, op = _split_name(n)
        return PathParts("config", _normalize_token(topic), _normalize_token(op) if op else None)
    if domain == "diagnostics":
        topic, op = _split_name(n)
        return PathParts("doctor", _normalize_token(topic), _normalize_token(op) if op else None)
    if domain == "help":
        if n in {"version"}:
            return PathParts("version", "version", None)
        return PathParts("help", _normalize_token(n), None)

    topic, op = _split_name(n)
    return PathParts("run", _normalize_token(topic), _normalize_token(op) if op else None)


def canonical_path(parts: PathParts) -> str:
    toks = [parts.entrypoint, parts.topic]
    if parts.op:
        toks.append(parts.op)
    return " ".join(toks)


def classify_surface_stability(command: Dict[str, Any], parts: PathParts, domain: str) -> Tuple[str, str]:
    name = command.get("name", "").lower()

    if command.get("deprecated") is True:
        return "plumbing", "deprecated"

    if parts.entrypoint == "ws" and parts.op in WS_OPS_SURFACE:
        return "surface", "stable"

    if parts.entrypoint == "run" and (parts.topic, parts.op) in RUN_CORE:
        return "surface", "stable"

    if parts.entrypoint == "gov" and parts.topic in GOV_TOPICS_SURFACE and parts.op is None:
        return "surface", "stable"

    if parts.entrypoint == "inspect" and parts.topic in INSPECT_TOPICS_SURFACE and parts.op is None:
        return "surface", "stable"

    if parts.entrypoint == "verify" and parts.topic in {"verify", "test"} and parts.op is None:
        return "surface", "stable"

    if parts.entrypoint == "bundle" and parts.topic == "bundle" and parts.op is None:
        return "surface", "stable"

    if domain in {"governance", "inspection", "verification", "bundle", "workspace", "diagnostics", "configuration"}:
        if "_" not in name:
            return "ancillary", "experimental"
        if parts.op in INFORMATIVE_OPS:
            return "ancillary", "experimental"
        return "ancillary", "planned"

    if domain == "runtime":
        if parts.op in {"status", "check", "health", "trace"}:
            return "ancillary", "experimental"
        return "plumbing", "planned"

    if domain == "help":
        return "ancillary", "experimental"

    return "plumbing", "planned"


def ensure_aliases(command: Dict[str, Any], path: str, group: str, name: str) -> List[str]:
    aliases = command.get("aliases", [])
    out: List[str] = []
    if isinstance(aliases, list):
        for a in aliases:
            if isinstance(a, str) and a.strip():
                out.append(a.strip())

    legacy = f"{group} {name}"
    if legacy != path and legacy not in out:
        out.append(legacy)

    seen = set()
    uniq = []
    for a in out:
        if a not in seen:
            uniq.append(a)
            seen.add(a)
    return uniq


def normalize(commands_doc: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    cmds = commands_doc.get("commands", [])
    normalized_commands: List[Dict[str, Any]] = []
    unclassified: List[str] = []

    for cmd in cmds:
        c = dict(cmd)
        cid = str(c.get("id", ""))
        group = str(c.get("group", ""))
        name = str(c.get("name", ""))
        boundaries = c.get("law_boundaries", [])
        if not isinstance(boundaries, list):
            boundaries = []

        domain = classify_domain(group, cid, name)
        layer = classify_layer(group, boundaries, cid)
        parts = classify_path(group, name, domain)
        cpath = canonical_path(parts)
        surface, stability = classify_surface_stability(c, parts, domain)

        if domain not in DOMAIN_ENUM or layer not in LAYER_ENUM:
            unclassified.append(cid)

        c["surface"] = surface
        c["stability"] = stability
        c["entrypoint"] = parts.entrypoint
        c["topic"] = parts.topic
        if parts.op:
            c["op"] = parts.op
        else:
            c.pop("op", None)
        c["domain"] = domain
        c["layer"] = layer
        c["canonical_path"] = cpath
        c["help_order"] = int(c.get("help_order", 1000))
        c["hidden"] = bool(c.get("hidden", False))
        c["aliases"] = ensure_aliases(c, cpath, group, name)

        normalized_commands.append(c)

    normalized_commands.sort(key=lambda x: (x.get("id", ""), x.get("canonical_path", "")))

    doc_out = dict(commands_doc)
    doc_out["commands"] = normalized_commands

    surface_items = [
        {
            "id": c["id"],
            "canonical_path": c["canonical_path"],
            "summary": c.get("summary", ""),
            "entrypoint": c["entrypoint"],
            "topic": c["topic"],
            "op": c.get("op", None),
            "domain": c["domain"],
            "layer": c["layer"],
            "stability": c["stability"],
        }
        for c in normalized_commands
        if c.get("surface") == "surface"
    ]

    surface_doc = {
        "version": doc_out.get("version", "1.0"),
        "source": "registry/commands.v1.json",
        "surface_entrypoints": sorted({c["entrypoint"] for c in surface_items}),
        "commands": surface_items,
    }

    topics: Dict[str, Dict[str, List[Dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    for c in normalized_commands:
        topics[c["entrypoint"]][c["topic"]].append(
            {
                "id": c["id"],
                "op": c.get("op", None),
                "canonical_path": c["canonical_path"],
                "surface": c["surface"],
                "stability": c["stability"],
                "summary": c.get("summary", ""),
            }
        )

    topics_doc = {
        "version": doc_out.get("version", "1.0"),
        "source": "registry/commands.v1.json",
        "entrypoints": {},
    }
    for entry in sorted(topics):
        topics_doc["entrypoints"][entry] = {}
        for topic in sorted(topics[entry]):
            topics_doc["entrypoints"][entry][topic] = sorted(
                topics[entry][topic], key=lambda it: (it["op"] or "", it["id"])
            )

    cnt_surface = Counter(c["surface"] for c in normalized_commands)
    cnt_stability = Counter(c["stability"] for c in normalized_commands)
    cnt_domain = Counter(c["domain"] for c in normalized_commands)
    cnt_layer = Counter(c["layer"] for c in normalized_commands)
    cnt_entry = Counter(c["entrypoint"] for c in normalized_commands if c["surface"] == "surface")

    report = {
        "commands_total": len(normalized_commands),
        "surface_entrypoints": len(cnt_entry),
        "surface_entrypoint_names": sorted(cnt_entry),
        "surface_counts": dict(sorted(cnt_surface.items())),
        "stability_counts": dict(sorted(cnt_stability.items())),
        "domain_counts": dict(sorted(cnt_domain.items())),
        "layer_counts": dict(sorted(cnt_layer.items())),
        "unclassified": sorted(set(unclassified)),
    }

    return doc_out, surface_doc, topics_doc, report


def write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_report(path: Path, report: Dict[str, Any]) -> None:
    lines = [
        "# Command Taxonomy Report v1",
        "",
        f"- commands_total: {report['commands_total']}",
        f"- surface_entrypoints: {report['surface_entrypoints']}",
        f"- surface_entrypoint_names: {', '.join(report['surface_entrypoint_names'])}",
        "",
        "## Surface Counts",
    ]
    lines.extend([f"- {k}: {v}" for k, v in report["surface_counts"].items()])
    lines.extend(["", "## Stability Counts"])
    lines.extend([f"- {k}: {v}" for k, v in report["stability_counts"].items()])
    lines.extend(["", "## Domain Counts"])
    lines.extend([f"- {k}: {v}" for k, v in report["domain_counts"].items()])
    lines.extend(["", "## Layer Counts"])
    lines.extend([f"- {k}: {v}" for k, v in report["layer_counts"].items()])
    lines.extend(["", "## Unclassified"])
    if report["unclassified"]:
        lines.extend([f"- {x}" for x in report["unclassified"]])
    else:
        lines.append("- none")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    doc = json.loads(COMMANDS_PATH.read_text(encoding="utf-8"))
    out, surface_doc, topics_doc, report = normalize(doc)

    write_json(COMMANDS_PATH, out)
    write_json(SURFACE_OUT_PATH, surface_doc)
    write_json(TOPICS_OUT_PATH, topics_doc)
    write_report(REPORT_PATH, report)

    if report["surface_entrypoints"] > 12:
        print(f"[taxonomy] WARN: surface_entrypoints={report['surface_entrypoints']} (target <= 12)")

    print("[taxonomy] OK")
    print(f"[taxonomy] commands_total={report['commands_total']}")
    print(f"[taxonomy] surface_entrypoints={report['surface_entrypoints']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
