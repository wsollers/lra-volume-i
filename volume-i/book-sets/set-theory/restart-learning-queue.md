# Set Theory Restart Learning Queue

Status: working queue for the analysis/topology/measure restart.

Purpose: rebuild understanding theorem by theorem, beginning with Volume I Set
Theory.  This file is a tactical queue, not active LaTeX content and not a
replacement for `chapter.yaml`.

## Operating Rule

For each theorem-like target:

1. Read the statement and all definitions/axioms it depends on.
2. Explain the statement in plain language.
3. Produce or review the handwritten proof.
4. Populate Lean or a deliberate Lean `sorry` stub in the Lean repo.
5. Populate the LaTeX proof only after the proof is understood.
6. Keep dependencies explicit so later volumes can cite the result instead of
   duplicating it.

Definitions and axioms are learning checkpoints, but they do not create proof
obligations.  They should still be understood before proving later theorem-like
targets.

## Current State Snapshot

As of this queue creation:

- Active Set Theory topics: `model`, `sets`, `families`.
- Active Set Theory proof files: 26.
- Proof bodies are restart stubs with TODO placeholders.
- `gate-1-set-manipulation-theorems.md` records the Volume I existence audit
  for the 79 Gate 1 set-manipulation targets used later by Volume IV.
- The first theorem now has checked typed-set Lean stubs:
  `LRA.VolumeI.Set.TTSet.EmptySetExistsUnique` and
  `LRA.VolumeI.Set.LRASet.EmptySetExistsUnique`.
- The second theorem now has checked typed-set Lean stubs:
  `LRA.VolumeI.Set.TTSet.PairSetExistsUnique` and
  `LRA.VolumeI.Set.LRASet.PairSetExistsUnique`.
- The third theorem now has a checked typed-family Lean stub:
  `LRA.VolumeI.Set.IndexedUnionExistsUnique`.
- The fourth theorem now has checked typed-set Lean stubs:
  `LRA.VolumeI.Set.TTSet.BinaryUnionExistsUnique` and
  `LRA.VolumeI.Set.LRASet.BinaryUnionExistsUnique`.
- The fifth theorem now has checked typed-set Lean stubs:
  `LRA.VolumeI.Set.TTSet.SeparationExistsUnique` and
  `LRA.VolumeI.Set.LRASet.SeparationExistsUnique`.
- The sixth theorem now has checked typed-set Lean stubs:
  `LRA.VolumeI.Set.TTSet.IntersectionExistsUnique` and
  `LRA.VolumeI.Set.LRASet.IntersectionExistsUnique`.
- The seventh theorem now has checked typed-set Lean stubs:
  `LRA.VolumeI.Set.TTSet.DifferenceExistsUnique` and
  `LRA.VolumeI.Set.LRASet.DifferenceExistsUnique`.
- The eighth theorem now has checked typed-set Lean stubs:
  `LRA.VolumeI.Set.TTSet.SymmetricDifferenceExistsUnique` and
  `LRA.VolumeI.Set.LRASet.SymmetricDifferenceExistsUnique`.
- The ninth theorem now has checked typed-set Lean stubs:
  `LRA.VolumeI.Set.TTSet.RelativeComplementExistsUnique` and
  `LRA.VolumeI.Set.LRASet.RelativeComplementExistsUnique`.
- The tenth theorem now has a checked typed relative-power-set Lean stub:
  `LRA.VolumeI.Set.RelativePowerSetExistsUnique`.
- The eleventh theorem now has a checked typed-set Lean stub:
  `LRA.VolumeI.Set.Operations.Laws.UnionMonotoneInclusion`.
- The twelfth theorem now has a checked typed-set Lean stub:
  `LRA.VolumeI.Set.Operations.Laws.IntersectionMonotoneInclusion`.
- The thirteenth theorem now has a checked typed relative-power-set Lean stub:
  `LRA.VolumeI.Set.RelativePowerSetMonotoneInclusion`.
- The fourteenth theorem now has a checked typed-set Lean stub:
  `LRA.VolumeI.Set.Operations.Laws.ComplementAntitoneInclusion`.
- The fifteenth theorem now has a checked typed-set Lean stub:
  `LRA.VolumeI.Set.Operations.Laws.DifferenceMonotoneLeft`.
