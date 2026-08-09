# 010: Existence and Uniqueness of Power Set's Output

Target: `thm:power-set-output-exists-unique`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-power-set-output-exists-unique.tex`

Status: ready for handwritten proof, then LaTeX population.  A typed relative
power-set Lean stub now exists.

## Statement

For any set `A`, there exists a unique set `P` whose members are exactly the
subsets of `A`:

```text
forall A,
  exists! P, forall S,
    S in P iff S subset A.
```

## Dependencies

- `ax:power-set`: for every set `A`, there exists a set containing exactly the
  subsets of `A`.
- `ax:extensionality`: two sets are equal iff they have the same elements.
- `def:subset`: `S subset A` means every element of `S` is an element of `A`.

## Plain-Language Reading

The power set moves one level up.  The elements of `P(A)` are not the elements
of `A`; they are the subsets of `A`.

So if:

```text
x in A
```

talks about ordinary elements, then:

```text
S in P(A)
```

talks about sets `S` satisfying `S subset A`.

This theorem is the doorway from manipulating individual sets to manipulating
families of subsets.

## Proof Skeleton

1. Let `A` be an arbitrary set.
2. Use the Axiom of Power Set to choose a set `P` such that for every `S`,
   `S in P iff S subset A`.
3. To prove uniqueness, let `P'` be another set satisfying the same membership
   profile.
4. Show `P' = P` by Extensionality.
5. For arbitrary `S`, prove `S in P' iff S in P`.
6. If `S in P'`, use the profile for `P'` to get `S subset A`, then use the
   profile for `P` to conclude `S in P`.
7. Conversely, if `S in P`, use the profile for `P` to get `S subset A`, then
   use the profile for `P'` to conclude `S in P'`.
8. Therefore the candidates have the same members, so Extensionality gives
   `P' = P`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State the exact membership profile of `P(A)`.
2. Explain why elements of `P(A)` are subsets of `A`, not elements of `A`.
3. Expand `S subset A` into an elementwise implication.
4. Prove uniqueness by comparing two witnesses `P` and `P'`.
5. Explain why this theorem turns collections of subsets into legitimate sets.
6. Connect this to later families: topologies, sigma-algebras, and filters are
   collections of subsets, hence live inside a power set.

## Formal Proof Draft

This is the proof shape to reproduce by hand before the LaTeX proof file is
populated:

```text
Let A be an arbitrary set.  By the Axiom of Power Set, choose a set P such
that, for every set S, S is an element of P iff S is a subset of A.  We prove
that P is unique with this property.

Let P' be any other set with the same membership profile.  By Extensionality,
it is enough to show that P' and P have the same elements.  Let S be arbitrary.

If S is an element of P', then the membership profile for P' gives that S is a
subset of A.  The membership profile for P then gives that S is an element of
P.  Conversely, if S is an element of P, then the membership profile for P
gives that S is a subset of A.  The membership profile for P' then gives that
S is an element of P'.  Hence S in P' iff S in P for every S.  By
Extensionality, P' = P.

Therefore, for arbitrary A, there exists a unique set P whose elements are
exactly the subsets of A.  Since A was arbitrary, the claim holds for every A.
```

## Lean Formalization

Current checked Lean target after restart:

- `LRA.VolumeI.Set.RelativePowerSetExistsUnique`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\PowerSets.lean
```

Typed-set analogue:

```text
forall Ambient : LRASet Alpha,
  exists powerSet : LRASet (LRASet Alpha),
    (forall Subset : LRASet Alpha,
      Member Subset powerSet iff Subset subset Ambient) and
      forall other : LRASet (LRASet Alpha),
        (forall Subset : LRASet Alpha,
          Member Subset other iff Subset subset Ambient) ->
            other = powerSet
```

For the active typed-set Lean target, existence is supplied by
`RelativePowerSet Ambient`, and uniqueness is proved by extensionality for
typed sets over the carrier `LRASet Alpha`.

## Common Failure Modes

- Treating elements of `P(A)` as elements of `A`.
- Forgetting that `S` ranges over sets.
- Proving only that every member of `P` is a subset of `A`, not the reverse.
- Forgetting uniqueness by Extensionality.
- Confusing the absolute typed power set of a carrier with the relative power
  set of an ambient set.

## What This Unlocks

Power sets make families of subsets into mathematical objects:

```text
Topology on X        subset P(X)
Set algebra on X     subset P(X)
Sigma-algebra on X   subset P(X)
Filter on X          subset P(X)
```

This is the bridge from basic set operations into the Volume IV set-algebra
toolkit.
