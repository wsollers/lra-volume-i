<!--
GENERATED FILE — DO NOT EDIT BY HAND.

Source repo: wsollers/lra-governance
Source commit: d98bb51fc80e683b38a9d1e76f4a0c91037ede0a
Generated from:
- docs/governance/...
- docs/architecture/...
- docs/governance/repo-overlays/lra-volume.md

Regenerate from lra-governance.
Emergency downstream edits must be ported upstream.
-->

# Agent Instructions

## Global Agent Rules

- Treat generated instruction files as derived artifacts.
- Canonical governance, workflows, validators, schemas, prompts, and shared
  scripts live in `../lra-governance`, or `F:/repos/lra-governance` on the
  local Windows checkout. Use `LRA_GOVERNANCE_ROOT` when the checkout is
  elsewhere.
- Do not edit copied governance files in this repo. Leaf governance tools must
  be wrappers that delegate to `lra-governance` and fail clearly if the
  canonical checkout is unavailable.
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
- external `lra-common` consumed by the build environment,
- the volume-owned bibliography shard,
- volume-to-monorepo content sync.

This overlay may contain negative guard rails that say specialist rules do not
apply to volume repos. It must not contain positive Lean-specific, C++ /
Vulkan / simulation, numerical-analysis / benchmark / plotting, or PDF
extraction workflow rules.

## Agent Scope

Volume agents may edit only the owning `volume-N/` content unless a task
explicitly says otherwise. They should not edit copied `common/`, generated governance wrappers, or canonical YAML. Shared LaTeX infrastructure belongs in `lra-common` and is supplied to builds by the Docker image or an explicit checkout.

Volume tasks should preserve Overleaf readiness and monorepo sync shape.

## Provider Notes

Codex reads this file as the local agent entrypoint.
