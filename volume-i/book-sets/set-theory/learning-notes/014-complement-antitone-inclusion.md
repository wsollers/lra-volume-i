# 014: Complement is Inclusion-Antitone

Target: `thm:complement-antitone-inclusion`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-complement-antitone-inclusion.tex`

Status: ready for handwritten proof, then LaTeX population.  A typed-set Lean
stub now exists.

## Statement

Let complements be taken relative to a fixed ambient set `U`.  If
`A subset B subset U`, then:

```text
B^c subset A^c.
```

Equivalently, using relative complement notation:

```text
A subset B -> U \ B subset U \ A.
```

## Dependencies

- `def:subset`: to prove inclusion, take an arbitrary element.
- `def:complement`: `x in A^c iff x in U and x notin A`.
- `cor:relative-complement-exists-unique`: complement is relative to `U`.

## Plain-Language Reading

Complement reverses inclusion.  If `A` is inside `B`, then being outside `B`
is a stronger condition than being outside `A`.

The picture is:

```text
A smaller than B
outside B smaller than outside A
```

This is the first explicit antitone law in the queue.

## Proof Skeleton

1. Fix the ambient set `U`.
2. Assume `A subset B`.
3. To prove `B^c subset A^c`, let `x in B^c`.
4. By relative complement membership, get `x in U` and `x notin B`.
5. To prove `x in A^c`, keep `x in U` and prove `x notin A`.
6. Suppose for contradiction that `x in A`.
7. Since `A subset B`, get `x in B`.
8. This contradicts `x notin B`.
9. Therefore `x notin A`, so `x in A^c`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State the ambient set before using complement notation.
2. Explain why complement reverses inclusion.
3. Expand `x in B^c` as `x in U and x notin B`.
4. Prove `x notin A` by contradiction using `A subset B`.
5. Preserve the ambient membership `x in U`.
6. Say why this is antitone, not monotone.

## Formal Proof Draft

```text
Fix an ambient set U and assume A subset B.  To prove B^c subset A^c, let x be
an arbitrary element of B^c.  Since complements are relative to U, x is an
element of U and x is not an element of B.

We must prove that x is an element of A^c.  The ambient membership x in U is
already known, so it remains to prove x is not an element of A.  Suppose toward
a contradiction that x is an element of A.  Since A subset B, x is an element
of B.  This contradicts x notin B.  Therefore x notin A.

Thus x is in U and x is not in A, so x is in A^c.  Hence B^c subset A^c.
```

## Lean Formalization

Current checked Lean target after restart:

- `LRA.VolumeI.Set.Operations.Laws.ComplementAntitoneInclusion`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Complement.lean
```

Typed-set analogue:

```text
forall Ambient Left Right : LRASet Alpha,
  Subset Left Right ->
    Subset (RelativeComplement Ambient Right)
      (RelativeComplement Ambient Left)
```

The explicit assumptions `Left subset Ambient` and `Right subset Ambient` are
part of the source context for complement notation.  The Lean set-difference
formulation only needs `Left subset Right` to prove the displayed inclusion.

## Common Failure Modes

- Proving `A^c subset B^c`, which is the wrong direction.
- Forgetting the ambient membership `x in U`.
- Treating complement as absolute.
- Trying to use `A subset B` on `x notin B`; instead use contradiction.
- Calling the operation monotone instead of antitone.

## What This Unlocks

Complement antitonicity is the order-theoretic engine behind De Morgan laws,
closed/open duality in topology, and complement closure in set algebras and
sigma-algebras.
