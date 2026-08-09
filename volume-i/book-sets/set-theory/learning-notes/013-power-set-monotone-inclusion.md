# 013: Power Set is Inclusion-Monotone

Target: `thm:power-set-monotone-inclusion`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-power-set-monotone-inclusion.tex`

Status: ready for handwritten proof, then LaTeX population.  A typed relative
power-set Lean stub now exists.

## Statement

If `A subset B`, then every subset of `A` is also a subset of `B`:

```text
A subset B -> P(A) subset P(B).
```

## Dependencies

- `def:subset`: both for `A subset B` and for the higher-level inclusion
  `P(A) subset P(B)`.
- `def:power-set`: `S in P(A) iff S subset A`.

## Plain-Language Reading

Power set is monotone: enlarging the base set enlarges the collection of
available subsets.

The proof has two levels:

1. Take an arbitrary element `S` of `P(A)`.
2. Since `S` is itself a set, prove `S subset B` by taking an arbitrary
   `x in S`.

Then `x in S` gives `x in A`, and `A subset B` gives `x in B`.

## Proof Skeleton

1. Assume `A subset B`.
2. To prove `P(A) subset P(B)`, let `S in P(A)`.
3. By the power-set membership rule, `S subset A`.
4. To show `S in P(B)`, prove `S subset B`.
5. Let `x in S`.
6. Since `S subset A`, get `x in A`.
7. Since `A subset B`, get `x in B`.
8. Therefore `S subset B`, hence `S in P(B)`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. Explain why `S in P(A)` means `S subset A`.
2. Expand `P(A) subset P(B)` as a statement about arbitrary subsets `S`.
3. Run the nested arbitrary-element proof for `S subset B`.
4. Chain `x in S -> x in A -> x in B`.
5. Keep the two subset levels distinct.
6. Explain why this theorem is essential for families of subsets.

## Formal Proof Draft

```text
Assume A subset B.  To prove P(A) subset P(B), let S be an arbitrary element
of P(A).  By the definition of power set, S subset A.  We must prove that
S is an element of P(B), equivalently that S subset B.

Let x be an arbitrary element of S.  Since S subset A, x is an element of A.
Since A subset B, x is an element of B.  Therefore every element of S is an
element of B, so S subset B.  Hence S is an element of P(B).  Therefore
P(A) subset P(B).
```

## Lean Formalization

Current checked Lean target after restart:

- `LRA.VolumeI.Set.RelativePowerSetMonotoneInclusion`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\PowerSets.lean
```

Typed-set analogue:

```text
forall Left Right : LRASet Alpha,
  Subset Left Right ->
    Subset (RelativePowerSet Left) (RelativePowerSet Right)
```

Here the final `Subset` is a subset relation between typed sets over the
carrier `LRASet Alpha`; its elements are themselves typed sets.

## Common Failure Modes

- Treating `S in P(A)` as `S in A`.
- Forgetting that `S` is a set.
- Proving only `A subset B` again instead of `S subset B`.
- Losing track of the two arbitrary variables `S` and `x`.
- Not using the power-set membership profile in both the premise and
  conclusion.

## What This Unlocks

Power-set monotonicity is the first order law at the level of families.  It
will reappear whenever a topology, set algebra, sigma-algebra, or measurable
structure on a smaller ambient set is compared with one on a larger ambient
set.
