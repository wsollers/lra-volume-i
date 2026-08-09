# Gate 54: Borel Sigma-Algebra

## Target

Introduce `def:borel-sigma-algebra`.

## Statement Shape

Let \((X,\tau)\) be a topological space.  The Borel sigma-algebra of
\((X,\tau)\) is

\[
  \mathcal B(X,\tau)=\sigma(\tau).
\]

Its members are called Borel sets.

## Why This Gate Exists

This is the bridge from topology to measure theory.

Topology gives the open sets \(\tau\).  Measure theory needs a sigma-algebra.
The Borel sigma-algebra is the smallest sigma-algebra that contains all open
sets.

## Proof Status

This is a definition checkpoint, so there is no proof file.

Lean declaration:

- `BorelSigmaAlgebra`

## Dependencies

- `def:topology`
- `def:generated-sigma-algebra`
- `thm:generated-sigma-algebra-closure-laws`

## Common Mistakes

- Saying Borel sets are just open sets.  Every open set is Borel, but Borel
  sets also include the sets forced by sigma-algebra closure.
- Treating Borel generation as a cardinality topic.  Here it is a closure
  construction.
- Forgetting that the topology supplies the generator \(\tau\), while
  sigma-generation supplies the closure operation.

## Next Gate

Prove the Borel sigma-algebra closure laws:

- \(\tau\subseteq\mathcal B(X,\tau)\);
- \(\mathcal B(X,\tau)\) is a sigma-algebra;
- it is the smallest sigma-algebra containing \(\tau\).
