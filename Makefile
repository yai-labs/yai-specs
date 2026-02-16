
# ===============================
# yai-specs — Quality Gates
# ===============================

.PHONY: all check tree

all: check

# "check" non compila niente: valida JSON e header presence
check:
	@echo "[specs] checking file presence..."
	@test -f protocol/yai_protocol_ids.h
	@test -f vault/yai_vault_abi.h
	@test -f protocol/runtime/rpc_runtime.h

	@echo "[specs] validating JSON (if python3 available)..."
	@command -v python3 >/dev/null 2>&1 && \
	  python3 - <<'PY' || true
import json, glob, sys
bad = []
for p in glob.glob("**/*.json", recursive=True):
    try:
        json.load(open(p,"r",encoding="utf-8"))
    except Exception as e:
        bad.append((p,str(e)))
if bad:
    print("JSON errors:")
    for p,e in bad: print(" -",p,":",e)
    sys.exit(1)
print("OK")
PY

tree:
	@find . -maxdepth 3 -type f | sort
