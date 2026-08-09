# 032: Basic Preimage Laws

Target: `thm:basic-preimage-laws`

Proof file: `volume-i/book-sets/functions/proofs/functions/prf-basic-preimage-laws.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs now exist for all displayed laws.

## Statement

For functions `f : A -> B` and `g : B -> C`:

```text
f^{-1}(B) = A
f^{-1}(empty) = empty
f^{-1}(S triangle T) = f^{-1}(S) triangle f^{-1}(T)
id_A^{-1}(U) = U
(g comp f)^{-1}(R) = f^{-1}(g^{-1}(R))
f^{-1}(S) subset A
S subset T -> f^{-1}(S) subset f^{-1}(T)
f = h pointwise -> f^{-1}(S) = h^{-1}(S)
S = T -> f^{-1}(S) = f^{-1}(T)
R0 subset R1 -> (g comp f)^{-1}(R0) subset (g comp f)^{-1}(R1)
f^{-1}(S \ (T union R0)) =
  f^{-1}(S) \ (f^{-1}(T) union f^{-1}(R0))
```

## Dependencies

- `def:function`: a rule assigning one output to each input.
- `def:identity`: the function that returns each input unchanged.
- `def:composition`: `(g comp f)(a) = g(f(a))`.
- `def:preimage`: `a in f^{-1}(S)` iff `f(a) in S`.
- `def:subset`: every member of the left set belongs to the right set.
- `def:union`, `def:set-difference`, `def:sym-diff`: target-side set
  operations pulled back through preimage.

## Plain-Language Reading

A preimage asks which inputs land in a target set.  Because it is defined by
substituting `f(a)` into a membership predicate, it preserves logical structure
exactly.  This is why preimages are the natural language for topology and
measure: a function is continuous or measurable when pulling back the relevant
families of sets preserves their defining property.

## Proof Skeleton

1. Start every part with an arbitrary input `a in A`.
2. Expand the definition:

   ```text
   a in f^{-1}(S) iff f(a) in S
   ```

3. For universe and empty set, simplify `f(a) in B` and `f(a) in empty`.
4. For symmetric difference, expand both sides to the same exclusive-or
   condition.
5. For identity, use `id_A(a) = a`.
6. For composition, use `(g comp f)(a) = g(f(a))`.
7. For monotonicity, apply `S subset T` after obtaining `f(a) in S`.
8. For congruence in the function, replace `f(a)` with `h(a)`.
9. For congruence in the set, replace the target set by the equal one.
10. For the mixed difference/union law, expand both sides until both read:

    ```text
    f(a) in S and not (f(a) in T or f(a) in R0)
    ```

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. State the defining membership equivalence for preimage.
2. Prove the preimage of the whole codomain is the whole domain.
3. Prove the preimage of the empty set is empty.
4. Prove preimage commutes with composition.
5. Prove preimage monotonicity from subset inclusion.
6. Prove preimage preserves symmetric difference.
7. Prove the mixed difference-over-union drill identity.

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Functions.PreimageUniversal`
- `LRA.VolumeI.Functions.PreimageEmpty`
- `LRA.VolumeI.Functions.PreimageUnion`
- `LRA.VolumeI.Functions.PreimageIntersection`
- `LRA.VolumeI.Functions.PreimageDifference`
- `LRA.VolumeI.Functions.PreimageComplement`
- `LRA.VolumeI.Functions.PreimageSymmetricDifference`
- `LRA.VolumeI.Functions.PreimageIdentity`
- `LRA.VolumeI.Functions.PreimageComposition`
- `LRA.VolumeI.Functions.PreimageSubsetUniversal`
- `LRA.VolumeI.Functions.PreimageMonotone`
- `LRA.VolumeI.Functions.PreimageCongrFunction`
- `LRA.VolumeI.Functions.PreimageCongrSet`
- `LRA.VolumeI.Functions.PreimageCompositionMonotone`
- `LRA.VolumeI.Functions.PreimageDifferenceUnion`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Functions\Preimages.lean
```

## Common Failure Modes

- Treating `f^{-1}` as an inverse function instead of a preimage operator.
- Forgetting that `f^{-1}(S)` is a subset of the domain, not the codomain.
- Reversing the order in the composition law.
- Trying to prove image-style statements with preimage reasoning.

## What This Unlocks

This is the exact theorem pattern behind continuity and measurability.  Later,
instead of arbitrary target sets, the target sets will be open sets, closed
sets, Borel sets, or measurable sets.
