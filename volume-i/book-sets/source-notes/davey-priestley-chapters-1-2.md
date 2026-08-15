# Davey-Priestley Source Notes: Chapters 1-2

Source: B. A. Davey and H. A. Priestley, *Introduction to Lattices and Order*,
scanned PDF at `D:\Readings\Sources\Foundations\Lattice and Order Theory\Introduction to Lattices and Order - Davey.pdf`.

OCR source used:
`D:\Readings\indexes\lra\objects\pdf\4a8be3cd2682552aa3f3b318511c35b12f09ac58f185bcbe9bd6e5ec6abe9c11\extraction\ocr\page-00007.txt`
through `page-00034.txt`, spot-checked against the user-supplied page photos.

Note: the OCR is noisy. These notes are a source-guided summary, not a
verbatim transcription.

## Chapter 1: Ordered Sets

### Chapter Spine

Chapter 1 builds the basic language of ordered sets, first by examples and
then by structural constructions. The flow is:

- order and partial order;
- chains, antichains, and order-isomorphisms;
- motivating examples from number systems, powersets, social sciences,
  computation, binary strings, partial maps, intervals, and semantic domains;
- finite diagrams and covering relations;
- duality, top/bottom, lifting, maximal/minimal elements;
- sums, products, and lexicographic products;
- down-sets and the complete ordered set `O(P)`;
- order-preserving maps, order-embeddings, and ordered sets of maps;
- the category of ordered sets and order-preserving maps.

### Definitions and Terms

- **Order / partial order**: a reflexive, antisymmetric, transitive relation on
  a set.
- **Ordered set**: a set equipped with an order.
- **Strict order**: the associated relation `x < y` meaning `x <= y` and
  `x != y`; the exercises also stress the converse construction from a strict
  transitive irreflexive relation.
- **Chain**: an ordered set, or a subset of one, in which every pair is
  comparable.
- **Antichain**: an ordered set, or a subset of one, in which no two distinct
  elements are comparable.
- **Order-isomorphism**: a bijection between ordered sets that preserves and
  reflects order.
- **Order type**: the structure shared by order-isomorphic ordered sets.
- **Covering relation**: `x` is covered by `y` when `x < y` and no element lies
  strictly between them.
- **Diagram / Hasse diagram**: a finite ordered set drawn by placing larger
  elements higher and drawing cover edges.
- **Dual ordered set**: the ordered set obtained by reversing all comparisons.
- **Duality Principle**: any statement about ordered sets has a dual obtained
  by reversing the order and swapping dual terms.
- **Bottom / top**: least and greatest elements, denoted by bottom/top symbols
  in the book.
- **Lifting**: adjoining a new bottom element to an ordered set.
- **Flat order**: the lifted order obtained from a set treated first as an
  antichain.
- **Maximal / minimal element**: an element with no strictly larger/smaller
  element in the ordered set.
- **Disjoint union**: side-by-side sum with no new cross-comparisons.
- **Linear sum**: ordered sum in which every element of the first summand is
  below every element of the second.
- **Separated sum**: disjoint union followed by adjoining a new bottom.
- **Coalesced sum**: sum formed by identifying existing bottom elements.
- **Product / coordinatewise order**: Cartesian product ordered coordinate by
  coordinate.
- **Lexicographic order**: product order comparing earlier coordinates first.
- **Down-set**: a subset closed downward.
- **Up-set**: a subset closed upward.
- **`O(P)`**: the ordered set of all down-sets of `P`, ordered by inclusion.
- **Order-preserving map**: a map `phi : P -> Q` with `x <= y` implying
  `phi(x) <= phi(y)`.
- **Order-embedding**: an order-preserving map that also reflects order.
- **Ordered set of maps**: a function set ordered pointwise.
- **Higher-order function**: a function taking functions as arguments or values.

### Numbered Results

- **1.17 Lemma**: for finite ordered sets, an order-preserving bijection is an
  order-isomorphism exactly when it respects cover-diagram structure.
- **1.18 Proposition**: two finite ordered sets are order-isomorphic exactly when
  they admit diagrams of the same shape with corresponding labels.
- **1.26 Proposition**: for `X = {1, ..., n}`, the characteristic-vector map
  `P(X) -> 2^n` is an order-isomorphism.
- **1.30 Lemma**: membership in a principal down-set characterizes the order:
  the down-set assignment embeds an ordered set into its down-set lattice.
- **1.32 Proposition**: down-set lattices transform sums/products of ordered
  sets by corresponding algebraic operations on `O(P)`.

### Main Mathematical Takeaways

- Ordered sets are not just abstract relations; they organize information,
  approximation, partial computation, preference, and divisibility.
