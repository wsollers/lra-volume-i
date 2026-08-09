# 033: Image of a Preimage

Target: `thm:image-of-preimage`

Proof file: `volume-i/book-sets/functions/proofs/functions/prf-image-of-preimage.tex`

Status: ready for handwritten proof, then LaTeX population.  Typed-set Lean
stubs now exist for both displayed laws.

## Statement

For a function `f : A -> B` and a target-side set `T subset B`:

```text
f(f^{-1}(T)) = T intersection im(f)
```

Consequently:

```text
T subset im(f) -> f(f^{-1}(T)) = T
```

## Dependencies

- `def:function`: each input has one output.
- `def:image-function`: `im(f)` is the set of target values hit by `f`.
- `def:image-set`: `b in f(S)` iff some `a in S` satisfies `f(a)=b`.
- `def:preimage`: `a in f^{-1}(T)` iff `f(a) in T`.
- `def:intersection`: membership in both sets.
- `def:subset`: containment needed for the equality corollary.

## Plain-Language Reading

If we pull `T` back to the domain and then push it forward again, we recover
only the part of `T` that `f` can actually reach.  Points of `T` outside
`im(f)` have no preimage, so they disappear.

## Proof Skeleton

1. To prove `f(f^{-1}(T)) subset T intersection im(f)`, take
   `b in f(f^{-1}(T))`.
2. Unpack image membership: there is an `a` with `a in f^{-1}(T)` and
   `f(a)=b`.
3. From `a in f^{-1}(T)`, get `f(a) in T`; using `f(a)=b`, get `b in T`.
4. The same witness `a` gives `b in im(f)`.
5. For the reverse inclusion, take `b in T intersection im(f)`.
6. From `b in im(f)`, choose `a` with `f(a)=b`.
7. Since `b in T`, the equality gives `f(a) in T`, hence `a in f^{-1}(T)`.
8. Therefore `b in f(f^{-1}(T))`.
9. If `T subset im(f)`, then `T intersection im(f)=T`, so the corollary
   follows.

## Cold-Proof Checklist

You own this theorem when you can do all of the following without looking:

1. Explain why `f(f^{-1}(T))` cannot contain values outside `T`.
2. Explain why it also cannot contain values outside `im(f)`.
3. Use an image witness to prove the reverse inclusion.
4. Derive the equality case from `T subset im(f)`.
5. State the common special case: surjective `f` makes `im(f)=B`.

## Lean Formalization

Current checked Lean targets after restart:

- `LRA.VolumeI.Functions.ImagePreimageEqIntersectionRange`
- `LRA.VolumeI.Functions.ImagePreimageEqOfSubsetRange`

Location:

```text
F:\repos\lra-lean\LRA\VolumeI\Functions\Images.lean
```

## Common Failure Modes

- Claiming `f(f^{-1}(T))=T` without checking that `T` is inside the range.
- Forgetting the witness needed to prove membership in an image.
- Confusing the image of the whole function with the codomain.

## What This Unlocks

This theorem clarifies the asymmetry between image and preimage.  It is the
right preparation for restrictions to images, surjectivity, quotient maps, and
later measure/topology statements where preimages are exact but images usually
are not.
