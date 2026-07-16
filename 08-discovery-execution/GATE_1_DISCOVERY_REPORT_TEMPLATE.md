# Gate 1 Discovery Report Template

**Program:** Darmstädter + Klevers AI Transformation  
**Decision:** GO / REVISE / STOP  
**Prepared by:**  
**Date:**  
**Evidence period:**  

---

## 1. Executive decision

### Recommendation

- [ ] GO — approve the 12-week narrow pilot.
- [ ] REVISE — approve only after the stated scope/data changes.
- [ ] STOP/PAUSE — do not fund the proposed pilot under current conditions.

### Decision statement

Write one paragraph stating:

- the selected line/product family or why none was selected;
- the measured business problem;
- the measured data/linkage feasibility;
- the recommended investment decision;
- the most important condition or risk.

### Management decision requested

| Decision | Requested answer |
|---|---|
| Approve scope | Yes / No / Conditions |
| Approve budget ceiling | |
| Approve named owner | |
| Approve team allocation | |
| Approve secure environment | |
| Approve data access | |
| Approve Gate 2 success criteria | |

---

## 2. Business problem and baseline

### Selected problem

Describe the quality/rework/traceability/root-cause problem in operational terms.

### Baseline KPIs

| KPI | Definition | Period | Value | Source | Coverage | Owner | Confidence |
|---|---|---|---:|---|---:|---|---|
| First-pass yield | | | | | | | |
| Scrap quantity/cost | | | | | | | |
| Rework quantity/hours/cost | | | | | | | |
| Defects per roll/1,000 m | | | | | | | |
| Quality hold time | | | | | | | |
| Release time | | | | | | | |
| Complaint rate/cost | | | | | | | |
| Root-cause investigation time | | | | | | | |

### Cost model

| Cost component | Low | Base | High | Confidence | Notes |
|---|---:|---:|---:|---|---|
| Scrap | | | | | |
| Rework | | | | | |
| Holds/lost capacity | | | | | |
| Complaints/replacements | | | | | |
| Investigation/admin effort | | | | | |
| Total addressable quality loss | | | | | |

State explicitly which values are posted actuals, calculated estimates, assumptions, or unavailable.

---

## 3. Candidate-scope comparison

| Criterion | Weight | Candidate A | Candidate B | Candidate C |
|---|---:|---:|---:|---:|
| Quality cost/value | 20% | | | |
| Data availability | 15% | | | |
| Roll linkage | 20% | | | |
| Volume/history | 10% | | | |
| Actionability | 10% | | | |
| Stakeholder support | 10% | | | |
| Operational risk | 10% | | | |
| Strategic learning | 5% | | | |
| Weighted score | 100% | | | |

### Selection rationale

Explain why the selected scope is superior and identify the fallback scope.

---

## 4. Source inventory and ownership

| Source | Owner | Access | Historical depth | Repeatable export | Critical identifiers | Feasibility | Blockers |
|---|---|---|---|---|---|---|---|
| INTEX | | | | | | | |
| ELSIS | | | | | | | |
| QC/lab | | | | | | | |
| Production | | | | | | | |
| Rework/scrap | | | | | | | |
| Shipment | | | | | | | |
| Complaints/CAPA | | | | | | | |
| Finance/cost | | | | | | | |

---

## 5. Cross-system linkage results

| Metric | Candidate A | Candidate B | Selected scope threshold | Assessment |
|---|---:|---:|---:|---|
| Order-to-roll | | | | |
| Roll-to-production | | | | |
| Roll-to-ELSIS | | | | |
| Roll-to-QC | | | | |
| Roll-to-rework/scrap | | | | |
| Roll-to-shipment | | | | |
| Complaint traceability | | | | |
| Complete passport | | | | |
| Exact/composite matches | | | | |
| Manual reconciliation | | | | |

### Canonical identifier decision

Document:

- canonical roll ID strategy;
- source aliases;
- parent/child rules;
- normalization rules;
- unresolved ambiguity;
- future capture changes.

---

## 6. Data-quality findings

| Dimension | Score 1–5 | Evidence | Pilot impact | Remediation |
|---|---:|---|---|---|
| Identifier completeness | | | | |
| Identifier stability | | | | |
| Timestamp quality | | | | |
| Process context | | | | |
| ELSIS events/images | | | | |
| QC/lab consistency | | | | |
| Defect-label quality | | | | |
| Cost-data quality | | | | |
| Repeatable extraction | | | | |
| Security/privacy readiness | | | | |

