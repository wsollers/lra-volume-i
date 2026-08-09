# Gate 1 Theorem Statements: Elementwise Set Manipulation

Status: Volume I existence audit for the Gate 1 theorem-statement list.

Source list: `F:\repos\lra-volume-iv\volume-iv\book-spaces\algebras-of-sets\gate-1-set-manipulation-theorems.md`.

Scope: this file records whether each target already has a Volume I theorem,
lemma, proposition, or corollary statement covering the result. It does not
author proofs and does not create theorem artifacts.

Status categories:

- `exists in Volume I`: a theorem-like Volume I statement covers the target,
  possibly as one item of a bundled theorem.
- `partial/nearby statement`: Volume I has a definition, exposition note, or
  theorem-like statement from which the target is immediate, but not a direct
  theorem-like target as listed.
- `not found`: no covering theorem-like statement was found in the inspected
  Volume I set/function chapters.

## Summary

| Status | Count |
| --- | ---: |
| exists in Volume I | 75 |
| partial/nearby statement | 4 |
| not found | 0 |
| total | 79 |

## 1. Extensionality and Subset Criteria

| Target | Status | Volume I coverage |
| --- | --- | --- |
| `set_ext_iff` | exists in Volume I | `thm:extensional-equality-criteria`, `volume-i/book-sets/set-theory/notes/sets/notes-set-operations.tex`. |
| `subset_antisymm_eq` | exists in Volume I | `thm:extensional-equality-criteria`, `volume-i/book-sets/set-theory/notes/sets/notes-set-operations.tex`. |
| `subset_iff_union_eq_right` | exists in Volume I | `thm:subset-absorption-criteria`, `volume-i/book-sets/set-theory/notes/sets/notes-set-operations.tex`, includes `A\subseteq B \iff A\cup B=B`. |
| `subset_iff_inter_eq_left` | exists in Volume I | `thm:subset-absorption-criteria`, `volume-i/book-sets/set-theory/notes/sets/notes-set-operations.tex`, includes `A\subseteq B \iff A\cap B=A`. |

## 2. Identity and Domination Laws

| Target | Status | Volume I coverage |
| --- | --- | --- |
| `union_empty` | exists in Volume I | `thm:identity-absorption`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A \cup \varnothing = A`. |
| `empty_union` | exists in Volume I | `thm:identity-absorption`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `\varnothing\cup A=A`. |
| `inter_univ` | exists in Volume I | `thm:identity-absorption`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A \cap U = A`. |
| `univ_inter` | exists in Volume I | `thm:identity-absorption`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `U\cap A=A`. |
| `union_univ` | exists in Volume I | `thm:identity-absorption`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\cup U=U`. |
| `univ_union` | exists in Volume I | `thm:identity-absorption`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `U\cup A=U`. |
| `inter_empty` | exists in Volume I | `thm:identity-absorption`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\cap\varnothing=\varnothing`. |
| `empty_inter` | exists in Volume I | `thm:identity-absorption`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `\varnothing\cap A=\varnothing`. |

## 3. Idempotent, Commutative, and Associative Laws

| Target | Status | Volume I coverage |
| --- | --- | --- |
| `union_idempotent` | exists in Volume I | `thm:idempotency`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\cup A=A`. |
| `inter_idempotent` | exists in Volume I | `thm:idempotency`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\cap A=A`. |
| `union_comm` | exists in Volume I | `thm:commutativity`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, bundled with intersection commutativity. |
| `inter_comm` | exists in Volume I | `thm:commutativity`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, bundled with union commutativity. |
| `union_assoc` | exists in Volume I | `thm:associativity`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, bundled with intersection associativity. |
| `inter_assoc` | exists in Volume I | `thm:associativity`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, bundled with union associativity. |

## 4. Distributive Laws