- The sixteenth theorem now has a checked typed-set Lean stub:
  `LRA.VolumeI.Set.Operations.Laws.DifferenceAntitoneRight`.
- The seventeenth theorem has checked typed-set Lean stubs:
  `LRA.VolumeI.Set.Operations.Laws.DeMorganUnion` and
  `LRA.VolumeI.Set.Operations.Laws.DeMorganIntersection`.
- The eighteenth theorem has checked typed-set Lean stubs:
  `LRA.VolumeI.Set.Operations.Laws.ComplementIndexedUnion` and
  `LRA.VolumeI.Set.Operations.Laws.ComplementIndexedIntersection`.
- The nineteenth target is prose-governed for now.  A full Lean theorem for
  `cor:set-duality` requires a syntax and interpretation theory for set
  expressions; the current Lean files cover concrete dual laws instead.
- The twentieth theorem has checked typed-set Lean stubs:
  `LRA.VolumeI.Set.Operations.Laws.UnionCommutative` and
  `LRA.VolumeI.Set.Operations.Laws.IntersectionCommutative`.
- The twenty-first theorem has checked typed-set Lean stubs:
  `LRA.VolumeI.Set.Operations.Laws.UnionAssociative` and
  `LRA.VolumeI.Set.Operations.Laws.IntersectionAssociative`.
- The twenty-second theorem now has checked typed-set Lean stubs:
  `LRA.VolumeI.Set.Operations.Laws.IntersectionDistributesOverUnion` and
  `LRA.VolumeI.Set.Operations.Laws.UnionDistributesOverIntersection`.
- The twenty-third theorem now has checked typed-set Lean stubs:
  `LRA.VolumeI.Set.Operations.Laws.IntersectionDistributesOverIndexedUnion` and
  `LRA.VolumeI.Set.Operations.Laws.UnionDistributesOverIndexedIntersection`.
- The twenty-fourth theorem has checked typed-set Lean stubs for identity and
  absorption:
  `LRA.VolumeI.Set.Operations.Laws.UnionEmpty`,
  `LRA.VolumeI.Set.Operations.Laws.IntersectionUniversal`,
  `LRA.VolumeI.Set.Operations.Laws.AbsorptionUnionIntersection`, and
  `LRA.VolumeI.Set.Operations.Laws.AbsorptionIntersectionUnion`.
- The twenty-fifth theorem has a checked typed-set Lean stub:
  `LRA.VolumeI.Set.Operations.Laws.DoubleComplement`.
- The twenty-sixth target is now Lean-ready through later topology-prep
  vocabulary: `LRA.VolumeI.Set.FiniteSubcoverIffRelativeComplementNotFIP`
  records the finite-subcover/FIP duality form.
- The twenty-seventh theorem now has checked typed-set Lean stubs:
  `LRA.VolumeI.Set.Operations.Laws.SubsetIffUnionEqRight` and
  `LRA.VolumeI.Set.Operations.Laws.SubsetIffIntersectionEqLeft`.
- The twenty-eighth theorem has checked typed-set Lean stubs:
  `LRA.VolumeI.Set.Operations.Laws.UnionIdempotent` and
  `LRA.VolumeI.Set.Operations.Laws.IntersectionIdempotent`.
- The twenty-ninth theorem now has checked typed-set Lean stubs:
  `LRA.VolumeI.Set.Operations.Laws.ComplementEmpty`,
  `LRA.VolumeI.Set.Operations.Laws.ComplementUniversal`,
  `LRA.VolumeI.Set.Operations.Laws.UnionComplement`,
  `LRA.VolumeI.Set.Operations.Laws.ComplementUnion`,
  `LRA.VolumeI.Set.Operations.Laws.IntersectionComplement`, and
  `LRA.VolumeI.Set.Operations.Laws.ComplementIntersection`.
- The thirtieth theorem now has checked typed-set Lean stubs for the core
  difference identities, distributions, subset, and disjointness laws in
  `LRA.VolumeI.Set.Operations.Laws.Difference`.
- The thirty-first theorem now has checked typed-set Lean stubs for the
  symmetric-difference definition, equivalent forms, commutativity,
  associativity, identity, self-inverse, zero iff equality, and subset-of-union
  laws in `LRA.VolumeI.Set.Operations.Laws.SymmetricDifference`.
