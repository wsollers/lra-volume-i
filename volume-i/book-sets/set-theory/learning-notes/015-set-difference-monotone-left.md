# 015: Set Difference is Inclusion-Monotone in the Left Argument

Target: `thm:set-difference-monotone-left`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-set-difference-monotone-left.tex`

Status: ready for handwritten proof, then LaTeX population.  A typed-set Lean
stub now exists.

## Statement

If `A subset B`, then removing the same set `C` from both sides preserves
inclusion:

```text
A subset B -> A \ C subset B \ C.
```

## Dependencies

- `def:subset`: to prove inclusion, take an arbitrary element.
- `def:set-difference`: `x in A \ C iff x in A and x notin C`.

## Plain-Language Reading

Set difference is monotone in the set being subtracted from.  If `A` is inside
`B`, then the part of `A` outside `C` is inside the part of `B` outside `C`.

The exclusion condition does not change:

```text
x notin C
```

is carried from the premise to the conclusion.

## Proof Skeleton

1. Assume `A subset B`.
2. To prove `A \ C subset B \ C`, let `x in A \ C`.
3. By the difference membership rule, get `x in A` and `x notin C`.
4. Use `A subset B` on `x in A` to get `x in B`.
5. Combine `x in B` with the unchanged fact `x notin C`.
6. Conclude `x in B \ C`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. Expand the subset goal into an arbitrary-element proof.
2. Expand difference membership into a conjunction.
3. Use the inclusion hypothesis only on the left membership.
4. Preserve the nonmembership condition unchanged.
5. Explain why this is monotone in the left argument.
6. Contrast it with theorem 16, where difference is antitone in the right
   argument.

## Formal Proof Draft

```text
Assume A subset B.  To prove A \ C subset B \ C, let x be an arbitrary element
of A \ C.  Then x is an element of A and x is not an element of C.  Since
A subset B, x is an element of B.  Together with x notin C, this gives that
x is an element of B \ C.  Therefore A \ C subset B \ C.
```

## Lean Formalization

Current checked Lean target after restart:

- `LRA.VolumeI.Set.Operations.Laws.DifferenceMonotoneLeft`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Difference.lean
```

Typed-set analogue:

```text
forall Left Right Fixed : LRASet Alpha,
  Subset Left Right ->
    Subset (Difference Left Fixed) (Difference Right Fixed)
```

## Common Failure Modes

- Forgetting to keep `x notin C`.
- Trying to prove equality instead of inclusion.
- Using the inclusion hypothesis on the wrong set.
- Assuming difference is monotone in both arguments.
- Confusing `A \ C` with `C \ A`.

## What This Unlocks

This theorem is the left-side half of order behavior for set difference.  It is
needed before the right-side antitone law, and both are later used in Boolean
algebra and measure-theoretic set estimates.
