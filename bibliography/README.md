# Volume Bibliography

This directory is owned by `lra-volume-i`.

Bibliography shards are book-owned and used directly by this volume repository. They are not copied to a monorepo or to `lra-common`.

Current shards:

- `volume-i-foundational-geometry.bib`
- `volume-i-mathematical-logic-and-proof.bib`
- `volume-i-set-theory.bib`

Add entries only to the shard for the owning book root, then run:

```powershell
python scripts/check_bibliography.py --bib-dir bibliography
```

Do not add unrelated volume bibliography files here.
