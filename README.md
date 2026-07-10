# Darmstädter + Klevers AI Transformation Program

This private repository is the strategy, governance, execution, architecture, and evidence hub for the Darmstädter + Klevers AI Transformation Program.

The objective is not to deploy isolated AI tools. The objective is to convert technical-textile know-how, materials knowledge, process evidence, quality data, laboratory results, certifications, inspection information, supplier knowledge, and expert experience into a secure and measurable industrial intelligence capability.

> **Current program status:** Foundation and discovery preparation. The next formal step is management approval for a two-week, read-only data discovery sprint.

## Strategic recommendation

Start small and prove value:

1. approve a two-week discovery sprint;
2. inspect INTEX, ELSIS, QC, laboratory, production, quality-cost, and complaint data;
3. measure identifier linkage and data quality;
4. select one line and one product family;
5. establish a Finance-approved baseline;
6. prepare the final 12-week Roll Quality Intelligence pilot case;
7. scale only after measurable value, security, feasibility, and ownership are demonstrated.

The initial program does **not** include machine control, ERP writeback, autonomous release, autonomous customer communication, or hidden employee monitoring.

---

## Start here

### Management

- [German management one-pager](deliverables/de/MANAGEMENT_ONE_PAGER_DE.md)
- [English management one-pager](deliverables/en/MANAGEMENT_ONE_PAGER_EN.md)
- [Corporate AI transformation strategy](01-strategy/AI_TRANSFORMATION_STRATEGY_CORPORATE.md)
- [Program charter](00-program-governance/AI_TRANSFORMATION_CHARTER.md)

### Program team

- [RACI and stakeholder model](00-program-governance/RACI_AND_STAKEHOLDERS.md)
- [Risk register and decision log](00-program-governance/RISK_REGISTER_AND_DECISION_LOG.md)
- [Data discovery playbook](02-data-discovery/DATA_DISCOVERY_PLAYBOOK.md)
- [Pilot charter and work plan](03-quality-intelligence-pilot/PILOT_CHARTER_AND_WORKPLAN.md)

### Technical and data team

- [Roll Quality Passport schema](03-quality-intelligence-pilot/ROLL_QUALITY_PASSPORT_SCHEMA.md)
- [Technical-textile defect taxonomy v0.1](03-quality-intelligence-pilot/DEFECT_TAXONOMY_V0.1.md)
- [Target architecture](04-architecture/TARGET_ARCHITECTURE.md)
- [AI governance, security, privacy, and IP controls](04-architecture/AI_GOVERNANCE_SECURITY_AND_IP.md)
- [Prototype workspace](06-prototype/README.md)

### Business case and funding

- [KPI baseline and ROI model](05-business-case/KPI_BASELINE_AND_ROI_MODEL.md)
- [Funding and partner strategy](05-business-case/FUNDING_AND_PARTNER_STRATEGY.md)

### Personal working material

- [Mohsen AI leadership strategy](personal-private/MOHSEN_AI_LEADERSHIP_STRATEGY.md)

The personal leadership document is intentionally separated from the corporate management package.

---

## Program architecture

```text
.
├── 00-program-governance/
│   ├── AI_TRANSFORMATION_CHARTER.md
│   ├── RACI_AND_STAKEHOLDERS.md
│   └── RISK_REGISTER_AND_DECISION_LOG.md
│
├── 01-strategy/
│   └── AI_TRANSFORMATION_STRATEGY_CORPORATE.md
│
├── 02-data-discovery/
│   └── DATA_DISCOVERY_PLAYBOOK.md
│
├── 03-quality-intelligence-pilot/
│   ├── PILOT_CHARTER_AND_WORKPLAN.md
│   ├── ROLL_QUALITY_PASSPORT_SCHEMA.md
│   └── DEFECT_TAXONOMY_V0.1.md
│
├── 04-architecture/
│   ├── TARGET_ARCHITECTURE.md
│   └── AI_GOVERNANCE_SECURITY_AND_IP.md
│
├── 05-business-case/
│   ├── KPI_BASELINE_AND_ROI_MODEL.md
│   └── FUNDING_AND_PARTNER_STRATEGY.md
│
├── 06-prototype/
│   └── README.md
│
├── deliverables/
│   ├── de/
│   └── en/
│
├── personal-private/
│   └── MOHSEN_AI_LEADERSHIP_STRATEGY.md
│
├── docs/
│   ├── ARTIFACT_INDEX_FA.md
│   └── PROJECT_PROCESS_FA.md
│
└── outputs/
    ├── AI_TRANSFORMATION_STRATEGY_REPORT.md
    ├── board presentations
    ├── PDF and preview artifacts
    └── presentation QA outputs
```

