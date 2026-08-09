# 016: Set Difference is Inclusion-Antitone in the Right Argument

Target: `thm:set-difference-antitone-right`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-set-difference-antitone-right.tex`

Status: ready for handwritten proof, then LaTeX population.  A typed-set Lean
stub now exists.

## Statement

If `C subset D`, then removing the larger set gives a smaller result:

```text
C subset D -> A \ D subset A \ C.
```

## Dependencies

- `def:subset`: to prove inclusion, take an arbitrary element.
- `def:set-difference`: `x in A \ D iff x in A and x notin D`.

## Plain-Language Reading

Set difference reverses inclusion in the set being removed.  If `D` contains
everything in `C` and perhaps more, then asking to be outside `D` is stronger
than asking to be outside `C`.

The left membership condition does not change:

```text
x in A
```

is carried from the premise to the conclusion.

## Proof Skeleton

1. Assume `C subset D`.
2. To prove `A \ D subset A \ C`, let `x in A \ D`.
3. By the difference membership rule, get `x in A` and `x notin D`.
4. To prove `x notin C`, assume for contradiction that `x in C`.
5. Use `C subset D` on `x in C` to get `x in D`.
6. Contradict `x notin D`.
7. Combine `x in A` with `x notin C`.
8. Conclude `x in A \ C`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. Expand the subset goal into an arbitrary-element proof.
2. Expand difference membership into a conjunction.
3. Preserve the left membership condition unchanged.
4. Convert `x notin D` into `x notin C` using contradiction and `C subset D`.
5. Explain why this is antitone in the right argument.
6. Contrast it with theorem 15, where difference is monotone in the left
   argument.

## Formal Proof Draft

```text
Assume C subset D.  To prove A \ D subset A \ C, let x be an arbitrary element
of A \ D.  Then x is an element of A and x is not an element of D.  We claim
that x is not an element of C.  If x were an element of C, then since C subset
D, x would be an element of D, contradicting x notin D.  Hence x notin C.
Together with x in A, this gives x in A \ C.  Therefore A \ D subset A \ C.
```

## Lean Formalization

Current checked Lean target after restart:

- `LRA.VolumeI.Set.Operations.Laws.DifferenceAntitoneRight`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Difference.lean
```

Typed-set analogue:

```text
forall Smaller Larger Fixed : LRASet Alpha,
  Subset Smaller Larger ->
    Subset (Difference Fixed Larger) (Difference Fixed Smaller)
```

## Common Failure Modes

- Trying to preserve `x notin D` directly as `x notin C`.
- Reversing the final inclusion.
- Forgetting that right-side inclusion reverses under set difference.
- Using the inclusion hypothesis backward.
- Confusing `A \ D` with `D \ A`.

## What This Unlocks

This theorem completes the basic order behavior of set difference: monotone in
the left argument and antitone in the right argument.  That pattern reappears
in Boolean algebra, relative complements, measure estimates, and later
monotonicity arguments for functions and preimages.