| Target | Status | Volume I coverage |
| --- | --- | --- |
| `inter_union_distrib_left` | exists in Volume I | `thm:distributivity`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`. |
| `union_inter_distrib_left` | exists in Volume I | `thm:distributivity`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`. |
| `inter_union_distrib_right` | partial/nearby statement | Follows from `thm:distributivity` and `thm:commutativity`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`; not stated in right-distributive orientation. |
| `union_inter_distrib_right` | partial/nearby statement | Follows from `thm:distributivity` and `thm:commutativity`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`; not stated in right-distributive orientation. |

## 5. Complement Laws

| Target | Status | Volume I coverage |
| --- | --- | --- |
| `union_compl` | exists in Volume I | `thm:complement-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\cup A^c=U`. |
| `compl_union_eq_univ` | exists in Volume I | `thm:complement-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A^c\cup A=U`. |
| `inter_compl` | exists in Volume I | `thm:complement-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\cap A^c=\varnothing`. |
| `compl_inter_eq_empty` | exists in Volume I | `thm:complement-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A^c\cap A=\varnothing`. |
| `compl_compl` | exists in Volume I | `thm:involution`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`. |
| `compl_empty` | exists in Volume I | `thm:complement-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `\varnothing^c=U`. |
| `compl_univ` | exists in Volume I | `thm:complement-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `U^c=\varnothing`. |

## 6. De Morgan Laws

| Target | Status | Volume I coverage |
| --- | --- | --- |
| `demorgan_compl_union` | exists in Volume I | `thm:de-morgan`, `volume-i/book-sets/set-theory/notes/families/notes-set-duality.tex`. |
| `demorgan_compl_inter` | exists in Volume I | `thm:de-morgan`, `volume-i/book-sets/set-theory/notes/families/notes-set-duality.tex`. |
| `compl_finite_union` | exists in Volume I | `thm:indexed-de-morgan`, `volume-i/book-sets/set-theory/notes/families/notes-set-duality.tex`, stated for indexed families rather than specifically finite families. |
| `compl_finite_inter` | exists in Volume I | `thm:indexed-de-morgan`, `volume-i/book-sets/set-theory/notes/families/notes-set-duality.tex`, stated for indexed families with a nonempty-index condition rather than specifically finite families. |

## 7. Difference Laws

| Target | Status | Volume I coverage |
| --- | --- | --- |
| `diff_eq_inter_compl` | exists in Volume I | `thm:difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\setminus B=A\cap B^c`. |
| `diff_empty` | exists in Volume I | `thm:difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\setminus\varnothing=A`. |
| `empty_diff` | exists in Volume I | `thm:difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `\varnothing\setminus A=\varnothing`. |
| `diff_self` | exists in Volume I | `thm:difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\setminus A=\varnothing`. |
| `diff_union` | exists in Volume I | `thm:difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\setminus(B\cup C)=(A\setminus B)\cap(A\setminus C)`. |
| `diff_inter` | exists in Volume I | `thm:difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\setminus(B\cap C)=(A\setminus B)\cup(A\setminus C)`. |
| `union_diff_distrib` | exists in Volume I | `thm:difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `(A\cup B)\setminus C=(A\setminus C)\cup(B\setminus C)`. |
| `inter_diff_distrib` | exists in Volume I | `thm:difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `(A\cap B)\setminus C=(A\setminus C)\cap(B\setminus C)`. |
| `diff_subset_left` | exists in Volume I | `thm:difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\setminus B\subseteq A`. |
| `diff_disjoint_right` | exists in Volume I | `thm:difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `(A\setminus B)\cap B=\varnothing`. |

## 8. Symmetric Difference Laws

| Target | Status | Volume I coverage |
| --- | --- | --- |
| `symm_diff_def` | exists in Volume I | `thm:symmetric-difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\triangle B=(A\setminus B)\cup(B\setminus A)`. |
| `symm_diff_eq_union_diff_inter` | exists in Volume I | `thm:symmetric-difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\triangle B=(A\cup B)\setminus(A\cap B)`. |
| `symm_diff_comm` | exists in Volume I | `thm:symmetric-difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\triangle B=B\triangle A`. |
| `symm_diff_empty` | exists in Volume I | `thm:symmetric-difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\triangle\varnothing=A`. |
| `empty_symm_diff` | exists in Volume I | `thm:symmetric-difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `\varnothing\triangle A=A`. |
| `symm_diff_self` | exists in Volume I | `thm:symmetric-difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\triangle A=\varnothing`. |
| `symm_diff_assoc` | exists in Volume I | `thm:symmetric-difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `(A\triangle B)\triangle C=A\triangle(B\triangle C)`. |
| `symm_diff_eq_empty_iff` | exists in Volume I | `thm:symmetric-difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\triangle B=\varnothing\iff A=B`. |
| `symm_diff_subset_union` | exists in Volume I | `thm:symmetric-difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\triangle B\subseteq A\cup B`. |

## 9. Preimage Laws

| Target | Status | Volume I coverage |
| --- | --- | --- |
| `preimage_univ` | exists in Volume I | `thm:basic-preimage-laws`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `preimage_empty` | exists in Volume I | `thm:basic-preimage-laws`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `preimage_union` | exists in Volume I | `thm:preimage-ops`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `preimage_inter` | exists in Volume I | `thm:preimage-ops`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `preimage_compl` | exists in Volume I | `thm:preimage-ops`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `preimage_diff` | exists in Volume I | `thm:preimage-ops`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `preimage_symm_diff` | exists in Volume I | `thm:basic-preimage-laws`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `preimage_finite_union` | exists in Volume I | `thm:indexed-preimage-ops`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`, stated for indexed families rather than specifically finite families. |
| `preimage_finite_inter` | exists in Volume I | `thm:indexed-preimage-ops`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`, stated for indexed families with a nonempty-index condition rather than specifically finite families. |

## 10. Preimages and Composition

| Target | Status | Volume I coverage |
| --- | --- | --- |
| `preimage_id` | exists in Volume I | `thm:basic-preimage-laws`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `preimage_comp` | exists in Volume I | `thm:basic-preimage-laws`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `preimage_is_subset_univ` | exists in Volume I | `thm:basic-preimage-laws`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `preimage_mono` | exists in Volume I | `thm:basic-preimage-laws`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `preimage_congr_function` | exists in Volume I | `thm:basic-preimage-laws`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `preimage_congr_set` | exists in Volume I | `thm:basic-preimage-laws`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `preimage_comp_mono` | exists in Volume I | `thm:basic-preimage-laws`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |

## 11. Image and Preimage Interaction

| Target | Status | Volume I coverage |
| --- | --- | --- |
| `subset_preimage_image` | exists in Volume I | `thm:image-preimage-adjunction`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `image_preimage_subset` | exists in Volume I | `thm:image-preimage-adjunction`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `image_union` | exists in Volume I | `thm:image-ops`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `image_inter_subset` | exists in Volume I | `thm:image-ops`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `image_preimage_eq_inter_range` | exists in Volume I | `thm:image-of-preimage`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `image_preimage_eq_of_subset_range` | exists in Volume I | `thm:image-of-preimage`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `preimage_image_eq_of_injective` | exists in Volume I | `thm:image-preimage-adjunction`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`, gives equality for every subset iff `f` is injective. |

## 12. Mixed Manipulation Targets

| Target | Status | Volume I coverage |
| --- | --- | --- |
| `mixed_diff_union_compl` | partial/nearby statement | Same equality as `diff_inter`, mentioned in exposition under `thm:involution`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`; not a theorem-like drill target. |
| `mixed_diff_inter_compl` | partial/nearby statement | Same equality as `diff_union`, mentioned in exposition under `thm:involution`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`; not a theorem-like drill target. |
| `mixed_preimage_diff_union` | exists in Volume I | `thm:basic-preimage-laws`, `volume-i/book-sets/functions/notes/functions/notes-composition.tex`. |
| `mixed_symm_diff_empty_eq` | exists in Volume I | `thm:symmetric-difference-laws`, `volume-i/book-sets/set-theory/notes/families/notes-set-algebra.tex`, includes `A\triangle B=\varnothing\iff A=B`; by `def:set-equality`, this is equivalent to mutual inclusion. |