- Finite posets are often best understood through Hasse diagrams, but diagram
  use is justified by order-theoretic definitions.
- Duality is a bookkeeping device that turns every proof about upper concepts
  into a proof about lower concepts.
- The powerset `P(X)` and the Boolean cube `2^n` are the same ordered object
  up to characteristic-vector relabeling.
- Down-sets are a central construction: `O(P)` turns any ordered set into an
  inclusion-ordered family of sets.
- Products and sums are structural constructors for ordered sets, with
  coordinatewise order as the default product order.
- Pointwise order on function spaces is the bridge to analysis and later domain
  theory.

### Exercise Signals

The chapter exercises emphasize:

- reconstructing non-strict orders from strict orders;
- listing small finite posets up to isomorphism;
- divisibility diagrams;
- testing order-preservation;
- binary-string orders and tree-like structures;
- drawing products and down-set lattices;
- transitive closure and finite linear extensions;
- Dilworth's theorem as a capstone direction.

## Chapter 2: Lattices and Complete Lattices

### Chapter Spine

Chapter 2 develops lattices first as ordered sets and then as algebraic
structures. The flow is:

- upper/lower bounds, suprema, infima;
- lattice and complete lattice definitions;
- examples from chains, powersets, down-set lattices, divisibility, subgroup
  lattices, and normal subgroup lattices;
- algebraic laws for join and meet;
- sublattices, products, homomorphisms, embeddings, and isomorphisms;
- ideals and filters;
- arbitrary joins/meets and complete-lattice criteria;
- intersection structures and closure systems;
- Knaster-Tarski fixed point theorem;
- chain conditions and completeness;
- join-irreducible and meet-irreducible elements.

### Definitions and Terms

- **Upper bound / lower bound**: an ambient element above/below every element
  of a subset.
- **Least upper bound / supremum**: the least element among all upper bounds.
- **Greatest lower bound / infimum**: the greatest element among all lower
  bounds.
- **Join**: `x \/ y`, the supremum of `{x,y}` when it exists.
- **Meet**: `x /\ y`, the infimum of `{x,y}` when it exists.
- **Lattice**: a nonempty ordered set in which every pair has a join and a
  meet.
- **Complete lattice**: a nonempty ordered set in which every subset has a
  join and a meet.
- **Lattice of sets**: a family of sets closed under finite unions and
  intersections.
- **Complete lattice of sets**: a family of sets closed under arbitrary unions
  and intersections.
- **Down-set lattice**: `O(P)`, a complete lattice under union/intersection.
- **Connecting Lemma**: in a lattice, `a <= b`, `a \/ b = b`, and
  `a /\ b = a` are equivalent.
- **Bounded lattice**: a lattice with zero and one, equivalently bottom and top.
- **Sublattice**: a nonempty subset closed under inherited join and meet.
- **Product lattice**: a Cartesian product with coordinatewise join and meet.
- **Lattice homomorphism**: a map preserving finite joins and finite meets.
- **Lattice isomorphism**: a bijective lattice homomorphism.
- **Embedding**: a one-to-one homomorphism identifying a lattice with a
  sublattice of another.
- **`{0,1}`-homomorphism**: a bounded-lattice homomorphism preserving both
  zero and one.
- **Ideal**: a nonempty down-set closed under finite joins.
- **Filter**: the dual notion, a nonempty up-set closed under finite meets.
- **Proper ideal/filter**: an ideal/filter not equal to the whole lattice.
- **Principal ideal/filter**: the ideal/filter generated by one element.
- **Preserves existing joins/meets**: a map carries any join/meet that exists
  in the domain to the corresponding join/meet of the image in the codomain.
- **Intersection structure / meet-structure / closure system**: a nonempty
  family of subsets closed under nonempty intersections.
- **Topped intersection structure**: an intersection structure that also
  contains the ambient set.
- **Fixpoint**: an element `x` with `F(x) = x`.
- **Length of a finite chain**: one less than the number of elements.
- **Finite length**: having a longest finite chain.
- **No infinite chains**: every chain is finite.
- **Ascending chain condition (ACC)**: every increasing sequence eventually
  stabilizes.
- **Descending chain condition (DCC)**: the dual stabilizing condition.
- **Join-irreducible element**: a nonzero element that cannot be expressed as a
  nontrivial join.
- **Meet-irreducible element**: the dual notion.
- **Join-dense subset**: a subset whose joins generate every element.
- **Meet-dense subset**: the dual notion.

### Numbered Results

- **2.8 Connecting Lemma**: for `a,b` in a lattice, `a <= b` iff `a \/ b = b`
  iff `a /\ b = a`.
