# 002: Existence and Uniqueness of Pairing's Output

Target: `thm:pairing-output-exists-unique`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-pairing-output-exists-unique.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs now exist; the older ZFC semantic-reading name is archived and should not
be treated as active restart evidence.

## Statement

For any sets `x_1` and `x_2`, there exists a unique set `P` whose members are
exactly `x_1` and `x_2`:

```text
forall x_1, forall x_2,
  exists! P, forall w, w in P iff (w = x_1 or w = x_2).
```

## Dependencies

- `ax:pairing`: for any two sets, there exists a set whose members are exactly
  those two inputs.
- `ax:extensionality`: two sets are equal iff they have the same elements.

## Plain-Language Reading

The Pairing axiom gives existence of a set with the intended membership
profile.  Extensionality turns that profile into uniqueness: if two candidate
pair sets have the same "is one of these two inputs" membership test, then they
have exactly the same elements and therefore are equal.

This theorem licenses brace notation:

```text
{x_1, x_2}
```

The singleton `{x}` is not a separate primitive; it is the special case
`{x, x}`.

## Proof Skeleton

1. Let `x_1` and `x_2` be arbitrary sets.
2. Use the Axiom of Pairing to choose a set `P` such that for every `w`,
   `w in P iff (w = x_1 or w = x_2)`.
3. To prove uniqueness, let `P'` be another set satisfying the same membership
   profile.
4. Show `P' = P` by Extensionality.
5. For arbitrary `w`, prove `w in P' iff w in P`.
6. If `w in P'`, use the profile for `P'` to get `w = x_1 or w = x_2`, then use
   the profile for `P` to conclude `w in P`.
7. Conversely, if `w in P`, use the profile for `P` to get
   `w = x_1 or w = x_2`, then use the profile for `P'` to conclude
   `w in P'`.
8. Therefore the candidates have the same members, so Extensionality gives
   `P' = P`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State the exact membership profile supplied by Pairing.
2. Explain why the inputs `x_1` and `x_2` are fixed before uniqueness is proved.
3. Prove uniqueness by comparing two witnesses `P` and `P'`, not by arguing from
   notation.
4. Use both directions of each witness's biconditional in the correct place.
5. Explain why the proof still works when `x_1 = x_2`.
6. State how singleton notation is licensed as the diagonal case `{x, x}`.

## Formal Proof Draft

This is the proof shape to reproduce by hand before the LaTeX proof file is
populated:

```text
Let x_1 and x_2 be arbitrary sets.  By the Axiom of Pairing, choose a set P
such that, for every object w, w is an element of P iff w = x_1 or w = x_2.
We prove that P is unique with this property.

Let P' be any other set such that, for every object w, w is an element of P'
iff w = x_1 or w = x_2.  By Extensionality, it is enough to prove that P' and P
have the same elements.  Let w be arbitrary.

If w is an element of P', then the membership profile for P' gives
w = x_1 or w = x_2.  The membership profile for P then gives w is an element of
P.  Conversely, if w is an element of P, then the membership profile for P gives
w = x_1 or w = x_2.  The membership profile for P' then gives w is an element
of P'.  Hence w in P' iff w in P for every w.  By Extensionality, P' = P.

Therefore, for the arbitrary inputs x_1 and x_2, there exists a unique set P
whose elements are exactly x_1 and x_2.  Since the inputs were arbitrary, the
claim holds for all x_1 and x_2.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.TTSet.PairSetExistsUnique`
- `LRA.VolumeI.Set.LRASet.PairSetExistsUnique`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\TT\Set.lean
```

Typed-set analogue:

```text
forall left right : Alpha,
  exists pairSet : TTSet Alpha,
    (forall element,
      Member element pairSet iff element = left or element = right) and
      forall other : TTSet Alpha,
        (forall element,
          Member element other iff element = left or element = right) ->
            other = pairSet
```

For the active typed-set Lean target, existence is supplied by
`Union (Singleton left) (Singleton right)`, and uniqueness is proved by
`TTSet.Extensionality` or `LRASet.Extensionality`.

## Common Failure Modes

- Treating `{x_1, x_2}` as already defined before proving uniqueness.
- Forgetting the leading `forall x_1 forall x_2`.
- Comparing `P` and `P'` only one way instead of proving a biconditional for
  every element.
- Missing the case `x_1 = x_2`; the statement must naturally include
  singleton sets.
- Confusing the pair set `{x_1, x_2}` with the ordered pair `(x_1, x_2)`.

## What This Unlocks

Once this theorem is owned, pair-set notation and singleton notation are
licensed.  Binary union is then constructed as the union over the pair
`{A, B}`, so this theorem is a direct dependency of the next derived set
operation.
