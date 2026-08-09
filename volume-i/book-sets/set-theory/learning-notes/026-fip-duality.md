# 026: FIP--Cover Duality

Target: `prop:fip-duality`

Proof file: `volume-i/book-sets/set-theory/proofs/families/prf-fip-duality.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs now exist for the cover/FIP vocabulary and the full finite-subcover/FIP
equivalence.

## Statement

Let `X` be a set, let `A subset X`, and let `{U_alpha}_{alpha in I}` be a
family of subsets of `X`.  Define:

```text
F_alpha = X \ U_alpha
```

Then:

```text
{U_alpha} covers A
  <-> {F_alpha intersection A}_{alpha in I} does not have the FIP.
```

Equivalently:

```text
{U_alpha} does not cover A
  <-> the relative complement family {F_alpha intersection A} has the FIP.
```

## Dependencies

- `def:cover-full`: a family covers `A` iff every point of `A` lies in some
  family member.
- `def:fip`: every finite subcollection has nonempty intersection.
- `def:complement`: converts membership outside an open cover member into
  membership in the corresponding complement.
- `def:intersection`: relative complements are intersected with `A`.
- `def:subset`: cover statements are subset statements.
- `thm:indexed-de-morgan`: complements exchange unions and intersections.

## Plain-Language Reading

A cover fails when some point of `A` escapes every covering set.  Such an
escaped point lies in every complement `F_alpha` and also lies in `A`.

For finite subcovers, the same idea is finite: if no finite list of the
`U_alpha` covers `A`, then every finite list of the relative complements
`F_alpha intersection A` has a common point.  That is exactly the finite
intersection property.

## Proof Skeleton

To connect covers with FIP:

1. Fix a finite index set `I_0 subset I`.
2. The finite subfamily `{U_alpha}_{alpha in I_0}` covers `A` exactly when:

   ```text
   A subset union_{alpha in I_0} U_alpha
   ```

3. It fails to cover `A` exactly when there exists `x in A` such that:

   ```text
   for all alpha in I_0, x notin U_alpha
   ```

4. By complement membership, this means:

   ```text
   for all alpha in I_0, x in F_alpha
   ```

5. Since also `x in A`, this means:

   ```text
   x in intersection_{alpha in I_0} (F_alpha intersection A)
   ```

6. Therefore failure of every finite subcover is equivalent to every finite
   intersection of the relative complements being nonempty.
7. That condition is exactly FIP.

## Cold-Proof Checklist

You own this proposition when you can do all of the following without looking:

1. State cover/FIP duality in both directions.
2. Explain why complements are intersected with `A`.
3. Translate failure of a finite cover into an escaping point.
4. Translate the escaping point into a common point of finitely many
   complements.
5. Explain how indexed De Morgan supports the total-family version.
6. Connect the proposition to the compactness equivalence:
   open-cover compactness vs. closed-set FIP compactness.

## Formal Proof Draft

```text
Fix a finite subcollection indexed by I_0.  This finite subcollection covers A
iff every x in A belongs to at least one U_alpha with alpha in I_0.  It fails
to cover A iff there exists x in A such that x belongs to no U_alpha for
alpha in I_0.  For such an x, membership in no U_alpha is the same as
membership in every complement F_alpha.  Since x is also in A, x belongs to
every F_alpha intersection A.  Hence the finite intersection of the relative
complements is nonempty.

Conversely, if the finite intersection of the relative complements is nonempty,
choose x in it.  Then x is in A and x is in every F_alpha, so x is in no
U_alpha from the finite subcollection.  Therefore that finite subcollection
does not cover A.  Thus finite subcovers fail exactly when finite intersections
of relative complements are nonempty, which is precisely the FIP formulation.
```

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.Covers`
- `LRA.VolumeI.Set.Subcover`
- `LRA.VolumeI.Set.FiniteSubcover`
- `LRA.VolumeI.Set.HasNoFiniteSubcover`
- `LRA.VolumeI.Set.HasFiniteSubcover`
- `LRA.VolumeI.Set.FiniteIntersectionProperty`
- `LRA.VolumeI.Set.RelativeComplementCollection`
- `LRA.VolumeI.Set.CoverFailureIffRelativeComplementIntersectionNonempty`
- `LRA.VolumeI.Set.NoFiniteSubcoverIffRelativeComplementFIP`
- `LRA.VolumeI.Set.FiniteSubcoverIffRelativeComplementNotFIP`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Families.lean
```

The active Lean statement is written in finite-subcover form:

```text
HasFiniteSubcover C A
  <-> not FiniteIntersectionProperty(RelativeComplementCollection A C)
```

This is the compactness-ready version: an open-cover compactness proof will
instantiate `C` as an open cover, while the FIP side will be read as the
relative closed-complement family.

## Common Failure Modes

- Proving only the infinite-cover version and forgetting finite subcovers.
- Forgetting to intersect complements with `A`.
- Confusing "has the FIP" with "total intersection is nonempty."
- Dropping the word finite in the FIP condition.
- Treating open/closed language as essential; the proposition is set algebra
  before topology gives "open" and "closed" meaning.

## What This Unlocks

FIP--cover duality is the set-theoretic bridge to compactness.  Later topology
will define compactness by finite subcovers, while many proofs use the dual
closed-set FIP form.  This gate ensures that the conversion is already owned
before topology adds geometric content.
