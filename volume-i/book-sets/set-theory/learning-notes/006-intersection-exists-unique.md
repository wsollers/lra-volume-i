# 006: Existence and Uniqueness of Intersection

Target: `cor:intersection-exists-unique`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-intersection-exists-unique.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs now exist.

## Statement

For any sets `A` and `B`, there exists a unique set `C` whose members are
exactly the elements common to `A` and `B`:

```text
forall A, forall B,
  exists! C, forall x,
    x in C iff (x in A and x in B).
```

The source text introduces this set by separation:

```text
A intersection B := {x in A | x in B}.
```

## Dependencies

- `thm:separation-output-exists-unique`: licenses bounded set-builder
  formation.
- `ax:extensionality`: used implicitly through Separation's uniqueness, and
  directly if proving the membership-profile version.

## Plain-Language Reading

Intersection is the subset of `A` cut out by the property "is also a member of
`B`."  This is why Separation is the right parent theorem: we start with an
ambient set `A`, then keep precisely the elements satisfying the predicate
`x in B`.

The resulting membership rule is the familiar one:

```text
x in A intersection B iff x in A and x in B.
```

## Proof Skeleton

1. Let `A` and `B` be arbitrary sets.
2. Apply Separation to the ambient set `A` with the formula `phi(x) := x in B`.
3. Obtain a unique set `C` such that for every `x`,
   `x in C iff (x in A and x in B)`.
4. Define `A intersection B := C`.
5. If proving uniqueness directly, let `C'` be another set with the same
   membership profile.
6. Use Extensionality: for arbitrary `x`, prove `x in C' iff x in C`.
7. Transfer membership through the shared profile
   `x in A and x in B` in both directions.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. Identify the ambient set used for Separation.
2. Identify the predicate used for Separation.
3. State why no new axiom is needed beyond Separation.
4. Derive the membership profile of `A intersection B`.
5. Explain why the construction is symmetric even though the definition uses
   `A` as the ambient set.
6. Distinguish intersection from pair-set formation and binary union.

## Formal Proof Draft

This is the proof shape to reproduce by hand before the LaTeX proof file is
populated:

```text
Let A and B be arbitrary sets.  Apply the separation-output theorem to the set
A and the formula x in B.  This gives a unique set C such that, for every
object x, x is an element of C iff x is an element of A and x is an element of
B.  Define A intersection B to be this set.

The membership profile follows immediately from the defining property of the
separated subset: for every x, x is an element of A intersection B iff
x is an element of A and x is an element of B.

If C' is any other set with the same membership profile, then C' and
A intersection B have the same elements.  By Extensionality, C' equals
A intersection B.  Therefore the intersection exists and is unique.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.TTSet.IntersectionExistsUnique`
- `LRA.VolumeI.Set.LRASet.IntersectionExistsUnique`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\TT\Set.lean
```

Typed-set analogue:

```text
forall left right : LRASet Alpha,
  exists intersectionSet : LRASet Alpha,
    (forall element,
      Member element intersectionSet iff
        Member element left and Member element right) and
      forall other : LRASet Alpha,
        (forall element,
          Member element other iff
            Member element left and Member element right) ->
              other = intersectionSet
```

For the active typed-set Lean target, existence is supplied by
`Intersection left right`, and uniqueness is proved by `LRASet.Extensionality`.

## Common Failure Modes

- Forgetting that intersection is derived from Separation.
- Choosing the wrong predicate; it should be `x in B`.
- Dropping the ambient condition `x in A`.
- Saying symmetry is obvious before proving or recalling commutativity.
- Proving only one inclusion instead of the full membership biconditional.

## What This Unlocks

Intersection becomes the second basic binary operation.  It is needed for
finite set algebra, distributivity, complements, De Morgan laws, finite
intersection property arguments, and eventually topology.
