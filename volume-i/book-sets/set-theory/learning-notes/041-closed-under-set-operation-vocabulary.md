# 041: Closed Under Set Operation Vocabulary

Target: `def:closed-under-set-operation-vocabulary`

Status: definition checkpoint.  Lean vocabulary exists; no LaTeX proof file is
expected.

## Core Idea

An operation existing is different from a family being closed under that
operation.

If `A` and `B` are subsets of `X`, then `A union B` exists as a subset of `X`.
But if `F` is a selected family of subsets of `X`, the closure question is:

```text
A in F and B in F  ->  A union B in F
```

That second statement is extra structure.

## Vocabulary

- Unary closure: one admitted input gives one admitted output.
- Binary closure: two admitted inputs give one admitted output.
- Indexed closure: an indexed family of admitted inputs gives one admitted
  output.
- Collection closure: a subcollection of admitted inputs gives one admitted
  output.

## Concrete Closures

The definitions now cover:

- complements;
- pairwise unions;
- pairwise intersections;
- pairwise differences;
- pairwise symmetric differences;
- countable unions;
- countable intersections;
- arbitrary unions;
- arbitrary intersections.

## Why This Matters

Topologies, set algebras, and sigma-algebras are mostly different closure
packages:

- topologies: arbitrary unions and finite intersections;
- set algebras: complements and finite unions/intersections;
- sigma-algebras: complements and countable unions/intersections.

This checkpoint gives us the language for saying those things precisely.

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.ClosedUnderUnaryOperation`
- `LRA.VolumeI.Set.ClosedUnderBinaryOperation`
- `LRA.VolumeI.Set.ClosedUnderIndexedOperation`
- `LRA.VolumeI.Set.ClosedUnderCollectionOperation`
- `LRA.VolumeI.Set.ClosedUnderComplements`
- `LRA.VolumeI.Set.ClosedUnderPairwiseUnions`
- `LRA.VolumeI.Set.ClosedUnderPairwiseIntersections`
- `LRA.VolumeI.Set.ClosedUnderPairwiseDifferences`
- `LRA.VolumeI.Set.ClosedUnderPairwiseSymmetricDifferences`
- `LRA.VolumeI.Set.ClosedUnderCountableUnions`
- `LRA.VolumeI.Set.ClosedUnderCountableIntersections`
- `LRA.VolumeI.Set.ClosedUnderArbitraryUnions`
- `LRA.VolumeI.Set.ClosedUnderArbitraryIntersections`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Families.lean
```

## Common Failure Modes

- Treating `A union B exists` as if it meant every family containing `A` and
  `B` contains `A union B`.
- Forgetting that finite closure requires a later induction theorem.
- Confusing countable closure with arbitrary closure.
- Forgetting that closure is always relative to a selected family.
