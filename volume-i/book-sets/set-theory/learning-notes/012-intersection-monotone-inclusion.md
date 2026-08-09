# 012: Intersection is Inclusion-Monotone

Target: `thm:intersection-monotone-inclusion`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-intersection-monotone-inclusion.tex`

Status: ready for handwritten proof, then LaTeX population.  A typed-set Lean
stub now exists.

## Statement

If `A subset B`, then intersection with a fixed set preserves inclusion in
either argument:

```text
A subset B ->
  (A intersection C subset B intersection C) and
  (C intersection A subset C intersection B).
```

## Dependencies

- `def:subset`: to prove `X subset Y`, take arbitrary `x in X` and prove
  `x in Y`.
- `def:intersection`: `x in A intersection C iff x in A and x in C`.

## Plain-Language Reading

Intersection is order-preserving.  If every element of `A` is already in `B`,
then any element common to `A` and `C` is also common to `B` and `C`.

Unlike union monotonicity, there is no case split.  Membership in an
intersection gives both required facts at once.

## Proof Skeleton

1. Assume `A subset B`.
2. To prove `A intersection C subset B intersection C`, let
   `x in A intersection C`.
3. By the intersection membership rule, get `x in A` and `x in C`.
4. Use `A subset B` on `x in A` to get `x in B`.
5. Combine `x in B` and `x in C` to get `x in B intersection C`.
6. To prove `C intersection A subset C intersection B`, let
   `x in C intersection A`.
7. Get `x in C` and `x in A`.
8. Use `A subset B` to get `x in B`.
9. Combine `x in C` and `x in B` to get `x in C intersection B`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. Expand the subset goal into an arbitrary-element proof.
2. Expand intersection membership into a conjunction.
3. Use the inclusion hypothesis to transport only the `A` membership.
4. Preserve the fixed-set membership unchanged.
5. Prove both left-fixed and right-fixed versions.
6. Explain why this is monotonicity in the subset poset.

## Formal Proof Draft

```text
Assume A subset B.  First prove A intersection C subset B intersection C.
Let x be an arbitrary element of A intersection C.  Then x is in A and x is in
C.  Since A subset B, x is in B.  Together with x in C, this gives that x is
in B intersection C.  Hence A intersection C subset B intersection C.

Now prove C intersection A subset C intersection B.  Let x be an arbitrary
element of C intersection A.  Then x is in C and x is in A.  Since A subset B,
x is in B.  Together with x in C, this gives that x is in C intersection B.
Hence C intersection A subset C intersection B.
```

## Lean Formalization

Current checked Lean target after restart:

- `LRA.VolumeI.Set.Operations.Laws.IntersectionMonotoneInclusion`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Intersection.lean
```

Typed-set analogue:

```text
forall Left Right Fixed : LRASet Alpha,
  Subset Left Right ->
    Subset (Intersection Left Fixed) (Intersection Right Fixed) and
    Subset (Intersection Fixed Left) (Intersection Fixed Right)
```

## Common Failure Modes

- Treating intersection like union and splitting into cases.
- Forgetting that intersection membership supplies both components.
- Applying `A subset B` to the fixed-set membership instead of the `A`
  membership.
- Proving only one side of the theorem.
- Trying to prove equality instead of inclusion.

## What This Unlocks

Intersection monotonicity is the meet-side counterpart of union monotonicity.
It is used constantly in lattice arguments, finite intersection property
proofs, topology, and measure-theoretic closure arguments.
