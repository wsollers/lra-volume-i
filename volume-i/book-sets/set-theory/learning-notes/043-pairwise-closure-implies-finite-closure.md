# 043: Pairwise Closure Implies Finite Closure

Target: `thm:pairwise-closure-implies-finite-closure`

Proof file:
`volume-i/book-sets/set-theory/proofs/families/prf-pairwise-closure-implies-finite-closure.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs exist for finite union and finite intersection closure.

## Statement

Let `F` be a family of subsets of `X`.

If:

```text
empty in F
F is closed under pairwise unions
```

then `F` is closed under finite unions.

If:

```text
X in F
F is closed under pairwise intersections
```

then `F` is closed under finite intersections.

## Empty Finite Conventions

The empty finite union is `empty`.

The empty finite intersection is `X`.

Those conventions are why the theorem needs `empty in F` for finite unions and
`X in F` for finite intersections.

## Plain-Language Reading

A two-input closure rule can be iterated along a finite list.  The base case is
the neutral element, and the induction step combines one more admitted set
with the finite output already built from the tail.

## Proof Skeleton

For finite unions:

1. Prove by induction on the finite list.
2. Empty list: the union is `empty`, which belongs to `F`.
3. Cons step: suppose the list is `A :: tail`.
4. The head `A` belongs to `F`.
5. By induction, the finite union of `tail` belongs to `F`.
6. Pairwise union closure gives `A union finiteUnion(tail)` belongs to `F`.

For finite intersections, use the same proof with `X` as the empty-list output
and pairwise intersection closure in the cons step.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State the empty finite union and empty finite intersection conventions.
2. Explain why pairwise closure alone is not enough for the empty finite case.
3. Run the induction proof for finite unions.
4. Run the dual induction proof for finite intersections.
5. Identify where the head-membership and tail-membership hypotheses enter.

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.FiniteUnionFromList`
- `LRA.VolumeI.Set.FiniteIntersectionFromList`
- `LRA.VolumeI.Set.ClosedUnderFiniteUnions`
- `LRA.VolumeI.Set.ClosedUnderFiniteIntersections`
- `LRA.VolumeI.Set.PairwiseUnionClosureImpliesFiniteUnionClosure`
- `LRA.VolumeI.Set.PairwiseIntersectionClosureImpliesFiniteIntersectionClosure`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Families.lean
```

## Common Failure Modes

- Forgetting the empty-list base case.
- Claiming pairwise union closure alone implies finite union closure, without
  ensuring the empty finite union belongs to the family.
- Treating finite closure as countable closure.
- Losing the induction hypothesis when moving from the tail to the whole list.

## What This Unlocks

This theorem lets a finite algebra definition use binary closure rules while
still allowing finite unions and finite intersections later.
