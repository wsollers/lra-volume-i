# 009: Existence and Uniqueness of Relative Complement

Target: `cor:relative-complement-exists-unique`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-relative-complement-exists-unique.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs now exist.

## Statement

Let `U` be a fixed ambient set.  For every set `A`, there exists a unique set
`C` whose members are exactly the elements of `U` that are not elements of `A`:

```text
forall A,
  exists! C, forall x,
    x in C iff (x in U and x notin A).
```

The source text introduces this relative complement by:

```text
A^c := U \ A.
```

## Dependencies

- `cor:set-difference-exists-unique`: licenses `U \ A`.

## Plain-Language Reading

Complement is not absolute in ZFC.  There is no set of "all things not in A"
because there is no universal set of all sets.  Complements are taken relative
to an already fixed ambient set `U`.

So `A^c` means:

```text
the elements of U that are outside A
```

not:

```text
everything in the universe of all mathematical objects that is outside A
```

## Proof Skeleton

1. Fix an ambient set `U`.
2. Let `A` be arbitrary.
3. Apply set-difference existence/uniqueness to `U` and `A`.
4. Obtain a unique set `C` such that for every `x`,
   `x in C iff (x in U and x notin A)`.
5. Define the relative complement of `A` in `U` by `A^c := U \ A`.
6. Uniqueness is inherited from set difference, or proved directly by
   Extensionality from the displayed membership profile.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State the ambient set before using complement notation.
2. Explain why ZFC has no absolute complement operation over all sets.
3. State `A^c := U \ A`.
4. State the membership profile `x in A^c iff x in U and x notin A`.
5. Explain why changing `U` changes the complement.
6. Connect this theorem to topology: complements are always relative to the
   underlying space.

## Formal Proof Draft

This is the proof shape to reproduce by hand before the LaTeX proof file is
populated:

```text
Fix an ambient set U.  Let A be an arbitrary set.  By the set-difference
theorem applied to U and A, the set U \ A exists and is unique.  Define the
relative complement of A in U, denoted A^c when U is understood, to be U \ A.

By the membership profile of set difference, for every object x, x is an
element of A^c iff x is an element of U and x is not an element of A.

If C is any other set with this membership profile, then C and A^c have the
same elements.  By Extensionality, C = A^c.  Therefore the relative complement
exists and is unique.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.TTSet.RelativeComplement`
- `LRA.VolumeI.Set.TTSet.RelativeComplementExistsUnique`
- `LRA.VolumeI.Set.LRASet.RelativeComplement`
- `LRA.VolumeI.Set.LRASet.RelativeComplementExistsUnique`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\TT\Set.lean
```

Typed-set analogue:

```text
forall ambient set : LRASet Alpha,
  exists complementSet : LRASet Alpha,
    (forall element,
      Member element complementSet iff
        Member element ambient and not Member element set) and
      forall other : LRASet Alpha,
        (forall element,
          Member element other iff
            Member element ambient and not Member element set) ->
              other = complementSet
```

For the active typed-set Lean target, existence is supplied by
`RelativeComplement ambient set`, and uniqueness is proved by
`LRASet.Extensionality`.

## Common Failure Modes

- Using complement notation before fixing the ambient set.
- Forgetting the condition `x in U`.
- Treating `A^c` as the set of all objects not in `A`.
- Confusing relative complement `U \ A` with set difference `A \ U`.
- Assuming different ambient sets give the same complement.

## What This Unlocks

Relative complement is the complement operation used in set algebras,
topologies, measurable spaces, and Borel sigma-algebras.  Closure under
complement always means complement relative to the underlying space.
