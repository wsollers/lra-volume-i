# 005: Existence and Uniqueness of Separation's Output

Target: `thm:separation-output-exists-unique`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-separation-output-exists-unique.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs now exist.

## Statement

Let `A` be a set and let `phi(x)` be a formula.  There exists a unique set `B`
whose members are exactly the members of `A` satisfying `phi`:

```text
forall A,
  exists! B, forall x,
    x in B iff (x in A and phi x).
```

## Dependencies

- `ax:separation`: for a formula `phi`, every set `A` has a subset containing
  exactly those members of `A` satisfying `phi`.
- `ax:extensionality`: two sets are equal iff they have the same elements.

## Plain-Language Reading

Separation is bounded set-builder formation.  It does not say that every
property determines a universal set of all objects satisfying it.  It says that
once an ambient set `A` is already available, we may carve out the part of `A`
whose elements satisfy a formula `phi`.

The bounded set-builder notation

```text
{x in A | phi x}
```

is licensed only after existence and uniqueness are proved.

## Proof Skeleton

1. Let `A` be an arbitrary set and fix a formula `phi(x)`.
2. Use the Axiom Schema of Separation to choose a set `B` such that for every
   `x`, `x in B iff (x in A and phi(x))`.
3. To prove uniqueness, let `B'` be another set satisfying the same membership
   profile.
4. Show `B' = B` by Extensionality.
5. For arbitrary `x`, prove `x in B' iff x in B`.
6. If `x in B'`, use the profile for `B'` to get `x in A and phi(x)`, then use
   the profile for `B` to conclude `x in B`.
7. Conversely, if `x in B`, use the profile for `B` to get
   `x in A and phi(x)`, then use the profile for `B'` to conclude `x in B'`.
8. Therefore the candidates have the same members, so Extensionality gives
   `B' = B`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State why Separation is bounded by an existing set `A`.
2. Explain why unrestricted comprehension would be dangerous here.
3. State the exact membership profile of `{x in A | phi x}`.
4. Prove uniqueness by comparing two witnesses `B` and `B'`.
5. Use both directions of the membership-profile biconditional correctly.
6. Explain how intersection and set difference are special cases of
   Separation.

## Formal Proof Draft

This is the proof shape to reproduce by hand before the LaTeX proof file is
populated:

```text
Let A be an arbitrary set and let phi(x) be a formula.  By the Axiom Schema of
Separation, choose a set B such that, for every object x, x is an element of B
iff x is an element of A and phi(x) holds.  We prove that B is unique with this
property.

Let B' be any other set with the same membership profile.  By Extensionality,
it is enough to show that B' and B have the same elements.  Let x be arbitrary.

If x is an element of B', then the membership profile for B' gives that x is
an element of A and phi(x) holds.  The membership profile for B then gives that
x is an element of B.  Conversely, if x is an element of B, then the membership
profile for B gives that x is an element of A and phi(x) holds.  The membership
profile for B' then gives that x is an element of B'.  Hence x in B' iff
x in B for every x.  By Extensionality, B' = B.

Therefore, for the fixed formula phi and arbitrary set A, there exists a unique
set B whose elements are exactly the elements of A satisfying phi.  Since A was
arbitrary, the claim holds for every A.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.TTSet.Separation`
- `LRA.VolumeI.Set.TTSet.SeparationExistsUnique`
- `LRA.VolumeI.Set.LRASet.Separation`
- `LRA.VolumeI.Set.LRASet.SeparationExistsUnique`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\TT\Set.lean
```

Typed-set analogue:

```text
forall ambient : LRASet Alpha,
forall property : Alpha -> Prop,
  exists separatedSet : LRASet Alpha,
    (forall element,
      Member element separatedSet iff
        Member element ambient and property element) and
      forall other : LRASet Alpha,
        (forall element,
          Member element other iff
            Member element ambient and property element) ->
              other = separatedSet
```

For the active typed-set Lean target, existence is supplied by
`Separation ambient property`, and uniqueness is proved by
`LRASet.Extensionality`.

## Common Failure Modes

- Forgetting that `phi` is fixed before the output set is formed.
- Dropping the bounded condition `x in A`.
- Treating Separation as unrestricted comprehension.
- Proving only that the separated set is a subset of `A`, not the exact
  biconditional membership profile.
- Using set-builder notation before the theorem has licensed it.

## What This Unlocks

Separation is the engine behind the next derived operations:

```text
A intersection B = {x in A | x in B}
A \ B          = {x in A | x notin B}
```

It is also the first serious guardrail against naive set comprehension.  This
is where the chapter starts training the habit "form subsets of known sets,
not sets of all things satisfying a property."
