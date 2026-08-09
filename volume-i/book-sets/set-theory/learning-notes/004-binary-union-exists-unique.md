# 004: Existence and Uniqueness of Binary Union

Target: `cor:binary-union-exists-unique`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-binary-union-exists-unique.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs now exist.

## Statement

For any sets `A` and `B`, there exists a unique set `C` whose elements are
exactly the elements belonging to `A` or to `B`:

```text
forall A, forall B,
  exists! C, forall x,
    x in C iff (x in A or x in B).
```

The source text introduces this set by definition:

```text
A union B := bigcup {A, B}.
```

## Dependencies

- `thm:pairing-output-exists-unique`: licenses the pair set `{A, B}`.
- `thm:union-output-exists-unique`: licenses the union over `{A, B}`.
- `ax:extensionality`: used implicitly through the two upstream uniqueness
  theorems, and directly if proving the membership-profile version.

## Plain-Language Reading

Binary union is the first derived set operation.  It is not a primitive axiom.
To build `A union B`, first form the pair set `{A, B}`.  Then take the union of
that pair set.  An object `x` belongs to the result exactly when it belongs to
some member of `{A, B}`, which means it belongs to `A` or it belongs to `B`.

This is the first real payoff of the licensing pattern:

```text
axiom-licensed pair + axiom-licensed big union = derived binary union
```

## Proof Skeleton

1. Let `A` and `B` be arbitrary sets.
2. By Pairing, the pair set `{A, B}` exists and is unique.
3. By Union's Output, `bigcup {A, B}` exists and is unique.
4. Define `A union B := bigcup {A, B}`.
5. Show the membership profile:
   `x in A union B iff x in A or x in B`.
6. Forward direction:
   - if `x in bigcup {A, B}`, then there exists `W` with
     `W in {A, B}` and `x in W`;
   - since `W in {A, B}`, either `W = A` or `W = B`;
   - therefore `x in A` or `x in B`.
7. Reverse direction:
   - if `x in A`, then use the witness `W = A`;
   - if `x in B`, then use the witness `W = B`;
   - in either case, `x in bigcup {A, B}`.
8. Uniqueness of the set with this binary-union profile follows by
   Extensionality.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. Explain why binary union is derived, not primitive.
2. State the definition `A union B := bigcup {A, B}`.
3. Expand membership in `bigcup {A, B}` into an existential witness.
4. Use membership in `{A, B}` to split into the two cases `W = A` and `W = B`.
5. Prove the reverse direction by choosing the correct witness set.
6. State why the final output is unique.

## Formal Proof Draft

This is the proof shape to reproduce by hand before the LaTeX proof file is
populated:

```text
Let A and B be arbitrary sets.  By the pairing theorem, the pair set {A, B}
exists and is unique.  By the union-output theorem applied to {A, B}, the set
bigcup {A, B} exists and is unique.  Define A union B to be this set.

We verify its membership profile.  Let x be arbitrary.  If x is an element of
bigcup {A, B}, then there is a set W such that W is an element of {A, B} and
x is an element of W.  Since W is an element of {A, B}, either W = A or W = B.
In the first case, x is an element of A.  In the second case, x is an element
of B.  Hence x is an element of A or x is an element of B.

Conversely, suppose x is an element of A or x is an element of B.  If x is an
element of A, choose W = A.  Since A is an element of {A, B}, this witnesses
that x is an element of bigcup {A, B}.  If x is an element of B, choose W = B.
Since B is an element of {A, B}, this again witnesses that x is an element of
bigcup {A, B}.  Therefore x is an element of A union B iff x is an element of
A or x is an element of B.

Finally, if C is any other set with this same membership profile, then C and
A union B have the same elements.  By Extensionality, C = A union B.  Thus
binary union exists and is unique.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.TTSet.BinaryUnionExistsUnique`
- `LRA.VolumeI.Set.LRASet.BinaryUnionExistsUnique`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\TT\Set.lean
```

Typed-set analogue:

```text
forall left right : LRASet Alpha,
  exists unionSet : LRASet Alpha,
    (forall element,
      Member element unionSet iff
        Member element left or Member element right) and
      forall other : LRASet Alpha,
        (forall element,
          Member element other iff
            Member element left or Member element right) ->
              other = unionSet
```

For the active typed-set Lean target, existence is supplied by
`Union left right`, and uniqueness is proved by `LRASet.Extensionality`.

## Common Failure Modes

- Treating `A union B` as primitive before deriving it.
- Forgetting the witness `W` in the forward direction.
- Saying `W in {A, B}` means `W in A or W in B`; it means `W = A or W = B`.
- Proving the membership profile but not uniqueness of the output.
- Confusing binary union `A union B` with set-indexed union `bigcup x`.

## What This Unlocks

Once this theorem is owned, union becomes a basic operation available for
algebraic laws: commutativity, associativity, identity with the empty set,
idempotence, distributivity, and monotonicity.
