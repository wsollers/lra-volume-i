# 042: Closure Rule Intersection Stability

Target: `thm:closure-rule-intersection-stability`

Proof file:
`volume-i/book-sets/set-theory/proofs/families/prf-closure-rule-intersection-stability.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs exist for unary, binary, indexed, and collection-operation forms.

## Statement

Let `S` be a collection system, so its members are families of subsets of `X`.
If every member family of `S` is closed under a fixed operation, then:

```text
intersection S
```

is closed under that same operation.

This applies to unary, binary, indexed, and collection operations.

## Plain-Language Reading

If every admissible family obeys a rule, then the common part of all admissible
families still obeys the rule.

That is exactly why generated structures work.  The generated object is the
intersection of all admissible structures containing the seed family; this
theorem says the intersection still satisfies the closure rules that made those
structures admissible.

## Proof Skeleton

1. Let the input or inputs belong to `intersection S`.
2. To show the operation output belongs to `intersection S`, take an arbitrary
   member family `F` of `S`.
3. Since the inputs belong to `intersection S`, they belong to `F`.
4. Since `F` has the closure rule, the operation output belongs to `F`.
5. Since `F` was arbitrary, the output belongs to every member family of `S`.
6. Therefore the output belongs to `intersection S`.

For collection operations, use the same idea with a subcollection: if
`G subset intersection S`, then for each member family `F` of `S`, also
`G subset F`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. Keep the levels straight: set, family of sets, collection system.
2. Unfold membership in an intersection of families.
3. Explain why closure of each member family transfers to the intersection.
4. Handle the binary case with two inputs.
5. Handle the collection-operation case by proving a subcollection inclusion
   into each member family.

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.UnaryClosureStableUnderCollectionIntersection`
- `LRA.VolumeI.Set.BinaryClosureStableUnderCollectionIntersection`
- `LRA.VolumeI.Set.IndexedClosureStableUnderCollectionIntersection`
- `LRA.VolumeI.Set.CollectionClosureStableUnderCollectionIntersection`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Families.lean
```

## Common Failure Modes

- Trying to prove the output belongs to the collection system `S`, instead of
  to the intersection of its member families.
- Forgetting that an element of `intersection S` is itself a subset of `X`.
- Treating the theorem as specific to union when it is really operation-generic.
- In the collection-operation case, forgetting to transfer
  `G subset intersection S` into `G subset F` for each member family `F`.

## What This Unlocks

This is the technical reason the intersection of all algebras containing a
seed is still an algebra, and later why the intersection of all sigma-algebras
containing a seed is still a sigma-algebra.
