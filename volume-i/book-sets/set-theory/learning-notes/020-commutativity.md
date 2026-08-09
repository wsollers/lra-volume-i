# 020: Commutativity of Union and Intersection

Target: `thm:commutativity`

Proof file: `volume-i/book-sets/set-theory/proofs/families/prf-commutativity.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs already exist for both laws.

## Statement

For sets `A` and `B`:

```text
A union B = B union A
A intersection B = B intersection A
```

## Dependencies

- `ax:extensionality`: to prove equality of sets by equality of members.
- `def:union`: `x in A union B iff x in A or x in B`.
- `def:intersection`: `x in A intersection B iff x in A and x in B`.

## Plain-Language Reading

Union and intersection are symmetric operations.  The order of the two inputs
does not change which elements are selected.

For union, the proof swaps the two cases of an `or`.  For intersection, the
proof swaps the two components of an `and`.

## Proof Skeleton

For union:

1. Use extensionality.  Let `x` be arbitrary.
2. Prove `x in A union B <-> x in B union A`.
3. If `x in A union B`, split into cases:
   - if `x in A`, then `x in B union A` by the right branch;
   - if `x in B`, then `x in B union A` by the left branch.
4. Prove the converse the same way with `A` and `B` swapped.

For intersection:

1. Use extensionality.  Let `x` be arbitrary.
2. Prove `x in A intersection B <-> x in B intersection A`.
3. If `x in A intersection B`, extract `x in A` and `x in B`.
4. Reorder the pair as `x in B` and `x in A`.
5. Prove the converse the same way.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State both commutativity identities.
2. Start each equality proof with extensionality.
3. Use case analysis for union membership.
4. Use pair/projection manipulation for intersection membership.
5. Explain the logical forms `P or Q <-> Q or P` and `P and Q <-> Q and P`.
6. Avoid saying "obvious by symmetry" before the elementwise proof is owned.

## Formal Proof Draft

```text
For union, prove equality by extensionality.  Let x be arbitrary.  If x is in
A union B, then either x is in A or x is in B.  In the first case, x is in
B union A by the right inclusion; in the second case, x is in B union A by the
left inclusion.  The reverse implication is identical with A and B interchanged.

For intersection, prove equality by extensionality.  Let x be arbitrary.  If x
is in A intersection B, then x is in A and x is in B.  Therefore x is in B and
x is in A, so x is in B intersection A.  The reverse implication is identical.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.Operations.Laws.UnionCommutative`
- `LRA.VolumeI.Set.Operations.Laws.IntersectionCommutative`

Locations:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Union.lean
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Intersection.lean
```

Typed-set analogues:

```text
Union A B = Union B A
Intersection A B = Intersection B A
```

## Common Failure Modes

- Proving only one of union or intersection.
- Treating equality as one inclusion rather than two directions.
- Forgetting to swap the union cases.
- Forgetting to reorder both components of intersection membership.
- Skipping extensionality.

## What This Unlocks

Commutativity is one of the basic rewrite permissions for set algebra.  It is
small, but it appears everywhere: Boolean algebra, finite unions/intersections,
topological bases, sigma-algebras, and measure manipulations all assume this
law can be used without hesitation.
