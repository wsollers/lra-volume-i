# Gate 50: Sigma-Algebras Are Closed Under Intersection

## Target

Introduce `thm:sigma-algebras-closed-under-intersection`.

## Statement Shape

Let \(\mathfrak S\) be a family of sigma-algebras on \(X\).  Then

\[
  \bigcap_{\Sigma\in\mathfrak S}\Sigma
\]

is a sigma-algebra on \(X\).

## Why This Gate Exists

This is the existence engine for generated sigma-algebras.

If a starting family \(\mathcal E\subseteq\mathcal P(X)\) is given, the
generated sigma-algebra should be

\[
  \bigcap\{\Sigma:\Sigma\text{ is a sigma-algebra on }X
  \text{ and }\mathcal E\subseteq\Sigma\}.
\]

That construction only works because intersections of sigma-algebras remain
sigma-algebras.

## Proof Strategy

Let \(\mathcal I=\bigcap_{\Sigma\in\mathfrak S}\Sigma\).

To prove \(A\in\mathcal I\), prove \(A\in\Sigma\) for every
\(\Sigma\in\mathfrak S\).

Apply that pattern to each axiom:

1. \(X\in\mathcal I\) because every member sigma-algebra contains \(X\).
2. If \(A\in\mathcal I\), then \(A\in\Sigma\) for every \(\Sigma\), so
   \(X\setminus A\in\Sigma\) for every \(\Sigma\), hence
   \(X\setminus A\in\mathcal I\).
3. If \(A_n\in\mathcal I\) for every \(n\), then \(A_n\in\Sigma\) for every
   \(n\) and every \(\Sigma\), so \(\bigcup_n A_n\in\Sigma\) for every
   \(\Sigma\), hence \(\bigcup_n A_n\in\mathcal I\).

## Proof Status

The proof body is intentionally withheld until the handwritten proof gate is
complete.

Proof stub:

- `volume-i/book-sets/set-theory/proofs/families/prf-sigma-algebras-closed-under-intersection.tex`

Lean declaration:

- `SigmaAlgebrasClosedUnderIntersection`

## Common Mistakes

- Proving only finite intersection stability.  The theorem is about the
  intersection of a family of sigma-algebras, not closure under finite
  intersections inside one sigma-algebra.
- Forgetting that membership in the intersection means membership in every
  sigma-algebra in the indexing family.
- Thinking generated sigma-algebras require choosing a particular smallest
  object directly.  The smallest object is obtained by intersecting all
  candidates.

## Next Gate

Define the generated sigma-algebra \(\sigma(\mathcal E)\) as the intersection
of all sigma-algebras containing \(\mathcal E\).