### Critical gaps

List gaps that could invalidate analysis or future modeling.

---

## 7. Defect taxonomy findings

| Source term | Proposed code | Definition agreed? | Severity rule? | Historical mapping | Owner |
|---|---|---:|---:|---|---|
| | | | | | |

Summarize:

- top defects by frequency;
- top defects by cost/severity;
- ambiguous labels;
- observed vs suspected vs confirmed causes;
- required version-1.0 changes.

---

## 8. Proposed 12-week pilot

### Scope

- Site:
- Line:
- Product family:
- Historical window:
- Primary business question:
- Users:

### In scope

- read-only extraction;
- roll quality passport;
- defect Pareto;
- linkage and data-quality improvement;
- root-cause evidence retrieval;
- dashboard;
- optional explainable analytical baseline.

### Out of scope

- PLC/HMI/machine control;
- ERP writeback;
- automatic release;
- automatic customer communication;
- employee scoring;
- uncontrolled public AI;
- guaranteed predictive model or new computer-vision deployment.

### Deliverables

| Deliverable | Owner | Acceptance test | Due week |
|---|---|---|---:|
| Data contracts | | | |
| Curated roll dataset | | | |
| Roll passport prototype | | | |
| Defect taxonomy v1.0 | | | |
| Defect Pareto/dashboard | | | |
| Root-cause evidence workflow | | | |
| Data-quality report | | | |
| Optional analytical model | | | |
| Final value report | | | |

---

## 9. Architecture, security, privacy, and IP

Document:

- approved hosting/storage;
- data zones;
- read-only ingestion;
- role-based access;
- customer and employee minimization;
- encryption/backup/retention/deletion;
- logging/audit;
- approved AI services;
- prohibited data flows;
- source citation and human-approval requirements;
- vendor/IP conditions;
- access-removal process.

### Architecture decisions

| ADR | Decision | Owner | Status |
|---|---|---|---|
| Hosting | | | |
| Identity/access | | | |
| Source ingestion | | | |
| Structured storage | | | |
| Images/documents | | | |
| Analytics/dashboard | | | |
| Retrieval/LLM | | | |

---

## 10. Resources, cost, and value

### Cost estimate

| Category | Internal effort | External cost | Notes |
|---|---:|---:|---|
| Program lead | | | |
| Source owners | | | |
| IT/security | | | |
| Data engineering | | | |
| Analytics/dashboard | | | |
| ELSIS/vendor support | | | |
| Infrastructure/licenses | | | |
| Contingency | | | |
| Total | | | |

### Benefit scenarios

| Scenario | Annual addressable value | Pilot-captured share | Expected annual benefit | Confidence |
|---|---:|---:|---:|---|
| Low | | | | |
| Base | | | | |
| High | | | | |

### Economic tests

- estimated payback period;
- first-year net benefit;
- cost-to-learn justification;
- conditions required for benefit realization.

Do not present hypothetical opportunity as realized savings.

---

## 11. Risk register

| Risk | Probability | Impact | Mitigation | Owner | Residual risk |
|---|---|---|---|---|---|
| Poor linkage | | | | | |
| Weak ELSIS export | | | | | |
| Missing process history | | | | | |
| Inconsistent labels | | | | | |
| Cost uncertainty | | | | | |
| IP leakage | | | | | |
| Privacy/employee trust | | | | | |
| Scope expansion | | | | | |
| Vendor dependency | | | | | |
| Low adoption | | | | | |

---

## 12. Gate 1 recommendation conditions

### GO conditions

- [ ] Selected scope has measurable value.
- [ ] Required ownership and access exist.
- [ ] Core linkage is sufficient or remediable.
- [ ] Pilot remains read-only and low risk.
- [ ] Security/privacy/IP approach is approved.
- [ ] Cost/value logic is validated.
- [ ] Cross-functional owners accept deliverables and metrics.

### Revise conditions

List exact scope, access, identifier, data-capture, or budget changes required.

### Stop conditions

List the evidence that makes the current scope economically, technically, legally, or organizationally unsuitable.

---

## 13. Decision record

| Role | Name | Decision | Conditions/comments | Date |
|---|---|---|---|---|
| Executive sponsor | | | | |
| Production | | | | |
| Quality | | | | |
| R&D | | | | |
| Packaging/Inspection | | | | |
| IT/Security | | | | |
| Finance | | | | |
| AI Transformation Lead | | | | |
