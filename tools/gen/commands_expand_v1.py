#!/usr/bin/env python3
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CMDS = ROOT / "registry" / "commands.v1.json"
PRIMS = ROOT / "registry" / "primitives.v1.json"
PRIMS_SCHEMA = ROOT / "registry" / "schema" / "primitives.v1.schema.json"
REGISTRY_MD = ROOT / "REGISTRY.md"
SPEC_MAP_MD = ROOT / "SPEC_MAP.md"
CLI_README = ROOT / "contracts" / "cli" / "README.md"

GROUPS = [
    "boot", "bundle", "control", "engine", "governance", "inspect", "kernel",
    "lifecycle", "memory", "mind", "orch", "root", "substrate", "verify",
]
TARGET_PER_GROUP = 200

GROUP_META = {
    "boot": {
        "objects": ["runtime", "probe", "health", "deps", "profile", "cache", "service", "node", "artifact", "overlay"],
        "ops": ["status", "prepare", "verify", "warmup", "reload", "check", "report", "snapshot", "resume", "audit", "trace", "sync", "refresh", "reconcile", "guard", "index", "bootstrap", "inspect", "seal", "unseal"],
        "args": [
            {"name": "ws", "flag": "--ws", "type": "string", "required": False},
            {"name": "profile", "flag": "--profile", "type": "string", "required": False},
            {"name": "timeout_ms", "flag": "--timeout-ms", "type": "int", "required": False},
        ],
        "outputs": ["json", "text"],
        "side_effects": ["read_files", "rpc_call"],
        "law_hooks": ["I-001", "I-002", "Lx"],
        "law_invariants": ["I-001-traceability", "I-002-determinism"],
        "law_boundaries": ["Lx-docs"],
        "uses": ["S-016", "S-017", "T-012"],
    },
    "bundle": {
        "objects": ["manifest", "payload", "index", "release", "signature", "proof", "channel", "target", "package", "policy"],
        "ops": ["build", "seal", "verify", "publish", "import", "export", "lint", "inspect", "repack", "attach", "detach", "merge", "split", "promote", "rollback", "sync", "digest", "stamp", "audit", "trace"],
        "args": [
            {"name": "ws", "flag": "--ws", "type": "string", "required": False},
            {"name": "bundle_ref", "flag": "--bundle", "type": "string", "required": False},
            {"name": "dry_run", "flag": "--dry-run", "type": "bool", "required": False, "default": False},
        ],
        "outputs": ["json"],
        "side_effects": ["read_files", "write_files", "rpc_call"],
        "law_hooks": ["I-001", "I-002", "I-003"],
        "law_invariants": ["I-001-traceability", "I-002-determinism", "I-003-governance"],
        "law_boundaries": ["L1-kernel", "L2-engine"],
        "uses": ["O-006", "S-005", "S-011", "T-012"],
    },
    "control": {
        "objects": ["session", "route", "provider", "chat", "shell", "policy", "target", "dispatch", "authority", "context"],
        "ops": ["call", "open", "close", "list", "get", "set", "apply", "validate", "bind", "rebind", "check", "status", "sync", "rotate", "audit", "trace", "forward", "relay", "gate", "authorize"],
        "args": [
            {"name": "target_plane", "flag": "--target", "type": "enum", "values": ["kernel", "engine", "root"], "required": False},
            {"name": "ws", "flag": "--ws", "type": "string", "required": False},
            {"name": "role", "flag": "--role", "type": "enum", "values": ["operator", "system"], "required": False},
        ],
        "outputs": ["json"],
        "side_effects": ["rpc_call"],
        "law_hooks": ["I-001", "I-002", "I-003", "L1", "L2"],
        "law_invariants": ["I-001-traceability", "I-002-determinism", "I-003-governance"],
        "law_boundaries": ["L1-kernel", "L2-engine"],
        "uses": ["T-003", "T-007", "S-016", "S-002"],
    },
    "engine": {
        "objects": ["job", "queue", "worker", "pipeline", "state", "session", "checkpoint", "plan", "metric", "policy"],
        "ops": ["ping", "status", "start", "stop", "pause", "resume", "list", "inspect", "verify", "reconcile", "scale", "drain", "heal", "trace", "audit", "sync", "refresh", "guard", "assign", "unassign"],
        "args": [
            {"name": "ws", "flag": "--ws", "type": "string", "required": False},
            {"name": "job_id", "flag": "--job", "type": "string", "required": False},
            {"name": "timeout_ms", "flag": "--timeout-ms", "type": "int", "required": False},
        ],
        "outputs": ["json", "text"],
        "side_effects": ["rpc_call"],
        "law_hooks": ["I-001", "I-002", "L2"],
        "law_invariants": ["I-001-traceability", "I-002-determinism"],
        "law_boundaries": ["L2-engine"],
        "uses": ["S-016", "S-012", "T-003"],
    },
    "governance": {
        "objects": ["claim", "assertion", "controlset", "exception", "scope", "policy", "decision", "evidence", "baseline", "gate"],
        "ops": ["claim", "assert", "controls", "exception", "scope", "review", "approve", "deny", "waive", "trace", "audit", "validate", "lock", "unlock", "compare", "reconcile", "publish", "attest", "report", "status"],
        "args": [
            {"name": "ws", "flag": "--ws", "type": "string", "required": False},
            {"name": "claim_id", "flag": "--claim", "type": "string", "required": False},
            {"name": "strict", "flag": "--strict", "type": "bool", "required": False, "default": False},
        ],
        "outputs": ["json"],
        "side_effects": ["read_files", "rpc_call"],
        "law_hooks": ["I-001", "I-002", "I-003"],
        "law_invariants": ["I-001-traceability", "I-002-determinism", "I-003-governance"],
        "law_boundaries": ["L1-kernel", "L2-engine"],
        "uses": ["T-016", "T-017", "T-018", "T-020"],
    },
    "inspect": {
        "objects": ["status", "logs", "events", "trace", "metrics", "health", "sessions", "routes", "jobs", "alerts"],
        "ops": ["status", "logs", "tail", "query", "watch", "snapshot", "stream", "filter", "summarize", "diff", "compare", "export", "validate", "audit", "trace", "monitor", "sync", "index", "report", "verify"],
        "args": [
            {"name": "ws", "flag": "--ws", "type": "string", "required": False},
            {"name": "limit", "flag": "--limit", "type": "int", "required": False},
            {"name": "follow", "flag": "--follow", "type": "bool", "required": False, "default": False},
        ],
        "outputs": ["json", "text"],
        "side_effects": ["read_files", "rpc_call"],
        "law_hooks": ["I-001", "I-002"],
        "law_invariants": ["I-001-traceability", "I-002-determinism"],
        "law_boundaries": ["L1-kernel", "L2-engine", "L3-mind"],
        "uses": ["S-016", "S-017", "T-012"],
    },
    "kernel": {
        "objects": ["ws", "session", "resource", "quota", "mount", "policy", "boundary", "route", "enforce", "audit"],
        "ops": ["ping", "create", "reset", "destroy", "list", "status", "apply", "validate", "enforce", "reconcile", "attach", "detach", "freeze", "thaw", "snapshot", "restore", "trace", "guard", "permit", "deny"],
        "args": [
            {"name": "ws", "flag": "--ws", "type": "string", "required": False},
            {"name": "action", "flag": "--action", "type": "string", "required": False},
            {"name": "arming", "flag": "--arming", "type": "bool", "required": False, "default": False},
        ],
        "outputs": ["json"],
        "side_effects": ["rpc_call", "write_session"],
        "law_hooks": ["I-001", "I-002", "I-003", "I-006", "L1"],
        "law_invariants": ["I-001-traceability", "I-002-determinism", "I-003-governance", "I-006-external-effect-boundary"],
        "law_boundaries": ["L1-kernel"],
        "uses": ["T-003", "T-007", "S-005", "S-023", "T-012"],
    },
    "lifecycle": {
        "objects": ["stack", "workspace", "engine", "mind", "runtime", "session", "service", "daemon", "plane", "profile"],
        "ops": ["up", "down", "restart", "status", "reload", "drain", "heal", "reconcile", "prepare", "cleanup", "migrate", "resume", "pause", "bootstrap", "shutdown", "verify", "trace", "audit", "sync", "roll"],
        "args": [
            {"name": "ws", "flag": "--ws", "type": "string", "required": False},
            {"name": "force", "flag": "--force", "type": "bool", "required": False, "default": False},
            {"name": "timeout_ms", "flag": "--timeout-ms", "type": "int", "required": False},
        ],
        "outputs": ["json", "text"],
        "side_effects": ["spawn_processes", "signal_processes", "rpc_call"],
        "law_hooks": ["I-001", "I-002", "I-006", "L1", "L2", "L3"],
        "law_invariants": ["I-001-traceability", "I-002-determinism", "I-006-external-effect-boundary"],
        "law_boundaries": ["L1-kernel", "L2-engine", "L3-mind"],
        "uses": ["O-004", "O-005", "S-016", "S-023", "S-026", "T-012"],
    },
    "memory": {
        "objects": ["graph", "embed", "index", "vector", "node", "edge", "context", "session", "archive", "snapshot"],
        "ops": ["graph", "embed", "index", "query", "attach", "detach", "link", "unlink", "trace", "audit", "status", "verify", "repair", "compact", "reload", "sync", "checkpoint", "restore", "tag", "prune"],
        "args": [
            {"name": "ws", "flag": "--ws", "type": "string", "required": False},
            {"name": "key", "flag": "--key", "type": "string", "required": False},
            {"name": "limit", "flag": "--limit", "type": "int", "required": False},
        ],
        "outputs": ["json"],
        "side_effects": ["rpc_call", "read_files"],
        "law_hooks": ["I-001", "I-002", "L3"],
        "law_invariants": ["I-001-traceability", "I-002-determinism"],
        "law_boundaries": ["L3-mind"],
        "uses": ["S-006", "S-016", "T-012"],
    },
    "mind": {
        "objects": ["agent", "planner", "memory", "session", "intent", "proposal", "prompt", "state", "model", "context"],
        "ops": ["ping", "status", "propose", "plan", "summarize", "classify", "embed", "retrieve", "trace", "audit", "verify", "checkpoint", "restore", "sync", "refresh", "explain", "inspect", "route", "queue", "flush"],
        "args": [
            {"name": "ws", "flag": "--ws", "type": "string", "required": False},
            {"name": "session_id", "flag": "--session", "type": "string", "required": False},
            {"name": "timeout_ms", "flag": "--timeout-ms", "type": "int", "required": False},
        ],
        "outputs": ["json"],
        "side_effects": ["rpc_call"],
        "law_hooks": ["I-001", "L3"],
        "law_invariants": ["I-001-traceability"],
        "law_boundaries": ["L3-mind"],
        "uses": ["S-016", "S-006", "T-003"],
    },
    "orch": {
        "objects": ["trial", "runner", "report", "job", "queue", "plan", "pack", "dataset", "result", "campaign"],
        "ops": ["run", "report", "plan", "queue", "cancel", "resume", "status", "verify", "audit", "trace", "list", "export", "import", "merge", "split", "sync", "promote", "rollback", "gate", "dispatch"],
        "args": [
            {"name": "ws", "flag": "--ws", "type": "string", "required": False},
            {"name": "trial_id", "flag": "--trial", "type": "string", "required": False},
            {"name": "json", "flag": "--json", "type": "bool", "required": False, "default": False},
        ],
        "outputs": ["json"],
        "side_effects": ["rpc_call", "read_files"],
        "law_hooks": ["I-001", "I-002", "I-003"],
        "law_invariants": ["I-001-traceability", "I-002-determinism", "I-003-governance"],
        "law_boundaries": ["L2-engine"],
        "uses": ["O-005", "T-022", "S-017", "T-012"],
    },
    "root": {
        "objects": ["router", "handshake", "session", "context", "authority", "relay", "plane", "channel", "envelope", "trace"],
        "ops": ["ping", "status", "route", "relay", "forward", "validate", "authorize", "attach", "detach", "sync", "inspect", "audit", "trace", "rotate", "refresh", "reconcile", "checkpoint", "recover", "guard", "gate"],
        "args": [
            {"name": "ws", "flag": "--ws", "type": "string", "required": False},
            {"name": "role", "flag": "--role", "type": "enum", "values": ["operator", "system"], "required": False},
            {"name": "arming", "flag": "--arming", "type": "bool", "required": False, "default": False},
        ],
        "outputs": ["json", "text"],
        "side_effects": ["rpc_call"],
        "law_hooks": ["I-001", "I-002", "I-003", "L1", "L2", "L3"],
        "law_invariants": ["I-001-traceability", "I-002-determinism", "I-003-governance"],
        "law_boundaries": ["L1-kernel", "L2-engine", "L3-mind"],
        "uses": ["T-003", "T-007", "S-016", "S-002"],
    },
    "substrate": {
        "objects": ["ns", "ref", "key", "hash", "artifact", "store", "schema", "record", "timeline", "manifest"],
        "ops": ["declare", "resolve", "verify", "inspect", "list", "index", "compose", "validate", "attach", "detach", "seal", "unseal", "export", "import", "snapshot", "restore", "trace", "audit", "gc", "compact"],
        "args": [
            {"name": "ws", "flag": "--ws", "type": "string", "required": False},
            {"name": "ref", "flag": "--ref", "type": "string", "required": False},
            {"name": "limit", "flag": "--limit", "type": "int", "required": False},
        ],
        "outputs": ["json"],
        "side_effects": ["read_files", "write_files"],
        "law_hooks": ["I-001", "I-002"],
        "law_invariants": ["I-001-traceability", "I-002-determinism"],
        "law_boundaries": ["Lx-docs"],
        "uses": ["S-001", "S-002", "S-005", "S-006", "S-007", "S-008"],
    },
    "verify": {
        "objects": ["suite", "proof", "report", "gate", "vector", "trace", "bundle", "policy", "evidence", "check"],
        "ops": ["verify", "test", "replay", "check", "validate", "audit", "trace", "status", "compare", "diff", "report", "export", "import", "seal", "attest", "summarize", "index", "sync", "reconcile", "lint"],
        "args": [
            {"name": "ws", "flag": "--ws", "type": "string", "required": False},
            {"name": "strict", "flag": "--strict", "type": "bool", "required": False, "default": False},
            {"name": "json", "flag": "--json", "type": "bool", "required": False, "default": False},
        ],
        "outputs": ["json"],
        "side_effects": ["read_files", "rpc_call"],
        "law_hooks": ["I-001", "I-002", "I-003"],
        "law_invariants": ["I-001-traceability", "I-002-determinism", "I-003-governance"],
        "law_boundaries": ["L1-kernel", "L2-engine", "L3-mind"],
        "uses": ["O-007", "S-017", "T-012"],
    },
}

