# Gate 48: Sigma-Algebra

## Target

Introduce `def:sigma-algebra`.

## Statement Shape

Let \(X\) be a set.  A sigma-algebra on \(X\) is a family
\(\Sigma\subseteq\mathcal P(X)\) such that:

1. \(\Sigma\) is a set algebra on \(X\);
2. if \(A_n\in\Sigma\) for every \(n\in\mathbb N\), then
   \(\bigcup_{n\in\mathbb N}A_n\in\Sigma\).

## Why This Gate Exists

Set algebras are finite Boolean workspaces.  Sigma-algebras add the first
countable closure rule needed for measure theory.

This gate should make the distinction sharp:

- topology will require arbitrary unions;
- sigma-algebras require countable unions;
- both structures reuse the same earlier family and closure vocabulary.

## Proof Status

This is a definition checkpoint, so there is no proof file.

The matching Lean declaration is:

- `SigmaAlgebra` in `LRA.VolumeI.Set.Families`

## Next Gate

The next theorem should extract the basic closure consequences of a
sigma-algebra:

- every sigma-algebra is a set algebra;
- every sigma-algebra is closed under countable unions;
- every sigma-algebra is closed under countable intersections, by complement
  closure and indexed De Morgan.
