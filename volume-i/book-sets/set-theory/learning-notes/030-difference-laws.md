# 030: Difference Laws

Target: `thm:difference-laws`

Proof file: `volume-i/book-sets/set-theory/proofs/families/prf-difference-laws.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs now exist for all displayed laws.

## Statement

For sets `A`, `B`, and `C`:

```text
A \ B = A intersection B^c
A \ empty = A
empty \ A = empty
A \ A = empty
A \ (B union C) = (A \ B) intersection (A \ C)
A \ (B intersection C) = (A \ B) union (A \ C)
(A union B) \ C = (A \ C) union (B \ C)
(A intersection B) \ C = (A \ C) intersection (B \ C)
A \ B subset A
(A \ B) intersection B = empty
```

## Dependencies

- `def:set-difference`: `x in A \ B iff x in A and x notin B`.
- `def:complement`: converts `x notin B` into `x in B^c`.
- `def:union`: membership is disjunction.
- `def:intersection`: membership is conjunction.
- `def:empty-set`: no element belongs to the empty set.
- `def:subset`: difference is contained in its left argument.
- `thm:de-morgan`: powers the right-argument union/intersection laws.
- `thm:complement-laws`: powers disjointness and extreme cases.

## Plain-Language Reading

Set difference means "keep the part of `A` outside `B`."  Every law in this
bundle is a controlled way of unpacking that phrase.

The identity `A \ B = A intersection B^c` is the master translation.  Once it
is available, difference laws become ordinary union/intersection/complement
laws.

## Proof Skeleton

For `A \ B = A intersection B^c`:

1. Use extensionality.  Let `x` be arbitrary.
2. Expand `x in A \ B` as `x in A` and `x notin B`.
3. Expand `x in B^c` as `x notin B`.
4. Rebuild intersection membership.

For identities:

1. `A \ empty = A`: `x notin empty` is automatic.
2. `empty \ A = empty`: membership in the difference already requires
   membership in `empty`.
3. `A \ A = empty`: membership would require `x in A` and `x notin A`.

For distribution:

1. Expand the difference as membership in the left side plus nonmembership in
   the right side.
2. Use De Morgan when the right side is a union or intersection.
3. Use ordinary distributivity when the left side is a union or intersection.
4. Rebuild the target expression.

For subset and disjointness:

1. `A \ B subset A`: extract the first component of difference membership.
2. `(A \ B) intersection B = empty`: membership gives both `x notin B` and
   `x in B`, contradiction.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State the master identity `A \ B = A intersection B^c`.
2. Prove each identity law by element membership.
3. Explain why right-side union turns into intersection.
4. Explain why right-side intersection turns into union.
5. Prove left-side distribution using ordinary union/intersection logic.
6. Extract `A \ B subset A` immediately from the definition.
7. Prove disjointness by contradiction.

## Formal Proof Draft

```text
The identity A \ B = A intersection B^c follows directly from membership:
x is in A \ B iff x is in A and not in B, which is exactly x in A and x in B^c.

For A \ empty = A, membership is x in A and x notin empty, and the second
condition is automatic.  For empty \ A = empty, membership requires x in empty.
For A \ A = empty, membership would require both x in A and x notin A.

For A \ (B union C), membership is x in A and x notin B union C.  By De Morgan,
this is x in A, x notin B, and x notin C, which is exactly membership in
(A \ B) intersection (A \ C).  The law for A \ (B intersection C) is analogous,
using the other De Morgan law.

For (A union B) \ C, membership is x in A union B and x notin C; distribute the
shared condition x notin C over the union.  For (A intersection B) \ C,
membership is x in A, x in B, and x notin C, which is the same as membership in
both A \ C and B \ C.

Finally, A \ B is contained in A because membership in A \ B includes membership
in A.  It is disjoint from B because membership in (A \ B) intersection B would
include both x notin B and x in B.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.Operations.Laws.DifferenceAsIntersectionComplement`
- `LRA.VolumeI.Set.Operations.Laws.DifferenceEmpty`
- `LRA.VolumeI.Set.Operations.Laws.EmptyDifference`
- `LRA.VolumeI.Set.Operations.Laws.DifferenceSelf`
- `LRA.VolumeI.Set.Operations.Laws.DifferenceUnion`
- `LRA.VolumeI.Set.Operations.Laws.DifferenceIntersection`
- `LRA.VolumeI.Set.Operations.Laws.UnionDifferenceDistributes`
- `LRA.VolumeI.Set.Operations.Laws.IntersectionDifferenceDistributes`
- `LRA.VolumeI.Set.Operations.Laws.DifferenceSubsetLeft`
- `LRA.VolumeI.Set.Operations.Laws.DifferenceDisjointRight`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Difference.lean
```

## Common Failure Modes

- Forgetting the left membership condition in `A \ B`.
- Reversing De Morgan in `A \ (B union C)`.
- Treating difference as commutative.
- Proving disjointness as subset instead of equality with empty.
- Forgetting that `(A union B) \ C` distributes over the left union.

## What This Unlocks

Difference laws are the working language for removing exceptional sets.  They
show up in topology when restricting complements, in measure theory when
estimating set differences, and in analysis whenever domains are trimmed by
conditions.
