# KPI Baseline and ROI Model

## 1. Purpose

The program must be evaluated with operational and financial evidence, not AI activity metrics. This document defines the initial KPI framework, calculation rules, and low/base/high ROI scenarios for discovery and pilot decisions.

All values must be validated by Quality, Production, and Finance/Controlling. Unknown values remain unknown; they must not be invented for presentation purposes.

## 2. Measurement principles

1. Use a fixed baseline period, normally the most recent representative 12 months.
2. Separate product families, lines, and special events when they materially change the baseline.
3. Define numerator, denominator, unit, source, owner, and exclusions for every KPI.
4. Reconcile operational quantity with financial cost.
5. Avoid double counting—for example, scrap material and lost sales capacity may overlap.
6. Report data coverage and uncertainty next to every estimate.
7. Use low, base, and high scenarios rather than one precise but unsupported forecast.
8. Track realized benefits separately from identified opportunities.

## 3. Core baseline KPIs

### Quality

| KPI | Definition | Unit | Source | Owner | Baseline | Coverage |
|---|---|---|---|---|---:|---:|
| First-pass yield | Quantity released without rework / total produced quantity | % | ERP/QC | Quality | TBD | TBD |
| Rework rate | Reworked quantity / produced quantity | % | ERP/production | Quality/Production | TBD | TBD |
| Scrap rate | Scrapped quantity / produced quantity | % | ERP/production | Quality/Production | TBD | TBD |
| Scrap cost | Material + processing + disposal cost attributable to scrap | EUR/year | Finance/ERP | Finance | TBD | TBD |
| Defects per 1,000 m | Count of defined defects / inspected meters × 1,000 | count | ELSIS/QC | Quality/Packaging | TBD | TBD |
| Major defects per 1,000 m | Severity 3–4 defect count / inspected meters × 1,000 | count | ELSIS/QC | Quality | TBD | TBD |
| Repeat-defect recurrence | Recurring confirmed/supported defect cases / total relevant cases | % | NCR/CAPA/complaints | Quality | TBD | TBD |
| Quality hold rate | Held quantity / produced quantity | % | QC/ERP | Quality | TBD | TBD |
| Release lead time | Release timestamp – production completion timestamp | hours/days | ERP/QC | Quality | TBD | TBD |
| Retest rate | Retested samples / total tested samples | % | Lab/QC | Quality/Lab | TBD | TBD |

### Complaints and customer response

| KPI | Definition | Unit | Baseline |
|---|---|---|---:|
| Complaint rate | Complaints / shipments or relevant quantity | count/rate | TBD |
| Complaint investigation time | Time from complaint receipt to documented root-cause hypothesis | hours/days | TBD |
| Complaint closure time | Time from receipt to approved closure | days | TBD |
| Repeat complaint rate | Complaints matching prior category/cause within defined period | % | TBD |
| Complaint cost | Investigation + test + replacement + credit + freight + external cost | EUR/year | TBD |

### Data and traceability

| KPI | Definition | Target / baseline |
|---|---|---|
| Order-to-roll linkage | Rolls linked unambiguously to production/order record | Baseline TBD; pilot target agreed after discovery |
| Roll-to-inspection linkage | Rolls linked to inspection events/images/summary | Baseline TBD |
| Roll-to-QC linkage | Rolls linked to required QC/lab evidence | Baseline TBD |
| Critical field completeness | Complete required fields / expected fields | Baseline TBD |
| Identifier ambiguity | Records with multiple plausible matches / records linked | Baseline TBD |
| Evidence retrieval time | Time to assemble a defined quality case | Baseline TBD |

### R&D and knowledge

| KPI | Definition | Baseline |
|---|---|---:|
| Similar-project retrieval time | Time to find relevant prior trials and evidence | TBD |
| Experiment documentation completeness | Experiments with required structured fields / total | TBD |
| Repeated experiment rate | Experiments repeating prior work without documented reason | TBD |
| Technical document retrieval time | Time to find approved TDS/SDS/certificate/test evidence | TBD |
| Knowledge answer evidence coverage | Valid answers with correct source reference / evaluated questions | TBD |

## 4. Quality-cost model

### 4.1 Cost of scrap

```text
Scrap cost =
  raw material consumed
+ coating/chemical/lamination material
+ direct labor
+ machine time
+ energy/utilities
+ waste handling/disposal
+ external processing
- recoverable salvage value
```

Document which components are already included in ERP costing to prevent double counting.

### 4.2 Cost of rework

```text
Rework cost =
  rework labor hours × loaded labor rate
+ additional machine hours × approved machine-hour rate
+ additional material
+ energy/utilities
+ additional inspection and testing
+ handling/internal logistics
+ external processing
+ incremental scrap caused by rework
```

### 4.3 Cost of quality holds and delay

```text
Hold/delay cost =
  additional handling and storage
+ expedited production/logistics
+ rescheduling/changeover impact
+ contractual penalty or premium freight
+ contribution margin at risk, if Finance approves method
```

Do not automatically count total order value as a loss.

