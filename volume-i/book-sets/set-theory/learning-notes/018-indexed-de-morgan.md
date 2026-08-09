# 018: De Morgan's Laws for Indexed Families

Target: `thm:indexed-de-morgan`

Proof file: `volume-i/book-sets/set-theory/proofs/families/prf-indexed-de-morgan.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs already exist for both indexed laws.

## Statement

For an indexed family `{A_i}_{i in I}` of subsets of a fixed universe `U`:

```text
U \ union_{i in I} A_i = intersection_{i in I} (U \ A_i)
```

and, with the chapter's stated nonempty-index convention:

```text
if I != empty, then
  U \ intersection_{i in I} A_i = union_{i in I} (U \ A_i)
```

## Dependencies

- `def:indexed-family`: the family keeps each set `A_i` as its own set.
- `def:indexed-union`: `x in union_i A_i iff exists i, x in A_i`.
- `def:indexed-intersection`: `x in intersection_i A_i iff forall i, x in A_i`.
- `def:complement`: `x in U \ A_i iff x notin A_i`.
- `ax:extensionality`: to prove set equality by proving the same members.

## Plain-Language Reading

Indexed De Morgan is the quantifier version of binary De Morgan:

```text
not (exists i, P i) <-> forall i, not P i
not (forall i, P i) <-> exists i, not P i
```

The first law is the one used constantly in topology and measure: being outside
the union means being outside every set in the family.

## Convention Note

The chapter statement records a nonempty-index condition for the second law.
That is a useful guardrail when the text has not yet fully fixed empty
intersection and empty union conventions.

In the typed Lean model, the indexed operations are predicate-level operations:

```text
x in IndexedIntersection Family <-> forall i, x in Family i
x in IndexedUnion Family        <-> exists i, x in Family i
```

With those definitions, the empty-index case is handled by the logic of
`forall` and `exists`.

## Proof Skeleton

For the complement of the indexed union:

1. Use extensionality.  Let `x` be arbitrary.
2. Expand membership in the complement of the indexed union.
3. This gives `not exists i, x in A_i`.
4. To prove membership in the indexed intersection of complements, fix `i`.
5. Show `x notin A_i`; otherwise `exists i, x in A_i`.
6. Conversely, assume `x` belongs to every complement `U \ A_i`.
7. If `x` were in the indexed union, some `i` would have `x in A_i`.
8. Contradict the `i`th complement membership.

For the complement of the indexed intersection:

1. Use extensionality.  Let `x` be arbitrary.
2. Expand membership in the complement of the indexed intersection.
3. This gives `not forall i, x in A_i`.
4. Classically obtain `exists i, x notin A_i`.
5. Conclude `x` lies in the indexed union of complements.
6. Conversely, if `x` lies in some complement `U \ A_i`, then `x notin A_i`.
7. Therefore `x` cannot lie in every `A_i`.
8. Conclude `x` lies in the complement of the indexed intersection.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State both indexed De Morgan identities.
2. Translate indexed union into an existential statement.
3. Translate indexed intersection into a universal statement.
4. Prove `not exists -> forall not`.
5. Identify the classical step in `not forall -> exists not`.
6. Explain why indexed families must preserve the component sets instead of
   collapsing the family into one big union.

## Formal Proof Draft

```text
For the first identity, prove equality by extensionality.  Let x be arbitrary.
If x is outside the indexed union, then there is no index i with x in A_i.
Hence for each i, x is outside A_i, so x is in every complement U \ A_i.
Thus x lies in the indexed intersection of the complements.  Conversely, if x
lies in every complement U \ A_i and x were in the indexed union, then for some
i, x would lie in A_i, contradicting the i-th complement condition.

For the second identity, prove equality by extensionality.  If x is outside the
indexed intersection, then x is not in every A_i.  Classically, there is some
index i such that x is not in A_i, so x lies in the indexed union of the
complements.  Conversely, if x lies in some complement U \ A_i, then x is not
in A_i, so x cannot be in the indexed intersection.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.Operations.Laws.ComplementIndexedUnion`
- `LRA.VolumeI.Set.Operations.Laws.ComplementIndexedIntersection`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Indexed.lean
```

Typed-set analogues:

```text
Complement (IndexedUnion Family)
  = IndexedIntersection (fun i => Complement (Family i))

Complement (IndexedIntersection Family)
  = IndexedUnion (fun i => Complement (Family i))
```

## Common Failure Modes

- Collapsing the family into a single set and losing the index.
- Confusing `forall i, not P i` with `not forall i, P i`.
- Forgetting the classical logic step for the second identity.
- Ignoring the empty-index convention in prose.
- Proving only one direction of the set equality.

## What This Unlocks

Indexed De Morgan is the mechanism behind open/closed duality, compactness
arguments through covers and finite intersections, and measure-theoretic
continuity from above and below.  This is one of the first gates that directly
points toward topology and measure.
