
# ===============================
# yai-specs — Quality Gates
# ===============================

.PHONY: all check ci lint-docs formal-coverage formal-bindings-check tree docs docs-clean clean

all: docs check

ci: check formal-bindings-check formal-coverage

# "check" non compila niente: valida JSON e header presence
check:
	@echo "[specs] checking file presence..."
	@test -f specs/protocol/include/yai_protocol_ids.h
	@test -f specs/vault/include/yai_vault_abi.h
	@test -f specs/protocol/runtime/include/rpc_runtime.h

	@echo "[specs] validating JSON (if python3 available)..."
	@command -v python3 >/dev/null 2>&1 && python3 -c "code='''import json, glob, sys\nbad = []\nfor p in glob.glob(\"**/*.json\", recursive=True):\n    try:\n        json.load(open(p, \"r\", encoding=\"utf-8\"))\n    except Exception as e:\n        bad.append((p, str(e)))\nif bad:\n    print(\"JSON errors:\")\n    for p, e in bad:\n        print(\" -\", p, \":\", e)\n    sys.exit(1)\nprint(\"OK\")\n'''; exec(code)"

lint-docs:
	@bash tools/validate/check_links.sh

formal-bindings-check:
	@echo "[formal] checking required bindings..."
	@test -f formal/bindings/BINDING_PROTOCOL.md
	@test -f formal/bindings/BINDING_VAULT.md
	@test -f formal/bindings/BINDING_GRAPH.md
	@test -f formal/bindings/BINDING_CONTROL.md
	@test -f formal/bindings/BINDING_CLI.md
	@test -f formal/bindings/BINDING_COMPLIANCE.md
	@echo "[formal] bindings check: OK"

formal-coverage:
	@python3 tools/formal/validate_traceability.py

tree:
	@find . -maxdepth 3 -type f | sort

# ===============================
# Docs (Doxygen)
# ===============================

DOXYGEN ?= doxygen
DOXY_OUT ?= dist/docs

docs:
	@mkdir -p $(DOXY_OUT)
	@$(DOXYGEN) Doxyfile
	@echo "[specs] docs: $(DOXY_OUT)/doxygen/html/index.html"

docs-clean:
	@rm -rf $(DOXY_OUT)

clean: docs-clean
