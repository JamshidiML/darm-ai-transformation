# Target Architecture for Darm Industrial AI

## 1. Architecture objective

Create a secure, modular, evidence-preserving platform that connects selected operational and knowledge sources without disrupting production systems. The first implementation is read-only and pilot-specific, but the design should support future quality intelligence, R&D materials intelligence, knowledge retrieval, predictive models, and governed user applications.

## 2. Architectural principles

1. **Read-only ingestion first.** Source systems remain systems of record.
2. **No direct machine control in the pilot.** Analytics and evidence retrieval are separated from operational control.
3. **Data minimization.** Ingest only fields required for an approved use case.
4. **Preserve provenance.** Every value and document chunk must identify source, timestamp, version, and transformation.
5. **Separate raw, standardized, and analytical layers.** Never overwrite source truth.
6. **Open, exportable formats.** Prefer CSV/Parquet/JSON, SQL, standard object storage, and documented APIs.
7. **Modular components.** Avoid coupling data, retrieval, models, and user interfaces to one vendor.
8. **Identity and access by role.** Sensitive recipes, customers, costs, and employee-related information require separate authorization.
9. **Human approval at decision boundaries.** AI output does not equal technical approval.
10. **Observable and testable systems.** Data quality, retrieval quality, model behavior, access, and failures must be monitored.

## 3. Logical architecture

```text
┌─────────────────────────────────────────────────────────────────┐
│                         USER APPLICATIONS                       │
│ Management dashboard | Quality passport | R&D copilot | Search │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│                   APPLICATION / SERVICE LAYER                   │
│ APIs | workflow services | evidence viewer | approval workflow │
└───────────────┬──────────────────────────────┬──────────────────┘
                │                              │
┌───────────────▼──────────────┐ ┌────────────▼──────────────────┐
│ ANALYTICS & MODEL LAYER      │ │ KNOWLEDGE & RETRIEVAL LAYER  │
│ KPI | Pareto | anomaly | ML  │ │ metadata | graph | vector     │
│ explainability | monitoring  │ │ search | citations | cases    │
└───────────────┬──────────────┘ └────────────┬──────────────────┘
                │                              │
┌───────────────▼──────────────────────────────▼──────────────────┐
│                   CURATED / SEMANTIC DATA                       │
│ Roll passport | product | recipe refs | tests | defects | KPIs │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│              STANDARDIZED / QUALITY-CONTROLLED DATA             │
│ canonical IDs | units | taxonomy mapping | validation | lineage │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│                         RAW LANDING ZONE                         │
│ immutable approved exports | checksums | source metadata         │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│                         SOURCE SYSTEMS                           │
│ INTEX | ELSIS | QC | lab | production | files | complaints     │
└─────────────────────────────────────────────────────────────────┘

Cross-cutting: identity, access control, encryption, audit logs,
retention, backup, data catalog, governance, monitoring, incident response.
```

## 4. Pilot architecture

The pilot should use the smallest maintainable architecture that satisfies security and reproducibility.

### Source layer

- approved INTEX export;
- approved ELSIS database/event/image export or summary export;
- selected QC/lab Excel, CSV, PDF, or database extracts;
- selected production records;
- finance-approved scrap/rework/quality-cost data;
- approved complaint sample if required.

### Secure landing area

Requirements:

- company-approved storage;
- access limited to named pilot members;
- encryption at rest and in transit;
- immutable/raw folders or versioned snapshots;
- file checksum and ingestion timestamp;
- retention and deletion rules;
- no sensitive operational data in GitHub.

### Transformation layer

Responsibilities:

- schema validation;
- column and unit standardization;
- canonical identifiers;
- taxonomy mapping;
- pseudonymization/minimization;
- duplicate handling;
- provenance and transformation version;
- data-quality metrics.

### Curated pilot layer

Minimum entities:

- order;
- production order;
- article/product family;
- roll and parent/child roll;
- line/run;
- material and recipe references;
- inspection run and defect events;
- QC/lab sample and test result;
- rework/scrap/release;
- shipment/complaint where approved;
- KPI and cost aggregates.

### Analytics layer

Pilot capabilities:

- linkage coverage;
- completeness and quality dashboards;
- defect Pareto;
- recurrence analysis;
- quality cost by product/defect/time where valid;
- process/quality relationships with explicit limitations;
- roll quality passport views.

