# 003: Existence and Uniqueness of Union's Output

Target: `thm:union-output-exists-unique`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-union-output-exists-unique.tex`

Status: ready for handwritten proof, then LaTeX population.  A typed indexed
union Lean stub now exists.  The older ZFC semantic-reading name is archived
and should not be treated as active restart evidence.

## Statement

For any set `x`, there exists a unique set `U` whose elements are exactly the
elements of members of `x`:

```text
forall x,
  exists! U, forall z,
    z in U iff exists w, w in x and z in w.
```

## Dependencies

- `ax:union`: for every set `x`, there exists a set containing exactly the
  elements of members of `x`.
- `ax:extensionality`: two sets are equal iff they have the same elements.

## Plain-Language Reading

The Union axiom flattens one membership layer.  If `x` is a set whose elements
are themselves sets, then `bigcup x` collects the objects that occur inside at
least one member of `x`.

Existence comes from the Union axiom.  Uniqueness comes from Extensionality:
two candidates are equal because they have the same membership test,
`z belongs to some member of x`.

## Proof Skeleton

1. Let `x` be an arbitrary set.
2. Use the Axiom of Union to choose a set `U` such that for every `z`,
   `z in U iff exists w, w in x and z in w`.
3. To prove uniqueness, let `U'` be another set satisfying the same membership
   profile.
4. Show `U' = U` by Extensionality.
5. For arbitrary `z`, prove `z in U' iff z in U`.
6. If `z in U'`, use the profile for `U'` to obtain a witness `w` with
   `w in x` and `z in w`; then use the profile for `U` to conclude `z in U`.
7. Conversely, if `z in U`, use the profile for `U` to obtain such a witness
   `w`; then use the profile for `U'` to conclude `z in U'`.
8. Therefore the candidates have the same members, so Extensionality gives
   `U' = U`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State the membership profile of `bigcup x`.
2. Explain why the theorem flattens a set of sets by one level.
3. Keep the element variable `z` distinct from the witness set `w`.
4. Use the existential witness correctly in both directions of the uniqueness
   proof.
5. Explain why uniqueness is not part of the Union axiom by itself; it is
   supplied by Extensionality.
6. Say how this theorem combines with Pairing to define binary union.

## Formal Proof Draft

This is the proof shape to reproduce by hand before the LaTeX proof file is
populated:

```text
Let x be an arbitrary set.  By the Axiom of Union, choose a set U such that,
for every object z, z is an element of U iff there exists a set w such that
w is an element of x and z is an element of w.  We prove that U is unique with
this property.

Let U' be any other set with the same membership profile.  By Extensionality,
it is enough to show that U' and U have the same elements.  Let z be arbitrary.

If z is an element of U', then the membership profile for U' gives a witness
w such that w is an element of x and z is an element of w.  The membership
profile for U then gives z is an element of U.  Conversely, if z is an element
of U, then the membership profile for U gives a witness w such that w is an
element of x and z is an element of w.  The membership profile for U' then
gives z is an element of U'.  Thus z in U' iff z in U for every z.  By
Extensionality, U' = U.

Therefore, for arbitrary x, there exists a unique set U whose elements are
exactly the elements of members of x.  Since x was arbitrary, the claim holds
for every x.
```

## Lean Formalization

Current checked Lean target after restart:

- `LRA.VolumeI.Set.IndexedUnionExistsUnique`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Families.lean
```

Typed-family analogue:

```text
forall Family : IndexedFamily Index Alpha,
  exists unionSet : LRASet Alpha,
    (forall element,
      Member element unionSet iff
        exists IndexValue, Member element (Family IndexValue)) and
      forall other : LRASet Alpha,
        (forall element,
          Member element other iff
            exists IndexValue, Member element (Family IndexValue)) ->
              other = unionSet
```

This is not literally the same formal object as the ZFC union axiom.  The source
theorem uses one set `x` whose members are sets.  The active typed Lean restart
uses an indexed family `Family : Index -> LRASet Alpha`.  Pedagogically, both
express the same operating rule: membership in a union is membership in at
least one member of the family.

For the active typed-set Lean target, existence is supplied by
`IndexedUnion Family`, and uniqueness is proved by `LRASet.Extensionality`.

## Common Failure Modes

- Forgetting the witness `w` in the existential condition.
- Reversing the membership condition into `w in z` instead of `z in w`.
- Treating `bigcup x` as binary union before binary union has been derived.
- Proving only existence from the Union axiom and skipping uniqueness by
  Extensionality.
- Confusing the ZFC set-indexed union with a typed indexed union; they play the
  same role, but the encodings are different.

## What This Unlocks

Once this theorem is owned, the notation `bigcup x` is licensed.  Together with
pairing, it yields binary union:

```text
A union B := bigcup {A, B}.
```

This is the first place where the chapter clearly moves from primitive
axiom-licensed outputs to derived operations.
