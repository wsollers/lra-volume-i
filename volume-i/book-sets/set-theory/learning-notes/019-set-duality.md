# 019: Principle of Set Duality

Target: `cor:set-duality`

Proof file: `volume-i/book-sets/set-theory/proofs/families/prf-set-duality.tex`

Status: ready for handwritten proof, then LaTeX population.  No Lean theorem
stub is added yet, because the current Lean development does not define a
syntax of set expressions or a dualization operation on that syntax.

## Statement

Any identity involving `union`, `intersection`, `empty set`, and the universe
that holds for all subsets of a fixed universe remains valid after replacing
each symbol by its dual:

```text
union        <-> intersection
empty set    <-> universe
complement   stays complement
```

## Dependencies

- `def:set-duality`: defines the syntactic dual operation on set expressions.
- `thm:de-morgan`: explains why complements exchange unions and intersections.
- `ax:extensionality`: validates identities by elementwise equivalence.
- Basic operation definitions for union, intersection, empty set, universe, and
  complement.

## Plain-Language Reading

Set duality is a theorem-saving device.  Once an identity is proved in one
form, its mirror identity follows by systematically swapping the two lattice
operations and the two extreme sets.

For example:

```text
A intersection (B union C) = (A intersection B) union (A intersection C)
```

duals to:

```text
A union (B intersection C) = (A union B) intersection (A union C)
```

## Proof Skeleton

1. Fix a universe `U`.
2. Interpret each set expression by its element-membership predicate.
3. Observe the dictionary:
   - union corresponds to `or`;
   - intersection corresponds to `and`;
   - empty set corresponds to `false`;
   - universe corresponds to `true`;
   - complement corresponds to `not`.
4. Dualizing the set expression corresponds to dualizing the logical formula.
5. Propositional duality says valid formulas remain valid under
   `or <-> and` and `false <-> true` when negation is handled by De Morgan.
6. Transfer the resulting pointwise logical equivalence back to set equality by
   extensionality.

## Cold-Proof Checklist

You own this corollary when you can do all of the following without looking:

1. State exactly which symbols are swapped.
2. Explain why complements remain complements.
3. Give one nontrivial example of a dual identity.
4. Distinguish a rigorous metatheorem from a single set equality.
5. Explain why a Lean formalization would need a syntax of set expressions.
6. Use duality as a shortcut without treating it as a substitute for knowing
   the elementwise proof.

## Formal Proof Draft

```text
Fix a universe U.  Each set expression built from union, intersection, empty
set, U, and complement determines a predicate on elements of U.  Under this
translation, union becomes logical disjunction, intersection becomes logical
conjunction, empty set becomes false, U becomes true, and complement becomes
negation.  Replacing union by intersection and empty set by U is therefore the
same as replacing disjunction by conjunction and false by true in the
corresponding logical formula.  De Morgan's laws show that this replacement is
compatible with complements.  Hence any universally valid identity translates
to a valid dual pointwise equivalence.  By extensionality, the corresponding
dual set identity is valid.
```

## Lean Formalization

Current status:

```text
deferred
```

The existing Lean development formalizes concrete dual laws such as:

- `LRA.VolumeI.Set.Operations.Laws.DeMorganUnion`
- `LRA.VolumeI.Set.Operations.Laws.DeMorganIntersection`
- `LRA.VolumeI.Set.Operations.Laws.ComplementIndexedUnion`
- `LRA.VolumeI.Set.Operations.Laws.ComplementIndexedIntersection`

Formalizing the general principle itself would require additional infrastructure:

- an inductive syntax for set expressions;
- an interpretation function from expressions to `LRASet`;
- a dualization function on expressions;
- a theorem connecting interpretation of dual expressions to pointwise logical
  duality.

That is useful, but it is not part of the tactical restart gate.

## Common Failure Modes

- Treating duality as an operation on actual sets rather than on expressions.
- Forgetting to swap `empty set` and `universe`.
- Swapping complements instead of leaving complement as the same operation.
- Using duality before proving the base identity.
- Hiding a real proof obligation behind the word "obvious."

## What This Unlocks

Duality makes the later algebra efficient: commutativity, associativity,
distributivity, identity, absorption, and topology's open/closed pairings all
come in mirrored pairs.  The point is not to avoid proofs; it is to recognize
when two proofs have the same logical skeleton.
