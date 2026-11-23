#!/usr/bin/env python3
"""Level 1 — local model validation for maturity-model-autonomous-operations (CR-AM-11 §14).

Checks:
  1. model.yaml parses and matches the Assessment-Models manifest contract
     (`Assessment-Models/assessment-ci/schemas/model-manifest.schema.json`)
  2. the §15 contract handshake is well formed (contract id + version + source)
  3. maturity/scale.yaml declares 6 levels with ordinals 0..5 (L-0 Not Assessed,
     plus capability levels L-1..L-5 per dea-metamodel #214) and the
     expected identifiers, plus a conformant ordering/progression contract
  4. maturity/model/autonomous-operations.yaml carries the model identity, and its level references
     resolve against the scale
  5. examples/autonomous-operations-2026.yaml computes correctly: the aggregated score lies in [0, 100],
     the resolved band matches the canonical v2 bands, and the
     effort-adjusted value applies that band's effort multiplier

Exit 0 with OK when clean; exit 1 listing every failure otherwise.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


def load(rel: str):
    p = ROOT / rel
    if not p.is_file():
        errors.append(f"missing file: {rel}")
        return {}
    return yaml.safe_load(p.read_text()) or {}


manifest = load("model.yaml")
scale = load("maturity/scale.yaml")
register = load("maturity/model/autonomous-operations.yaml")
example = load("examples/autonomous-operations-2026.yaml")

# 1 — manifest shape
for key in ("id", "type", "name", "version", "conformance"):
    if key not in manifest:
        errors.append(f"model.yaml: missing required field {key}")
if manifest.get("type") not in ("maturity-model", "assessment-model", "assessment-tool"):
    errors.append(f"model.yaml: invalid type {manifest.get('type')!r}")

# 2 — contract handshake
conf = manifest.get("conformance") or {}
contract = conf.get("contract") or {}
if not contract.get("id"):
    errors.append("model.yaml: conformance.contract.id is required")
if not conf.get("version"):
    errors.append("model.yaml: conformance.version is required")
src = conf.get("source") or {}
if not src.get("organization") or not src.get("repository"):
    errors.append("model.yaml: conformance.source organization+repository are required")

# The Operations relationship is already formalized in the model register and
# touchpoints.yaml. Keep the typed manifest declaration in lockstep so Level 2
# can discover and validate the separately governed artifact.
touchpoint_decl = (manifest.get("touchpoints") or {}).get("declaration")
if touchpoint_decl != "touchpoints.yaml":
    errors.append("model.yaml: touchpoints.declaration must point to touchpoints.yaml")
elif not (ROOT / touchpoint_decl).is_file():
    errors.append("model.yaml: declared touchpoint artifact does not exist")

# 3 — scale
EXPECTED_LEVELS = ['L-0', 'L-1', 'L-2', 'L-3', 'L-4', 'L-5']
levels_actual = scale.get("levels") or []
if len(levels_actual) != len(EXPECTED_LEVELS):
    errors.append(f"scale: expected {len(EXPECTED_LEVELS)} levels, found {len(levels_actual)}")
for i, lvl in enumerate(levels_actual):
    if lvl.get("ordinal") != i:
        errors.append(f"scale: level {i} ordinal is {lvl.get('ordinal')!r}, expected {i}")
    if lvl.get("id") not in EXPECTED_LEVELS:
        errors.append(f"scale: unexpected level id {lvl.get('id')!r}")
    if not lvl.get("name") or not lvl.get("definition"):
        errors.append(f"scale: level {lvl.get('id')} requires name and definition")
if levels_actual and levels_actual[0].get("name") != "Not Assessed":
    errors.append("scale: level ordinal 0 must be the Not Assessed entry (L-0)")
if scale.get("ordering") != "ascending":
    errors.append("scale: ordering must be 'ascending'")
prog = scale.get("progression") or {}
if not prog.get("topology") or not prog.get("function"):
    errors.append("scale: progression requires topology and function")

# 4 — register identity + level resolution
if register.get("repo_id") != manifest.get("id"):
    errors.append(
        f"register repo_id {register.get('repo_id')!r} != manifest id {manifest.get('id')!r}"
    )
if not register.get("id"):
    errors.append("register: canonical model id is required")
scale_ids = {l.get("id") for l in levels_actual}
for ref in register.get("scale_levels", []) or []:
    if ref not in scale_ids:
        errors.append(f"register: scale level {ref!r} does not exist in the scale")

# 5 — example scoring math against the CANONICAL v2 bands
V2_BANDS = [('level-1-emergent', (0, 20), 'Emergent', 1.0, 'Ad Hoc'), ('level-2-structured', (21, 45), 'Structured', 1.5, 'Defined'), ('level-3-systematic', (46, 70), 'Systematic', 2.5, 'Managed'), ('level-4-adaptive', (71, 88), 'Adaptive', 4.0, 'Quantitatively Managed'), ('level-5-self-optimising', (89, 100), 'Self-Optimising', 6.0, 'Optimising')]


def band_for(score: float):
    for band, upper in zip(V2_BANDS, (20.0, 45.0, 70.0, 88.0, 100.0)):
        if score <= upper:
            return band[0], band[2], band[3]
    return None, None, None


def marginal_points(score: float) -> list[float]:
    lower = 0.0
    points = []
    for upper in (20.0, 45.0, 70.0, 88.0, 100.0):
        points.append(max(0.0, min(score, upper) - lower))
        lower = upper
    return points


def effort_adjusted_value(score: float) -> float:
    return sum(p / m for p, m in zip(marginal_points(score), (1.0, 1.5, 2.5, 4.0, 6.0)))


agg = example.get("aggregated_score")
if not isinstance(agg, (int, float)):
    errors.append("example: aggregated_score must be numeric")
else:
    if not (0 <= agg <= 100):
        errors.append(f"example: aggregated_score {agg} is outside [0, 100]")
    band_id, band_name, mult = band_for(float(agg))
    if band_id is None:
        errors.append(f"example: aggregated_score {agg} resolves to no canonical v2 band")
    else:
        declared = example.get("resolved_band")
        if declared != band_id:
            errors.append(f"example: resolved_band {declared!r} != computed {band_id!r}")
        eav = example.get("effort_adjusted_value")
        if eav is not None and mult is not None:
            expected = effort_adjusted_value(float(agg))
            if abs(float(eav) - expected) > 0.01:
                errors.append(
                    f"example: effort_adjusted_value {eav} != marginal-band EAV ({expected:.2f})"
                )
            display = example.get("effort_adjusted_value_display")
            if display is not None and abs(float(display) - round(expected, 2)) > 0.001:
                errors.append("example: effort_adjusted_value_display must be rounded marginal-band EAV")

# 6 — reconciliation/enrichment assets (evaluation, questionnaire, docs, extra examples)
evaluation = load("maturity/evaluation.yaml")
if evaluation.get("id") != "dea:evaluation-autonomous-operations-v1":
    errors.append("evaluation: unexpected id")
sc = evaluation.get("scoring") or {}
if abs(sum((sc.get("dimension_weights") or {}).values()) - 1.0) > 1e-9:
    errors.append("evaluation: dimension_weights do not sum to 1")
for pname, pw in (sc.get("weight_profiles") or {}).items():
    if abs(sum(pw.values()) - 1.0) > 1e-9:
        errors.append(f"evaluation: weight profile {pname} does not sum to 1")
lp = sc.get("level_points") or {}
if sorted(lp) != ["L-1", "L-2", "L-3", "L-4", "L-5"]:
    errors.append("evaluation: level_points must cover L-1..L-5")
if lp.get("L-0") not in (None, 0):
    errors.append("evaluation: L-0 (Not Assessed) must score 0 points")
if not isinstance(sc.get("effort_adjusted_value"), dict):
    errors.append("evaluation: effort_adjusted_value must define the normative marginal-band formula")
elif "P_k(S) / M_k" not in sc["effort_adjusted_value"].get("formula", ""):
    errors.append("evaluation: EAV formula must use marginal band points divided by band multipliers")
questionnaire = load("maturity/assessment-questionnaire.yaml")
qids = [c["id"] for sec in questionnaire.get("sections", []) for c in sec.get("criteria", [])]
reg_ids = [str(c["id"]) for d in register.get("dimensions", []) for sd in d.get("sub_dimensions", []) for c in sd.get("criteria", [])]
if sorted(qids) != sorted(reg_ids):
    errors.append("questionnaire criteria do not match the register criteria exactly")
for rel in ("docs/GOVERNANCE.md", "docs/REPO-STANDARD.md", "docs/ARCHITECTURE.md",
            "docs/EXTRACTION-CHECKLIST.md", "docs/RECONCILIATION.md",
            "examples/assessment-example-gate.yaml", "examples/benchmark-weight-profiles.yaml"):
    if not (ROOT / rel).is_file():
        errors.append(f"missing reconciled asset: {rel}")

if errors:
    print(f"FAIL — {len(errors)} error(s):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"OK — maturity-model-autonomous-operations: manifest + scale ({len(levels_actual)} levels) + register + example + evaluation/questionnaire/docs valid")
