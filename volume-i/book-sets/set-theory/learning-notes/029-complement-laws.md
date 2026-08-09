# 029: Complement Extreme and Complementarity Laws

Target: `thm:complement-laws`

Proof file: `volume-i/book-sets/set-theory/proofs/families/prf-complement-laws.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs now exist for all displayed laws.

## Statement

For a set `A` inside a fixed universe `U`:

```text
empty^c = U
U^c = empty
A union A^c = U
A^c union A = U
A intersection A^c = empty
A^c intersection A = empty
```

## Dependencies

- `ax:extensionality`: to prove equality of sets by equality of members.
- `def:empty-set`: no element belongs to the empty set.
- `def:complement`: `x in A^c iff x notin A`, relative to `U`.
- `def:union`: membership is disjunction.
- `def:intersection`: membership is conjunction.
- `def:subset`: the prose statement keeps `A` inside the fixed universe.

## Plain-Language Reading

Complement divides the universe into two pieces: the set and everything outside
the set.  Their union is the whole universe, and their intersection is empty.

The extreme cases say that the outside of nothing is everything, and the
outside of everything is nothing.

## Proof Skeleton

For `empty^c = U`:

1. Use extensionality.  Let `x` be arbitrary.
2. `x in empty^c` means `x notin empty`, which is always true.
3. Thus every ambient element is in `empty^c`.

For `U^c = empty`:

1. Use extensionality.  Let `x` be arbitrary.
2. `x in U^c` means `x notin U`.
3. But every ambient element is in `U`; contradiction.

For `A union A^c = U`:

1. Use extensionality.  Let `x` be arbitrary.
2. Classically split on whether `x in A`.
3. If yes, `x in A union A^c`.
4. If no, `x in A^c`, so again `x in A union A^c`.
5. The reverse inclusion is automatic because both sides live in `U`.

For `A intersection A^c = empty`:

1. Use extensionality.  Let `x` be arbitrary.
2. If `x in A intersection A^c`, then `x in A` and `x notin A`.
3. Contradiction, so no element belongs to the intersection.

The reversed-order union and intersection laws follow by the same proof or by
commutativity.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State the two complement extreme laws.
2. State both union complementarity orientations.
3. State both intersection disjointness orientations.
4. Explain why `A union A^c = U` uses excluded middle in ordinary classical
   set theory.
5. Explain why `A intersection A^c = empty` is contradiction.
6. Keep complements relative to a fixed universe throughout.

## Formal Proof Draft

```text
The complement of empty is U because no element is in empty, so every ambient
element is outside empty.  The complement of U is empty because no ambient
element is outside U.

For A union A^c = U, let x be an ambient element.  Either x is in A or not.  If
x is in A, then x is in the union.  If not, then x is in A^c and hence in the
union.  Conversely, every element of A union A^c is an ambient element.  The
law A^c union A = U is the same argument with the union branches reversed.

For A intersection A^c = empty, suppose x is in the intersection.  Then x is
in A and x is not in A, contradiction.  Hence the intersection has no elements.
The law A^c intersection A = empty is the same argument with the two
components reversed.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.Operations.Laws.ComplementEmpty`
- `LRA.VolumeI.Set.Operations.Laws.ComplementUniversal`
- `LRA.VolumeI.Set.Operations.Laws.UnionComplement`
- `LRA.VolumeI.Set.Operations.Laws.ComplementUnion`
- `LRA.VolumeI.Set.Operations.Laws.IntersectionComplement`
- `LRA.VolumeI.Set.Operations.Laws.ComplementIntersection`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Complement.lean
```

Typed-set analogues:

```text
Complement Empty = Universal
Complement Universal = Empty
Union A (Complement A) = Universal
Union (Complement A) A = Universal
Intersection A (Complement A) = Empty
Intersection (Complement A) A = Empty
```

## Common Failure Modes

- Forgetting that complement is relative to `U`.
- Proving `A union A^c = A` instead of `U`.
- Proving `A intersection A^c = A` instead of `empty`.
- Dropping the reversed-order versions required by the audit.
- Forgetting the classical case split for union complementarity.

## What This Unlocks

These laws make complement usable as a Boolean algebra operation.  They are
basic tools for open/closed duality, partitions by a predicate, set algebra,
and later sigma-algebra closure under complements.
