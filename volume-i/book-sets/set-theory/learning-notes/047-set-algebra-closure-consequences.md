# 047: Set Algebra Closure Consequences

Target: `thm:set-algebra-closure-consequences`

Proof file:
`volume-i/book-sets/set-theory/proofs/families/prf-set-algebra-closure-consequences.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs exist for the main closure consequences.

## Statement

If `A` is a set algebra on `X`, then:

```text
empty in A
A is closed under complements
A is closed under finite unions
A is closed under finite intersections
A is closed under pairwise differences
A is closed under pairwise symmetric differences
```

## Plain-Language Reading

A set algebra is a finite Boolean workspace.  Once you are inside it, the
ordinary finite set manipulations stay inside it.

## Proof Skeleton

1. Unpack `SetAlgebra A`.
2. Empty set: use `X in A` and complement closure, since `X^c = empty`.
3. Complements and finite unions are direct clauses of the definition.
4. Finite intersections follow from complement closure plus finite union
   closure.
5. Difference follows from `A \ B = A intersection B^c`.
6. Symmetric difference follows from
   `A triangle B = (A \ B) union (B \ A)`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. Unpack the set algebra definition without adding extra hypotheses.
2. Derive `empty in A`.
3. Derive finite intersection closure from Gate 44.
4. Derive difference closure using complement and intersection closure.
5. Derive symmetric-difference closure using difference closure and finite
   union closure.

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.SetAlgebraContainsEmpty`
- `LRA.VolumeI.Set.SetAlgebraClosedUnderComplements`
- `LRA.VolumeI.Set.SetAlgebraClosedUnderFiniteUnions`
- `LRA.VolumeI.Set.SetAlgebraClosedUnderFiniteIntersections`
- `LRA.VolumeI.Set.SetAlgebraClosedUnderPairwiseDifferences`
- `LRA.VolumeI.Set.SetAlgebraClosedUnderPairwiseSymmetricDifferences`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Families.lean
```

## Common Failure Modes

- Requiring countable closure by accident.
- Forgetting that difference is intersection with a complement.
- Trying to prove symmetric-difference closure directly instead of using its
  union-of-differences representation.
- Forgetting that finite disjoint unions are already covered by finite union
  closure once the inputs are known to be in the algebra.

## What This Unlocks

This completes the first finite set-algebra package needed before generated
algebras, sigma-algebras, and Borel generation.
