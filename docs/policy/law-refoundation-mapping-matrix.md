# Law Refoundation Mapping Matrix

| Current path | Current semantic role | Target semantic role | Action | Rationale | Notes / follow-up |
|---|---|---|---|---|---|
| `foundation/axioms/` | primary principles, mixed legacy wording | principles expressed with `core/exec/brain` ontology | `rewrite` | axioms must track real runtime ontology | keep IDs where stable (`A-001..A-004`) |
| `foundation/invariants/` | behavioral constraints, partial legacy references | constraints tied to sovereign/execution/cognitive planes | `rewrite` | protect behavior, not package history | focus on I-004 and I-006 first |
| `foundation/boundaries/` | `L0/L1/L2/L3` anchored to vault/kernel/engine/mind | boundaries anchored to `core/exec/brain` + shared layers | `rewrite` | current model encodes obsolete topology | likely keep `L0-vault`, rewrite `L1-L3` semantics |
| `foundation/terminology/` | mixed primary and historical terms | strict primary/historical/deprecated taxonomy | `rewrite` | remove normative ambiguity | add migration alias rules |
| `runtime/README.md` | runtime model by legacy package roles | runtime model by planes (`core/exec/brain`) | `rewrite` | avoid narrative drift | introduce explicit historical-role note |
| `runtime/boot/*` | startup package identity | historical alias under `core` lifecycle | `realign` | startup semantics moved into core lifecycle | label as historical role only |
| `runtime/root/*` | root control identity | historical alias under `core` dispatch/authority | `realign` | root no longer primary ontology | keep migration notes where needed |
| `runtime/kernel/*` | sovereign plane identity by old name | sovereign `core` semantics | `realign` | prevent authority model drift | declass old `kernel` term |
| `runtime/engine/*` | execution plane identity by old name | `exec` plane semantics | `realign` | align external-effect model | inspect `engine_cortex.v1.json` terminology |
| `runtime/mind/*` | cognitive subsystem as separate world | `brain` plane semantics | `realign` | brain is integrated runtime plane | classify graph docs as cognitive-memory contracts |
| `contracts/control/` | control plane with root/kernel language | control contracts owned by `core` plane | `realign` | control authority belongs to core | preserve stable schema names when possible |
| `contracts/protocol/` | protocol contracts + legacy role references | cross-cutting protocol layer contracts | `realign` | protocol is not authority plane | verify `roles.h`/`transport.h` wording |
| `contracts/cli/` | CLI surface with mixed runtime references | stable CLI surface + updated ontology notes | `realign` | avoid unnecessary breaking changes | mostly doc-level edits |
| `contracts/providers/` | provider trust contracts, mixed mind wording | cognitive provider contracts under `brain` governance | `realign` | keep trust semantics, update ontology | avoid conflating with authority plane |
| `contracts/vault/` | vault ABI and state anchor | foundational authority-state contract | `keep` | ABI stability critical | only language cleanup if needed |
| `formal/` | formal artifacts using `YAI_KERNEL` names | formal model aligned to new ontology | `realign` | high drift risk if untouched | phase after runtime/contracts |
| `registry/` | primitive/artifact registry | ontology-neutral contract registry | `realign` | avoid freezing legacy package vocabulary | inspect `primitives.v1.json` and `artifacts.v1.json` |
| `schema/` | generic schema set | ontology-aligned neutral schemas | `realign` | keep stable schema IDs, update semantics | ensure no legacy package lock-in |
| `README.md` | top-level narrative partly legacy | top-level narrative on new ontology | `rewrite` | entry docs define normative framing | do after foundation + runtime/contracts |
| `FOUNDATION.md` | foundation policy summary | aligned to rewritten axioms/invariants/boundaries | `rewrite` | must mirror foundation truth | rewrite after foundation wave |
| `SPEC_MAP.md` | spec topology map by legacy labels | spec map by planes and layers | `rewrite` | map must match runtime ontology | include migration aliases section |
| `REGISTRY.md` | registry guidance | ontology-neutral registry governance | `realign` | reduce semantic drift in machine catalogs | tie to registry/schema pass |
| `docs/pointers/` | pointer docs with mixed historical terms | pointers aligned to primary ontology | `realign` | pointers are fast-entry docs and can spread drift | update after top-level docs rewrite |
