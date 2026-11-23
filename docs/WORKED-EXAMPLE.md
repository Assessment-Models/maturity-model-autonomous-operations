# Worked example: from criterion scores to a decision

This document narrates the two examples shipped in `examples/`, step by step, including the arithmetic and, more importantly, the decisions each result should trigger. Read it alongside `examples/autonomous-operations-2026.yaml` and `examples/assessment-example-gate.yaml`; numbers here are taken from those files.

## Example A: a healthy aggregate (examples/autonomous-operations-2026.yaml)

Scope: an illustrative whole-organization assessment using the default weight profile. The example records dimension scores rather than per-criterion detail, but the arithmetic is identical either way: dimension score = mean of its criteria, index = weighted mean of dimensions.

| Dimension | Score | Weight (default) | Contribution |
|---|---|---|---|
| Party | 56 | 0.15 | 8.40 |
| Strategy | 72 | 0.20 | 14.40 |
| Technology | 68 | 0.20 | 13.60 |
| Operations | 74 | 0.20 | 14.80 |
| Culture | 66 | 0.10 | 6.60 |
| Data | 68 | 0.15 | 10.20 |
| **AO Autonomy Index** | | | **68.00** |

**Resolution:**

1. Index 68 falls in 46-70: band **Systematic**, AO stage **Closed-Loop Automated**.
2. EAV = 20/1.0 + 25/1.5 + 23/2.5 = **45.87**. This uses marginal band contributions, not the full index multiplied by the resolved band's multiplier.
3. Gating criteria: this example demonstrates aggregation; in a real assessment, confirm all four gating criteria (4.1.1 to 4.1.4) score at or above the level implied by the resolved band before accepting it.

**How to read it:**

- The per-dimension profile is flat (60 to 74): no dimension is dragging. That shape matters more than the headline number. A 68 built on a flat profile is durable; a 68 built on Strategy 90 and Culture 30 is not.
- **Reaching the next band** (Adaptive, 71-88) needs roughly 3 index points. Points get more expensive as you climb: the effort multiplier rises from 2.5× to 4.0×, and the model treats that as a planning signal, not a reason to stop.
- The cheapest route to Adaptive here is the heaviest-weighted dimensions that score lowest among them (Party at 56, weighted 0.15), plus confirming the gating spine is comfortably at L-3 or above, so nothing caps the band.

## Example B: the weakest-link gate (examples/assessment-example-gate.yaml)

Scope: two value streams, order-to-activate and trouble-to-resolve, default weight profile. Eight criteria were scored in this illustrative sample:

| Criterion | OODA stage / theme | Level | Band | Points | Gating |
|---|---|---|---|---|---|
| 4.1.1 | Observe (detect) | L-3 | 3: Systematic | 70 | yes |
| 4.1.2 | Orient (root-cause) | L-2 | 2: Structured | 45 | yes |
| 4.1.3 | Decide | L-3 | 3: Systematic | 70 | yes |
| 4.1.4 | Act | L-3 | 3: Systematic | 70 | yes |
| 4.2.5 | Operations flow criterion | L-3 | 3: Systematic | 70 | no |
| 3.3.8 | Technology criterion | L-3 | 3: Systematic | 70 | no |
| 2.4.7 | Strategy: guardrails, escalation & audit | L-2 | 2: Structured | 45 | no |
| 3.1.8 | Technology criterion | L-2 | 2: Structured | 45 | no |

**Resolution, as recorded in the example:**

1. The sampled Operations slice averages **63.75**; the illustrative weighted index across dimensions is **64**.
2. Index 64 falls in 46-70: **band from index = Systematic**.
3. Weakest-link gate: the lowest in-scope gating criterion is **4.1.2 (root-cause) at L-2**, which maps to the **Structured** band (21-45).
4. The gate caps the result: **org band = Structured**, AO stage = **Instrumented & Assisted**, EAV = 20/1.0 + 25/1.5 + 19/2.5 = **44.27**. Evidence confidence: Medium.

**How to read it:**

- The index landed in Systematic, but root-causing is still human-led, so the organization is capped at Structured. The gate exists to make the real blocker visible instead of letting a healthy average hide it.
- **The decision this result should trigger:** invest in automating root-cause (the Orient stage) before spending anything on polishing detection or party engagement. Moving 4.1.2 from L-2 to L-3 alone can lift the entire organization's band, at a fraction of the effort of raising dimension averages.
- Note the secondary signal: 2.4.7 (guardrails, escalation, audit) also sits at L-2. Raising the gate without raising guardrail maturity would be exactly the wrong lesson to take: the model scores bounded autonomy, not unleashed automation. An estate that acts autonomously without auditable guardrails is a risk, not a maturity gain.

## Using your own results

Every assessment report contains: the AO Autonomy Index, the resolved band and AO stage, the per-dimension profile, per-criterion levels with evidence references, confidence, the weight profile used, the gate outcome, the marginal-band EAV, gaps, and a roadmap to the next band. When you read yours:

1. **Check the gate first.** If the gate caps you, the gating stage is the roadmap's first item, ahead of everything else.
2. **Read the profile shape.** Spread (max minus min dimension) tells you about durability; the weighted contributions tell you where a point is cheapest.
3. **Check confidence before celebrating.** A High-confidence 55 outranks a Low-confidence 70. Self-attestation caps at Medium by design.
4. **Sequence by effort-adjusted value, not by gap size.** The biggest gap is not always the best investment once band multipliers apply.
5. **Record the weight profile.** Results are only comparable across assessments with the same profile and scope; changing scope mid-series breaks the trend line.