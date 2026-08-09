# 023: Distributive Laws for Indexed Families

Target: `thm:indexed-distributivity`

Proof file: `volume-i/book-sets/set-theory/proofs/families/prf-indexed-distributivity.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs now exist for both indexed laws.

## Statement

For a fixed set `A` and an indexed family `{B_i}_{i in I}`:

```text
A intersection union_{i in I} B_i
  = union_{i in I} (A intersection B_i)
```

and, with the chapter's stated nonempty-index convention:

```text
if I != empty, then
  A union intersection_{i in I} B_i
    = intersection_{i in I} (A union B_i)
```

## Dependencies

- `def:indexed-family`: the expression `i |-> B_i` is preserved as a family.
- `def:indexed-union`: membership is existential over the index.
- `def:indexed-intersection`: membership is universal over the index.
- `def:union`: membership is disjunction.
- `def:intersection`: membership is conjunction.
- `ax:extensionality`: to prove set equality by proving identical members.

## Plain-Language Reading

Indexed distributivity pushes a fixed set operation through every member of a
family, then recombines the transformed family.

The first law says that to be in `A` and in at least one `B_i` is the same as
being in at least one set of the family `A intersection B_i`.

The second law is the universal version: to be in `A` or in every `B_i` is the
same as being in every set of the family `A union B_i`.

## Convention Note

The chapter statement includes `I != empty` for the second identity.  That
keeps the prose aligned with ordinary empty-intersection conventions before
they are fully fixed.

The typed Lean statement is written directly with the current definitions of
`IndexedUnion` and `IndexedIntersection`, so the empty-index behavior is
determined by the logical meanings of `exists` and `forall`.

## Proof Skeleton

For `A intersection union_i B_i`:

1. Use extensionality.  Let `x` be arbitrary.
2. Expand the left side into `x in A` and `exists i, x in B_i`.
3. Choose a witness `i`.
4. Combine `x in A` and `x in B_i` to get `x in A intersection B_i`.
5. Use the same `i` as the witness for the indexed union on the right.
6. Conversely, expand the right side to get some `i` with
   `x in A intersection B_i`.
7. Extract `x in A` and `x in B_i`.
8. Use `i` to show `x in union_i B_i`, then conclude the left side.

For `A union intersection_i B_i`:

1. Use extensionality.  Let `x` be arbitrary.
2. Expand the left side into `x in A` or `forall i, x in B_i`.
3. To prove membership in the indexed intersection on the right, fix `i`.
4. If `x in A`, then `x in A union B_i`.
5. If `forall i, x in B_i`, then in particular `x in B_i`, so
   `x in A union B_i`.
6. Conversely, assume `forall i, x in A union B_i`.
7. Classically split on whether `x in A`.
8. If not, each `x in A union B_i` forces `x in B_i`; conclude
   `x in intersection_i B_i`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State both indexed distributive identities.
2. Translate indexed union into an existential witness.
3. Translate indexed intersection into a universal condition.
4. Preserve the witness `i` in the first law.
5. Fix an arbitrary `i` when proving membership in an indexed intersection.
6. Explain why the family is transformed pointwise before being recombined.

## Formal Proof Draft

```text
For the first identity, prove equality by extensionality.  Let x be arbitrary.
If x is in A intersection union_i B_i, then x is in A and there exists an index
i such that x is in B_i.  For that same i, x is in A intersection B_i, so x is
in union_i (A intersection B_i).  Conversely, if x is in
union_i (A intersection B_i), then for some i, x is in A intersection B_i.
Thus x is in A and x is in B_i, so x is in A and in union_i B_i.

For the second identity, prove equality by extensionality.  If x is in
A union intersection_i B_i, then either x is in A or x is in every B_i.  To
show x is in intersection_i (A union B_i), fix i.  In the first case, x is in
A union B_i; in the second case, x is in B_i and hence in A union B_i.
Conversely, suppose x is in every A union B_i.  If x is in A, then x is in
A union intersection_i B_i.  If x is not in A, then each union membership
forces x in B_i, so x is in the indexed intersection and therefore in the left
side.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.Operations.Laws.IntersectionDistributesOverIndexedUnion`
- `LRA.VolumeI.Set.Operations.Laws.UnionDistributesOverIndexedIntersection`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Indexed.lean
```

Typed-set analogues:

```text
Intersection A (IndexedUnion Family)
  = IndexedUnion (fun i => Intersection A (Family i))

Union A (IndexedIntersection Family)
  = IndexedIntersection (fun i => Union A (Family i))
```

## Common Failure Modes

- Collapsing the family before applying the fixed operation.
- Losing the existential witness in the first law.
- Trying to prove indexed-intersection membership without fixing an index.
- Ignoring the chapter's nonempty-index convention in prose.
- Forgetting the classical split on `x in A` in the reverse direction of the
  second law.

## What This Unlocks

Indexed distributivity is one of the technical engines for topology and
measure.  It is how fixed intersections interact with arbitrary unions and how
fixed unions interact with arbitrary intersections, which is exactly the shape
of many closure and generated-structure arguments.