No predictive model is required to prove pilot success.

### Knowledge/retrieval layer

Optional pilot capability:

- approved documents only;
- metadata and chunking;
- source and page/record citations;
- role-aware access;
- evaluation questions and expected sources;
- refusal when evidence is absent.

## 5. Future-state architecture

After value is proven, the platform may add:

- scheduled/API/CDC connectors;
- time-series storage for process signals;
- object storage for inspection images;
- knowledge graph for products, materials, processes, tests, standards, suppliers, outcomes;
- vector retrieval for documents, cases, and images;
- feature store where justified;
- model registry and MLOps;
- workflow integration with ERP/QMS after separate approval;
- digital lab notebook;
- controlled operator/R&D knowledge capture;
- human-approved recommendation services.

## 6. Data zones and permitted content

| Zone | Purpose | Allowed content | Access |
|---|---|---|---|
| Raw | Preserve approved source extract | Original exports/files + metadata | Restricted technical/admin |
| Standardized | Clean and align | Canonical columns, units, IDs, mappings | Pilot engineering/data team |
| Curated | Business-ready entities | Roll passport, tests, defects, KPIs | Role-based business users |
| Analytical | Derived outputs | Aggregates, features, model outputs | Use-case users |
| Knowledge | Approved documents/chunks/graph | TDS/SDS/reports/certificates/cases | Document-level role controls |
| Public/demo | Non-sensitive demonstration | Synthetic/anonymized data only | Approved broader access |

## 7. Data contract template

Every source should define:

```yaml
source_id: DS-EXAMPLE-01
owner: role/name
purpose: approved use case
source_system: system
export_method: method
refresh: one-time|daily|weekly|monthly
schema_version: 1.0
primary_keys: []
foreign_keys: []
critical_fields: []
units: {}
allowed_values: {}
pii_or_employee_data: []
customer_confidential: []
ip_classification: internal|confidential|highly_restricted
retention: rule
quality_slo:
  completeness: target
  uniqueness: target
  linkage: target
lineage: source-to-target description
```

## 8. Model lifecycle requirements

Before any predictive model is operationally used:

- approved problem statement and decision workflow;
- baseline comparison;
- documented train/validation/test split respecting time, product, and leakage risks;
- performance by product family and important subgroups;
- calibration where probabilities are used;
- error analysis and cost of false positives/negatives;
- explainability appropriate to risk;
- human override;
- versioned data, code, features, model, and evaluation;
- drift monitoring;
- rollback and retirement process.

## 9. Retrieval/LLM requirements

- approved source corpus;
- document-level permissions;
- citations to source document/page/record;
- answer includes uncertainty and missing evidence;
- no unsupported technical claim;
- evaluation set covering correct answer, no-answer, conflicting sources, outdated documents, and access-control cases;
- prompt and model versions logged;
- human approval for customer, quality, safety, certification, legal, and process outputs.

## 10. Architecture decisions

Use Architecture Decision Records (ADRs) for material choices.

Template:

```text
ADR-XXX: Title
Status: proposed|accepted|deprecated|superseded
Date:
Context:
Decision:
Options considered:
Consequences:
Security/privacy impact:
Cost/lock-in impact:
Owner:
Review date:
```

Initial ADRs to create after discovery:

- ADR-001: Pilot hosting environment
- ADR-002: Approved storage and data zones
- ADR-003: INTEX ingestion method
- ADR-004: ELSIS export and image/event storage
- ADR-005: Canonical roll identifier strategy
- ADR-006: Dashboard/application framework
- ADR-007: Document retrieval stack
- ADR-008: Identity and access model
- ADR-009: Analytics/model tracking approach

## 11. GitHub boundary

This repository may contain:

- documentation;
- schemas;
- data contracts without sensitive values;
- code;
- tests;
- synthetic data;
- configuration templates with no secrets;
- architecture and governance records.

This repository must not contain:

- real formulations or recipe percentages;
- customer-identifiable records;
- employee emails or performance data;
- raw ERP exports;
- raw ELSIS inspection images unless formally approved and access-controlled outside normal Git use;
- credentials, tokens, keys, or connection strings;
- confidential supplier pricing;
- unredacted complaints;
- sensitive production parameters not approved for repository storage.
