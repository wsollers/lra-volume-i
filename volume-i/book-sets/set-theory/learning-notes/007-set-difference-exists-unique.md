# 007: Existence and Uniqueness of Set Difference

Target: `cor:set-difference-exists-unique`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-set-difference-exists-unique.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs now exist.

## Statement

For any sets `A` and `B`, there exists a unique set `C` whose members are
exactly the elements of `A` that are not elements of `B`:

```text
forall A, forall B,
  exists! C, forall x,
    x in C iff (x in A and x notin B).
```

The source text introduces this set by separation:

```text
A \ B := {x in A | x notin B}.
```

## Dependencies

- `thm:separation-output-exists-unique`: licenses bounded set-builder
  formation.
- `ax:extensionality`: used implicitly through Separation's uniqueness, and
  directly if proving the membership-profile version.

## Plain-Language Reading

Set difference is the subset of `A` cut out by the property "is not a member of
`B`."  It keeps the part of `A` outside `B`.

The membership rule is:

```text
x in A \ B iff x in A and x notin B.
```

The operation is asymmetric.  Usually `A \ B` and `B \ A` are different sets.

## Proof Skeleton

1. Let `A` and `B` be arbitrary sets.
2. Apply Separation to the ambient set `A` with the formula
   `phi(x) := x notin B`.
3. Obtain a unique set `C` such that for every `x`,
   `x in C iff (x in A and x notin B)`.
4. Define `A \ B := C`.
5. If proving uniqueness directly, let `C'` be another set with the same
   membership profile.
6. Use Extensionality: for arbitrary `x`, prove `x in C' iff x in C`.
7. Transfer membership through the shared profile
   `x in A and x notin B` in both directions.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. Identify the ambient set used for Separation.
2. Identify the predicate used for Separation.
3. State the exact membership profile of `A \ B`.
4. Explain why `A \ B` is generally not the same as `B \ A`.
5. Explain why the output is automatically a subset of `A`.
6. Anticipate the later order behavior: monotone in `A`, antitone in `B`.

## Formal Proof Draft

This is the proof shape to reproduce by hand before the LaTeX proof file is
populated:

```text
Let A and B be arbitrary sets.  Apply the separation-output theorem to the set
A and the formula x notin B.  This gives a unique set C such that, for every
object x, x is an element of C iff x is an element of A and x is not an element
of B.  Define A \ B to be this set.

The membership profile follows immediately from the defining property of the
separated subset: for every x, x is an element of A \ B iff x is an element of
A and x is not an element of B.

If C' is any other set with the same membership profile, then C' and A \ B have
the same elements.  By Extensionality, C' equals A \ B.  Therefore set
difference exists and is unique.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.TTSet.DifferenceExistsUnique`
- `LRA.VolumeI.Set.LRASet.DifferenceExistsUnique`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\TT\Set.lean
```

Typed-set analogue:

```text
forall left right : LRASet Alpha,
  exists differenceSet : LRASet Alpha,
    (forall element,
      Member element differenceSet iff
        Member element left and not Member element right) and
      forall other : LRASet Alpha,
        (forall element,
          Member element other iff
            Member element left and not Member element right) ->
              other = differenceSet
```

For the active typed-set Lean target, existence is supplied by
`Difference left right`, and uniqueness is proved by `LRASet.Extensionality`.

## Common Failure Modes

- Dropping the ambient condition `x in A`.
- Writing `x notin A and x in B`, which describes the wrong side.
- Treating difference as symmetric.
- Forgetting that the predicate for Separation is `x notin B`.
- Proving only subset containment rather than the full biconditional.

## What This Unlocks

Set difference is needed for relative complements, symmetric difference,
Boolean ring addition, and the later monotonicity/antitonicity laws:

```text
A_1 subset A_2  ->  A_1 \ B subset A_2 \ B
B_1 subset B_2  ->  A \ B_2 subset A \ B_1
```