- The thirty-second theorem now has checked typed-set/function Lean stubs for
  basic preimage laws in `LRA.VolumeI.Functions.Preimages`, including
  universe, empty set, union, intersection, difference, complement, symmetric
  difference, identity, composition, monotonicity, congruence, and a mixed
  difference/union drill.
- The thirty-third theorem now has checked typed-set/function Lean stubs for
  the image of a preimage in `LRA.VolumeI.Functions.Images`, including
  `f(f^{-1}(T)) = T \cap \operatorname{im}(f)` and the subset-of-range equality
  criterion.
- The thirty-fourth theorem now has checked typed-set Lean stubs for
  extensional equality criteria in
  `LRA.VolumeI.Set.Operations.Laws.SubsetCriteria`, including pointwise
  membership equivalence and mutual subset inclusion.
- The thirty-fifth checkpoint now has checked typed-set Lean vocabulary in
  `LRA.VolumeI.Set.Families` for set collections, indexed families of subsets,
  collection unions/intersections, covers, subcovers, finite collections,
  finite subcovers, FIP, and elementwise expansion lemmas for covers and
  subcovers.
- The thirty-sixth theorem now has checked typed-set Lean stubs for the
  cover-failure/relative-complement bridge in `LRA.VolumeI.Set.Families`.
- The thirty-seventh theorem now has checked typed-set Lean stubs for the
  no-finite-subcover/FIP bridge in `LRA.VolumeI.Set.Families`.
- The thirty-eighth proposition now has checked typed-set Lean stubs for the
  finite-subcover/FIP duality in `LRA.VolumeI.Set.Families`.
- The thirty-ninth theorem now has checked typed-set Lean stubs for collection
  systems, closure systems, generated collections, and generation closure laws
  in `LRA.VolumeI.Set.Families`.
- The fortieth checkpoint completed the generated-topology/generated-sigma
  audit.  The result is deliberately conservative: generated topology and
  generated sigma-algebra should wait until closure-rule vocabulary, finite
  algebras, and countable closure have been learned.
- The forty-first checkpoint now has checked typed-set Lean vocabulary for
  unary, binary, indexed, collection, countable, and arbitrary closure
  predicates in `LRA.VolumeI.Set.Families`.
- The forty-second theorem now has checked typed-set Lean stubs for closure
  rule stability under intersections of collection systems in
  `LRA.VolumeI.Set.Families`.
- The forty-third theorem now has checked typed-set Lean stubs for finite
  union/intersection list folds and pairwise-to-finite closure in
  `LRA.VolumeI.Set.Families`.
- The forty-fourth theorem now has checked typed-set Lean stubs for
  complement-driven union/intersection closure duality at pairwise and finite
  levels in `LRA.VolumeI.Set.Families`.
- The forty-fifth checkpoint now has checked typed-set Lean vocabulary for
  concrete family-of-subsets set algebras in `LRA.VolumeI.Set.Families`.
- The forty-sixth theorem now has checked typed-set Lean stubs for equivalent
  set-algebra axiom packages in `LRA.VolumeI.Set.Families`.
- The forty-seventh theorem now has checked typed-set Lean stubs for set
  algebra closure consequences in `LRA.VolumeI.Set.Families`.
- The forty-eighth checkpoint now has checked typed-set Lean vocabulary for
  sigma-algebras as set algebras closed under countable unions in
  `LRA.VolumeI.Set.Families`.
- The forty-ninth theorem now has checked typed-set Lean stubs for
  sigma-algebra closure consequences, including countable intersections, in
  `LRA.VolumeI.Set.Families`.
- The fiftieth theorem now has a checked typed-set Lean stub for intersections
  of sigma-algebras in `LRA.VolumeI.Set.Families`.
- The fifty-first checkpoint now has checked typed-set Lean vocabulary for
  generated sigma-algebras in `LRA.VolumeI.Set.Families`.
- The fifty-second theorem now has checked typed-set Lean stubs for generated
  sigma-algebra closure laws in `LRA.VolumeI.Set.Families`.
- The fifty-third checkpoint now has checked typed-set Lean vocabulary for
  topologies as open-set families in `LRA.VolumeI.Set.Families`.