- **2.9 Theorem**: join and meet satisfy associativity, commutativity,
  idempotency, and absorption, together with their dual laws.
- **2.10 Theorem**: conversely, a nonempty set with two binary operations
  satisfying the lattice identities carries an induced order for which the
  original operations are join and meet.
- **2.19 Proposition**: a lattice homomorphism is order-preserving; a lattice
  isomorphism is exactly an order-isomorphism.
- **2.22 Lemma**: arbitrary joins/meets obey the expected bound tests,
  monotonicity in the indexing subset, and cross-inequality criteria.
- **2.23 Lemma**: when joins/meets exist, joins and meets of unions split into
  binary joins/meets of the component joins/meets.
- **2.24 Lemma**: every finite nonempty subset of a lattice has a join and a
  meet.
- **2.25 Corollary**: every finite lattice is complete.
- **2.27 Lemma**: order-preserving maps compare images of existing joins/meets
  in the expected direction; order-isomorphisms preserve all existing joins and
  meets.
- **2.28 Lemma**: if an ambient join/meet of a subset lands inside an induced
  suborder, it is also the join/meet in the suborder.
- **2.29 Corollary**: for families of sets, ambient unions/intersections give
  joins/meets whenever they remain in the family.
- **2.30 Lemma**: if every nonempty subset has a meet, then every subset with an
  upper bound has a join, computed as the meet of its upper bounds.
- **2.31 Theorem**: for a nonempty ordered set, complete-lattice status is
  equivalent to existence of all meets, and also to having a top element plus
  all nonempty meets.
- **2.32 Corollary**: a subset family closed under nonempty intersections and
  containing the ambient set is a complete lattice under inclusion.
- **2.35 Knaster-Tarski Fixpoint Theorem**: every order-preserving self-map of a
  complete lattice has greatest and least fixed points, obtained from pre- and
  post-fixed point sets.
- **2.39 Lemma**: ACC is equivalent to every nonempty subset having a maximal
  element.
- **2.40 Theorem**: an ordered set has no infinite chains iff it satisfies both
  ACC and DCC.
- **2.41 Theorem**: in a lattice satisfying ACC, every nonempty join reduces to
  a finite join; with a bottom element this gives completeness; no infinite
  chains also imply completeness.
- **2.45 Proposition**: in a lattice satisfying DCC, join-irreducibles separate
  strict non-comparisons below an element and every element is the join of the
  join-irreducibles beneath it.
- **2.46 Theorem**: under DCC, join-irreducibles are join-dense; under ACC,
  join-dense representations can be taken finite; with no infinite chains,
  every element is a finite join of join-irreducibles, and any join-dense set
  must contain them.

### Main Mathematical Takeaways

- Lattices are exactly the ordered sets where binary sup/inf operations are
  everywhere defined.
- The order-theoretic and algebraic presentations of lattices are equivalent.
- Complete lattices require arbitrary joins/meets, but one side often suffices:
  all meets plus a top element imply all joins.
- Powersets and down-set lattices are the model complete lattices.
- Not every naturally occurring lattice of sets has joins given by union; for
  closure systems, meets are intersections but joins are generated closures.
- Homomorphisms are stronger than monotone maps: they preserve both lattice
  operations, not merely order.
- Ideals and filters are lattice-theoretic versions of algebraic and
  topological closure behavior.
- Knaster-Tarski is the chapter's major complete-lattice theorem and is a
  bridge to fixed-point semantics and Schröder-Bernstein.
- Chain conditions give finiteness-like hypotheses that force completeness or
  finite join decompositions.
- Join-irreducibles play the role of prime-like building blocks in finite or
  chain-finite lattices.

## LRA Integration Targets

Existing Volume I coverage already includes many Chapter 1 and 2 concepts:

- `volume-i/book-sets/orderings/notes/order/notes-order.tex`
- `volume-i/book-sets/orderings/notes/order/notes-order-hasse-sup-duality.tex`
- `volume-i/book-sets/orderings/notes/order/notes-order-induced.tex`
- `volume-i/book-sets/lattices/notes/lattices/notes-lattices.tex`

Potential follow-up additions from Davey-Priestley Chapters 1-2:

- add explicit down-set lattice notes and results for `O(P)`;
- add sum/coalesced-sum/separated-sum constructions for ordered sets;
- add a short source-aligned account of pointwise orders on function spaces;
- add lattice ideals and filters;
- add complete-lattice criteria via meet-closure/intersection structures;
- add ACC/DCC and join-irreducible decomposition notes;
- consider proof stubs for Davey-Priestley results 2.8, 2.10, 2.19, 2.31,
  2.35, 2.39, 2.41, and 2.46.
