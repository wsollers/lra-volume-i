# 036: Cover Failure and Relative Complements

Target: `thm:cover-failure-relative-complements`

Proof file: `volume-i/book-sets/set-theory/proofs/families/prf-cover-failure-relative-complements.tex`

Status: ready for handwritten proof, then LaTeX population. Typed-set Lean
stubs now exist for the relative-complement collection and the cover-failure
equivalence.

## Statement

For a set `A` and a collection `C` of sets:

```text
not Covers(C, A)
  iff
intersection_{U in C} (A \ U) is nonempty
```

## Dependencies

- `def:cover-full`: `C` covers `A` iff every point of `A` lies in some member
  of `C`.
- `def:set-difference`: `x in A \ U` iff `x in A` and `x notin U`.
- `def:indexed-intersection`: membership in every member of a family.
- `def:empty-set`: nonempty means there is a witness.
- `def:subset`: cover statements are subset statements.

## Plain-Language Reading

A cover fails when some point of `A` escapes every covering set.  That escaped
point belongs to `A`, and it belongs to none of the `U` in `C`.  Equivalently,
it belongs to every relative complement `A \ U`.

This is the atom inside FIP-cover duality.  The finite version says: every
finite subcover fails iff every finite intersection of these relative
complements is nonempty.

## Proof Skeleton

Forward direction:

1. Assume `C` does not cover `A`.
2. By negating the cover condition, choose `x in A` such that no `U in C`
   contains `x`.
3. For each `U in C`, conclude `x in A \ U`.
4. Therefore `x` lies in the intersection of all `A \ U`.

Reverse direction:

1. Assume `x` lies in every `A \ U`.
2. Then `x in A`.
3. Also, for every `U in C`, `x notin U`.
4. Hence no member of `C` covers `x`, so `C` does not cover `A`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. Negate the cover statement correctly.
2. Explain why the witness must still lie in `A`.
3. Translate "missed by `U`" into membership in `A \ U`.
4. Convert a single escaping point into nonempty intersection.
5. Explain how this becomes FIP when restricted to finite subcollections.

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.RelativeComplementCollection`
- `LRA.VolumeI.Set.CoverFailureIffRelativeComplementIntersectionNonempty`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Families.lean
```

## Common Failure Modes

- Forgetting the relative part: the complements are `A \ U`, not merely `U^c`.
- Proving an infinite total-intersection statement and calling it FIP.
- Losing the escaped point when moving from cover failure to intersection
  nonemptiness.

## What This Unlocks

This theorem is the finite-subcover/FIP bridge in its simplest form.  Applying
it to each finite subcollection produces the compactness duality used later in
topology and metric spaces.
