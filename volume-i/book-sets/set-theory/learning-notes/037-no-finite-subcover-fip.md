# 037: No Finite Subcover and FIP

Target: `thm:no-finite-subcover-fip`

Proof file: `volume-i/book-sets/set-theory/proofs/families/prf-no-finite-subcover-fip.tex`

Status: ready for handwritten proof, then LaTeX population. Typed-set Lean
stubs now exist for the no-finite-subcover predicate and its FIP equivalence.

## Statement

For a set `A` and a collection `C` of sets:

```text
forall finite C0 subset C, not Covers(C0, A)
  iff
FiniteIntersectionProperty({A \ U | U in C})
```

## Dependencies

- `def:cover-full`: cover means every point of `A` lands in some member of the
  collection.
- `def:subcover`: a subcollection that still covers.
- `def:finite-cover`: finite subcover means finite subcollection plus cover.
- `def:fip`: every finite subcollection has nonempty intersection.
- `thm:cover-failure-relative-complements`: one failed cover is one nonempty
  intersection of relative complements.

## Plain-Language Reading

No finite subcover means every finite selection of covering sets misses at
least one point of `A`.  For each finite selection, the missed point lies in
all corresponding relative complements `A \ U`.  So every finite intersection
of those relative complements is nonempty: that is exactly FIP.

## Proof Skeleton

1. Let `C0` be a finite subcollection of `C`.
2. Apply cover-failure/relative-complement duality to `C0`.
3. `C0` fails to cover `A` iff:

   ```text
   intersection_{U in C0} (A \ U) is nonempty
   ```

4. Quantify this equivalence over every finite `C0 subset C`.
5. Recognize the right side as the finite intersection property of
   `{A \ U | U in C}`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State what "no finite subcover" means with quantifiers.
2. State FIP with quantifiers.
3. Apply the cover-failure theorem to one finite subcollection.
4. Explain why quantifying over finite subcollections gives FIP.
5. Explain why this is the set-theoretic heart of compactness duality.

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.HasNoFiniteSubcover`
- `LRA.VolumeI.Set.NoFiniteSubcoverIffRelativeComplementFIP`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Families.lean
```

## Common Failure Modes

- Forgetting to restrict to finite subcollections.
- Treating FIP as nonempty total intersection.
- Forgetting the complements are relative to `A`.
- Confusing "no finite subcover" with "not a cover."

## What This Unlocks

This theorem is the direct precursor to compactness: every open cover has a
finite subcover is dual to every closed family with FIP having nonempty total
intersection.
