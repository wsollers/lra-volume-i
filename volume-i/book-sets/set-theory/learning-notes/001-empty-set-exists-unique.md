# 001: Existence and Uniqueness of the Empty Set

Target: `thm:empty-set-exists-unique`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-empty-set-exists-unique.tex`

Status: ready for handwritten proof, then LaTeX population.  A typed-set Lean
stub now exists; the untyped ZFC-object formalization remains future work.

## Statement

There exists a unique set `E` such that no object is an element of `E`:

```text
exists! E, forall x, x notin E.
```

## Dependencies

- `ax:empty-set`: there exists a set with no elements.
- `ax:extensionality`: two sets are equal iff they have the same elements.

## Plain-Language Reading

The Empty Set axiom gives at least one set with no members.  Extensionality
then says there cannot be two different such sets, because any two sets with no
members have exactly the same membership profile.

This is the first template for definitional licensing:

1. prove existence of an object satisfying the intended membership condition;
2. prove uniqueness by showing any two witnesses have the same elements;
3. introduce notation for the unique object.

## Proof Skeleton

1. Use the Axiom of Empty Set to choose a set `E` such that
   `forall x, x notin E`.
2. To prove uniqueness, suppose `E'` is another set such that
   `forall x, x notin E'`.
3. Show `E' = E` by Extensionality.
4. For arbitrary `x`, prove
   `x in E' iff x in E`.
5. Both sides are false:
   - `x in E'` contradicts `forall x, x notin E'`;
   - `x in E` contradicts `forall x, x notin E`.
6. Therefore the membership profiles agree for every `x`, so `E' = E`.
7. Conclude `exists! E, forall x, x notin E`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State exactly what the Empty Set axiom gives: existence only.
2. State exactly what Extensionality is used for: uniqueness only.
3. Explain why uniqueness cannot be obtained from the Empty Set axiom alone.
4. Given two witnesses `E` and `E'`, prove `E = E'` by taking an arbitrary
   object `x`.
5. Prove both implications in `x in E iff x in E'` by contradiction from the
   no-member hypotheses.
6. Say why the proof licenses the notation `empty`, rather than merely naming
   one arbitrary witness.

## Formal Proof Draft

This is the proof shape to reproduce by hand before the LaTeX proof file is
populated:

```text
By the Axiom of Empty Set, choose a set E such that no object is an element of E.
We prove that E is the unique set with this property.

Let E' be any set such that no object is an element of E'.  By Extensionality,
it is enough to prove that every object has the same membership relation to E'
and E.  Let x be arbitrary.  If x is in E', then this contradicts the fact that
E' has no elements; hence x is in E follows vacuously.  Conversely, if x is in
E, then this contradicts the fact that E has no elements; hence x is in E'
follows vacuously.  Thus x in E' iff x in E for every x.  By Extensionality,
E' = E.

Therefore there exists a unique set E such that no object is an element of E.
```

The tiny subtlety: the implications are not proving that a contradiction
somehow produces membership information mathematically.  They are using the
logical rule that from an impossible hypothesis, any implication with that
hypothesis is true.

## Common Failure Modes

- Proving only `exists E` and then introducing `empty` without uniqueness.
- Saying "both are empty, so they are equal" before Extensionality has been
  invoked.
- Forgetting that Extensionality requires a biconditional for every object, not
  just two one-sided nonmembership statements.
- Treating `empty` as already available before the theorem has licensed the
  notation.

## Handwritten Proof Prompt

Write the proof without symbolic shortcuts first:

> Let `E` be a set with no elements, supplied by the Empty Set axiom.  Now let
> `E'` be any other set with no elements.  To prove `E' = E`, it suffices by
> Extensionality to prove that every object belongs to `E'` iff it belongs to
> `E`.  But no object belongs to either set, so the two membership conditions
> are equivalent for every object.  Hence `E' = E`.

After writing that in your own words, convert it into the two-layer LaTeX proof
shape.

## Lean Formalization

Current checked Lean targets:

- `LRA.VolumeI.Set.TTSet.EmptySetExistsUnique`
- `LRA.VolumeI.Set.LRASet.EmptySetExistsUnique`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\TT\Set.lean
```

These are typed-set analogues of the source theorem:

```text
exists empty : TTSet Alpha,
  (forall element, not Member element empty) and
    forall other : TTSet Alpha,
      (forall element, not Member element other) -> other = empty
```

The source theorem itself is untyped/ZFC-flavored.  The active Lean restart does
not yet expose an object-level theorem of the form currently named in LaTeX:

```text
LRA.VolumeI.Set.ZFCSet.ZFCProvidesEmptySet
```

That name belongs to the older archived ZFC architecture and should not be
treated as a live proof target unless the ZFC object layer is rebuilt.

Expected proof pattern:

```text
obtain <E, hE> from empty_set_axiom
refine ExistsUnique.intro E hE ?unique
intro E' hE'
apply extensionality
intro x
constructor
  intro hx
  exact False.elim (hE' x hx)
  intro hx
  exact False.elim (hE x hx)
```

For the active typed-set Lean target, existence is supplied by the definition
`Empty Alpha`; uniqueness is proved by `LRASet.Extensionality` or
`TTSet.Extensionality`.

## What This Unlocks

Once this theorem is owned, the notation `empty` / `varnothing` is licensed as
the unique set with no elements.  Later identity laws such as
`A union empty = A` and `A intersection empty = empty` depend on this
membership profile.
