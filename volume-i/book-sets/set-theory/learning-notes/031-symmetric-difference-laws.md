# 031: Symmetric Difference Laws

Target: `thm:symmetric-difference-laws`

Proof file: `volume-i/book-sets/set-theory/proofs/families/prf-symmetric-difference-laws.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs now exist for all displayed laws.

## Statement

For sets `A`, `B`, and `C`:

```text
A triangle B = (A \ B) union (B \ A)
A triangle B = (A union B) \ (A intersection B)
A triangle B = B triangle A
(A triangle B) triangle C = A triangle (B triangle C)
A triangle empty = A
empty triangle A = A
A triangle A = empty
A triangle B = empty <-> A = B
A triangle B subset A union B
```

## Dependencies

- `def:sym-diff`: membership means belonging to exactly one of the two sets.
- `def:set-difference`: one-sided membership removal.
- `def:union`: combines the two one-sided differences.
- `def:intersection`: identifies shared membership.
- `def:empty-set`: identity and self-inverse laws.
- `def:subset`: containment in the union.
- `thm:difference-laws`: translates and simplifies symmetric difference.

## Plain-Language Reading

The symmetric difference keeps exactly the points where two sets disagree.
That makes it behave like Boolean exclusive-or:

```text
P xor Q
```

It is commutative and associative, the empty set is its identity, and every set
is its own inverse.  Saying `A triangle B = empty` means there are no points
where `A` and `B` disagree, so `A = B`.

## Proof Skeleton

1. Expand `A triangle B` as `(A \ B) union (B \ A)`.
2. Use difference membership to get:

   ```text
   (x in A and x notin B) or (x in B and x notin A)
   ```

3. For `(A union B) \ (A intersection B)`, expand membership as:

   ```text
   (x in A or x in B) and not (x in A and x in B)
   ```

4. Show these are equivalent by cases.
5. Commutativity swaps the two one-sided difference branches.
6. Associativity is the associativity of exclusive-or; prove by pointwise case
   analysis on membership in `A`, `B`, and `C`.
7. Identity and self-inverse follow by simplifying exactly-one membership.
8. `A triangle B = empty iff A = B` follows because disagreement is empty iff
   membership in `A` and `B` agrees for every point.
9. `A triangle B subset A union B` follows because each branch already contains
   membership in `A` or `B`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State symmetric difference as union of one-sided differences.
2. State symmetric difference as union minus intersection.
3. Translate membership into exclusive-or.
4. Prove identity with empty set on both sides.
5. Prove self-inverse: `A triangle A = empty`.
6. Explain why `A triangle B = empty` is equivalent to `A = B`.
7. Prove containment in `A union B` by branch extraction.

## Formal Proof Draft

```text
By definition, A triangle B is (A \ B) union (B \ A), so membership means
x is in A and not B, or x is in B and not A.  This is equivalent to saying
x is in A union B but not in A intersection B, giving
A triangle B = (A union B) \ (A intersection B).

Commutativity follows by swapping the two branches.  Associativity follows
from the pointwise exclusive-or truth table: a point belongs to either side
exactly when it belongs to an odd number of A, B, and C.  The empty set is the
identity because no point belongs to empty.  A triangle A is empty because no
point can belong to A and not A.

If A triangle B is empty, then no point belongs to exactly one of A and B, so
membership in A is equivalent to membership in B for every point; hence A = B.
Conversely, if A = B, then no point belongs to exactly one of them, so the
symmetric difference is empty.  Finally, every point in A triangle B lies in A
or in B, so A triangle B is contained in A union B.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.Operations.Laws.SymmetricDifferenceAsUnionDifferences`
- `LRA.VolumeI.Set.Operations.Laws.SymmetricDifferenceAsUnionDifferenceIntersection`
- `LRA.VolumeI.Set.Operations.Laws.SymmetricDifferenceCommutative`
- `LRA.VolumeI.Set.Operations.Laws.SymmetricDifferenceEmpty`
- `LRA.VolumeI.Set.Operations.Laws.EmptySymmetricDifference`
- `LRA.VolumeI.Set.Operations.Laws.SymmetricDifferenceSelf`
- `LRA.VolumeI.Set.Operations.Laws.SymmetricDifferenceAssociative`
- `LRA.VolumeI.Set.Operations.Laws.SymmetricDifferenceEqEmptyIff`
- `LRA.VolumeI.Set.Operations.Laws.SymmetricDifferenceSubsetUnion`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\SymmetricDifference.lean
```

## Common Failure Modes

- Confusing symmetric difference with ordinary difference.
- Forgetting the second one-sided difference branch.
- Proving commutativity but not associativity.
- Treating `A triangle B = empty` as disjointness rather than equality.
- Forgetting that symmetric difference is contained in the union.

## What This Unlocks

Symmetric difference is the Boolean-algebra operation behind "sets differ only
on..." arguments.  It later becomes useful in measure theory, where small
symmetric difference means two sets are almost the same.
