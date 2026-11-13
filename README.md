# Autonomous Operations Maturity Model

Autonomous Operations (AO) maturity and assessment model — the enterprise operating model in which value streams are instrumented with AI, data and closed-loop control so that agents and autonomous systems learn, self-govern and self-adapt, with intent driving the closed loops. Harvested and cleaned from an industry AO maturity workbook (v1.8.0), gap-filled against 2025-26 industry sources.

## Status

`1.0.1` · stable — canonical upstream scale, OODA stages as model metadata

## Repository standard

This repository is the **reference implementation** of the
[AM-MODEL-REPOSITORY-STANDARD](https://github.com/Assessment-Models/maturity-model-standard)
(`standard.yaml`, conformance level `structural`), established by
[CR-AM-ORG-RES-000](https://github.com/Assessment-Models/maturity-model-standard/blob/main/change-requests/CR-AM-ORG-RES-000.md).
The declaration, structure and version coherence (README ↔ `model.yaml` ↔ `VERSION`
↔ `standard.yaml`) are validated by the reusable repository-standard conformance
workflow, alongside the three CI levels below.

## Placement

This repository is the independent home of the `dea:maturity-autonomous-operations` maturity
model. Under the Assessment-Models organisation taxonomy (CR-AM-11 §8,
`.github/GOVERNANCE.md`) a maturity model is an independently versioned asset
with its own releases, issues, roadmap and contributors.

Assessment-Models is categorically the home of **capability** assessment
assets. The maturity model for *enterprise architecture practice itself* is
owned by the DEA federation (`technehub-labs`), not by this organisation.

## Scoring scheme

Canonical v2 bands — `dea:maturity-bands-v2` v1.0.0
(`technehub-labs/dea-metamodel`). Non-linear band widths 20/25/25/18/12 with
per-level effort multipliers 1.0 → 6.0:

| Band id | Name | Range | Width | Effort multiplier | Legacy (v1) name |
|---|---|---|---|---|---|
| `level-1-emergent` | Emergent | 0–20 | 21 | 1.0× | Ad Hoc |
| `level-2-structured` | Structured | 21–45 | 25 | 1.5× | Defined |
| `level-3-systematic` | Systematic | 46–70 | 25 | 2.5× | Managed |
| `level-4-adaptive` | Adaptive | 71–88 | 18 | 4.0× | Quantitatively Managed |
| `level-5-self-optimising` | Self-Optimising | 89–100 | 12 | 6.0× | Optimising |

## Layout

```
maturity-model-autonomous-operations/
├── model.yaml                       # CR-AM-11 §15 contract handshake
├── standard.yaml                    # CR-AM-ORG-RES-000 repository-standard declaration
├── VERSION
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── maturity/
│   ├── scale.yaml                     # canonical AO scale (bound, not minted)
│   └── model/autonomous-operations.yaml
├── examples/
│   └── autonomous-operations-2026.yaml
├── scripts/
│   └── local_validate.py            # Level 1 validator
└── .github/workflows/
    ├── local-model-ci.yml           # Level 1
    ├── contract-conformance.yml     # Level 2 (reusable from assessment-ci)
    └── repository-standard.yml      # repository-standard conformance
                                       # (reusable from maturity-model-standard)
```

## CI levels

1. **Level 1 — local model CI** (`.github/workflows/local-model-ci.yml`):
   runs `scripts/local_validate.py` — manifest contract, handshake shape,
   scale integrity, register-to-scale resolution, worked-example scoring math
   against the canonical v2 bands.
2. **Level 2 — contract conformance**
   (`.github/workflows/contract-conformance.yml`): reuses
   `Assessment-Models/assessment-ci/.github/workflows/contract-conformance.yml`
   to resolve the §15 handshake against the published contract suite at the
   pinned `dea-metamodel` release.
3. **Level 3 — ecosystem CI**: the registration record in
   `Assessment-Models/assessment-registry` is resolved by the ecosystem
   validator on every registry pull request.
4. **Repository-standard conformance**
   (`.github/workflows/repository-standard.yml`): reuses
   `Assessment-Models/maturity-model-standard/.github/workflows/repository-conformance.yml`
   to validate the repository-standard declaration, structure and version
   coherence (CR-AM-ORG-RES-000).

## Provenance

`technehub-labs/dea-metamodel` — `assessment-models/maturity/scale-examples/autonomous-operations-5level.yaml` (canonical scale, v1.0.0, status stable) for the level ladder; `Assessment-Models/dea-catalog-maturity-models` — `maturity-models/autonomous-operations/` bundle for the criteria register, carried verbatim.

Level semantics (characteristics, exit criteria, evidence) are carried
**verbatim** from the source; only the scoring fields differ between the
frozen v1-alpha lineage and the canonical v2 scheme.

## Licence

MIT — see `LICENSE`.
