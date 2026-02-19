# Formal Bindings

This directory contains human-readable, verifiable binding documents that connect:

- contracts (`contracts/*`)
- specs (`specs/*`, `compliance/*`)
- vectors (`vectors/*`)
- formal model artifacts (`formal/tla/*`, `formal/configs/*`)

Each binding file follows one canonical structure:
1. Scope
2. Source-of-truth pointers
3. Invariants covered
4. Spec artifacts
5. Test vectors
6. Formal model linkage
7. Known gaps / TODO

Use these files together with `formal/traceability.v1.json` for machine-readable validation.
