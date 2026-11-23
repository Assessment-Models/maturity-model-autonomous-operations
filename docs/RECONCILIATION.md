# Reconciliation — canonical repository state (2026-11-23)

This repository is the canonical home of the Autonomous Operations Maturity Model,
asset `maturity-model-autonomous-operations`, currently declaring model version
`2.0.0`. Its authoritative model artifacts are the root manifest, scale,
evaluation specification, criteria register, assessment questionnaire and
touchpoint declaration.

## 1. Model structure

The authoritative criteria register contains **157 criteria across 6 dimensions
and 32 sub-dimensions**:

| Dimension | Sub-dimensions | Criteria |
|---|---:|---:|
| Party | 7 | 42 |
| Strategy | 5 | 23 |
| Technology | 4 | 23 |
| Operations | 6 | 27 |
| Culture | 5 | 20 |
| Data | 5 | 22 |
| **Total** | **32** | **157** |

The README and model guide are explanatory views of this register. Counts and
criterion identity are governed by the YAML register, not by prose.

## 2. Scale and evaluation

The model owns the scale instance `dea:scale-autonomous-operations-v1`,
version `2.0.0`. It declares six entries:

- `L-0 Not Assessed`: an assessment-state sentinel, not a capability level.
- `L-1 Absent` through `L-5 Autonomous`: the five scored capability levels.

The five scored levels map one-to-one to the canonical v2 bands:

| Model level | Canonical band | Score range | Effort multiplier |
|---|---|---:|---:|
| L-1 | Emergent | 0–20 | 1.0 |
| L-2 | Structured | 21–45 | 1.5 |
| L-3 | Systematic | 46–70 | 2.5 |
| L-4 | Adaptive | 71–88 | 4.0 |
| L-5 | Self-Optimising | 89–100 | 6.0 |

The AO Autonomy Index is calculated from the model's declared dimension
weights. The weakest-link gate caps the reported maturity level at the lowest
in-scope gating criterion; it does not change the index.

Effort-adjusted value (EAV) is a separate supplementary measure calculated
from the unrounded index using marginal band contributions:

`EAV(S) = Σ(Pₖ(S) / Mₖ)`

Each score point is allocated once to its band interval and divided by that
band's effort multiplier. The whole index is not multiplied by the multiplier
of the resolved band. At index 68, EAV is 45.87; at index 64, EAV is 44.27.
EAV does not replace the AO Autonomy Index or determine the gated maturity
level.

The frozen v1-alpha catalog lineage retains its historical scale and scoring
semantics. It is not the source of the current repository's v2.0.0 model
semantics.

## 3. Relationship and touchpoint reconciliation

The model register retains its existing relationship to
`dea:maturity-operations` as `derived-from` (the source relationship label
`extends` is retained as provenance metadata). This relationship is not
removed, weakened or replaced by the touchpoint record.

The root manifest now declares the existing artifact through the optional
typed declaration:

```yaml
touchpoints:
  declaration: touchpoints.yaml
```

The touchpoint artifact mirrors Operations' `tp-ops-x-autonomous-operations`
with `tp-autonomous-operations-x-operations`. Its mapping remains directional:
Operations reliability evidence feeds Autonomous Operations; Autonomous
Operations retains ownership of the intent-driven closed-loop autonomy
assessment. Both records remain explicitly draft against
`maturity-touchpoint-contract@0.1.0-draft`. The manifest declaration establishes
artifact discovery and Level 2 path validation; it does not assert that the
draft touchpoint-record contract has been published or that ecosystem
reciprocity validation has passed.

The model's contract handshake remains
`maturity-scale-contract@1.0`, sourced from
`technehub-labs/dea-metamodel`. The evaluation's band reference and dependency
remain `dea:maturity-bands-v2@1.0.0`. These are distinct from the touchpoint
artifact handshake and are not conflated.

## 4. Registry and release identity

The Assessment Registry currently records version `2.0.0` and immutable
reference `8ccf747e483d3c1bd82a46d1a5bb09a045a1e81d`. That commit exists.
The repository currently has no `v2.0.0` tag; `v1.0.1` is present. Accordingly,
the registry's immutable commit reference is verifiable, but the version-to-tag
release convention is not yet complete. Do not describe `v2.0.0` as a
published Git tag until that tag is created and verified.

The registry record's notes still contain historical v1.0.1 and pending-branch
statements. Those should be reconciled in a separate registry change, preserving
the existing immutable v2.0.0 commit reference until release/tag disposition is
formally resolved.

## 5. Conformance and validation

- Level 1 local validation checks manifest identity, contract handshake shape,
  scale structure, register references, example scoring and evaluation assets.
- Level 2 contract conformance validates the manifest and resolves the declared
  contract against the pinned metamodel contract suite. The manifest's typed
  touchpoint declaration is checked for safe repository-relative path and
  file existence by the shared validator.
- Level 3 ecosystem validation remains responsible for registry resolution and
  cross-repository relationship/touchpoint reciprocity.

The reusable Level 2 workflow is now referenced by immutable commit SHA, as is
the repository-standard reusable workflow. The contract workflow currently
checks out its validator repository internally at `main`; this nested mutable
reference remains an upstream hardening item and is not represented here as
fully pinned.

## 6. Source-of-truth boundaries

- `model.yaml`: identity, contract handshake, dependencies, compatibility
  and typed optional artifact declarations.
- `maturity/scale.yaml`: model-owned level semantics.
- `maturity/evaluation.yaml`: scoring, aggregation, gating, EAV and assessment
  method.
- `maturity/model/autonomous-operations.yaml`: authoritative dimensions,
  sub-dimensions, criteria and model relationships.
- `touchpoints.yaml`: semantic seams, peer mappings, reciprocity and draft
  touchpoint-contract declaration.
- `assessment-registry`: asset identity and immutable release reference.
- `maturity-model-standard/registry/conformance.yaml`: repository-standard
  adoption and conformance classification.

No change in this reconciliation removes or weakens the Operations relationship,
changes model criteria, alters the five-level scoring semantics, or treats a
draft touchpoint contract as a published contract.
