# 028: Idempotency of Union and Intersection

Target: `thm:idempotency`

Proof file: `volume-i/book-sets/set-theory/proofs/families/prf-idempotency.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs already exist for both laws.

## Statement

For any set `A`:

```text
A union A = A
A intersection A = A
```

## Dependencies

- `ax:extensionality`: to prove equality of sets by equality of members.
- `def:union`: `x in A union A iff x in A or x in A`.
- `def:intersection`: `x in A intersection A iff x in A and x in A`.

## Plain-Language Reading

Repeating the same set does not change a union or an intersection.  Union says
"in `A` or in `A`," which is just "in `A`."  Intersection says "in `A` and in
`A`," which is also just "in `A`."

## Proof Skeleton

For `A union A = A`:

1. Use extensionality.  Let `x` be arbitrary.
2. If `x in A union A`, split into cases.
3. Both cases give `x in A`.
4. Conversely, if `x in A`, then `x in A union A` by either branch.

For `A intersection A = A`:

1. Use extensionality.  Let `x` be arbitrary.
2. If `x in A intersection A`, extract either component to get `x in A`.
3. Conversely, if `x in A`, pair the fact with itself to get
   `x in A intersection A`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State both idempotency identities.
2. Translate union idempotency into `P or P <-> P`.
3. Translate intersection idempotency into `P and P <-> P`.
4. Prove union idempotency by case split.
5. Prove intersection idempotency by duplicating and extracting membership.
6. Explain why idempotency is a Boolean/lattice law, not an arithmetic law.

## Formal Proof Draft

```text
For union, prove equality by extensionality.  Let x be arbitrary.  If x is in
A union A, then x is in A or x is in A, so in either case x is in A.
Conversely, if x is in A, then x is in A union A.  Therefore A union A = A.

For intersection, prove equality by extensionality.  Let x be arbitrary.  If x
is in A intersection A, then x is in A.  Conversely, if x is in A, then x is
in A and x is in A, so x is in A intersection A.  Therefore
A intersection A = A.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.Operations.Laws.UnionIdempotent`
- `LRA.VolumeI.Set.Operations.Laws.IntersectionIdempotent`

Locations:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Union.lean
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Intersection.lean
```

Typed-set analogues:

```text
Union A A = A
Intersection A A = A
```

## Common Failure Modes

- Confusing idempotency with identity laws involving `empty` or `universe`.
- Forgetting to prove both union and intersection.
- Treating repeated set occurrence like arithmetic multiplication by two.
- Skipping extensionality.
- Using absorption before recognizing this simpler special case.

## What This Unlocks

Idempotency is a core Boolean algebra law.  It supports finite set-expression
simplification, lattice reasoning, and later closure arguments where repeated
members of a finite family should not matter.
