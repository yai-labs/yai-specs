#!/usr/bin/env bash
set -euo pipefail

fail() { echo "[lint-normative] FAIL: $*" >&2; exit 1; }

# Hard forbidden legacy roots
FORBIDDEN_REGEX='(^|[^a-zA-Z0-9_])(contracts/|specs/|compliance/packs/|compliance/schema/|formal/bindings/)([^a-zA-Z0-9_]|$)'

# Only lint markdown + top-level docs
FILES=$(git ls-files '*.md')

# 1) No legacy paths
if rg -n "$FORBIDDEN_REGEX" $FILES >/dev/null; then
  echo "[lint-normative] Found forbidden legacy references:"
  rg -n "$FORBIDDEN_REGEX" $FILES || true
  fail "legacy references present"
fi

# 2) Canonical ABI references must appear in normative terminology + invariants (at least once)
REQ_FILES=(
  "foundation/terminology/glossary.md"
)

for f in "${REQ_FILES[@]}"; do
  test -f "$f" || fail "missing required file: $f"
  rg -n "registry/primitives\.v1\.json" "$f" >/dev/null || fail "$f missing primitives registry reference"
  rg -n "registry/commands\.v1\.json" "$f" >/dev/null || fail "$f missing commands registry reference"
  rg -n "registry/artifacts\.v1\.json" "$f" >/dev/null || fail "$f missing artifacts registry reference"
done

echo "[lint-normative] OK"
