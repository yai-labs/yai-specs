#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

if ! command -v rg >/dev/null 2>&1; then
  echo "[lint-docs] FAIL: ripgrep (rg) is required"
  exit 2
fi

fail=0

while IFS= read -r md; do
  dir="$(dirname "$md")"

  while IFS= read -r raw; do
    link="${raw#*\(}"
    link="${link%\)*}"

    # Skip anchors and external links.
    case "$link" in
      ""|\#*|http://*|https://*|mailto:*|tel:*) continue ;;
    esac

    # Remove optional title (markdown allows "path \"title\"").
    link="${link%% *}"
    # Remove angle brackets if present.
    link="${link#<}"
    link="${link%>}"
    # Drop in-file anchor.
    path_part="${link%%#*}"

    case "$path_part" in
      ""|\#*) continue ;;
    esac

    if [[ "$path_part" = /* ]]; then
      target="$ROOT/${path_part#/}"
    else
      target="$dir/$path_part"
    fi

    if [[ ! -e "$target" ]]; then
      echo "[lint-docs] missing link target: $md -> $link"
      fail=1
    fi
  done < <(rg -o '\[[^]]+\]\([^)]+\)' "$md" -N || true)
done < <(rg --files "$ROOT" -g '*.md')

if [[ "$fail" -ne 0 ]]; then
  echo "[lint-docs] FAIL"
  exit 1
fi

echo "[lint-docs] OK"
