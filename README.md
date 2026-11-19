# Autonomous Operations Maturity Model

**`dea:maturity-autonomous-operations`** · release 1.0.1 (stable) · MIT license

This model measures how mature an organization is at **running** Autonomous Operations: an operating model in which value streams are instrumented with AI, data, and closed-loop control, so that agents and autonomous systems progressively take over routine cognitive work under designed human oversight.

It assesses the **operating model, not the technology count**. Two organizations with identical AI tooling can score very differently, because the model scores governance, evidence, party experience, culture, and data as heavily as the automation itself.

---

## Who this is for

- **Operations and technology leaders** planning closed-loop automation and wanting an honest baseline before investing.
- **Transformation offices** that need to track AO progress quarter over quarter with a repeatable instrument.
- **Assessors and auditors** who need evidence-based, traceable scoring rather than opinion.

**Not for:** general AI-adoption strategy, task automation tooling, or digital transformation at large. Those are covered by sibling models in this organization (see [When to use a sibling model](#when-to-use-a-sibling-model)).

## What it assesses

Six dimensions, 32 sub-dimensions, 157 criteria. Each criterion is scored L-0 to L-4 against defined anchors, and evidence is required for every score.

| Dimension | What it measures | Sub-dims | Criteria |
|---|---|---|---|
| 1 Party | Customer, partner, employee, and smart-things engagement, experience, insight, and trust | 7 | 41 |
| 2 Strategy | Value model, business architecture, financial management, governance, sustainability | 5 | 22 |
| 3 Technology | Autonomy capabilities, architecture, resources, agent lifecycle | 4 | 22 |
| 4 Operations | Closed-loop flows: anomaly, assurance, complaints, value uplift, net-zero, fulfillment | 6 | 25 |
| 5 Culture | Innovation, quality, culture management, alignment, workplace enablement | 5 | 19 |
| 6 Data | Data lifecycle, quality, security, governance, value realization | 5 | 26 |

**The grain of the model.** Every criterion names a specific, observable capability. A real example from the Party dimension:

> **1.1.1 Predictive Engagement.** The organization enables Predictive Engagement by using intelligent automation and customer insights (such as behavioral data and user profiles) to proactively anticipate customer needs and dynamically determine the right target, channel, and timing of engagement.

And the corresponding questionnaire item asks: *"To what extent is Predictive Engagement in place within the assessment scope?"*, with observable behavior, requested evidence (CX analytics and NPS/CSAT exports, channel telemetry and consent records, campaign performance data, and more), and the L-0 to L-4 level anchors.

## The five levels

Progression is defined by **who owns each OODA stage** (Observe, Orient, Decide, Act):

| Level | Name | Band (range) | AO stage | Who decides and acts |
|---|---|---|---|---|
| L-0 | Absent | 1: Emergent (0-20) | Manual & Reactive | Humans perform every OODA stage |
| L-1 | Initial | 2: Structured (21-45) | Instrumented & Assisted | Machines observe; humans orient and decide |
| L-2 | Defined | 3: Systematic (46-70) | Closed-Loop Automated | Loops decide within rules; humans set goals and handle exceptions |
| L-3 | Automated | 4: Adaptive (71-88) | Goal-Driven Autonomy | Agents decide and act within guardrails; humans set intent and audit |
| L-4 | Autonomous | 5: Self-Optimising (89-100) | Self-Improving Ecosystem | Loops self-learn ecosystem-wide; humans govern values and audit |

**Numbering convention.** Scale levels count from zero (L-0 to L-4, the capability ladder you score) while the canonical bands they resolve to count from one (level-1 to level-5, the band ladder the index lands in). The ladders are offset by one: L-0 resolves to band 1, L-2 to band 3. When reading or writing results, always pair them ("L-2, band 3 Systematic"). Renumbering the scale levels is not a local edit: the scale binds the canonical instance owned upstream in `technehub-labs/dea-metamodel`, and level semantics change only through a change request (see Governance below). A change request proposing to resolve the offset by renumbering the scale to L-0 plus L-1..L-5, aligned one-to-one with the bands, is filed upstream ([dea-metamodel #214](https://github.com/technehub-labs/dea-metamodel/issues/214)); until the ecosystem ratifies and releases it, the pairing convention above applies.

## How scoring works

1. Each of the 157 criteria is scored L-0 to L-4; the level maps to points (L-0 = 20, L-1 = 45, L-2 = 70, L-3 = 88, L-4 = 100).
2. Dimension score = mean of its criteria. **AO Autonomy Index (0-100)** = weighted mean of dimensions (weights are declared in `maturity/evaluation.yaml`; the default profile weights Strategy, Operations, and Technology at 0.20 each, Data and Party at 0.15, Culture at 0.10; a `comms-provider` profile weights Operations higher).
3. The index resolves to a maturity band.
4. **Weakest-link gate:** the organization's band cannot exceed the band of its lowest in-scope gating criterion. The four gating criteria (4.1.1 to 4.1.4) are the closed-loop spine: detect, root-cause, decide, act. A loop that cannot act cannot make the organization autonomous.
5. **Effort-adjusted value** = index × effort multiplier of the resolved band (1.0× to 6.0×), a planning signal for portfolio decisions, not a score multiplier.

A full walkthrough with real numbers: [docs/WORKED-EXAMPLE.md](docs/WORKED-EXAMPLE.md).

## Run an assessment

- Define a **scope charter**: which value streams and scenarios, which weight profile, what is excluded.
- Gather an **evidence pack** per criterion; an independent assessor verifies a sample. Self-attestation alone caps confidence at Medium.
- Score against the anchors, aggregate, apply the gate, and publish the report: index, band, per-dimension profile, gaps, and roadmap.
- Reassess quarterly, or after major closed-loop or agent changes.

Start small: [docs/QUICKSTART.md](docs/QUICKSTART.md) walks a 60-minute pilot assessment on a single value stream.

For a narrative tour of the dimensions and what each level looks like in practice: [docs/MODEL-GUIDE.md](docs/MODEL-GUIDE.md).

## Documentation map

| Document | What it gives you |
|---|---|
| [docs/QUICKSTART.md](docs/QUICKSTART.md) | Run a 60-minute pilot assessment on one value stream |
| [docs/MODEL-GUIDE.md](docs/MODEL-GUIDE.md) | Dimension-by-dimension narrative, level anchors, glossary |
| [docs/WORKED-EXAMPLE.md](docs/WORKED-EXAMPLE.md) | End-to-end scoring walkthrough, including the weakest-link gate |
| [docs/GLOSSARY.md](docs/GLOSSARY.md) | Every term used in the model, defined in plain language |
| `maturity/model/autonomous-operations.yaml` | The criteria register (authoritative) |
| `maturity/scale.yaml` | The five-level scale (authoritative) |
| `maturity/evaluation.yaml` | Scoring model and assessment method (authoritative) |
| `maturity/assessment-questionnaire.yaml` | The instrument: one entry per criterion |
| `docs/ARCHITECTURE.md` | Repository and ecosystem architecture |
| `docs/REPO-STANDARD.md`, `docs/GOVERNANCE.md` | Repository conformance and governance (maintainers) |

## Key terms

All terms, including scoring and ecosystem vocabulary, are defined in [docs/GLOSSARY.md](docs/GLOSSARY.md). The essentials:

- **OODA loop:** Observe, Orient, Decide, Act; the closed-loop control pattern the model uses as its progression axis.
- **Gating criterion:** one of the four closed-loop spine criteria (4.1.1 to 4.1.4) that caps the organization's band.
- **Band:** the resolved maturity band (Emergent, Structured, Systematic, Adaptive, Self-Optimising), canonically numbered level-1 to level-5; scale levels count from zero, so always pair level and band when reading results.
- **Effort-adjusted value:** index × band effort multiplier; expresses that higher bands cost disproportionately more per point.
- **Confidence:** High (at least 80% of criteria independently verified), Medium (50-79%), Low (below 50% or self-attested only).

## When to use a sibling model

| If your question is about... | Use |
|---|---|
| The whole operating model for autonomous, closed-loop operations | **This model** |
| Digital transformation strategy or AI adoption at large | The Digital Transformation model |
| Technology capability and architecture in isolation | The Technology model |
| Operations and service delivery short of closed-loop autonomy | The Operations and Services-Delivery models |

Relationships between models are declared in the register and the assessment registry. They do not imply score equivalence.

## Repository layout

```text
maturity-model-autonomous-operations/
├── model.yaml · VERSION · CHANGELOG.md · CONTRIBUTING.md · LICENSE · README.md
├── maturity/  scale.yaml · evaluation.yaml · assessment-questionnaire.yaml · model/autonomous-operations.yaml
├── docs/      QUICKSTART.md · MODEL-GUIDE.md · WORKED-EXAMPLE.md · ARCHITECTURE · GOVERNANCE · REPO-STANDARD · RECONCILIATION · checklists
├── examples/  worked examples with computable v2-band scoring math
├── scripts/local_validate.py
└── .github/workflows/  local-model-ci.yml · contract-conformance.yml
```

The YAML artifacts are authoritative; documentation explains them. CI validates the model on every PR (Level 1), checks contract conformance against a pinned metamodel (Level 2), and resolves the registry identity (Level 3).

## Governance, lineage, and versioning

- **Lineage:** the criteria register was harvested from an industry AO maturity workbook (v1.8.0) and carried verbatim (157/157 criteria, zero diffs; see `docs/RECONCILIATION.md`), then gap-filled against 2025-26 industry sources. Inherited, adapted, and new content is recorded per criterion.
- **Ownership:** the Assessment-Models organization; this repository is independently versioned (SemVer, released as `vX.Y.Z` tags). Level semantics change only through a change request; canonical bands and contracts are owned upstream and referenced, never restated.
- **License:** MIT.