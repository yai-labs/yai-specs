#!/usr/bin/env bash
set -euo pipefail

fail() { echo "[lint-normative] FAIL: $*" >&2; exit 1; }

# Truly deprecated roots from old yai-law layout
FORBIDDEN_REGEX='(^|[^a-zA-Z0-9_])(specs/|compliance/packs/|compliance/schema/|formal/bindings/)([^a-zA-Z0-9_]|$)'

FILES=$(git ls-files '*.md' | while read -r f; do [[ -f "$f" ]] && echo "$f"; done)

if rg -n "$FORBIDDEN_REGEX" $FILES >/dev/null; then
  echo "[lint-normative] Found forbidden deprecated references:"
  rg -n "$FORBIDDEN_REGEX" $FILES || true
  fail "deprecated references present"
fi

if rg -n 'runtime/(boot|root)/' $FILES -g '!docs/policy/*.md' >/dev/null; then
  echo "[lint-normative] Found references to removed runtime legacy roots:"
  rg -n 'runtime/(boot|root)/' $FILES -g '!docs/policy/*.md' || true
  fail "references to removed runtime legacy roots present"
fi

for f in README.md FOUNDATION.md SPEC_MAP.md REGISTRY.md; do
  test -f "$f" || fail "missing required file: $f"
  rg -n '\bcore\b' "$f" >/dev/null || fail "$f missing 'core'"
  rg -n '\bexec\b' "$f" >/dev/null || fail "$f missing 'exec'"
  rg -n '\bbrain\b' "$f" >/dev/null || fail "$f missing 'brain'"
done

for f in foundation/terminology/glossary.md; do
  test -f "$f" || fail "missing required file: $f"
  rg -n 'registry/primitives\.v1\.json' "$f" >/dev/null || fail "$f missing primitives registry reference"
  rg -n 'registry/commands\.v1\.json' "$f" >/dev/null || fail "$f missing commands registry reference"
  rg -n 'registry/artifacts\.v1\.json' "$f" >/dev/null || fail "$f missing artifacts registry reference"
done

echo "[lint-normative] OK"
