# Roll Quality Intelligence Pilot Charter and Work Plan

**Pilot name:** Roll Quality Intelligence  
**Duration:** 12 weeks after discovery approval  
**Operating mode:** Read-only  
**Scope:** One line, one product family, one historical window  

## 1. Business problem

Quality evidence is distributed across orders, roll records, process settings, inspection data, QC/laboratory results, rework/scrap records, operator notes, shipment records, and complaints. This fragmentation slows root-cause analysis, hides repeated defects, weakens traceability, and limits organizational learning.

The pilot will determine whether these sources can be connected into a useful roll-level quality view and whether the resulting analysis reveals measurable improvement opportunities.

## 2. Pilot objectives

1. Create a canonical roll-level data model.
2. Measure linkage quality across selected sources.
3. Build a prototype roll quality passport.
4. Standardize the initial defect taxonomy.
5. Identify the largest recurring defect and quality-cost drivers.
6. Retrieve comparable historical cases and supporting evidence faster.
7. Quantify improvement opportunities and data-capture gaps.
8. Decide whether predictive quality and expanded computer vision are justified.

## 3. Scope boundaries

### Included

- one selected coating/finishing line;
- one selected product family;
- 6–12 months of historical data where available;
- order, article, roll, material/batch, recipe version, process, inspection, QC/lab, rework, scrap, release, shipment, and complaint evidence;
- approved read-only exports;
- dashboards and analytical prototypes;
- source-linked knowledge retrieval for approved pilot documents.

### Excluded

- machine control;
- automatic process recommendations to operators;
- ERP writeback;
- automatic quality release;
- automatic customer communication;
- employee productivity scoring;
- full-company rollout;
- production deployment of a new CV model unless separately approved after feasibility review.

## 4. Deliverables

| ID | Deliverable | Acceptance condition |
|---|---|---|
| D1 | Pilot data inventory and data contracts | Owners, fields, refresh, access, purpose, and quality documented |
| D2 | Canonical roll data model | Key entities and identifiers approved by IT, Quality, Production |
| D3 | Linkage and data-quality report | Match rates, gaps, ambiguity, and remediation plan quantified |
| D4 | Defect taxonomy v1 | Definitions, examples, severity, disposition, and ownership agreed |
| D5 | Roll quality passport prototype | Selected roll can be traced across available evidence |
| D6 | Defect Pareto and recurrence analysis | Top defect drivers visible by product/process/time where data allows |
| D7 | Root-cause evidence prototype | Similar cases and source records retrievable with provenance |
| D8 | Baseline and opportunity model | Finance-approved assumptions and low/base/high scenarios |
| D9 | Management dashboard | KPIs, findings, limitations, actions, and risks visible |
| D10 | Scale recommendation | Go/revise/stop decision for predictive quality/CV/platform expansion |

## 5. Success metrics

### Data and traceability

- order-to-roll linkage rate;
- roll-to-inspection linkage rate;
- roll-to-QC/lab linkage rate;
- percentage of records with valid timestamps;
- percentage of critical fields complete;
- number of manual reconciliation rules required.

### Quality and operations

- top five defect drivers identified;
- recurring defect patterns identified;
- time required to assemble evidence for a selected quality case;
- baseline scrap/rework/quality-hold/complaint metrics established;
- value of actionable improvement opportunities quantified.

### Adoption and governance

- named owners for all critical data sources;
- pilot team acceptance of definitions and outputs;
- IT/security approval of the next architecture;
- no unapproved data movement or operational writeback;
- documented human validation of technical findings.

## 6. Work packages

### WP0 — Mobilization (Week 1)

- confirm scope and owners;
- approve access and secure workspace;
- freeze selected line/product family/time window;
- confirm KPI definitions;
- create action, decision, and risk logs.

### WP1 — Data acquisition and profiling (Weeks 1–3)

- receive approved exports;
- document schemas and data contracts;
- profile completeness, duplicates, units, timestamps, and identifiers;
- identify sensitive fields and apply minimization/pseudonymization.

### WP2 — Identity and linkage foundation (Weeks 2–5)

- define canonical order/roll/product/batch keys;
- map source-specific identifiers;
- calculate match and ambiguity rates;
- create reconciliation rules;
- define future-state capture improvements.

### WP3 — Defect and quality model (Weeks 3–6)

- standardize defect names;
- define severity, status, disposition, and source confidence;
- connect defects to product, roll, position, time, process, QC, and action where possible;
- create defect Pareto and recurrence views.

### WP4 — Roll passport prototype (Weeks 4–8)

- build roll-level timeline and evidence view;
- connect order, product, material, process, inspection, QC, release, rework, shipment, and complaint evidence;
- add provenance and missing-data indicators.

### WP5 — Root-cause and opportunity analysis (Weeks 6–10)

- identify repeated patterns and comparable cases;
- test parameter/quality relationships where data supports valid analysis;
- document correlation versus causation limitations;
- create prioritized improvement hypotheses with human review.

### WP6 — Business case and scale recommendation (Weeks 9–12)

- validate quality-cost baseline;
- estimate low/base/high value scenarios;
- define action owners and verification methods;
- assess readiness for predictive quality and expanded CV;
- prepare final management gate review.

## 7. Weekly plan

| Week | Main outcome |
|---:|---|
| 1 | Mobilized team, frozen scope, approved data room |
| 2 | Initial exports, source documentation, profiling started |
| 3 | Data-quality report v0.1 and identifier map |
| 4 | First linkage results and taxonomy workshop |
| 5 | Canonical model and future capture gaps |
| 6 | Defect Pareto v0.1 and first roll-passport view |
| 7 | Passport coverage expanded and validated with users |
| 8 | Root-cause evidence prototype |
| 9 | Recurrence and parameter relationship analysis |
| 10 | Improvement hypotheses and financial validation |
| 11 | Final dashboard, risk review, scale options |
| 12 | Management demonstration and gate decision |

## 8. Validation rules

- Every analytical finding must identify its source data and coverage.
- Correlation must not be presented as proven causation.
- Technical conclusions require review by R&D/Quality/Production.
- Financial conclusions require Finance validation.
- Missing or unreliable data must be visible, not hidden.
- Models, if used, require a documented baseline, holdout evaluation, error analysis, and limitations.

## 9. Exit options

### Go

Data and business value support scale-up.

### Revise

Value is plausible but identifiers, data capture, scope, or architecture must be improved first.

### Stop

The selected use case does not justify investment, data cannot support it, or risks outweigh value. Stopping is an acceptable program outcome when supported by evidence.

## 10. Final management decision

The pilot ends with one of the following recommendations:

1. expand quality intelligence to additional products/lines;
2. improve data capture first, then rerun;
3. proceed to predictive quality baseline;
4. proceed to CV enhancement;
5. prioritize the R&D knowledge platform instead;
6. pause or stop the workstream.
