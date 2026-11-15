# Repository standard for maturity-model repositories (CR-AM-12, Layer 2)

Normative template every `maturity-model-<domain>` repository follows. Architecture is
standardized; **model content (dimensions, scale semantics, scoring, criteria) is model-owned**
and must never be inherited from another model (ADR-AM-12-03).

## 1. Required root files
`model.yaml` (manifest: id/type/name/version + §15 conformance handshake + compatibility +
dependencies, per `assessment-ci/schemas/model-manifest.schema.json`), `VERSION` (SemVer),
`CHANGELOG.md` (Keep a Changelog), `README.md` (per §3 spec), `CONTRIBUTING.md`, `LICENSE`.

## 2. Directory conventions
```
maturity/
  scale.yaml          # model-owned scale OR bound canonical instance (never restate canonical bands)
  model/<domain>.yaml # criteria/dimension register (machine-readable, authoritative)
  evaluation.yaml     # scoring + assessment method (optional enrichment slot)
  assessment-questionnaire.yaml  # instrument (optional enrichment slot)
docs/                 # GOVERNANCE.md, REPO-STANDARD.md, ARCHITECTURE.md, RECONCILIATION.md, checklists
examples/             # worked examples with computable scoring math
scripts/local_validate.py
.github/workflows/    # local-model-ci.yml (Level 1) + contract-conformance.yml (Level 2, pinned)
```

## 3. README specification (required sections)
Overview · why the model matters · purpose & scope · conceptual foundations · model architecture ·
maturity levels · assessment methodology · evidence framework · scoring & determination · worked
example · using results · ecosystem integration · repository architecture · governance/provenance/
versioning. Model-first: the README explains the authoritative YAML artifacts; repository mechanics
(CI, layout, license) go last.

## 4. Metadata conventions
SemVer versions; releases as immutable `vX.Y.Z` git tags; registry references are tags/SHAs/digests
(never main/master/latest); relationships use the upstream closed vocabulary (CR-AM-11 §17) with
`source_relationship_type` preserved on normalization; machine-readable YAML is authoritative over
prose (ADR-AM-12-04).

## 5. Governance rules
PR + rationale + CHANGELOG entry required; never alter level semantics without a CR; bands/contracts
are canonical upstream (dea-metamodel) — reference, don't copy; no git submodules (CR-AM-11 §23);
model definition stays separate from assessment execution/results/benchmarking (ADR-AM-12-09).

## 6. Conformance requirements
Level 1: `scripts/local_validate.py` green on every PR (manifest, handshake, scale integrity,
register↔scale resolution, example scoring math). Level 2: `contract-conformance.yml` reusing
`Assessment-Models/assessment-ci` at an immutable `dea-metamodel` pin. Level 3: registry record
resolves (`resolve.py <id> --check`).

## 7. Reference implementation
`maturity-model-autonomous-operations` (this repo). New model repos instantiate this template and
register in `assessment-registry`.
