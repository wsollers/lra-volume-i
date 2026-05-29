<!--
GENERATED FILE — DO NOT EDIT BY HAND.

Source repo: wsollers/lra-governance
Source commit: a55609adaf2be4bd68941a4cb78336e56d92a60b
Generated from:
- docs/governance/...
- docs/architecture/...
- docs/governance/repo-overlays/lra-volume.md

Regenerate from lra-governance.
Emergency downstream edits must be ported upstream before the next sync.
-->

# Agent Instructions

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

This overlay must not contain Lean-specific, C++ / Vulkan / simulation, or
numerical-analysis / benchmark / plotting rules.

## Agent Scope

Volume agents may edit only the owning `volume-N/` content unless a task
explicitly says otherwise. They should not edit synced `common/`,
`bibliography/`, generated governance wrappers, or canonical YAML.

Volume tasks should preserve Overleaf readiness and monorepo sync shape.

## Provider Notes

Codex reads this file as the local agent entrypoint.