- The fifty-fourth checkpoint now has checked typed-set Lean vocabulary for
  Borel sigma-algebras as sigma-algebras generated by open sets in
  `LRA.VolumeI.Set.Families`.
- The fifty-fifth theorem now has checked typed-set Lean stubs for Borel
  sigma-algebra closure and minimality laws in `LRA.VolumeI.Set.Families`.
- The fifty-sixth checkpoint now has checked typed-set Lean vocabulary for
  metric topology via open balls in `LRA.VolumeI.Set.Families`.
- The fifty-seventh checkpoint now has checked typed-set Lean vocabulary for
  Borel sigma-algebras on finite-dimensional Euclidean spaces in
  `LRA.VolumeI.Set.Families`.

## First Pass: Foundations and Single-Set Operations

This pass establishes the base vocabulary and the first proof habits:
extensionality, uniqueness by extensionality, existence from axioms, and
membership unfolding.

### Checkpoint 0: Primitive Setup

Read and understand:

- `def:set-membership`
- `ax:extensionality`
- `ax:empty-set`
- `ax:pairing`
- `ax:union`
- `ax:power-set`
- `ax:separation`

No proof files are expected for these axioms/definitions.

### Queue 1: First Existence and Uniqueness Theorems

| Order | Target | Proof file | Core dependencies | Learning point |
| ---: | --- | --- | --- | --- |
| 1 | `thm:empty-set-exists-unique` | `proofs/sets/prf-empty-set-exists-unique.tex` | `ax:empty-set`, `ax:extensionality` | Existence from an axiom; uniqueness by extensionality. |
| 2 | `thm:pairing-output-exists-unique` | `proofs/sets/prf-pairing-output-exists-unique.tex` | `ax:pairing`, `ax:extensionality` | Axiom gives a set with a membership condition; extensionality gives uniqueness. |
| 3 | `thm:union-output-exists-unique` | `proofs/sets/prf-union-output-exists-unique.tex` | `ax:union`, `ax:extensionality` | Unpack membership in a union over a family. |
| 4 | `cor:binary-union-exists-unique` | `proofs/sets/prf-binary-union-exists-unique.tex` | `thm:pairing-output-exists-unique`, `thm:union-output-exists-unique` | Build binary union from pairing plus union. |
| 5 | `thm:separation-output-exists-unique` | `proofs/sets/prf-separation-output-exists-unique.tex` | `ax:separation`, `ax:extensionality` | Definable subset extraction and uniqueness. |
| 6 | `cor:intersection-exists-unique` | `proofs/sets/prf-intersection-exists-unique.tex` | `thm:separation-output-exists-unique` | Intersection as a separated subset. |
| 7 | `cor:set-difference-exists-unique` | `proofs/sets/prf-set-difference-exists-unique.tex` | `thm:separation-output-exists-unique` | Difference as a separated subset. |
| 8 | `cor:symmetric-difference-exists-unique` | `proofs/sets/prf-symmetric-difference-exists-unique.tex` | `cor:set-difference-exists-unique`, `cor:binary-union-exists-unique` | Symmetric difference as a composite operation. |
| 9 | `cor:relative-complement-exists-unique` | `proofs/sets/prf-relative-complement-exists-unique.tex` | `cor:set-difference-exists-unique` | Complement relative to an ambient set. |
| 10 | `thm:power-set-output-exists-unique` | `proofs/sets/prf-power-set-output-exists-unique.tex` | `ax:power-set`, `ax:extensionality` | Families of subsets begin here. |

Stop after this queue and verify:

- all professional and detailed proof bodies are populated or deliberately
  still stubbed with a reason;
- dependencies no longer contain placeholder `TODO` lines;
- each proof restatement matches the note-side theorem statement;
- the Set Theory chapter validates.

## Second Pass: Inclusion and Monotonicity

This pass turns set operations into order-aware tools.

