# lra-volume-i

**Volume I: Mathematical Logic** — Overleaf-ready standalone repository.

Part of the [Learning Real Analysis](https://github.com/wsollers/Learning-Real-Analysis) project.

## Structure

```
main.tex              — volume root (Overleaf main document)
common/               — shared LaTeX infrastructure (synced from lra-common)
bibliography/         — shared bibliography (synced from monorepo)
volume-i/             — all LaTeX content for this volume
  index.tex
  <chapter>/
    index.tex
    chapter.yaml
    notes/
    proofs/
```

## Overleaf

Link this repo to Overleaf via **Menu → GitHub**. The main document is `main.tex`.

## common/ sync

The `common/` directory is automatically kept in sync with `lra-common` via a GitHub Actions workflow. Do not edit files in `common/` here — edit in `lra-common` instead.

## Building locally

```powershell
latexmk -lualatex main.tex
```