MISSING_PRIMITIVES = {
    "O-006": {"layer": 2, "family": "Orchestration", "domain": "Bundles", "name": "Bundle Assemble", "definition": "Assemble bundle payloads and manifests for governed delivery.", "ops": ["compose", "validate", "emit"], "depends_on": ["S-005", "S-011", "T-012"], "determinism": "deterministic", "failure_modes": ["E_BUNDLE_COMPOSE", "E_BUNDLE_VALIDATE"], "cli": {"canonical_id": "yai.bundle.bundle", "group": "bundle", "name": "bundle", "alias": "bundle-bundle"}},
    "O-007": {"layer": 2, "family": "Orchestration", "domain": "Verification", "name": "Verification Run", "definition": "Execute deterministic verification workflow and emit evidence pointers.", "ops": ["run", "report", "seal"], "depends_on": ["T-012", "S-014", "S-017"], "determinism": "deterministic", "failure_modes": ["E_VERIFY_FAIL", "E_VERIFY_INCOMPLETE"], "cli": {"canonical_id": "yai.verify.verify", "group": "verify", "name": "verify", "alias": "verify-verify"}},
    "T-016": {"layer": 1, "family": "Control", "domain": "Governance", "name": "Claim Registry", "definition": "Claim registry resolution for governance assertions and review.", "ops": ["resolve", "list", "bind"], "depends_on": ["S-007", "S-014"], "determinism": "deterministic", "failure_modes": ["E_CLAIM_UNKNOWN", "E_CLAIM_BIND"], "cli": {"canonical_id": "yai.governance.claim", "group": "governance", "name": "claim", "alias": "governance-claim"}},
    "T-017": {"layer": 1, "family": "Control", "domain": "Governance", "name": "Assertion Engine", "definition": "Evaluate governance assertions with deterministic reason codes.", "ops": ["assert", "explain", "diff"], "depends_on": ["T-016", "S-014"], "determinism": "deterministic", "failure_modes": ["E_ASSERT_FAIL", "E_ASSERT_INVALID"], "cli": {"canonical_id": "yai.governance.assert", "group": "governance", "name": "assert", "alias": "governance-assert"}},
    "T-018": {"layer": 1, "family": "Control", "domain": "Governance", "name": "Control Set", "definition": "Resolve and apply governance control sets for runtime decisions.", "ops": ["resolve", "apply", "audit"], "depends_on": ["T-016", "S-013"], "determinism": "deterministic", "failure_modes": ["E_CONTROLSET_MISSING", "E_CONTROLSET_INVALID"], "cli": {"canonical_id": "yai.governance.controls", "group": "governance", "name": "controls", "alias": "governance-controls"}},
    "T-020": {"layer": 1, "family": "Control", "domain": "Governance", "name": "Exception Handling", "definition": "Governed exception request and reconciliation lifecycle.", "ops": ["request", "review", "close"], "depends_on": ["T-016", "S-017"], "determinism": "deterministic", "failure_modes": ["E_EXCEPTION_DENIED", "E_EXCEPTION_INVALID"], "cli": {"canonical_id": "yai.governance.exception", "group": "governance", "name": "exception", "alias": "governance-exception"}},
    "T-022": {"layer": 1, "family": "Control", "domain": "Reporting", "name": "Report Emit", "definition": "Deterministic report emission and artifact linking.", "ops": ["build", "emit", "publish"], "depends_on": ["S-005", "S-011", "S-017"], "determinism": "deterministic", "failure_modes": ["E_REPORT_EMIT", "E_REPORT_SCHEMA"], "cli": {"canonical_id": "yai.orch.report", "group": "orch", "name": "report", "alias": "orch-report"}},
}


