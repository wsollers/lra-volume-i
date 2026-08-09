# 044: Complement-Union-Intersection Closure Duality

Target: `thm:complement-union-intersection-closure-duality`

Proof file:
`volume-i/book-sets/set-theory/proofs/families/prf-complement-union-intersection-closure-duality.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs exist for pairwise and finite closure duality.

## Statement

Let `F` be a family of subsets of `X`, and suppose `F` is closed under
complements.

Then:

```text
pairwise union closure        -> pairwise intersection closure
pairwise intersection closure -> pairwise union closure
finite union closure          -> finite intersection closure
finite intersection closure   -> finite union closure
```

## Plain-Language Reading

Once complements are allowed, unions and intersections are two faces of the
same operation.  De Morgan laws convert one into the other.

## Proof Skeleton

For the pairwise union-to-intersection direction:

1. Take `A, B in F`.
2. Since `F` is closed under complements, `A^c, B^c in F`.
3. Since `F` is closed under pairwise unions, `A^c union B^c in F`.
4. Since `F` is closed under complements, `(A^c union B^c)^c in F`.
5. By De Morgan and involution, `(A^c union B^c)^c = A intersection B`.

The reverse pairwise direction uses:

```text
A union B = (A^c intersection B^c)^c
```

The finite directions repeat the same idea with finite lists of complements.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State both De Morgan conversions.
2. Prove pairwise union closure gives pairwise intersection closure under
   complement closure.
3. Prove the reverse pairwise direction.
4. Explain why the finite versions are list-level versions of the same
   argument.
5. Remember that complement closure is essential; union closure alone does not
   imply intersection closure.

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.ComplementAndPairwiseUnionClosureImpliesPairwiseIntersectionClosure`
- `LRA.VolumeI.Set.ComplementAndPairwiseIntersectionClosureImpliesPairwiseUnionClosure`
- `LRA.VolumeI.Set.ComplementAndFiniteUnionClosureImpliesFiniteIntersectionClosure`
- `LRA.VolumeI.Set.ComplementAndFiniteIntersectionClosureImpliesFiniteUnionClosure`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Families.lean
```

## Common Failure Modes

- Forgetting to complement both inputs before applying the available closure
  rule.
- Forgetting the final complement after applying the available closure rule.
- Using De Morgan in the wrong direction.
- Claiming the result without complement closure.

## What This Unlocks

This theorem makes the set-algebra definitions economical.  Later we can define
a set algebra using complements plus finite unions, then derive finite
intersection closure instead of requiring every closure clause separately.
