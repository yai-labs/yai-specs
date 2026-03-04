# CLI

`contracts/cli/` contains the canonical CLI-facing contract surface of `yai-law`.

These artifacts define how the YAI CLI surface is interpreted, documented, and attached to the canonical command model consumed by downstream runtimes and tools.

## Scope

The CLI surface covers:

* CLI-facing contract interpretation
* command-surface notes and public interface guidance
* binding of the CLI surface to the canonical command registry

## Normative artifacts

Canonical machine-readable command artifacts are defined outside this directory:

* `registry/commands.v1.json`
* `registry/schema/commands.v1.schema.json`

CLI-facing supporting artifacts in this directory include:

* `BINDING.md`
* `notes/CLI_PUBLIC_INTERFACE.md`
* `notes/TUI_COCKPIT_V1.md`

## Normative role

`contracts/cli/` is normative where it defines binding expectations for the CLI surface, but the canonical machine-readable command model remains in the registry layer.

The CLI surface must remain aligned with:

* `registry/commands.v1.json`
* `registry/schema/commands.v1.schema.json`
* `registry/primitives.v1.json`
* `registry/artifacts.v1.json`
* `foundation/` for normative primacy
* `formal/` where CLI-relevant behavior is traced

If a CLI consumer diverges from the canonical command registry or from the attached CLI bindings, the consumer is non-conforming.

## Versioning and compatibility rules

* Breaking command-surface changes require compatibility review and an appropriate repository version change
* Additive compatible command changes require repository version review and `CHANGELOG.md` coverage
* CLI-facing notes must not redefine the canonical machine-readable command model
* Changes that affect command interpretation, validation, or expected behavior must be treated as compatibility-sensitive

## Consumers

Typical consumers include:

* `yai`
* `yai-cli`
* `yai-yx`
* tooling that consumes or validates canonical CLI command surfaces

## Change discipline

A CLI-surface change must update, as applicable:

* canonical command registry artifacts
* CLI binding and note artifacts in this directory
* `REGISTRY.md`
* `SPEC_MAP.md`
* `CHANGELOG.md`
* relevant validation artifacts when behavior changes

Silent drift between CLI behavior and the canonical command surface is non-compliant by definition.
## Registry scale profile

The CLI contract is expected to remain deterministic with large registries (target: 2800 command_id, 200 per group).
This profile validates discoverability and invocation surface under load; it does not replace product curation/taxonomy governance.
Consumers must support `yai help --all` and `yai help <command_id>` across the full canonical registry.
