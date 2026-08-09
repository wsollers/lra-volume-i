# 035: Set-Family and Cover Vocabulary

Targets:

- `def:indexed-family`
- `def:indexed-union`
- `def:indexed-intersection`
- `def:cover-full`
- `def:subcover`
- `def:finite-cover`
- `def:fip`

Proof file: none. This is a definition checkpoint, not a theorem gate.

Status: ready for concept ownership. Typed-set Lean vocabulary now exists for
the cover/FIP layer.

## Core Distinction

A family is not the same thing as the union of its members.

```text
family:      keeps the sets themselves as separate objects
union:       collapses the family into one set of points
```

This is the distinction that made the chapter necessary. Covers, topologies,
sigma-algebras, bases, filters, and Borel generators are all families or
collections of sets. Their meaning is destroyed if we collapse them too early.

## Definitions

An indexed family of subsets of `U` is a function:

```text
F : I -> P(U)
```

The indexed union is:

```text
x in union_i A_i iff exists i, x in A_i
```

The indexed intersection is:

```text
x in inter_i A_i iff forall i, x in A_i
```

A collection `C` covers `A` when:

```text
forall x in A, exists C0 in C, x in C0
```

A subcover is a subcollection that still covers the same set:

```text
C' subset C and C' covers A
```

A finite subcover is a subcover with finitely many members.

A collection `F` has the finite intersection property when every finite
subcollection has nonempty intersection.

## Cold-Understanding Checklist

You own this checkpoint when you can do all of the following without looking:

1. Explain why an indexed family is function-like data.
2. Explain why a collection of sets is a subset of a power set.
3. Translate a cover statement into an elementwise quantified statement.
4. Distinguish a cover from a subcover.
5. Explain why a finite subcover is finite as a collection of sets.
6. State FIP without accidentally claiming the total intersection is nonempty.
7. Explain how cover language prepares compactness.

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Set.SetCollection`
- `LRA.VolumeI.Set.IndexedFamilyOfSubsets`
- `LRA.VolumeI.Set.CollectionUnion`
- `LRA.VolumeI.Set.CollectionIntersection`
- `LRA.VolumeI.Set.Covers`
- `LRA.VolumeI.Set.Subcover`
- `LRA.VolumeI.Set.FiniteCollection`
- `LRA.VolumeI.Set.FiniteSubcover`
- `LRA.VolumeI.Set.FiniteIntersectionProperty`
- `LRA.VolumeI.Set.CoversElementwiseIff`
- `LRA.VolumeI.Set.SubcoverIff`
- `LRA.VolumeI.Set.FiniteSubcoverIff`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Set\Families.lean
```

## What This Unlocks

This vocabulary is the bridge to compactness and later closure systems. It is
also the correct substrate for topologies, sigma-algebras, generated
structures, and Borel sets.
