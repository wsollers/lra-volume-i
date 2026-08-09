# 025: Involution of Complement

Target: `thm:involution`

Proof file: `volume-i/book-sets/set-theory/proofs/families/prf-involution.tex`

Status: ready for handwritten proof, then LaTeX population.  A typed-set Lean
stub already exists.

## Statement

For any subset `A` of a fixed universe `U`:

```text
(A^c)^c = A
```

## Dependencies

- `ax:extensionality`: to prove equality of sets by equality of members.
- `def:complement`: `x in A^c iff x notin A`, relative to a fixed universe.
- Ambient-set convention: complements are interpreted inside the same universe.

## Plain-Language Reading

Taking the complement reverses membership.  Taking the complement again
reverses it back.

Elementwise, the theorem says:

```text
not (not (x in A)) <-> x in A
```

## Proof Skeleton

1. Use extensionality.  Let `x` be arbitrary.
2. Prove `x in (A^c)^c <-> x in A`.
3. Expand the outer complement: `x in (A^c)^c` means `x notin A^c`.
4. Expand the inner complement: `x in A^c` means `x notin A`.
5. Thus the left side says `not (not (x in A))`.
6. Use double-negation reasoning to recover `x in A`.
7. Conversely, if `x in A`, then `x` cannot be in `A^c`, so
   `x in (A^c)^c`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State complement involution relative to a fixed universe.
2. Start the equality proof with extensionality.
3. Expand both complement memberships.
4. Identify the double-negation step.
5. Explain why using the same universe matters.
6. Distinguish double complement from complement antitonicity.

## Formal Proof Draft

```text
Prove equality by extensionality.  Let x be arbitrary.  If x is in (A^c)^c,
then x is not in A^c.  Since A^c consists exactly of elements not in A, this
means it is not the case that x is not in A.  Hence x is in A.  Conversely, if
x is in A, then x is not in A^c, so x is in (A^c)^c.  Therefore
(A^c)^c = A.
```

## Lean Formalization

Current checked Lean target after restart:

- `LRA.VolumeI.Set.Operations.Laws.DoubleComplement`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Complement.lean
```

Typed-set analogue:

```text
Complement (Complement A) = A
```

## Common Failure Modes

- Forgetting complements are relative to the same universe.
- Treating `not not P -> P` as constructive without checking the logic context.
- Proving only one inclusion.
- Confusing `(A^c)^c = A` with `A^c = A`.
- Using the theorem before proving it.

## What This Unlocks

Complement involution is the other half of complement as an order-reversing
symmetry.  Together with De Morgan's laws, it powers open/closed duality,
finite set algebra, and later sigma-algebra closure under complements.
