# 034: Extensional Equality Criteria

Target: `thm:extensional-equality-criteria`

Proof file: `volume-i/book-sets/set-theory/proofs/sets/prf-extensional-equality-criteria.tex`

Status: ready for handwritten proof, then LaTeX population. Typed-set Lean
stubs now exist for both displayed criteria.

## Statement

For sets `A` and `B`:

```text
A = B iff forall x, x in A <-> x in B
A = B iff A subset B and B subset A
```

## Dependencies

- `ax:extensionality`: sets are equal exactly when they have the same members.
- `def:subset`: `A subset B` means every member of `A` is a member of `B`.
- `def:set-equality`: equality of sets is extensional.

## Plain-Language Reading

Sets have no hidden structure beyond membership. To prove two sets are equal,
show that every possible element belongs to the first exactly when it belongs
to the second. Operationally, this is usually done by proving both subset
directions.

## Proof Skeleton

1. For the membership criterion, apply extensionality directly.
2. For mutual inclusion, expand:

   ```text
   A subset B means forall x, x in A -> x in B
   B subset A means forall x, x in B -> x in A
   ```

3. Combine the two implications into a biconditional for each `x`.
4. Apply extensionality to conclude `A = B`.
5. Conversely, if `A = B`, replace one set by the other and both inclusions
   are immediate.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State the extensionality criterion.
2. State the mutual-inclusion criterion.
3. Turn two subset proofs into a pointwise biconditional.
4. Turn a pointwise biconditional into set equality.
5. Explain why this is the final step in most set identity proofs.

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.Operations.Laws.SetExtensionalityIff`
- `LRA.VolumeI.Set.Operations.Laws.SetEqualityIffMutualSubset`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\SubsetCriteria.lean
```

## Common Failure Modes

- Proving only one subset direction.
- Forgetting that the biconditional must hold for every element.
- Treating equality as a separate structure rather than membership agreement.

## What This Unlocks

This is the proof-closing move for nearly every set manipulation theorem in
the restart.
