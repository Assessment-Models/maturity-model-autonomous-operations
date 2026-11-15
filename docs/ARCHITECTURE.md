# Architecture — Assessment-Models maturity-model ecosystem (CR-AM-12)

Visual companion to `README.md`. The standard has four layers; this repository is the
Layer-3 **reference implementation**.

## Four layers

```mermaid
flowchart TB
    subgraph L1["Layer 1 — Ecosystem governance (org-governed)"]
        GOV[".github GOVERNANCE.md<br/>taxonomy + rules"]
        REG["assessment-registry<br/>identity spine, immutable refs"]
        CI["assessment-ci<br/>reusable CI + manifest schema"]
        META["technehub-labs/dea-metamodel<br/>canonical contracts + bands"]
    end
    subgraph L2["Layer 2 — Repository standard (CR-AM-12 deliverable)"]
        STD["docs/REPO-STANDARD.md<br/>template, README spec,<br/>directory + metadata conventions"]
    end
    subgraph L3["Layer 3 — Individual maturity models (model-owned content)"]
        AO["maturity-model-autonomous-operations<br/>REFERENCE IMPLEMENTATION (this repo)"]
        DTM["maturity-model-digital-transformation"]
        CAT["dea-catalog-maturity-models<br/>(frozen legacy lineage)"]
        FUT["maturity-model-&lt;domain&gt; …"]
    end
    subgraph L4["Layer 4 — Assessment consumers (not in model repos)"]
        AM["assessment-model-*"]
        EXE["assessment executions"]
        RES["results"]
        BENCH["benchmarking"]
    end
    L1 --> L2 --> L3
    META -. contracts .-> AO
    AO --> AM --> EXE --> RES --> BENCH
```

## Logical lifecycle

```mermaid
flowchart LR
    A["Ecosystem governance"] --> B["Repository standard"]
    C["Canonical contracts<br/>(dea-metamodel, pinned)"] --> D["Domain maturity model<br/>(this repo)"]
    B --> D
    D --> E["Assessment model"]
    E --> F["Assessment execution"]
    F --> G["Assessment result"]
    G --> H["Benchmarking & improvement"]
```

A maturity **model** defines maturity semantics (this repo). An assessment **model** defines how an
assessment is structured. An **execution** records an instance; a **result** records its determination.
These distinctions stay intact (CR-AM-01 decoupling): model repos never host executions, results,
or benchmarking (ADR-AM-12-09).

## This repository's place in the standard

```
maturity-model-autonomous-operations/
├── model.yaml                        # CR-AM-11 §15 contract handshake (manifest)
├── VERSION  CHANGELOG.md  CONTRIBUTING.md  LICENSE  README.md
├── maturity/
│   ├── scale.yaml                    # canonical scale, BOUND not minted (dea-metamodel)
│   ├── evaluation.yaml               # v2-band scoring + assessment method
│   ├── assessment-questionnaire.yaml # 157-criteria instrument
│   └── model/autonomous-operations.yaml  # criteria register (verbatim from lineage)
├── docs/                             # GOVERNANCE, REPO-STANDARD, ARCHITECTURE, …
├── examples/                         # worked examples (v2 band math)
├── scripts/local_validate.py         # Level 1 validator
└── .github/workflows/                # Level 1 local CI + Level 2 contract conformance
```
