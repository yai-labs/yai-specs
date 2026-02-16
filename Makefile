
# ===============================
# yai-specs — Quality Gates
# ===============================

.PHONY: all check tree docs docs-clean clean

all: docs check

# "check" non compila niente: valida JSON e header presence
check:
	@echo "[specs] checking file presence..."
	@test -f protocol/yai_protocol_ids.h
	@test -f vault/yai_vault_abi.h
	@test -f protocol/runtime/rpc_runtime.h

	@echo "[specs] validating JSON (if python3 available)..."
	@command -v python3 >/dev/null 2>&1 && python3 -c "code='''import json, glob, sys\nbad = []\nfor p in glob.glob(\"**/*.json\", recursive=True):\n    try:\n        json.load(open(p, \"r\", encoding=\"utf-8\"))\n    except Exception as e:\n        bad.append((p, str(e)))\nif bad:\n    print(\"JSON errors:\")\n    for p, e in bad:\n        print(\" -\", p, \":\", e)\n    sys.exit(1)\nprint(\"OK\")\n'''; exec(code)"

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