---

## Phase-gate roadmap

### Gate 0 — Management alignment

Decision requested:

- executive sponsor;
- AI transformation lead;
- cross-functional team;
- controlled read-only data access;
- approval for a two-week discovery sprint.

### Gate 1 — Discovery

Duration: 10 working days.

Outputs:

- source and owner inventory;
- INTEX and ELSIS export assessment;
- QC/lab/production/complaint data map;
- identifier linkage results;
- data-quality scores;
- quality-cost baseline;
- selected line and product family;
- pilot architecture, budget, risks, and value case;
- go/revise/stop recommendation.

### Gate 2 — Roll Quality Intelligence pilot

Duration: 12 weeks after approval.

Scope:

- one line;
- one product family;
- one historical window;
- read-only analytics and evidence retrieval.

Deliverables:

- roll-level quality passport;
- controlled defect taxonomy;
- linkage and data-quality report;
- defect Pareto and recurrence analysis;
- evidence-linked root-cause support;
- management dashboard;
- quantified improvement opportunities;
- recommendation on predictive quality and CV expansion.

### Gate 3 — Scale decision

Potential next workstreams:

- predictive quality;
- R&D knowledge graph and digital lab memory;
- source-cited technical knowledge assistant;
- supplier/material substitution intelligence;
- expanded computer vision;
- production, maintenance, energy, and planning intelligence.

---

## Core operating principles

1. **Business value before technology.**
2. **Read-only first.** Observe and explain before recommending; recommend before controlling.
3. **Human accountability.** AI does not approve products, certificates, customer claims, releases, or process changes.
4. **Source-linked technical outputs.** Evidence and uncertainty must remain visible.
5. **Security, privacy, and IP by design.**
6. **No shadow AI.** Use approved tools, architecture, and access routes.
7. **Operators and experts are co-designers, not monitoring targets.**
8. **Stage-gated investment.** No platform-scale commitment before value is demonstrated.
9. **Open, exportable, maintainable architecture.**
10. **Document decisions, risks, models, data quality, and realized value.**

---

## Data and confidentiality policy

This repository is private and should remain access-restricted.

### Allowed in this repository

- strategy and governance documents;
- architecture records;
- schemas and data contracts without sensitive values;
- code and tests;
- synthetic or explicitly approved anonymized examples;
- presentation artifacts;
- non-secret configuration templates.

### Do not commit

- real ERP exports;
- real ELSIS inspection images/events unless separately approved and stored appropriately;
- customer-identifiable records;
- employee emails or performance data;
- formulations, recipe percentages, or confidential process windows;
- supplier pricing;
- credentials, tokens, keys, passwords, certificates, or connection strings;
- unredacted complaints, QC reports, or sensitive laboratory records.

Sensitive operational data must remain in approved company infrastructure with role-based access, retention rules, and auditability.

---

## Original strategy artifacts

The original comprehensive strategy package remains available under `outputs/` and includes:

- `outputs/AI_TRANSFORMATION_STRATEGY_REPORT.md`
- English board presentation with speaker notes
- Persian editable presentation
- Persian PDF
- rendered previews and montages
- structural inspection outputs
- source assets

The original report is an internal working source. For management use, prefer the corporate strategy and German/English one-pagers in the execution structure above because the personal career strategy has been separated.

---

## Immediate operational backlog

1. Secure management approval for Gate 0.
2. Nominate sponsor and workstream owners.
3. Run the INTEX export and identifier audit.
4. Run the ELSIS data/image/export audit.
5. Inventory QC and laboratory data.
6. Inventory production parameters and historical availability.
7. Establish the Finance-approved quality-cost baseline.
8. Test linkage across representative rolls.
9. Score and select the pilot line/product family.
10. Prepare the Gate 1 management decision package.

GitHub issues are used to track these workstreams.
