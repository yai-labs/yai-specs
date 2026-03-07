# Docs + Surface Architecture Report v1

Status: active
Owner: yai-law

## Document class matrix

- `yai-law`: normative law authority
- `yai-sdk`: programmatic API/ABI authority
- `yai-cli`: operational UX/command authority
- `yai`: runtime procedural authority

## Truth-boundary matrix

- Normative semantics -> `yai-law`
- SDK behavior -> `yai-sdk`
- CLI usage/render -> `yai-cli`
- Runtime procedures -> `yai`

## Drift focus

Primary drift risk is legacy runtime naming reintroduced as primary ontology.
Current policy: use `core/exec/brain` as primary ontology and keep historical labels as aliases only.

## Residual items

- Some command metadata still contains historical layer labels for compatibility.
- Final cleanup is handled by decommission/hardening policy artifacts.
