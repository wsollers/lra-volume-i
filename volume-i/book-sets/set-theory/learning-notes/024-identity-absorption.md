# 024: Identity and Absorption Laws

Target: `thm:identity-absorption`

Proof file: `volume-i/book-sets/set-theory/proofs/families/prf-identity-absorption.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs already exist for all displayed laws.

## Statement

For sets `A`, `B`, and universe `U`:

```text
A union empty = A
empty union A = A
A intersection U = A
U intersection A = A
A union U = U
U union A = U
A intersection empty = empty
empty intersection A = empty
A union (A intersection B) = A
A intersection (A union B) = A
```

## Dependencies

- `ax:extensionality`: to prove equality of sets by equality of members.
- `def:empty-set`: no element belongs to the empty set.
- `def:universe` or ambient-set convention: every element under discussion lies
  in the universe.
- `def:union`: membership is disjunction.
- `def:intersection`: membership is conjunction.
- `def:subset`: used by the prose theorem to keep `A` inside the fixed universe.

## Plain-Language Reading

The identity laws say that adding nothing by union changes nothing, and
intersecting with the whole universe changes nothing.  The domination/null
laws say that union with the universe gives the universe, and intersection
with the empty set gives the empty set.

The absorption laws say that once membership in `A` is already known, adding
the extra condition `A intersection B` or the extra option `A union B` is
redundant.

## Proof Skeleton

For `A union empty = A`:

1. Use extensionality.  Let `x` be arbitrary.
2. Expand `x in A union empty` as `x in A` or `x in empty`.
3. The empty branch is impossible.
4. Conclude equivalence with `x in A`.

For `A intersection U = A`:

1. Use extensionality.  Let `x` be arbitrary.
2. Expand `x in A intersection U` as `x in A` and `x in U`.
3. The forward direction keeps `x in A`.
4. The reverse direction combines `x in A` with the ambient fact `x in U`.

For the symmetric identity orientations:

1. Either repeat the same elementwise proof with the arguments reversed, or use
   commutativity after proving the displayed orientation.

For the domination/null laws:

1. Expand `x in A union U` as `x in A or x in U`; the universe branch gives
   the reverse direction immediately.
2. Expand `x in A intersection empty` as `x in A and x in empty`; the empty
   component is impossible.
3. Handle the reversed orientations either directly or by commutativity.

For `A union (A intersection B) = A`:

1. Use extensionality.  Let `x` be arbitrary.
2. If `x in A union (A intersection B)`, split cases.
3. The left case is immediate.
4. The right case gives `x in A` and `x in B`, so keep `x in A`.
5. Conversely, if `x in A`, then `x` is in the union by the left branch.

For `A intersection (A union B) = A`:

1. Use extensionality.  Let `x` be arbitrary.
2. If `x in A intersection (A union B)`, keep the first component `x in A`.
3. Conversely, if `x in A`, then `x in A union B` by the left branch.
4. Combine `x in A` and `x in A union B`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State the union identity laws.
2. State the intersection identity laws.
3. State the union domination laws.
4. State the intersection null laws.
5. State both absorption laws.
6. Use the empty-set contradiction correctly.
7. Use the universe/ambient membership convention correctly.
8. Explain why absorption removes redundant occurrences of `A`.
9. Prove the laws elementwise without relying on rewrite automation.

## Formal Proof Draft

```text
For A union empty = A, use extensionality.  If x is in A union empty, then x is
in A or x is in empty.  The second case is impossible, so x is in A.  Conversely,
if x is in A, then x is in A union empty.

For A intersection U = A, use extensionality.  If x is in A intersection U,
then x is in A.  Conversely, if x is in A, then since A is considered inside U,
x is also in U, so x is in A intersection U.

For A union (A intersection B) = A, use extensionality.  Membership in the
left side means x is in A or x is in A intersection B.  The first case gives
x in A; the second case also gives x in A.  Conversely, x in A gives membership
in the left side by the left branch of the union.

For A intersection (A union B) = A, use extensionality.  Membership in the left
side directly gives x in A.  Conversely, if x is in A, then x is in A union B,
so x is in A intersection (A union B).
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.Operations.Laws.UnionEmpty`
- `LRA.VolumeI.Set.Operations.Laws.EmptyUnion`
- `LRA.VolumeI.Set.Operations.Laws.UnionUniversal`
- `LRA.VolumeI.Set.Operations.Laws.UniversalUnion`
- `LRA.VolumeI.Set.Operations.Laws.IntersectionUniversal`
- `LRA.VolumeI.Set.Operations.Laws.UniversalIntersection`
- `LRA.VolumeI.Set.Operations.Laws.IntersectionEmpty`
- `LRA.VolumeI.Set.Operations.Laws.EmptyIntersection`
- `LRA.VolumeI.Set.Operations.Laws.AbsorptionUnionIntersection`
- `LRA.VolumeI.Set.Operations.Laws.AbsorptionIntersectionUnion`

Locations:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Union.lean
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Intersection.lean
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Duality.lean
```

Typed-set analogues:

```text
Union A Empty = A
Union Empty A = A
Union A Universal = Universal
Union Universal A = Universal
Intersection A Universal = A
Intersection Universal A = A
Intersection A Empty = Empty
Intersection Empty A = Empty
Union A (Intersection A B) = A
Intersection A (Union A B) = A
```

## Common Failure Modes

- Forgetting that empty-set membership is impossible.
- Treating universe membership as an extra theorem without noting the ambient
  convention.
- Proving only identity and skipping absorption.
- Mixing up identity laws with domination/null laws.
- Losing the `x in A` component in the absorption proofs.
- Confusing absorption with idempotence.

## What This Unlocks

Identity and absorption are basic simplification moves for Boolean set algebra.
They are used constantly when reducing finite expressions, checking closure of
set algebras, and simplifying open/closed set arguments in topology.
