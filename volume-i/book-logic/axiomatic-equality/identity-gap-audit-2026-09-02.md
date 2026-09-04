# Identity Gap Audit

Date: 2026-09-02

## Scope

This note compares the current volume material in
`volume-i/book-logic/axiomatic-equality`
against the completed Lean identity development under
`../lra-lean/LRA/Identity`.

Primary volume sources:

- `volume-i/book-logic/axiomatic-equality/notes/logic-with-equality/notes-logic-with-equality.tex`
- `volume-i/book-logic/axiomatic-equality/proofs/logic-with-equality/*.tex`

Primary Lean sources:

- `../lra-lean/LRA/Identity/Theorems/Equivalence.lean`
- `../lra-lean/LRA/Identity/Theorems/Congruence.lean`
- `../lra-lean/LRA/Identity/Theorems/Distinctness.lean`
- `../lra-lean/LRA/Identity/Theorems/Witnesses.lean`
- `../lra-lean/LRA/Identity/Bridges/Diagonal.lean`
- `../lra-lean/LRA/Identity/Interop/Adapters.lean`
- `../lra-lean/LRA/Identity/Theorems/UniversalAlgebra.lean`
- `../lra-lean/LRA/Identity/Theorems/ModelTheory.lean`

## What Already Aligns Well

- The chapter already covers the core logical entry points: reflexivity, substitution, symmetry, transitivity, function congruence, relation congruence, unique existence, and two-element bounds.
- Those topics line up with the front edge of the Lean development:
  `IdentSymmetric`, `IdentTransitive`, `IdentPreservesFunctions`,
  `IdentPreservesRelations`, witness/cardinality definitions, and the general
  substitution-based viewpoint.
- The prose emphasis on formula-contexts in substitution is directionally
  consistent with the Lean interface, where Leibniz transport is the central
  primitive.

## Immediate Gaps

- Two proof files are still unfinished:
  `prf-axiomatic-equality-equivalence-relation.tex` and
  `prf-axiomatic-equality-relation-congruence.tex` still contain `TODO`
  placeholders.
- The `\LeanFormalizes{...}` links in the chapter are stale. The note still
  points to `LRA.VolumeI.Identity.*` modules, but the current implementation
  lives under `LRA.Identity.*` after the namespace refactor.
- The chapter stops just as it announces the bridge to first-order logic with
  equality. Lean now has a real model-theoretic bridge, but the volume chapter
  currently ends with only a short expositional remark.

## Substantive Mismatches

- The chapter defines an equality structure as diagonal by definition in
  `notes-logic-with-equality.tex` at the `Equality Structure` definition.
  Lean deliberately does not build diagonality into the structure. Instead,
  `EqualityStructure.isDiagonal` proves it from reflexivity plus Leibniz.
  This is the biggest conceptual mismatch.
- The chapter presents equality as already settled at the structure level,
  while Lean distinguishes:
  identity interface,
  diagonal bridge,
  interop with kernel equality,
  universal-algebra congruence,
  and model-theoretic collapse.
- Because of that, the chapter currently hides one of the strongest ideas in
  the Lean refactor: diagonality should be a theorem, not a field.

## Missing Lean Results Worth Surfacing

- `IdentLeibnizIff` has no explicit chapter-level counterpart. The substitution
  axiom is stated, but the bidirectional transport viewpoint is not isolated as
  its own theorem.
- Distinctness has only a definition in the volume chapter. Lean also proves
  `DistinctIrreflexive` and `DistinctSymmetric`.
- Witness logic is only partially surfaced. The chapter defines unique
  existence and small-cardinality bounds, but Lean also proves
  `HasNoWitnessNotHasWitness` and
  `ExactlyOneNotAtLeastTwoWitnesses`.
- The diagonal bridge is absent as a theorem. Lean has `IdentIsDiagonal`, plus
  the explicit interop lemmas `toEq` and `ofEq`.
- Universal algebra is absent from the current chapter. Lean proves
  `IdentIsCongruence`, defines `quotientByIdentToCarrier`, and proves the left
  and right inverse facts showing quotient-by-identity is trivial.
- The model-theoretic layer is absent. Lean proves
  `IdentityRelation.satisfiesIdentityTheory`,
  `EqualityStructure.isDiagonal`, and packages
  `EqualityStructure.ofReflexiveLeibnizRelation`.

## What Should Probably Be Added Here

- Finish the two incomplete proof files.
- Update the stale `\LeanFormalizes{...}` paths to the current Lean module
  layout.
- Add one explicit theorem or remark making the diagonal-collapse point visible:
  a relation satisfying full identity behavior is forced to agree with actual
  equality.
- Add a short theorem or remark for distinctness:
  `x != x` is impossible, and distinctness is symmetric.
- Add a short theorem or remark that exact uniqueness forbids two distinct
  witnesses. This would connect the current `Unique Existence` and
  `Two-Element Bounds` definitions instead of leaving them separate.

## What Can Stay For Later Chapters

- Full universal-algebra quotient infrastructure.
- The full model-theoretic packaging into equality structures and first-order
  models.
- The explicit Lean interop lemmas as code-facing infrastructure, unless this
  chapter is meant to double as a direct guide to the formalization.

## Elucidation Opportunities

- Clarify the difference between equality, equivalence, and congruence. The
  current chapter proves pieces of this, but does not yet foreground the
  distinction as a conceptual map.
- Explain why distinctness, uniqueness, and small-cardinality statements are
  not side topics. In Lean they are downstream expressions of identity.
- Make the theorem-level role of substitution more explicit: symmetry,
  transitivity, function congruence, and relation congruence are all the same
  move applied to different formula-contexts.
- If the chapter keeps the present definition of equality structure, note that
  this is a pedagogical shortcut and not the architecture used in the current
  Lean development.

## Recommended Next Pass

- First, finish the two open proof files and repair the Lean references.
- Second, decide whether the chapter should stay pedagogically lightweight or
  be brought into closer alignment with the Lean architecture.
- Third, if closer alignment is desired, the highest-value upgrade is to
  replace "diagonal by definition" with "diagonal by theorem" or at least to
  add a clear remark explaining that the formal development now proves this.