### 4.4 Complaint cost

```text
Complaint cost =
  internal investigation hours
+ laboratory/external test cost
+ replacement production
+ credits/claims
+ freight/returns
+ customer visits
+ disposal
+ approved estimate of lost margin or account risk
```

Separate direct cost from strategic/customer-risk estimates.

### 4.5 Cost of repeated problem solving

```text
Knowledge-loss cost =
  repeated investigation hours
+ repeated experiment/test cost
+ delayed development time
+ avoidable sample/production trials
```

This is often real but difficult to measure. Use time studies and representative cases rather than unsupported annual extrapolation.

## 5. Pilot benefit categories

| Benefit | Mechanism | Measurement method |
|---|---|---|
| Reduced scrap | Identify and remove repeatable defect drivers | Pre/post or controlled comparison with normalized product mix |
| Reduced rework | Earlier detection and better cause evidence | Rework quantity/hours and cost trend |
| Faster root-cause analysis | Linked roll evidence and similar-case retrieval | Timed case exercises and live case tracking |
| Faster quality release | Complete evidence and fewer searches | Production-complete to release time |
| Fewer repeat defects | Action ownership and recurrence monitoring | Repeat-defect rate over agreed window |
| Better complaint response | Faster evidence assembly | Investigation/closure time and case effort |
| Avoided new data/AI investment | Discovery identifies infeasible approaches early | Approved avoided-cost record |
| R&D time savings | Historical experiment and document retrieval | Timed tasks and project cycle metrics |

## 6. ROI scenario model

### Inputs

| Input | Symbol | Low | Base | High | Source/owner |
|---|---|---:|---:|---:|---|
| Annual addressable scrap cost | S | TBD | TBD | TBD | Finance |
| Expected scrap reduction | rs | TBD | TBD | TBD | Quality/Production |
| Annual addressable rework cost | R | TBD | TBD | TBD | Finance |
| Expected rework reduction | rr | TBD | TBD | TBD | Quality/Production |
| Annual complaint cost | C | TBD | TBD | TBD | Finance/Quality |
| Expected complaint-cost reduction | rc | TBD | TBD | TBD | Quality |
| Annual investigation/retrieval labor cost | K | TBD | TBD | TBD | Departments/Finance |
| Expected time reduction | rk | TBD | TBD | TBD | Pilot evidence |
| Annual platform operating cost | O | TBD | TBD | TBD | IT/Finance |
| One-time implementation cost | I | TBD | TBD | TBD | Project estimate |

### Annual gross benefit

```text
Annual gross benefit = (S × rs) + (R × rr) + (C × rc) + (K × rk)
```

### Annual net benefit

```text
Annual net benefit = Annual gross benefit – O
```

### First-year ROI

```text
First-year ROI = (Annual gross benefit – O – I) / I
```

### Payback period

```text
Payback months = I / (Annual net benefit / 12)
```

### Three-year value

```text
3-year net value =
  Year 1 gross benefit
+ Year 2 gross benefit
+ Year 3 gross benefit
- implementation cost
- three years of operating cost
- approved change-management and support cost
```

Finance may apply discounting/NPV rules.

## 7. Benefit confidence levels

| Confidence | Definition |
|---|---|
| C0 — Idea | No internal evidence; do not include in approved ROI |
| C1 — Estimated | Internal baseline exists; improvement assumption based on expert judgment |
| C2 — Supported | Pilot evidence or comparable internal cases support the assumption |
| C3 — Validated | Controlled/pre-post measurement demonstrates the benefit |
| C4 — Realized | Finance confirms the saving or cost avoidance |

Every benefit in a management report must show its confidence level.

## 8. Pilot cost model

Track:

- internal hours by function;
- external consulting/development;
- software/cloud/licenses;
- infrastructure/security;
- system/vendor support;
- data preparation;
- training/change management;
- travel/workshops;
- contingency;
- ongoing support and maintenance.

Do not treat internal employee time as free. Show it separately even when no cash leaves the company.

## 9. Discovery decision thresholds

Management should not approve the full pilot unless:

- at least one meaningful quality-cost baseline can be established;
- the selected product/line has measurable addressable value;
- critical data can be linked or a practical capture plan exists;
- pilot cost and internal effort are bounded;
- the base scenario is credible and downside risk is understood;
- success can be measured within or soon after the pilot.

## 10. Pilot value register

| Value ID | Finding/opportunity | Baseline | Proposed action | Expected annual value | Confidence | Owner | Verification date | Realized value |
|---|---|---:|---|---:|---|---|---|---:|
| V-001 | TBD | TBD | TBD | TBD | C0 | TBD | TBD | TBD |

## 11. Management dashboard minimum

Show:

- data linkage and completeness;
- scrap, rework, defect, hold, release, and complaint baseline;
- top defect drivers;
- top improvement opportunities;
- pilot cost versus budget;
- expected value by confidence level;
- risks and blockers;
- actions with owners;
- gate recommendation.

Do not use number of documents, prompts, models, or dashboards as primary value KPIs.