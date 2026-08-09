# Gate 52: Generated Sigma-Algebra Closure Laws

## Target

Introduce `thm:generated-sigma-algebra-closure-laws`.

## Statement Shape

Let \(\mathcal E,\mathcal F\subseteq\mathcal P(X)\).  Then:

1. \(\mathcal E\subseteq\sigma(\mathcal E)\);
2. if \(\mathcal E\subseteq\mathcal F\), then
   \(\sigma(\mathcal E)\subseteq\sigma(\mathcal F)\);
3. \(\sigma(\mathcal E)\) is a sigma-algebra on \(X\);
4. \(\sigma(\sigma(\mathcal E))=\sigma(\mathcal E)\).

## Why This Gate Exists

This gate turns generated sigma-algebra from a definition into a tool.  It
says that sigma-generation is a closure operator on families of subsets:

- extensive: it contains the starting family;
- monotone: larger starting data generates a larger sigma-algebra;
- closed: the generated object is actually a sigma-algebra;
- idempotent: closing twice adds nothing after closing once.

## Proof Strategy

Use the generic generated-collection theorem with the collection system of all
sigma-algebras.

Two facts make the specialization work:

1. intersections of sigma-algebras are sigma-algebras;
2. there is at least one sigma-algebra containing any generator, namely
   \(\mathcal P(X)\).

Then the four laws are exactly the generated-collection closure laws translated
into sigma-algebra language.

## Proof Status

The proof body is intentionally withheld until the handwritten proof gate is
complete.

Proof stub:

- `volume-i/book-sets/set-theory/proofs/families/prf-generated-sigma-algebra-closure-laws.tex`

Lean declarations:

- `GeneratedSigmaAlgebraCandidateNonempty`
- `GeneratedSigmaAlgebraExtensive`
- `GeneratedSigmaAlgebraMonotone`
- `GeneratedSigmaAlgebraIsSigmaAlgebra`
- `GeneratedSigmaAlgebraIdempotent`

## Common Mistakes

- Forgetting that \(\sigma(\mathcal E)\) is defined as an intersection of
  all eligible sigma-algebras, not as one arbitrary eligible sigma-algebra.
- Reversing monotonicity: if \(\mathcal E\subseteq\mathcal F\), then
  \(\sigma(\mathcal E)\subseteq\sigma(\mathcal F)\).
- Treating idempotence as obvious from notation instead of proving that
  \(\sigma(\mathcal E)\) is already sigma-closed.

## Next Gate

Move from abstract sigma-generation to Borel generation: define Borel
sigma-algebras from topology and then specialize to metric spaces and
\(\mathbb R^n\).
