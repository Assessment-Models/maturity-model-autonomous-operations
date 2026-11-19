# Glossary

Plain-language definitions for every term used in this repository. Where a term is normative, the authoritative definition lives in the machine-readable artifacts (`maturity/scale.yaml`, `maturity/evaluation.yaml`, and the criteria register in `maturity/model/autonomous-operations.yaml`); this glossary restates those definitions for readers. If a glossary entry ever disagrees with the YAML, the YAML wins.

## The model and its subject

- **Autonomous Operations (AO):** the operating model in which value streams are instrumented with AI, data, and closed-loop control, so that agents and autonomous systems learn, self-govern, and self-adapt, progressively shifting decisions and execution from humans to machines under designed human oversight.
- **Autonomy vs. automation:** automation executes predefined rules faster; autonomy means the system perceives, orients, decides, and acts toward a goal within governance constraints. The model scores the second.
- **Maturity (as assessed here):** the organization's ability to design, govern, operate, and continuously improve AO. It assesses the operating model, not the quantity of AI technology deployed.
- **Assessment subject:** the organization's operating model across its value streams; assessable per value stream or scenario, then rolled up organization-wide.
- **Value stream / scenario:** units of assessment scope, named in the scope charter. Criteria outside the declared scope neither score nor gate.
- **Intent:** the "what" expressed by humans (or partner systems) that a closed loop decomposes and fulfils; never the "how".

## Structure of the model

- **Dimension:** the top level of the assessment hierarchy. Six exist: Party, Strategy, Technology, Operations, Culture, Data.
- **Sub-dimension:** the 32 mid-level groupings inside dimensions.
- **Criterion:** the atomic assessed capability (157 total), each scored L-0 to L-4 with evidence. Identified by a dotted ID, e.g. 2.4.7.
- **Criteria register:** `maturity/model/autonomous-operations.yaml`; the authoritative structure of dimensions, sub-dimensions, and criteria.
- **Questionnaire:** the assessment instrument (`maturity/assessment-questionnaire.yaml`); one entry per criterion with the question, `what_to_observe`, `evidence_to_request`, level anchors, and gating flag.
- **Level anchors:** the observable, falsifiable definitions of L-0 to L-4 in `maturity/scale.yaml` against which every criterion is scored.

## The scale, bands, and stages

- **Scale:** the five ascending levels: L-0 Absent, L-1 Initial, L-2 Defined, L-3 Automated, L-4 Autonomous. Numbered from zero; see **level numbering**.
- **Band (canonical v2 band):** the index range the result resolves to, canonically numbered level-1 to level-5: Emergent (0-20), Structured (21-45), Systematic (46-70), Adaptive (71-88), Self-Optimising (89-100). Ranges are inclusive. See **level numbering**.
- **Level numbering:** two ladders with an offset of one. Scale levels (the capability ladder, what you score) count from zero: L-0 to L-4. Canonical bands (the band ladder, what the index resolves to) count from one: level-1 to level-5. L-0 resolves to band 1, L-1 to band 2, and so on. Always pair them in results ("L-2, band 3 Systematic"). Renumbering the scale levels is an upstream change request against the canonical scale owner, never a local edit. An upstream CR ([dea-metamodel #214](https://github.com/technehub-labs/dea-metamodel/issues/214)) proposes resolving the offset (L-0 plus L-1..L-5, one-to-one with the bands); adopt it only when the canonical instance releases the renumbering.
- **AO stage:** the model-level stage name for each level: Manual & Reactive, Instrumented & Assisted, Closed-Loop Automated, Goal-Driven Autonomy, Self-Improving Ecosystem.
- **OODA loop:** Observe, Orient, Decide, Act; the closed-loop control pattern every assessed loop follows.
- **OODA stage ownership:** the progression axis of the model. Maturity is defined by who owns each OODA stage, from humans owning all four at L-0 to a self-learning loop with humans governing values at L-4.

## Scoring

- **Level points:** the fixed points a scored level earns: L-0 = 20, L-1 = 45, L-2 = 70, L-3 = 88, L-4 = 100.
- **Unassessed criterion:** scores 0 points and lowers evidence confidence; it never inflates the index.
- **Dimension score:** the unweighted mean of its criteria's points.
- **AO Autonomy Index:** the 0-100 weighted mean of dimension scores; the model's headline result.
- **Weight profile:** the named dimension weight set chosen in the scope charter and recorded in the result. Two ship with the model: `default`, and `comms-provider` (weights Operations higher, for CSPs). Results are comparable only within the same profile.

## The gate

- **Gating criteria:** the four closed-loop spine criteria in Operations, marked `gating: true`: 4.1.1 (Observe: detect), 4.1.2 (Orient: root-cause), 4.1.3 (Decide), 4.1.4 (Act).
- **Weakest-link gate:** the organization's band cannot exceed the band of its lowest in-scope gating criterion. A loop that cannot act cannot make the organization autonomous. Scope-excluded criteria do not gate.

## Effort and value

- **Effort multiplier:** a per-band planning and cost signal (1.0x, 1.5x, 2.5x, 4.0x, 6.0x), expressing that earning a point costs more in higher bands. It is not a score multiplier.
- **Effort-adjusted value:** AO Autonomy Index × effort multiplier of the resolved band; makes diminishing returns explicit for portfolio decisions.

## Evidence and confidence

- **Evidence pack:** the artifacts, metrics, logs, audit-trail samples, dashboards, policies, and runbooks backing a criterion score. Every determination must trace to evidence.
- **Evidence provenance / validation / sufficiency:** recorded per evidence item: where it came from, whether it was verified, and whether it is enough to score against the anchor.
- **Assessor independence:** evidence is sampled and verified by an assessor independent of the team that produced it.
- **Self-attestation:** claims made without verification; alone, it caps confidence at Medium.
- **Confidence:** High = independently verified evidence for at least 80% of criteria in the dimension; Medium = 50-79% verified; Low = below 50% or self-attested only. Reported alongside every result.

## Roles and process

- **Assessor:** scores criteria and validates evidence; independent of the evidence owners.
- **Assessment subject:** the organization or value stream being assessed.
- **Evidence owner:** the party producing and standing behind an evidence item.
- **Reviewer:** reviews and approves results before publication.
- **Scope charter:** the required first input; declares value streams, scenarios, exclusions, and weight profile.
- **Cadence:** reassess quarterly (recommended), or event-driven after major closed-loop or agent deployments.
- **Roll-up:** combining per-value-stream or per-scenario results into an organization-wide result.
- **Level semantics:** definitionally frozen; changed only through a change request, never by editing scores.

## Ecosystem terms (upstream references)

- **dea:maturity-bands-v2:** the canonical band and multiplier definitions, owned in `technehub-labs/dea-metamodel`. This repository binds to them by ID and version; it never restates or modifies them.
- **dea-maturity-v2:** the score scheme this model evaluates under.
- **Contract handshake:** the pinned, declared agreement by which this repository conforms to the ecosystem's maturity-scale contract; checked by CI (Level 2), not asserted in prose.
- **CI levels:** Level 1 local validation on every PR; Level 2 contract conformance against a pinned metamodel; Level 3 registry resolution.
- **Release:** repository releases are SemVer `vX.Y.Z` tags; the model release (currently 1.0.1, stable) and repository conformance are tracked separately.