# Formal/Registry/Schema Mapping Matrix

| current path | current role | target role | action | rationale | compatibility impact | traceability impact | follow-up needed |
|---|---|---|---|---|---|---|---|
| `formal/README.md` | formal layer overview with legacy emphasis | ontology-aligned formal continuity guide | rewrite | separate artifact identity vs ontology | none | clarifies interpretation | none |
| `formal/tla/YAI_KERNEL.tla` | historical-named runtime model | historical name, core/exec/brain semantics | semantic-realign | preserve continuity while shifting semantics | none | medium | eventual rename plan |
| `formal/configs/YAI_KERNEL*.cfg` | config set for historical-named model | staged continuity configs | keep-with-historical-alias | avoid tooling break | none | none | rename in later phase |
| `formal/traceability.v1.json` | invariant mapping matrix | ontology-aware traceability matrix | semantic-realign | avoid legacy topology drift | none | high | enrich ontology fields per invariant |
| `formal/schema/traceability.v1.schema.json` | traceability schema | schema accepting ontology metadata | semantic-realign | allow explicit ontology context | low | high | enforce stricter field rules later |
| `registry/README.md` | registry docs with weak ontology policy | ontology-first registry policy | rewrite | prevent metadata drift | none | medium | command metadata cleanup |
| `registry/primitives.v1.json` | primitive catalog with legacy terms | primitives interpreted in core/exec/brain model | semantic-realign | keep IDs stable | none | medium | normalize legacy domains/layers |
| `registry/artifacts.v1.json` | artifact role registry | unchanged role model with ontology-safe interpretation | keep | already mostly neutral | none | low | none |
| `registry/commands.v1.json` | command catalog with legacy heavy metadata | stable command IDs with alias-aware semantics | semantic-realign | preserve CLI/SDK contracts | none | medium | layer metadata migration |
| `registry/commands.surface.v1.json` | default command surface index | compatibility surface with alias policy | semantic-realign | avoid runtime ontology confusion | none | low | future metadata normalization |
| `registry/commands.topics.v1.json` | entrypoint/topic map | stable map with alias policy | semantic-realign | no break for clients | none | low | future metadata normalization |
| `registry/schema/*.json` | registry validators | stable validators with ontology policy in docs | keep | avoid unnecessary validator churn | none | low | optional stricter rules later |
| `schema/README.md` | transversal schemas overview | ontology-safe schema posture | rewrite | prevent hidden legacy model | none | low | none |
| `schema/*.json` | payload schemas | stable schema lines with ontology-neutral interpretation | keep | compatibility first | none | low | add optional ontology annotations later |
