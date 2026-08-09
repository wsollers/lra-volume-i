# 046: Set Algebra Equivalent Definitions

Target: `thm:set-algebra-equivalent-definitions`

Proof file:
`volume-i/book-sets/set-theory/proofs/families/prf-set-algebra-equivalent-definitions.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs exist for the alternative axiom packages and equivalence theorems.

## Statement

For a family `A subset P(X)`, the following packages are equivalent:

```text
X in A, complement closure, finite union closure
empty in A, complement closure, finite union closure
X in A, complement closure, finite intersection closure
X in A, complement closure, finite union closure, finite intersection closure
```

## Plain-Language Reading

The set algebra definition is robust.  You can start from `X`, or from
`empty`, and you can require finite unions or finite intersections.  Complement
closure supplies the missing half.

## Proof Skeleton

1. From `X in A` and complement closure, get `empty in A` because
   `X^c = empty`.
2. From `empty in A` and complement closure, get `X in A` because
   `empty^c = X`.
3. From complement closure plus finite union closure, get finite intersection
   closure by Gate 44.
4. From complement closure plus finite intersection closure, get finite union
   closure by Gate 44.
5. Bundle and unbundle the clauses.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. Convert `X in A` to `empty in A` using complement closure.
2. Convert `empty in A` to `X in A` using complement closure.
3. Explain why finite union and finite intersection closure are equivalent
   under complement closure.
4. State the four packages without mixing countable closure into the theorem.
5. Prove the equivalence by clause unpacking, not by hand-waving.

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.SetAlgebraEmptyAxiomPackage`
- `LRA.VolumeI.Set.SetAlgebraFiniteIntersectionPackage`
- `LRA.VolumeI.Set.SetAlgebraFiniteBooleanClosurePackage`
- `LRA.VolumeI.Set.SetAlgebraEquivalentDefinitions`
- `LRA.VolumeI.Set.SetAlgebraIffEmptyAxiomPackage`
- `LRA.VolumeI.Set.SetAlgebraIffFiniteIntersectionPackage`
- `LRA.VolumeI.Set.SetAlgebraIffFiniteBooleanClosurePackage`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Families.lean
```

## Common Failure Modes

- Forgetting that the complement is relative to the ambient set `X`.
- Using countable unions instead of finite unions.
- Treating finite intersections as primitive after choosing the economical
  finite-union definition.
- Saying “Boolean combinations” without specifying the finite closure package.

## What This Unlocks

Next gate: set algebra closure consequences.  We will derive empty set
membership, finite intersections, differences, symmetric differences, and the
finite Boolean operations needed downstream.
