# 021: Associativity of Union and Intersection

Target: `thm:associativity`

Proof file: `volume-i/book-sets/set-theory/proofs/families/prf-associativity.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs already exist for both laws.

## Statement

For sets `A`, `B`, and `C`:

```text
(A union B) union C = A union (B union C)
(A intersection B) intersection C = A intersection (B intersection C)
```

## Dependencies

- `ax:extensionality`: to prove equality of sets by equality of members.
- `def:union`: membership is nested disjunction.
- `def:intersection`: membership is nested conjunction.

## Plain-Language Reading

Associativity says parentheses do not matter for repeated unions or repeated
intersections.  The underlying membership condition is the same:

```text
x in A or x in B or x in C
x in A and x in B and x in C
```

The proof is the disciplined version of "just reparenthesize it."

## Proof Skeleton

For union:

1. Use extensionality.  Let `x` be arbitrary.
2. Expand `x in (A union B) union C`.
3. This gives either `x in A union B` or `x in C`.
4. If `x in A union B`, split again into `x in A` or `x in B`.
5. Rebuild membership in `A union (B union C)`.
6. Prove the reverse direction by the same nested case analysis.

For intersection:

1. Use extensionality.  Let `x` be arbitrary.
2. Expand `x in (A intersection B) intersection C`.
3. This gives `(x in A and x in B)` and `x in C`.
4. Reassociate the conjunction into `x in A` and `(x in B and x in C)`.
5. Rebuild membership in `A intersection (B intersection C)`.
6. Prove the reverse direction by reversing the grouping.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State both associativity identities.
2. Expand each side into its element-membership condition.
3. Handle nested union membership by nested case analysis.
4. Handle nested intersection membership by regrouping conjunction data.
5. Explain why associativity permits finite unions/intersections without
   excessive parentheses.
6. Avoid using associativity as a rewrite before it has been proved in the
   current development.

## Formal Proof Draft

```text
For union, prove equality by extensionality.  Let x be arbitrary.  If x is in
(A union B) union C, then either x is in A union B or x is in C.  In the first
case, x is in A or x is in B.  If x is in A, then x is in
A union (B union C).  If x is in B, then x is in B union C and hence in
A union (B union C).  If x is in C, then x is in B union C and hence in
A union (B union C).  The reverse implication is analogous.

For intersection, prove equality by extensionality.  Let x be arbitrary.  If x
is in (A intersection B) intersection C, then x is in A and B, and also in C.
Thus x is in A and x is in B intersection C, so x is in
A intersection (B intersection C).  The reverse implication is obtained by
ungrouping x in A and x in B intersection C.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.Operations.Laws.UnionAssociative`
- `LRA.VolumeI.Set.Operations.Laws.IntersectionAssociative`

Locations:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Union.lean
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Intersection.lean
```

Typed-set analogues:

```text
Union (Union A B) C = Union A (Union B C)
Intersection (Intersection A B) C = Intersection A (Intersection B C)
```

## Common Failure Modes

- Treating nested union membership as a flat three-way disjunction too early.
- Forgetting one branch of the union case split.
- Losing one membership component in the intersection proof.
- Proving only union associativity and assuming intersection follows.
- Using commutativity when associativity alone is enough.

## What This Unlocks

Associativity lets later text write finite unions and intersections without
constant parenthetical clutter.  It is also the first step toward finite
set-algebra normalization, which later supports algebras of sets,
topological bases, and sigma-algebra generation.
