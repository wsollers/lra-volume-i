# 027: Subset Absorption Criteria

Target: `thm:subset-absorption-criteria`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-subset-absorption-criteria.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs now exist for both equivalences.

## Statement

For sets `A` and `B`:

```text
A subset B <-> A union B = B
A subset B <-> A intersection B = A
```

## Dependencies

- `def:subset`: `A subset B` means every member of `A` is a member of `B`.
- `def:set-equality`: equality is checked by same members or mutual inclusion.
- `def:union`: membership is disjunction.
- `def:intersection`: membership is conjunction.
- `ax:extensionality`: to turn elementwise equivalence into set equality.

## Plain-Language Reading

If `A` is already contained in `B`, then adding `A` to `B` by union changes
nothing:

```text
A union B = B
```

Likewise, intersecting `B` with the smaller set `A` leaves exactly `A`:

```text
A intersection B = A
```

These are absorption tests for inclusion.  They let us recognize subset
relations from equations.

## Proof Skeleton

For `A subset B <-> A union B = B`:

1. Assume `A subset B`.
2. Use extensionality to prove `A union B = B`.
3. If `x in A union B`, split cases.  The `A` case enters `B` by subset; the
   `B` case is immediate.
4. Conversely, if `x in B`, then `x in A union B` by the right branch.
5. For the reverse implication, assume `A union B = B`.
6. To prove `A subset B`, let `x in A`.
7. Then `x in A union B`, hence by the equality `x in B`.

For `A subset B <-> A intersection B = A`:

1. Assume `A subset B`.
2. Use extensionality to prove `A intersection B = A`.
3. If `x in A intersection B`, keep `x in A`.
4. Conversely, if `x in A`, use subset to get `x in B`, then build
   `x in A intersection B`.
5. For the reverse implication, assume `A intersection B = A`.
6. To prove `A subset B`, let `x in A`.
7. By equality, `x in A intersection B`, so extract `x in B`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State both absorption criteria for subset inclusion.
2. Prove the forward direction of the union criterion by cases.
3. Prove the reverse direction of the union criterion by inserting into the
   union and rewriting by equality.
4. Prove the forward direction of the intersection criterion by pairing
   `x in A` with `x in B`.
5. Prove the reverse direction of the intersection criterion by extracting the
   second component.
6. Explain why these are criteria for inclusion, not just algebraic identities.

## Formal Proof Draft

```text
Assume A subset B.  To prove A union B = B, use extensionality.  If x is in
A union B, then x is in A or x is in B.  In the first case, A subset B gives
x in B; in the second case, x in B already.  Conversely, if x is in B, then x
is in A union B.  Thus A union B = B.  Conversely, if A union B = B and x is in
A, then x is in A union B, hence x is in B.  Therefore A subset B.

Assume A subset B.  To prove A intersection B = A, use extensionality.  If x
is in A intersection B, then x is in A.  Conversely, if x is in A, then
A subset B gives x in B, so x is in A intersection B.  Conversely, if
A intersection B = A and x is in A, then x is in A intersection B, so x is in
B.  Therefore A subset B.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.Operations.Laws.SubsetIffUnionEqRight`
- `LRA.VolumeI.Set.Operations.Laws.SubsetIffIntersectionEqLeft`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\SubsetCriteria.lean
```

Typed-set analogues:

```text
Subset A B <-> Union A B = B
Subset A B <-> Intersection A B = A
```

## Common Failure Modes

- Reversing the union criterion into `A union B = A`.
- Reversing the intersection criterion into `A intersection B = B`.
- Forgetting to use equality in the reverse implication.
- Treating an equation as if it automatically gives an elementwise rewrite
  without saying why.
- Proving only one of the two criteria.

## What This Unlocks

These criteria convert between order statements and equations.  They are used
constantly in lattice theory, Boolean algebra, topology, and measure when an
inclusion is easier to prove or recognize as an absorption identity.