| Order | Target | Proof file | Core dependencies | Learning point |
| ---: | --- | --- | --- | --- |
| 11 | `thm:union-monotone-inclusion` | `proofs/sets/prf-union-monotone-inclusion.tex` | `def:subset`, `def:union` | Prove inclusion by taking an arbitrary element. |
| 12 | `thm:intersection-monotone-inclusion` | `proofs/sets/prf-intersection-monotone-inclusion.tex` | `def:subset`, `def:intersection` | Both sides of an intersection proof carry data. |
| 13 | `thm:power-set-monotone-inclusion` | `proofs/sets/prf-power-set-monotone-inclusion.tex` | `def:power-set`, `def:subset` | Inclusion lifts one level to power sets. |
| 14 | `thm:complement-antitone-inclusion` | `proofs/sets/prf-complement-antitone-inclusion.tex` | `def:complement`, `def:subset` | Complement reverses inclusion. |
| 15 | `thm:set-difference-monotone-left` | `proofs/sets/prf-set-difference-monotone-left.tex` | `def:set-difference`, `def:subset` | Difference is monotone in its left argument. |
| 16 | `thm:set-difference-antitone-right` | `proofs/sets/prf-set-difference-antitone-right.tex` | `def:set-difference`, `def:subset` | Difference is antitone in its right argument. |

Stop after this queue and verify:

- every proof uses elementwise inclusion cleanly;
- theorem dependencies cite definitions and prior monotonicity facts only when
  actually used;
- any Volume IV Gate 1 audit rows covered by these theorems are still accurate.

## Third Pass: Families and Algebraic Laws

Only begin this pass after the first two passes are genuinely understood.

| Order | Target | Proof file | Core dependencies | Learning point |
| ---: | --- | --- | --- | --- |
| 17 | `thm:de-morgan` | `proofs/families/prf-de-morgan.tex` | complements, union, intersection | Complement translates union into intersection and back. |
| 18 | `thm:indexed-de-morgan` | `proofs/families/prf-indexed-de-morgan.tex` | indexed union/intersection | Pointwise logic over arbitrary families. |
| 19 | `cor:set-duality` | `proofs/families/prf-set-duality.tex` | `def:set-duality`, `thm:de-morgan` | Formalize the duality principle carefully. |
| 20 | `thm:commutativity` | `proofs/families/prf-commutativity.tex` | union/intersection definitions | Boolean operations are symmetric. |
| 21 | `thm:associativity` | `proofs/families/prf-associativity.tex` | union/intersection definitions | Parentheses do not change membership logic. |
| 22 | `thm:distributivity` | `proofs/families/prf-distributivity.tex` | union/intersection definitions | Distribute conjunction over disjunction and conversely. |
| 23 | `thm:indexed-distributivity` | `proofs/families/prf-indexed-distributivity.tex` | indexed union/intersection | Binary laws become indexed laws. |
| 24 | `thm:identity-absorption` | `proofs/families/prf-identity-absorption.tex` | empty set, ambient set, union/intersection | Identity and absorption laws. |
| 25 | `thm:involution` | `proofs/families/prf-involution.tex` | complement definition | Complement twice returns the original set. |
| 26 | `prop:fip-duality` | `proofs/families/prf-fip-duality.tex` | covers, complements, finite intersections | Cover/FIP duality for topology. |

## Gate 1 Audit Relationship

The 79-target Gate 1 audit is a downstream dependency inventory.  It should not
force 79 printed theorem displays in Volume I.  Use it to decide which facts
need canonical theorem-like artifacts and which should remain consequences of
broader bundled theorems.

Current audit counts:

| Status | Count |
| --- | ---: |
| `exists in Volume I` | 75 |
| `partial/nearby statement` | 4 |
| `not found` | 0 |

## Fourth Pass: Tactical Gate 1 Additions

Only add direct theorem artifacts when they remove a real downstream gap.  Do
not explode every consequence into a separate theorem display merely to mirror
the 79-row audit.

