# 008: Existence and Uniqueness of Symmetric Difference

Target: `cor:symmetric-difference-exists-unique`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-symmetric-difference-exists-unique.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs now exist.

## Statement

For any sets `A` and `B`, there exists a unique set `C` whose members are
exactly the elements belonging to exactly one of `A` and `B`:

```text
forall A, forall B,
  exists! C, forall x,
    x in C iff
      ((x in A and x notin B) or (x in B and x notin A)).
```

The source text constructs this set by:

```text
A triangle B := (A \ B) union (B \ A).
```

## Dependencies

- `cor:set-difference-exists-unique`: licenses `A \ B` and `B \ A`.
- `cor:binary-union-exists-unique`: licenses the union of those two
  differences.

## Plain-Language Reading

Symmetric difference keeps the elements that appear on exactly one side.  It
throws away elements that appear in both sets and also throws away elements
that appear in neither set.

The construction and the membership profile are different views of the same
object:

```text
construction:       (A \ B) union (B \ A)
membership profile: (x in A and x notin B) or (x in B and x notin A)
```

## Proof Skeleton

1. Let `A` and `B` be arbitrary sets.
2. Use set difference to construct `A \ B`.
3. Use set difference to construct `B \ A`.
4. Use binary union to construct `(A \ B) union (B \ A)`.
5. Define `A triangle B` to be this union.
6. To derive the membership profile, let `x` be arbitrary.
7. Expand membership in the union:
   `x in (A \ B) union (B \ A)` iff
   `x in A \ B or x in B \ A`.
8. Expand each difference:
   `x in A \ B` iff `x in A and x notin B`;
   `x in B \ A` iff `x in B and x notin A`.
9. Combine these equivalences to obtain the exactly-one-side profile.
10. Uniqueness follows because the construction is a composition of unique
    outputs, or directly by Extensionality from the final membership profile.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State the construction `(A \ B) union (B \ A)`.
2. State the expanded membership profile.
3. Explain why the operation is symmetric even though each difference is not.
4. Expand union membership before expanding difference membership.
5. Explain why elements in `A intersection B` are excluded.
6. Explain why elements in neither `A` nor `B` are excluded.

## Formal Proof Draft

This is the proof shape to reproduce by hand before the LaTeX proof file is
populated:

```text
Let A and B be arbitrary sets.  By the set-difference theorem, the sets
A \ B and B \ A exist and are unique.  By the binary-union theorem, the set
(A \ B) union (B \ A) exists and is unique.  Define A triangle B to be this
set.

Let x be arbitrary.  By the membership rule for binary union, x is an element
of A triangle B iff x is an element of A \ B or x is an element of B \ A.  By
the membership rule for set difference, this is equivalent to saying that
(x is an element of A and x is not an element of B) or
(x is an element of B and x is not an element of A).

Thus A triangle B has exactly the elements belonging to exactly one of A and B.
If C is any other set with this same membership profile, then C and
A triangle B have the same elements.  By Extensionality, C = A triangle B.
Therefore symmetric difference exists and is unique.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.TTSet.SymmetricDifference`
- `LRA.VolumeI.Set.TTSet.SymmetricDifferenceExistsUnique`
- `LRA.VolumeI.Set.LRASet.SymmetricDifference`
- `LRA.VolumeI.Set.LRASet.SymmetricDifferenceExistsUnique`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\TT\Set.lean
```

Typed-set analogue:

```text
forall left right : LRASet Alpha,
  exists symmetricDifferenceSet : LRASet Alpha,
    (forall element,
      Member element symmetricDifferenceSet iff
        (Member element left and not Member element right) or
        (Member element right and not Member element left)) and
      forall other : LRASet Alpha,
        (forall element,
          Member element other iff
            (Member element left and not Member element right) or
            (Member element right and not Member element left)) ->
              other = symmetricDifferenceSet
```

For the active typed-set Lean target, existence is supplied by
`SymmetricDifference left right`, and uniqueness is proved by
`LRASet.Extensionality`.

## Common Failure Modes

- Writing ordinary union `A union B` instead of exclusive membership.
- Forgetting one of the two difference terms.
- Expanding `A \ B` as `x notin A and x in B`, which reverses the operation.
- Assuming uniqueness without either citing the unique component operations or
  using Extensionality on the expanded profile.
- Confusing symmetric difference with complement of intersection.

## What This Unlocks

Symmetric difference is the addition operation in the Boolean-ring viewpoint:

```text
A + B := A triangle B
A * B := A intersection B
```

Owning this theorem makes later Boolean algebra identities feel like ordinary
algebra rather than a pile of set diagrams.
