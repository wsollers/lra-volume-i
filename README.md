# lra-volume-i

**Volume I: Logic, Sets, and Proof** — Overleaf-ready standalone repository.

## Structure

```text
volume-i.tex          — full-volume root (Overleaf main document)
volume-i-<book>.tex   — individual book roots
common/               — shared LaTeX infrastructure supplied by lra-common; ignored here
bibliography/         — per-book bibliography shards
volume-i/             — all LaTeX content for this volume
```

## Overleaf

Upload or checkout `common/` beside this repository's TeX roots, then set the main document to `volume-i.tex` for the full volume or to one of the book roots:

```text
volume-i-foundational-geometry.tex, volume-i-mathematical-logic-and-proof.tex, volume-i-set-theory.tex
```

`common/` is ignored by git in this volume repo; edit shared infrastructure in `lra-common`.

## Building locally

```powershell
python F:\repos\lra-governance\tools\governance\build_volume_docker.py --root F:\repos\lra-volume-i --common-root F:\repos\lra-common
```
