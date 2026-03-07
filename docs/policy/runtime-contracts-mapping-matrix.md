# Runtime/Contracts Mapping Matrix

| current path | current role | target role | action | rationale | compatibility impact | follow-up needed |
|---|---|---|---|---|---|---|
| `runtime/README.md` | legacy-layer runtime overview | ontology-first runtime overview | rewrite | remove legacy topology primacy | none | monitor references |
| `runtime/boot/README.md` | boot layer primary narrative | absorbed into core lifecycle | remove | legacy runtime identity removed | low | ensure no docs link remains |
| `runtime/root/README.md` | root layer primary narrative | absorbed into core dispatch | remove | legacy runtime identity removed | low | ensure no docs link remains |
| `runtime/kernel/README.md` | kernel primary authority narrative | core sovereignty (kernel alias) | realign | preserve artifact continuity, change semantics | none | eventual path rename optional |
| `runtime/kernel/BINDING.md` | kernel binding | core binding with kernel alias | rewrite | align with new foundation | none | formal link refinement |
| `runtime/engine/README.md` | engine primary narrative | exec plane narrative | realign | align execution semantics | none | optional future rename |
| `runtime/mind/README.md` | mind primary narrative | brain plane narrative | realign | align cognitive semantics | none | optional future rename |
| `runtime/mind/graph/*` | mind graph surface | brain memory surface (alias path) | realign | preserve graph contracts without ontology drift | none | graph formalization |
| `contracts/control/README.md` | root/kernel control ambiguity | core control-plane contract | rewrite | authority must map to core | none | keep schema compatibility checks |
| `contracts/control/notes/CONTROL_PLANE.md` | legacy runtime terms | core/exec/brain control model | rewrite | remove semantic ambiguity | none | schema/model parity checks |
| `contracts/control/schema/control_call.v1.json` | target enums legacy-first | target enums ontology-first + aliases | realign | preserve callers while shifting primary semantics | additive | later alias deprecation schedule |
| `contracts/control/schema/exec_reply.v1.json` | target enums legacy-only | ontology-first + aliases | realign | position reply in core↔exec model | additive | eventual alias cleanup |
| `contracts/protocol/README.md` | protocol tied to legacy runtime reading | protocol as cross-cutting layer | rewrite | enforce layer semantics | none | deep contracts review |
| `contracts/protocol/include/*` | mixed legacy wording | neutral layer wording | realign | preserve ABI, clarify semantics | none | none |
| `contracts/cli/*` | partially legacy runtime framing | stable public surface over new ontology | realign | keep compatibility | none | command metadata cleanup later |
| `contracts/providers/*` | provider trust under legacy mind framing | brain-governed provider trust | realign | prevent authority confusion | none | deeper provider schema alignment |
| `contracts/vault/*` | stable but legacy references | stable L0 with core-aligned interpretation | keep-with-legacy-alias | avoid unnecessary ABI churn | none | review during top-level docs rewrite |
