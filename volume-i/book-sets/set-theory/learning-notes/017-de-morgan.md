# 017: De Morgan's Laws

Target: `thm:de-morgan`

Proof file: `volume-i/book-sets/set-theory/proofs/families/prf-de-morgan.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs already exist for both binary laws.

## Statement

For subsets `A` and `B` of a fixed universe:

```text
(A union B)^c = A^c intersection B^c
(A intersection B)^c = A^c union B^c
```

## Dependencies

- `def:union`: `x in A union B iff x in A or x in B`.
- `def:intersection`: `x in A intersection B iff x in A and x in B`.
- `def:complement`: `x in A^c iff x notin A`, relative to the fixed universe.
- `ax:extensionality`: to prove set equality by proving the same members.

## Plain-Language Reading

Complement turns "inside at least one" into "outside both", and turns "inside
both" into "outside at least one".

The theorem is set notation for two propositional logic equivalences:

```text
not (P or Q)  <->  (not P and not Q)
not (P and Q) <->  (not P or not Q)
```

## Proof Skeleton

For `(A union B)^c = A^c intersection B^c`:

1. Use extensionality.  Let `x` be arbitrary.
2. Prove both membership implications.
3. If `x in (A union B)^c`, then `x notin A union B`.
4. Show `x notin A` and `x notin B`; otherwise `x` would be in `A union B`.
5. Conclude `x in A^c intersection B^c`.
6. Conversely, if `x in A^c intersection B^c`, then `x notin A` and
   `x notin B`.
7. Show `x notin A union B` by cases on union membership.
8. Conclude `x in (A union B)^c`.

For `(A intersection B)^c = A^c union B^c`:

1. Use extensionality.  Let `x` be arbitrary.
2. If `x notin A intersection B`, then either `x notin A` or `x notin B`.
3. Conclude `x in A^c union B^c`.
4. Conversely, if `x in A^c union B^c`, split into cases.
5. In either case, `x` cannot be in `A intersection B`.
6. Conclude `x in (A intersection B)^c`.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State both binary De Morgan identities.
2. Translate each identity into an arbitrary-element biconditional.
3. Expand union, intersection, and complement membership correctly.
4. Prove `not (P or Q) -> not P and not Q` constructively.
5. Know where classical reasoning enters for `not (P and Q) -> not P or not Q`.
6. Explain why this is the first real duality theorem for set algebra.

## Formal Proof Draft

```text
For the first identity, prove equality by extensionality.  Let x be arbitrary.
If x is in the complement of A union B, then x is not in A union B.  Hence x is
not in A and x is not in B, since either membership would put x in A union B.
Thus x is in A^c intersection B^c.  Conversely, if x is in A^c intersection
B^c, then x is not in A and not in B.  If x were in A union B, then by cases
it would be in A or in B, contradiction.  Thus x is in the complement of
A union B.

For the second identity, again use extensionality.  If x is in the complement
of A intersection B, then x is not in both A and B.  Classically, x is not in
A or x is not in B, so x is in A^c union B^c.  Conversely, if x is in
A^c union B^c, split into cases.  In either case, x cannot be in
A intersection B.  Therefore x is in the complement of A intersection B.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.Operations.Laws.DeMorganUnion`
- `LRA.VolumeI.Set.Operations.Laws.DeMorganIntersection`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Operations\Laws\Duality.lean
```

Typed-set analogues:

```text
Complement (Union A B) = Intersection (Complement A) (Complement B)
Complement (Intersection A B) = Union (Complement A) (Complement B)
```

## Common Failure Modes

- Treating complements as absolute instead of relative to a fixed universe.
- Forgetting to prove both set inclusions or both directions of membership.
- Reversing the first law into `(A union B)^c = A^c union B^c`.
- Missing the classical logic step in the second law.
- Proving only one of the two De Morgan identities.

## What This Unlocks

De Morgan's laws are the bridge from elementwise set manipulation to set
algebra.  They reappear in topology when complements exchange open and closed
sets, and in measure theory when complements exchange countable unions and
countable intersections.
