#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List

REPO_ROOT = Path(__file__).resolve().parents[2]
TRACE_PATH = REPO_ROOT / "formal" / "traceability.v1.json"
SCHEMA_PATH = REPO_ROOT / "formal" / "schema" / "traceability.v1.schema.json"
LAW_INV_DIR = REPO_ROOT / "law" / "normative" / "invariants"


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def ensure_path_exists(path_str: str, errors: List[str], prefix: str) -> None:
    p = (REPO_ROOT / path_str).resolve()
    if not p.exists():
        errors.append(f"{prefix} path not found: {path_str}")


def validate_schema(instance: Dict[str, Any], schema: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    try:
        from jsonschema import Draft202012Validator
    except Exception as exc:  # pragma: no cover
        return [
            "jsonschema dependency is required (pip install jsonschema)",
            f"import error: {exc}",
        ]

    validator = Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(instance), key=lambda e: e.path):
        where = "$." + ".".join(str(x) for x in err.path) if err.path else "$"
        errors.append(f"schema error at {where}: {err.message}")
    return errors


def validate_traceability(data: Dict[str, Any]) -> List[str]:
    errors: List[str] = []

    repo_version = str(data.get("repo_version", "")).strip()
    version_file = (REPO_ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if repo_version != version_file:
        errors.append(f"repo_version mismatch: traceability={repo_version} VERSION={version_file}")

    invariants = data.get("invariants", [])
    for inv in invariants:
        iid = inv.get("id", "")
        title = inv.get("title", "")
        if not isinstance(iid, str) or not re.match(r"^I-\d{3}-", iid):
            errors.append(f"invalid invariant id: {iid}")
            continue

        inv_prefix = f"{iid}"

        expected_contract = LAW_INV_DIR / f"{iid}.md"
        if not expected_contract.exists():
            errors.append(f"{inv_prefix}: invariant file not found: {rel(expected_contract)}")

        contracts = inv.get("contracts", [])
        specs = inv.get("spec_artifacts", [])
        vectors = inv.get("vectors", [])
        formal = inv.get("formal", [])
        bindings = inv.get("bindings", [])

        for p in contracts:
            ensure_path_exists(str(p), errors, f"{inv_prefix} contract")
        for p in specs:
            ensure_path_exists(str(p), errors, f"{inv_prefix} spec_artifact")
        for p in vectors:
            ensure_path_exists(str(p), errors, f"{inv_prefix} vector")
        for p in bindings:
            ensure_path_exists(str(p), errors, f"{inv_prefix} binding")

        if not (len(specs) > 0 or len(vectors) > 0 or len(formal) > 0):
            errors.append(f"{inv_prefix}: must include at least one of spec_artifacts/vectors/formal")

        for fi in formal:
            module = fi.get("module", "")
            config = fi.get("config", "")
            if module:
                ensure_path_exists(str(module), errors, f"{inv_prefix} formal.module")
            if config:
                ensure_path_exists(str(config), errors, f"{inv_prefix} formal.config")

    return errors


def print_coverage_report(data: Dict[str, Any]) -> None:
    for inv in data.get("invariants", []):
        iid = inv.get("id", "?")
        cov = inv.get("coverage", {})
        docs = 1 if cov.get("docs") else 0
        tests = 1 if cov.get("tests") else 0
        formal_cov = 1 if cov.get("formal") else 0
        bindings = len(inv.get("bindings", []))
        specs = len(inv.get("spec_artifacts", []))
        vectors = len(inv.get("vectors", []))
        print(f"{iid}: docs={docs} tests={tests} formal={formal_cov} (bindings={bindings}, specs={specs}, vectors={vectors})")


def main() -> int:
    if not TRACE_PATH.exists():
        print(f"[formal] ERROR: missing {rel(TRACE_PATH)}")
        return 2
    if not SCHEMA_PATH.exists():
        print(f"[formal] ERROR: missing {rel(SCHEMA_PATH)}")
        return 2

    data = load_json(TRACE_PATH)
    schema = load_json(SCHEMA_PATH)

    errors = []
    errors.extend(validate_schema(data, schema))
    errors.extend(validate_traceability(data))

    if errors:
        print("[formal] FAIL:")
        for e in errors:
            print(f"- {e}")
        return 1

    print("[formal] OK: traceability matrix validated")
    print_coverage_report(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
