# 022: Distributive Laws

Target: `thm:distributivity`

Proof file: `volume-i/book-sets/set-theory/proofs/families/prf-distributivity.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs now exist for both laws.

## Statement

For sets `A`, `B`, and `C`:

```text
A intersection (B union C) = (A intersection B) union (A intersection C)
A union (B intersection C) = (A union B) intersection (A union C)
```

## Dependencies

- `ax:extensionality`: to prove equality of sets by equality of members.
- `def:union`: membership is disjunction.
- `def:intersection`: membership is conjunction.
- `cor:set-duality`: explains why the two identities are dual, though each
  should still be proved elementwise at this gate.

## Plain-Language Reading

Distributivity is the rule for pushing one set operation through another.

The first law says:

```text
x is in A and in at least one of B or C
```

is the same as:

```text
x is in both A and B, or x is in both A and C.
```

The second law is the dual statement with `union` and `intersection` swapped.

## Proof Skeleton

For `A intersection (B union C)`:

1. Use extensionality.  Let `x` be arbitrary.
2. Expand membership on the left as `x in A` and `(x in B or x in C)`.
3. Split on whether `x in B` or `x in C`.
4. In the first case, build `x in A intersection B`.
5. In the second case, build `x in A intersection C`.
6. Conclude membership in the union on the right.
7. Conversely, split membership in the right-hand union.
8. In either case, recover `x in A` and membership in `B union C`.

For `A union (B intersection C)`:

1. Use extensionality.  Let `x` be arbitrary.
2. Expand the left side as `x in A` or `(x in B and x in C)`.
3. If `x in A`, then `x` is in both `A union B` and `A union C`.
4. If `x in B and x in C`, then `x` is also in both unions.
5. Conversely, assume `x in A union B` and `x in A union C`.
6. Split on `x in A union B`.
7. If `x in A`, finish.
8. If `x in B`, split on `x in A union C`; either finish with `x in A` or
   combine `x in B` and `x in C`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State both distributive identities.
2. Translate the first law into `P and (Q or R) <-> (P and Q) or (P and R)`.
3. Translate the second law into `P or (Q and R) <-> (P or Q) and (P or R)`.
4. Carry all branches of the union case split.
5. Preserve repeated membership facts such as `x in A`.
6. Explain how distributivity enables normal forms for finite set expressions.

## Formal Proof Draft

```text
For the first identity, prove equality by extensionality.  Let x be arbitrary.
If x is in A intersection (B union C), then x is in A and x is in B union C.
If x is in B, then x is in A intersection B; if x is in C, then x is in
A intersection C.  Hence x is in the union of those two intersections.  The
reverse direction follows by splitting the right-hand union and rebuilding
x in A together with x in B union C.

For the second identity, prove equality by extensionality.  If x is in
A union (B intersection C), then either x is in A, in which case x is in both
A union B and A union C, or x is in B and C, in which case x is again in both
unions.  Conversely, if x is in both A union B and A union C, then either x is
in A, or x is in B and the second union gives x in A or x in C.  In the
remaining case, x is in B and C, so x is in A union (B intersection C).
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.Operations.Laws.IntersectionDistributesOverUnion`
- `LRA.VolumeI.Set.Operations.Laws.UnionDistributesOverIntersection`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Duality.lean
```

Typed-set analogues:

```text
Intersection A (Union B C) = Union (Intersection A B) (Intersection A C)
Union A (Intersection B C) = Intersection (Union A B) (Union A C)
```

## Common Failure Modes

- Losing the shared `x in A` in the first law.
- Forgetting that the second law requires a nested case split in the reverse
  direction.
- Proving only one distributive identity.
- Treating duality as a substitute for knowing the elementwise proof.
- Reversing one side of the equality.

## What This Unlocks

Distributivity is the main algebraic engine for rewriting finite set
expressions.  It prepares the ground for finite algebras of sets, normal forms,
topological bases, and the closure arguments behind generated algebras and
sigma-algebras.