def load(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def dump(p: Path, obj):
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def is_old_generated(c: dict) -> bool:
    cid = str(c.get("id", ""))
    summary = str(c.get("summary", ""))
    return (
        bool(re.match(r"^yai\.[a-z0-9_\-]+\.op\d{3}$", cid))
        or "registry-scale coverage" in summary.lower()
        or summary.startswith("Autogenerated ")
    )


def make_name(group: str, obj: str, op: str, suffix: int | None = None) -> str:
    base = f"{obj}_{op}"
    if suffix is None:
        return base
    return f"{base}_{suffix:03d}"


def expand_commands():
    data = load(CMDS)
    cmds = [c for c in data.get("commands", []) if not is_old_generated(c)]

    existing_ids = {c.get("id") for c in cmds if isinstance(c, dict)}
    existing_names = {g: {c.get("name") for c in cmds if c.get("group") == g} for g in GROUPS}

    by_group = {g: [c for c in cmds if c.get("group") == g] for g in GROUPS}

    generated = []
    for group in GROUPS:
      meta = GROUP_META[group]
      objects = meta["objects"]
      ops = meta["ops"]
      pool = [(o, op) for o in objects for op in ops]
      idx_pool = 0
      seq = 1
      while len(by_group[group]) + len([x for x in generated if x["group"] == group]) < TARGET_PER_GROUP:
          obj, op = pool[idx_pool % len(pool)]
          idx_pool += 1
          name = make_name(group, obj, op)
          if name in existing_names[group]:
              name = make_name(group, obj, op, seq)
              seq += 1
          cid = f"yai.{group}.{name}"
          if cid in existing_ids:
              name = make_name(group, obj, op, seq)
              seq += 1
              cid = f"yai.{group}.{name}"
          if cid in existing_ids:
              continue

          summary = f"{group} {op} operation on {obj} with deterministic contract and traceable outputs."
          cmd = {
              "id": cid,
              "name": name,
              "group": group,
              "summary": summary,
              "args": meta["args"],
              "outputs": meta["outputs"],
              "side_effects": meta["side_effects"],
              "law_hooks": meta["law_hooks"],
              "law_invariants": meta["law_invariants"],
              "law_boundaries": meta["law_boundaries"],
              "uses_primitives": meta["uses"],
              "emits_artifacts": [],
              "consumes_artifacts": [],
          }
          generated.append(cmd)
          existing_ids.add(cid)
          existing_names[group].add(name)

    cmds.extend(generated)
    cmds.sort(key=lambda c: (c.get("group", ""), c.get("name", ""), c.get("id", "")))
    data["commands"] = cmds
    dump(CMDS, data)


def expand_primitives_and_schema():
    p = load(PRIMS)
    items = p.get("primitives", [])
    have = {x.get("id") for x in items if isinstance(x, dict)}
    for pid, body in MISSING_PRIMITIVES.items():
        if pid in have:
            continue
        e = {"id": pid}
        e.update(body)
        items.append(e)
    items.sort(key=lambda x: x.get("id", ""))
    p["primitives"] = items
    if "rules" not in p:
        p["rules"] = {
            "cli_alias_format": "<group>-<name>",
            "cli_canonical_id_format": "yai.<group>.<name>",
            "notes": ["Primitives define stable capability surfaces and deterministic command mappings."]
        }
    dump(PRIMS, p)

    s = load(PRIMS_SCHEMA)
    sprops = s.setdefault("properties", {})
    sprops.setdefault("generated_from", {"type": "string"})
    sprops.setdefault("rules", {"type": "object", "additionalProperties": True})
    pid = sprops["primitives"]["items"]["properties"]["id"]
    pid["pattern"] = "^(?:[STO]-\\d{3}|R-\\d{3}|CLI-\\d{3})$"
    did = sprops["primitives"]["items"]["properties"]["depends_on"]["items"]
    did["pattern"] = "^(?:[STO]-\\d{3}|R-\\d{3}|CLI-\\d{3})$"
    sprops["primitives"]["items"]["properties"]["layer"]["maximum"] = 3
    sprops["primitives"]["items"]["properties"].setdefault(
        "cli",
        {
            "type": "object",
            "properties": {
                "canonical_id": {"type": "string"},
                "group": {"type": "string"},
                "name": {"type": "string"},
                "alias": {"type": "string"},
                "related": {"type": "array", "items": {"type": "string"}}
            },
            "additionalProperties": True
        }
    )
    dump(PRIMS_SCHEMA, s)


def patch_docs():
    reg_add = "\n## Registry scale\n\nCurrent command registry target is **200 command_id per group** across 14 groups (total 2800 IDs).\nThis profile is a **registry-scale stress and coverage surface**, not a final product taxonomy.\nExpansion is generated via `tools/gen/commands_expand_v1.py` and validated via `make validate-law-registry`.\n"
    spec_add = "\n## 12) Registry scale target\n\nCommand registry is maintained at 14 groups x 200 command_id (2800 total) through generator-driven expansion (`tools/gen/commands_expand_v1.py`).\nThe scale profile is intended to stress CLI/SDK/runtime contract paths while preserving deterministic semantics.\n"
    cli_add = "\n## Registry scale profile\n\nThe CLI contract is expected to remain deterministic with large registries (target: 2800 command_id, 200 per group).\nThis profile validates discoverability and invocation surface under load; it does not replace product curation/taxonomy governance.\nConsumers must support `yai help --all` and `yai help <command_id>` across the full canonical registry.\n"
    for p, marker, content in [
        (REGISTRY_MD, "## Registry scale", reg_add),
        (SPEC_MAP_MD, "## 12) Registry scale target", spec_add),
        (CLI_README, "## Registry scale profile", cli_add),
    ]:
        txt = p.read_text(encoding="utf-8")
        if marker in txt:
            # replace existing section conservatively
            parts = txt.split(marker)
            head = parts[0].rstrip() + "\n"
            p.write_text(head + content.strip() + "\n", encoding="utf-8")
        else:
            p.write_text(txt.rstrip() + "\n" + content + "\n", encoding="utf-8")


def main():
    expand_commands()
    expand_primitives_and_schema()
    patch_docs()


if __name__ == "__main__":
    main()