| Order | Target | Proof file | Core dependencies | Learning point |
| ---: | --- | --- | --- | --- |
| 27 | `thm:subset-absorption-criteria` | `proofs/sets/prf-subset-absorption-criteria.tex` | `def:subset`, `def:union`, `def:intersection`, extensionality | Convert between inclusions and absorption equations. |
| 28 | `thm:idempotency` | `proofs/families/prf-idempotency.tex` | `def:union`, `def:intersection`, extensionality | Repeated union/intersection with the same set changes nothing. |
| 29 | `thm:complement-laws` | `proofs/families/prf-complement-laws.tex` | `def:empty-set`, `def:complement`, `def:union`, `def:intersection` | Complements exhaust the universe and are disjoint. |
| 30 | `thm:difference-laws` | `proofs/families/prf-difference-laws.tex` | `def:set-difference`, complements, De Morgan, extensionality | Difference is intersection with complement and inherits Boolean laws. |
| 31 | `thm:symmetric-difference-laws` | `proofs/families/prf-symmetric-difference-laws.tex` | `def:sym-diff`, difference laws, extensionality | Symmetric difference records exactly where sets disagree. |
| 32 | `thm:basic-preimage-laws` | `functions/proofs/functions/prf-basic-preimage-laws.tex` | `def:preimage`, set operations, identity, composition | Preimages preserve set logic exactly; this is the pattern behind continuity and measurability. |
| 33 | `thm:image-of-preimage` | `functions/proofs/functions/prf-image-of-preimage.tex` | `def:image-set`, `def:preimage`, `def:image-function`, intersection | Images after preimages recover only the part of the target set lying in the range. |
| 34 | `thm:extensional-equality-criteria` | `proofs/sets/prf-extensional-equality-criteria.tex` | `def:subset`, extensionality | Equality of sets is pointwise membership equivalence, equivalently mutual inclusion. |

## Next Action

Gate 1 no longer has any missing Volume I theorem targets.  The remaining
partial rows are deliberate derived orientations or drills:

- right-distributive orientations of binary distributivity, obtained from
  `thm:distributivity` plus `thm:commutativity`;
- two mixed difference/complement drills, obtained from `thm:difference-laws`.

Do not add separate theorem displays for these unless a later validator or
downstream chapter needs a direct citation.

## Fifth Pass: Set-Family Vocabulary for Topology and Measure

The next forward step is not more finite Boolean-algebra polishing.  It is
the family vocabulary that makes topology, metric spaces, compactness, and
measure theory readable.

Candidate next additions, in order:

| Order | Target | Likely proof file | Core dependencies | Learning point |
| ---: | --- | --- | --- | --- |
| 35 | set-family, cover, subcover, finite-subcover, and FIP vocabulary | none; definition checkpoint | power set, indexed family, subset, union | Separate a family from the union of its members; covers are membership-through-a-family, not a single set. |
| 36 | `thm:cover-failure-relative-complements` | `proofs/families/prf-cover-failure-relative-complements.tex` | cover, difference, indexed intersection | A cover fails exactly when relative complements have a common point. |
| 37 | `thm:no-finite-subcover-fip` | `proofs/families/prf-no-finite-subcover-fip.tex` | finite subcover, FIP, cover-failure bridge | No finite subcover iff relative complements have FIP. |
| 38 | `prop:fip-duality` | `proofs/families/prf-fip-duality.tex` | covers, complements, finite intersections | Finite subcovers are dual to failure of FIP for relative complements. |
| 39 | `thm:generated-collection-closure-laws` | `proofs/families/prf-generated-collection-closure-laws.tex` | collection systems, closure systems, indexed intersections | Generation by intersection is extensive, monotone, closed, and idempotent. |
| 40 | generated topology / generated sigma-algebra audit | `learning-notes/040-generated-topology-sigma-audit.md` | generated collections, downstream topology and measurable-space structures | Decide what must be built before specializing generation to topology and measure. |

## Sixth Pass: Closure Rules and Finite Set Algebras

The audit says not to jump directly to generated topology or generated
sigma-algebras.  First we need closure predicates and finite algebra structure.

Candidate next additions, in order:

