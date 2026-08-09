# 011: Union is Inclusion-Monotone

Target: `thm:union-monotone-inclusion`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-union-monotone-inclusion.tex`

Status: ready for handwritten proof, then LaTeX population.  A typed-set Lean
stub now exists.

## Statement

If `A subset B`, then union with a fixed set preserves inclusion in either
argument:

```text
A subset B ->
  (A union C subset B union C) and
  (C union A subset C union B).
```

## Dependencies

- `def:subset`: to prove `X subset Y`, take arbitrary `x in X` and prove
  `x in Y`.
- `def:union`: `x in A union C iff x in A or x in C`.

## Plain-Language Reading

Union is order-preserving.  If every element of `A` is already an element of
`B`, then adding the same extra set `C` to both sides cannot break that
inclusion.

The proof is elementwise.  Start with an arbitrary element of the smaller union
and split into cases.

## Proof Skeleton

1. Assume `A subset B`.
2. To prove `A union C subset B union C`, let `x in A union C`.
3. By the union membership rule, either `x in A` or `x in C`.
4. If `x in A`, use `A subset B` to get `x in B`, hence `x in B union C`.
5. If `x in C`, immediately get `x in B union C`.
6. To prove `C union A subset C union B`, let `x in C union A`.
7. Split into cases: `x in C` or `x in A`.
8. If `x in C`, immediately get `x in C union B`.
9. If `x in A`, use `A subset B` to get `x in B`, hence `x in C union B`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. Expand the subset goal into an arbitrary-element proof.
2. Expand union membership into a disjunction.
3. Use the inclusion hypothesis only in the branch where `x in A`.
4. Explain why the `x in C` branch is automatic.
5. Prove both left-fixed and right-fixed versions.
6. Say why this is a monotonicity theorem in poset language.

## Formal Proof Draft

```text
Assume A subset B.  First prove A union C subset B union C.  Let x be an
arbitrary element of A union C.  Then x is in A or x is in C.  If x is in A,
then since A subset B, x is in B, and therefore x is in B union C.  If x is in
C, then x is also in B union C.  Hence A union C subset B union C.

Now prove C union A subset C union B.  Let x be an arbitrary element of
C union A.  Then x is in C or x is in A.  If x is in C, then x is in
C union B.  If x is in A, then A subset B gives x is in B, so x is in
C union B.  Hence C union A subset C union B.
```

## Lean Formalization

Current checked Lean target after restart:

- `LRA.VolumeI.Set.Operations.Laws.UnionMonotoneInclusion`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Union.lean
```

Typed-set analogue:

```text
forall Left Right Fixed : LRASet Alpha,
  Subset Left Right ->
    Subset (Union Left Fixed) (Union Right Fixed) and
    Subset (Union Fixed Left) (Union Fixed Right)
```

## Common Failure Modes

- Trying to prove set equality instead of subset inclusion.
- Forgetting to prove the second version `C union A subset C union B`.
- Applying `A subset B` to an element known only to be in `C`.
- Not splitting the union membership into cases.

## What This Unlocks

This is the first order-theoretic operation law in the queue.  The same proof
shape repeats for intersection, indexed unions, closure operators, topologies,
and sigma-algebras.
