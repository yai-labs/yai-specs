# ===============================
# yai-law — Quality Gates (hard mode)
# ===============================

SHELL := /bin/bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c

.PHONY: all ci check lint-layout lint-json lint-docs formal-coverage formal-bindings-check docs docs-clean clean tree

all: check

ci: lint-layout check formal-bindings-check formal-coverage validate-law-registry lint-docs

# --------------------------------
# Hard-mode layout gate
# --------------------------------
lint-layout:
	@echo "[layout] enforcing hard mode (no legacy roots)..."
	@test ! -d contracts
	@test ! -d specs
	@test ! -d compliance
	@echo "[layout] OK"

# --------------------------------
# Basic checks (presence + JSON parse)
# --------------------------------
check: lint-layout lint-json
	@echo "[check] checking required surface files..."
	@test -f law/surfaces/protocol/include/yai_protocol_ids.h
	@test -f law/surfaces/vault/include/yai_vault_abi.h
	@test -f law/surfaces/protocol/runtime/include/rpc_runtime.h
	@echo "[check] OK"

lint-json:
	@echo "[json] validating all *.json parse..."
	@command -v python3 >/dev/null 2>&1 || { echo "[json] python3 not found"; exit 1; }
	@python3 -c 'import json,glob,sys; bad=[]; \
	[bad.append((p,str(e))) for p in glob.glob("**/*.json", recursive=True) \
	 for e in [None] \
	 for _ in [0] \
	 if (lambda path: ( \
	     (lambda: (json.load(open(path,"r",encoding="utf-8")), None)[1])() \
	 ))(p) is not None]; \
	0 if not bad else (print("JSON errors:") or [print(" -",p,":",e) for p,e in bad] or sys.exit(1)); \
	print("[json] OK")'
# Nota: se vuoi più leggibile, sotto ti do una variante "python file" separata.

lint-docs:
	@echo "[docs] checking links..."
	@bash tools/validate/check_links.sh
	@echo "[docs] OK"

# --------------------------------
# Formal gates
# --------------------------------
formal-bindings-check:
	@echo "[formal] checking required bindings..."
	@test -f law/bindings/protocol/README.md
	@test -f law/bindings/vault/README.md
	@test -f law/bindings/graph/README.md
	@test -f law/bindings/control/README.md
	@test -f law/bindings/cli/README.md
	@test -f law/bindings/compliance/README.md
	@test -f law/bindings/kernel/README.md
	@echo "[formal] bindings: OK"

formal-coverage:
	@echo "[formal] validating traceability coverage..."
	@python3 tools/formal/validate_traceability.py
	@echo "[formal] coverage: OK"

validate-law-registry:
	@echo "[registry] validating ABI registries (primitives <-> commands)..."
	@python3 tools/validate/validate_registry.py
	@echo "[registry] OK"

# --------------------------------
# Docs (Doxygen)
# --------------------------------
DOXYGEN ?= doxygen
DOXY_OUT ?= dist/docs

docs:
	@echo "[doxygen] generating docs..."
	@mkdir -p $(DOXY_OUT)
	@$(DOXYGEN) Doxyfile
	@echo "[doxygen] OK: $(DOXY_OUT)/doxygen/html/index.html"

docs-clean:
	@rm -rf $(DOXY_OUT)

clean: docs-clean

tree:
	@find . -maxdepth 3 -type f | sort