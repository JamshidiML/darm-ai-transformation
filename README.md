# Darmstädter + Klevers AI Transformation Program

This private repository is the strategy, governance, execution, architecture, evidence, and prototype hub for the Darmstädter + Klevers AI Transformation Program.

The objective is not to deploy isolated AI tools. The objective is to convert technical-textile know-how, materials knowledge, process evidence, quality data, laboratory results, certifications, inspection information, supplier knowledge, and expert experience into a secure and measurable industrial intelligence capability.

> **Current program status:** Gate 0 management package complete; Gate 1 discovery execution kit and synthetic Roll Quality Passport prototype ready. The next external dependency is formal management authorization and controlled read-only access.

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

### Management and Gate 0

- [German management one-pager](deliverables/de/MANAGEMENT_ONE_PAGER_DE.md)
- [German management meeting agenda and speaking script](07-gate-0-management/MEETING_AGENDA_AND_SPEAKING_SCRIPT_DE.md)
- [Discovery approval record](07-gate-0-management/DISCOVERY_APPROVAL_RECORD.md)
- [Stakeholder nomination and access request](07-gate-0-management/STAKEHOLDER_NOMINATION_AND_ACCESS_REQUEST.md)
- [English management one-pager](deliverables/en/MANAGEMENT_ONE_PAGER_EN.md)
- [Corporate AI transformation strategy](01-strategy/AI_TRANSFORMATION_STRATEGY_CORPORATE.md)

### Discovery team

- [Discovery kickoff and daily plan](08-discovery-execution/DISCOVERY_KICKOFF_AND_DAILY_PLAN.md)
- [Source audit workbook](08-discovery-execution/SOURCE_AUDIT_WORKBOOK.md)
- [Stakeholder interview guides](08-discovery-execution/STAKEHOLDER_INTERVIEW_GUIDES.md)
- [Cross-system linkage test specification](08-discovery-execution/CROSS_SYSTEM_LINKAGE_TEST_SPEC.md)
- [Gate 1 discovery report template](08-discovery-execution/GATE_1_DISCOVERY_REPORT_TEMPLATE.md)
- [Data discovery playbook](02-data-discovery/DATA_DISCOVERY_PLAYBOOK.md)

### Program governance

- [Program charter](00-program-governance/AI_TRANSFORMATION_CHARTER.md)
- [RACI and stakeholder model](00-program-governance/RACI_AND_STAKEHOLDERS.md)
- [Risk register and decision log](00-program-governance/RISK_REGISTER_AND_DECISION_LOG.md)
- [Pilot charter and work plan](03-quality-intelligence-pilot/PILOT_CHARTER_AND_WORKPLAN.md)

### Technical and data team

- [Roll Quality Passport business schema](03-quality-intelligence-pilot/ROLL_QUALITY_PASSPORT_SCHEMA.md)
- [Technical-textile defect taxonomy v0.1](03-quality-intelligence-pilot/DEFECT_TAXONOMY_V0.1.md)
- [Target architecture](04-architecture/TARGET_ARCHITECTURE.md)
- [AI governance, security, privacy, and IP controls](04-architecture/AI_GOVERNANCE_SECURITY_AND_IP.md)
- [Synthetic prototype workspace](06-prototype/README.md)
- [Machine-readable Roll Quality Passport schema](06-prototype/schemas/roll_quality_passport.schema.json)
- [Synthetic passport examples](06-prototype/synthetic_data/roll_quality_passports.jsonl)
- [Passport validator](06-prototype/src/validate_passports.py)

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
│   ├── README.md
│   ├── schemas/
│   ├── synthetic_data/
│   ├── src/
│   └── tests/
│
├── 07-gate-0-management/
│   ├── MEETING_AGENDA_AND_SPEAKING_SCRIPT_DE.md
│   ├── DISCOVERY_APPROVAL_RECORD.md
│   └── STAKEHOLDER_NOMINATION_AND_ACCESS_REQUEST.md
│
├── 08-discovery-execution/
│   ├── DISCOVERY_KICKOFF_AND_DAILY_PLAN.md
│   ├── SOURCE_AUDIT_WORKBOOK.md
│   ├── STAKEHOLDER_INTERVIEW_GUIDES.md
│   ├── CROSS_SYSTEM_LINKAGE_TEST_SPEC.md
│   └── GATE_1_DISCOVERY_REPORT_TEMPLATE.md
│
├── deliverables/
│   ├── de/
│   └── en/
│
├── personal-private/
│   └── MOHSEN_AI_LEADERSHIP_STRATEGY.md
│
├── docs/
├── outputs/
└── .github/workflows/
    └── prototype-validation.yml
```

---

## Phase-gate roadmap

### Gate 0 — Management alignment

Decision requested:

- executive sponsor;
- AI Transformation Lead;
- cross-functional team;
- controlled read-only data access;
- approval for a two-week discovery sprint.

**Repository readiness:** complete. The meeting script, approval form, nomination table, and minimum-access request are prepared.

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

**Repository readiness:** complete. Daily plan, audit workbook, interview guides, linkage specification, and final report template are prepared.

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
- recommendation on predictive quality and computer-vision expansion.

### Gate 3 — Scale decision

Potential next workstreams:

- predictive quality;
- R&D knowledge graph and digital lab memory;
- source-cited technical knowledge assistant;
- supplier/material substitution intelligence;
- expanded computer vision;
- production, maintenance, energy, and planning intelligence.

---

## Synthetic technical prototype

The repository includes a working synthetic-only passport prototype with:

- JSON Schema contract;
- four representative synthetic records;
- validation CLI using only the Python standard library;
- unit tests;
- GitHub Actions validation.

Run locally:

```bash
python 06-prototype/src/validate_passports.py \
  06-prototype/synthetic_data/roll_quality_passports.jsonl

python -m unittest discover \
  -s 06-prototype/tests \
  -p 'test_*.py' \
  -v
```

The prototype rejects non-synthetic records by design. It must not be used as a path for uploading real company data to GitHub.

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

### Allowed

- strategy and governance documents;
- architecture records;
- schemas and data contracts without sensitive values;
- code and tests;
- synthetic or explicitly approved anonymized examples;
- presentation artifacts;
- non-secret configuration templates.

### Do not commit

- real ERP or INTEX exports;
- real ELSIS inspection images/events;
- customer-identifiable records;
- employee emails or performance data;
- formulations, recipe percentages, or confidential process windows;
- supplier pricing;
- credentials, tokens, keys, passwords, certificates, or connection strings;
- unredacted complaints, QC reports, or sensitive laboratory records;
- databases or models created from company data.

Sensitive operational data must remain in approved company infrastructure with role-based access, retention rules, and auditability.

---

## Original strategy artifacts

The original comprehensive strategy package remains under `outputs/`, including the strategy report, board presentations, Persian working versions, PDFs, rendered previews, structural inspection outputs, and source assets.

For management use, prefer the corporate strategy, German/English one-pagers, and Gate 0 documents because personal career content is separated.

---

## Immediate operational backlog

1. Hold the Gate 0 management meeting.
2. Record approval, conditions, sponsor, and owners.
3. Confirm the approved discovery workspace and transfer routes.
4. Run the INTEX audit.
5. Run the ELSIS audit.
6. Inventory QC/lab and production data.
7. Establish the Finance-approved baseline.
8. Execute the cross-system linkage test.
9. Validate the defect taxonomy and select the pilot scope.
10. Produce the Gate 1 go/revise/stop decision package.

GitHub issues #1–#10 track these workstreams.
