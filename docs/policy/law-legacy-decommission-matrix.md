# Law Legacy Decommission Matrix

| path | residual legacy element | final status | action taken | reason | normative risk if retained | follow-up |
|---|---|---|---|---|---|---|
| `runtime/boot/README.md` | boot as standalone runtime ontology layer | removed | deleted | ontology no longer primary | high | none |
| `runtime/root/README.md` | root as standalone runtime ontology layer | removed | deleted | ontology no longer primary | high | none |
| `runtime/kernel/README.md` | kernel naming | historical-alias-only | rewritten | artifact continuity | medium | optional future path rename |
| `runtime/engine/README.md` | engine naming | historical-alias-only | rewritten | artifact continuity | medium | optional future path rename |
| `runtime/mind/README.md` | mind naming | historical-alias-only | rewritten | artifact continuity | medium | optional future path rename |
| `formal/tla/YAI_KERNEL.tla` | historical artifact name | retained-with-justification | semantic realignment + explicit policy | tool continuity | medium | staged rename plan when safe |
| `formal/configs/YAI_KERNEL*.cfg` | historical artifact names | retained-with-justification | explicit staged-transition policy | config continuity | low | staged rename plan |
| `foundation/boundaries/L1-kernel.md` | historical label in file path | historical-alias-only | already rewritten in foundation phase | keep stable refs | medium | optional future filename transition |
| `foundation/boundaries/L2-engine.md` | historical label in file path | historical-alias-only | already rewritten in foundation phase | keep stable refs | medium | optional future filename transition |
| `foundation/boundaries/L3-mind.md` | historical label in file path | historical-alias-only | already rewritten in foundation phase | keep stable refs | medium | optional future filename transition |
| `registry/commands*.json` metadata | legacy layer tokens in generated metadata | deprecated | policy clarified, no mass rename yet | compatibility surface stability | medium | generated metadata normalization wave |
| `docs/pointers/RUNTIME_RESOLUTION.pointer.md` | legacy runtime binary naming prominence | rewritten | now yai/yai-core first | avoid operational drift | high | remove legacy env references later |
