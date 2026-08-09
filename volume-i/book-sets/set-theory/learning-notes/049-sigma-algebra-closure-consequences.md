# Gate 49: Sigma-Algebra Closure Consequences

## Target

Introduce `thm:sigma-algebra-closure-consequences`.

## Statement Shape

Let \(\Sigma\) be a sigma-algebra on \(X\).  Then:

1. \(\Sigma\) is a set algebra on \(X\);
2. \(\varnothing\in\Sigma\);
3. \(\Sigma\) is closed under complements;
4. \(\Sigma\) is closed under finite unions;
5. \(\Sigma\) is closed under finite intersections;
6. \(\Sigma\) is closed under countable unions;
7. \(\Sigma\) is closed under countable intersections.

## Why This Gate Exists

This is the first reusable sigma-algebra manipulation theorem.  After this
gate, later measure-theory proofs can cite one theorem instead of repeatedly
unpacking the definition.

The key new result is closure under countable intersections.  It is not an
axiom in this setup.  It is derived by:

1. complementing each set in the sequence;
2. taking the countable union of those complements;
3. complementing again;
4. applying indexed De Morgan.

## Proof Status

The proof body is intentionally withheld until the handwritten proof gate is
complete.

Proof stub:

- `volume-i/book-sets/set-theory/proofs/families/prf-sigma-algebra-closure-consequences.tex`

Lean declarations:

- `SigmaAlgebraIsSetAlgebra`
- `SigmaAlgebraContainsEmpty`
- `SigmaAlgebraClosedUnderComplements`
- `SigmaAlgebraClosedUnderFiniteUnions`
- `SigmaAlgebraClosedUnderFiniteIntersections`
- `SigmaAlgebraClosedUnderCountableUnions`
- `SigmaAlgebraClosedUnderCountableIntersections`

## Common Mistakes

- Treating countable intersection closure as part of the definition instead of
  deriving it.
- Forgetting that countable intersections require a countable indexed family,
  not an arbitrary family of subsets.
- Blurring sigma-algebra closure with topology closure: topology has arbitrary
  union closure and finite intersection closure; sigma-algebras have countable
  union closure and complement closure.

## Next Gate

Show that intersections of sigma-algebras are sigma-algebras.  This is the
technical engine behind generated sigma-algebras.
