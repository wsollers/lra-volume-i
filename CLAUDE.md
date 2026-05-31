<!--
GENERATED FILE — DO NOT EDIT BY HAND.

Source repo: wsollers/lra-governance
Source commit: d98bb51fc80e683b38a9d1e76f4a0c91037ede0a
Generated from:
- docs/governance/...
- docs/architecture/...
- docs/governance/repo-overlays/lra-volume.md

Regenerate from lra-governance.
Emergency downstream edits must be ported upstream before the next sync.
-->

# Claude Instructions

@AGENTS.md

If import semantics are unavailable, use the generated `AGENTS.md` content for
the same repository as the canonical local instruction body.

## Global Agent Rules

- Treat generated instruction files as derived artifacts.
- Follow the owning repository boundary for every task.
- Do not include secrets, credentials, tokens, or machine-local private values.
- Do not modify mathematical content during governance or wrapper-generation tasks.
- Do not touch `Learning-Real-Analysis/scripts/`.
- Port emergency downstream instruction repairs back to `lra-governance`.

## Repo Overlay

# lra-volume Overlay

Stub overlay for `lra-volume-i` through `lra-volume-v`.

Owned concerns:

- volume content only,
- Overleaf-ready volume roots,
- local copies of synced `common/` and `bibliography/`,
- volume-to-monorepo content sync.

This overlay may contain negative guard rails that say specialist rules do not
apply to volume repos. It must not contain positive Lean-specific, C++ /
Vulkan / simulation, numerical-analysis / benchmark / plotting, or PDF
extraction workflow rules.

## Agent Scope

Volume agents may edit only the owning `volume-N/` content unless a task
explicitly says otherwise. They should not edit synced `common/`,
`bibliography/`, generated governance wrappers, or canonical YAML.

Volume tasks should preserve Overleaf readiness and monorepo sync shape.

## Provider Notes

Claude should use this wrapper as a pointer to the generated repo instructions.
