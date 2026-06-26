# lra-volume-i

**Volume I: Logic, Sets, and Proof** - Overleaf-ready standalone repository.

## Structure

```text
volume-i.tex                    - full-volume root (Overleaf main document)
volume-<roman>-<book>.tex - individual book roots
bibliography/             - per-book bibliography shards
volume-i/                - all LaTeX content for this volume
```

Shared LaTeX infrastructure comes from sibling `../lra-common`; do not commit a local `common/` directory here.

## Overleaf

Use `volume-i.tex` for the full volume, or one of the book roots:

```text
volume-i-foundational-geometry.tex, volume-i-mathematical-logic-and-proof.tex, volume-i-set-theory.tex
```

For Overleaf, provide `common/` beside the TeX roots as local project staging only. Edit shared infrastructure in `lra-common`.

## Building Locally

Validate only:

```powershell
python ..\lra-governance\scripts\build_volume.py --root . --validate-only
```

Build all full-volume and book roots in digital mode:

```powershell
python ..\lra-governance\tools\governance\build_volume_docker.py --root . --common-root ..\lra-common --output-dir build\digital
```

Build all full-volume and book roots in print mode:

```powershell
python ..\lra-governance\tools\governance\build_volume_docker.py --root . --common-root ..\lra-common --print-edition --output-dir build\print
```

Build one book root:

```powershell
python ..\lra-governance\tools\governance\build_volume_docker.py --root . --common-root ..\lra-common --tex-root volume-i-foundational-geometry.tex --output-dir build\digital
```


