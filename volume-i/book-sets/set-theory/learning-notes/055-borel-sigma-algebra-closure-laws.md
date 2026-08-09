# Gate 55: Borel Sigma-Algebra Closure Laws

## Target

Introduce `thm:borel-sigma-algebra-closure-laws`.

## Statement Shape

Let \((X,\tau)\) be a topological space.  Then:

1. every open set is Borel, equivalently
   \(\tau\subseteq\mathcal B(X,\tau)\);
2. \(\mathcal B(X,\tau)\) is a sigma-algebra on \(X\);
3. if \(\mathcal M\) is a sigma-algebra on \(X\) and
   \(\tau\subseteq\mathcal M\), then
   \(\mathcal B(X,\tau)\subseteq\mathcal M\).

## Why This Gate Exists

This is the working theorem for Borel generation.

The most important part is the minimality clause.  It is the pattern behind
many later arguments:

1. define a candidate family of sets satisfying some desired property;
2. prove that candidate family is a sigma-algebra;
3. prove it contains all open sets;
4. conclude it contains all Borel sets.

## Proof Strategy

Use \(\mathcal B(X,\tau)=\sigma(\tau)\).

- Extensivity of generated sigma-algebras gives
  \(\tau\subseteq\mathcal B(X,\tau)\).
- Closure of generated sigma-algebras gives that \(\mathcal B(X,\tau)\) is a
  sigma-algebra.
- Minimality follows because \(\sigma(\tau)\) is the intersection of all
  sigma-algebras containing \(\tau\).

## Proof Status

The proof body is intentionally withheld until the handwritten proof gate is
complete.

Proof stub:

- `volume-i/book-sets/set-theory/proofs/families/prf-borel-sigma-algebra-closure-laws.tex`

Lean declarations:

- `TopologySubsetBorelSigmaAlgebra`
- `BorelSigmaAlgebraIsSigmaAlgebra`
- `BorelSigmaAlgebraMinimal`

## Common Mistakes

- Proving only that open sets are Borel but not proving minimality.
- Treating Borel sets as a topology.  The Borel family is a sigma-algebra.
- Forgetting that the topology hypothesis tells us what the open-set family is;
  the sigma-algebra properties come from generation.

## Next Gate

Define metric topology through open balls, then specialize Borel generation to
metric spaces and \(\mathbb R^n\).
