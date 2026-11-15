# Reconciliation — catalog bundle vs this repository (2026-11-12)

This repo (main `4c6d865`, v1.0.1) is the independent home of `dea:maturity-autonomous-operations`,
created via org governance. Reconciliation against the frozen catalog bundle
(`Assessment-Models/dea-catalog-maturity-models` @ `maturity-models/autonomous-operations/`):

## 1. Criteria register — carried verbatim ✅
`maturity/model/autonomous-operations.yaml` vs bundle `dimensions.yaml`: **157/157 criteria identical**
(ids, names, definitions, gating flags, provenance markers), 6 dimensions / 32 sub-dimensions
identical shape. Zero field diffs.

## 2. Scale & scoring — intentionally different, mapped ✅
- This repo binds the **canonical upstream scale** (`dea:scale-autonomous-operations-v1`, L-0 Absent …
  L-4 Autonomous, from `technehub-labs/dea-metamodel`) and scores on the **canonical v2 bands**
  (`dea:maturity-bands-v2` v1.0.0: inclusive ranges 0–20/21–45/46–70/71–88/89–100, i.e. 21/25/25/18/12
  integer scores, multipliers 1.0→6.0).
- The frozen v1-alpha catalog lineage keeps the v1 bands (Ad Hoc … Optimising).
- Mapping: L-0..L-4 ↔ canonical bands level-1..level-5 (legacy v1 names in `level_band_map`);
  OODA stage names carried as `ao_stage_by_ordinal` metadata.
- Effort-adjusted value = index × band multiplier (worked example: 68 × 2.5 = 170.0).

## 3. Assets ported from the bundle on this branch ✅
`maturity/evaluation.yaml`, `maturity/assessment-questionnaire.yaml` (157 criteria),
`examples/assessment-example-gate.yaml`, `examples/benchmark-weight-profiles.yaml`,
`docs/GOVERNANCE.md`, `docs/EXTRACTION-CHECKLIST.md`, enhanced `README.md`.

## 4. Pending
Registry record repoint (staged in `assessment-registry`, tag `v1.0.1`); catalog supersession
(PR merged in dea-catalog-maturity-models).