| Order | Target | Likely proof file | Core dependencies | Learning point |
| ---: | --- | --- | --- | --- |
| 41 | `def:closed-under-set-operation-vocabulary` | none; definition checkpoint | families, operations on sets | Separate an operation existing from a family being closed under that operation. |
| 42 | `thm:closure-rule-intersection-stability` | `proofs/families/prf-closure-rule-intersection-stability.tex` | closure predicates, collection intersections | Intersections of systems with a fixed closure rule preserve that rule. |
| 43 | `thm:pairwise-closure-implies-finite-closure` | `proofs/families/prf-pairwise-closure-implies-finite-closure.tex` | induction, finite families, pairwise union/intersection closure | Binary closure scales to finite closure. |
| 44 | `thm:complement-union-intersection-closure-duality` | `proofs/families/prf-complement-union-intersection-closure-duality.tex` | complements, De Morgan, finite closure | Complement closure converts union closure into intersection closure and conversely. |
| 45 | `def:set-algebra` | none; definition checkpoint | ambient set, complements, finite unions | A set algebra is a finite Boolean closure structure. |
| 46 | `thm:set-algebra-equivalent-definitions` | `proofs/families/prf-set-algebra-equivalent-definitions.tex` | finite closure, complements, empty/universal laws | Recognize equivalent axiom packages for set algebras. |
| 47 | `thm:set-algebra-closure-consequences` | `proofs/families/prf-set-algebra-closure-consequences.tex` | set algebra definition, difference laws, symmetric difference laws | Algebras are closed under the finite Boolean operations used later. |

## Seventh Pass: Sigma-Algebras and Countable Closure

This pass upgrades finite Boolean closure to the countable closure needed for
measure theory.  Keep the focus tactical: enough sigma-algebra structure to
support generated sigma-algebras, Borel sets in \(\mathbb R^n\), measurable
sets, and countable limiting arguments.

Candidate next additions, in order:

| Order | Target | Likely proof file | Core dependencies | Learning point |
| ---: | --- | --- | --- | --- |
| 48 | `def:sigma-algebra` | none; definition checkpoint | set algebra, countable unions, indexed families | A sigma-algebra is a finite Boolean workspace with countable-union closure. |
| 49 | `thm:sigma-algebra-closure-consequences` | `proofs/families/prf-sigma-algebra-closure-consequences.tex` | sigma-algebra, set algebra consequences, indexed De Morgan | Sigma-algebras are closed under the countable Boolean operations used in measure. |
| 50 | `thm:sigma-algebras-closed-under-intersection` | `proofs/families/prf-sigma-algebras-closed-under-intersection.tex` | closure-rule intersection stability, sigma-algebra closure rules | Intersections of sigma-algebras are sigma-algebras. |
| 51 | `def:generated-sigma-algebra` | none; definition checkpoint | generated collection, sigma-algebras closed under intersection | The generated sigma-algebra is the smallest sigma-algebra containing a family. |
| 52 | `thm:generated-sigma-algebra-closure-laws` | `proofs/families/prf-generated-sigma-algebra-closure-laws.tex` | generated collections, generated sigma-algebra | Generation is extensive, monotone, sigma-closed, and idempotent. |

## Eighth Pass: Topology and Borel Generation

This pass connects the set-family toolkit to topology and Borel
sigma-algebras without entering descriptive-set-theory cardinality questions.
The aim is enough structure for metric topology, measure theory, and
multivariable analysis.

Candidate next additions, in order:

| Order | Target | Likely proof file | Core dependencies | Learning point |
| ---: | --- | --- | --- | --- |
| 53 | `def:topology` | none; definition checkpoint | arbitrary unions, finite intersections, families | A topology is an open-set family, not a sigma-algebra. |
| 54 | `def:borel-sigma-algebra` | none; definition checkpoint | topology, generated sigma-algebra | Borel sets are generated from open sets. |
| 55 | `thm:borel-sigma-algebra-closure-laws` | `proofs/families/prf-borel-sigma-algebra-closure-laws.tex` | generated sigma-algebra closure laws | The Borel family is the smallest sigma-algebra containing the opens. |
| 56 | `def:metric-topology` | none; definition checkpoint | open balls, topology | A metric produces a topology by declaring ball-local sets open. |
| 57 | `def:borel-sigma-algebra-rn` | none; definition checkpoint | metric topology, Euclidean space | \(\mathcal B(\mathbb R^n)\) is generated by Euclidean open sets. |

Stop this pass before Borel hierarchy, cardinality, analytic sets, or
descriptive set theory.  Those are deliberately outside this tactical chapter.

## Next Block: Metric-Space Foundations

After Gate 57, the set-family toolkit has reached the intended tactical Borel
endpoint.  The next learning block should move into metric-space foundations:
metrics, open balls, metric topology as a genuine topology, closure/interior,
continuity, compactness, and then the Euclidean specializations needed for
multivariable analysis and measure theory.
