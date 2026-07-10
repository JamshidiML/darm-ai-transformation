# Data Discovery Playbook

**Purpose:** determine whether a narrow Roll Quality Intelligence pilot is feasible, valuable, secure, and maintainable before committing to the full 12-week implementation.

**Duration:** 10 working days.

## 1. Discovery questions

By the end of discovery, the team must answer:

1. Which systems and files contain order, roll, material, process, inspection, QC, laboratory, rework, scrap, shipment, and complaint information?
2. Who owns each source and who may authorize access?
3. Which identifiers exist, and can records be linked without manual guesswork?
4. What historical period is available?
5. How complete, consistent, accurate, timely, and interpretable is the data?
6. Which product family and line provide the strongest value/data combination?
7. What current quality costs and operational delays can be measured?
8. Which security, privacy, works-council, contractual, and IP controls are required?
9. What is the smallest credible pilot architecture?
10. What should management approve, revise, or reject?

---

## 2. Ten-day work plan

| Day | Main activity | Output |
|---:|---|---|
| 1 | Kickoff, scope freeze, stakeholder confirmation | Approved discovery charter and contact list |
| 2 | INTEX / ERP interview and export inspection | ERP source map and sample export |
| 3 | ELSIS / inspection-system technical audit | Inspection source map and export feasibility |
| 4 | QC and laboratory file audit | Test-result inventory and linkage assessment |
| 5 | Production/process data audit | Parameter-history and timestamp assessment |
| 6 | Complaint, rework, scrap, and release-data audit | Quality-loss source map |
| 7 | Identifier linkage test across sample records | Linkage matrix and unmatched-record analysis |
| 8 | KPI baseline workshop with Quality and Finance | Agreed definitions and initial ranges |
| 9 | Product-family/line selection and architecture workshop | Pilot candidate scorecard and target architecture |
| 10 | Management synthesis | Go/revise/stop recommendation, budget, risks, next plan |

---

## 3. Data-source inventory template

| Source ID | System / folder | Business process | Data owner | Technical owner | Format | Historical range | Update frequency | Key identifiers | Sensitive fields | Export method | Quality score | Pilot relevance | Status |
|---|---|---|---|---|---|---|---|---|---|---|---:|---|---|
| DS-ERP-01 | INTEX | Orders / products / production | TBD | TBD | CSV/DB/API? | TBD | TBD | Order, article, roll? | Customer, price | TBD | TBD | Critical | Open |
| DS-INS-01 | ELSIS | Inspection / defects | TBD | TBD | DB/images/export? | TBD | TBD | Roll, timestamp? | Operator | TBD | TBD | Critical | Open |
| DS-QC-01 | QC files | Quality tests / release | TBD | TBD | Excel/PDF | TBD | TBD | Roll, order, batch? | None/limited | File export | TBD | Critical | Open |
| DS-LAB-01 | Laboratory | R&D and validation tests | TBD | TBD | Excel/PDF/images | TBD | TBD | Project, sample, batch? | Customer/spec | File export | TBD | High | Open |
| DS-PROD-01 | Line/HMI/PLC/logs | Process settings | TBD | TBD | CSV/DB/paper | TBD | TBD | Timestamp, order, roll? | Operator | TBD | TBD | Critical | Open |
| DS-COM-01 | Complaint records | Customer complaint | TBD | TBD | Email/PDF/ERP | TBD | TBD | Customer, order, roll? | Personal/customer | TBD | TBD | High | Open |
| DS-COST-01 | Finance/controlling | Quality cost | TBD | TBD | ERP/Excel | TBD | Monthly | Job/order/article | Price/cost | TBD | TBD | Critical | Open |

Add one row for every distinct database, export, spreadsheet family, shared folder, instrument, paper workflow, and local machine store.

---

## 4. Data ownership and access matrix

| Data domain | Business owner | System owner | Data steward | Read access approved? | Purpose approved? | Retention rule | Privacy review | Security review | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Orders and articles | TBD | TBD | TBD | No | Discovery | TBD | Required if personal/customer data | Required | |
| Roll identity | TBD | TBD | TBD | No | Discovery | TBD | Low | Required | |
| Process parameters | TBD | TBD | TBD | No | Discovery | TBD | Review operator identifiers | Required | |
| Inspection images/labels | TBD | TBD | TBD | No | Discovery | TBD | Review operator metadata | Required | |
| QC / laboratory results | TBD | TBD | TBD | No | Discovery | TBD | Low | Required | |
| Rework / scrap | TBD | TBD | TBD | No | Baseline | TBD | Review employee fields | Required | |
| Complaints | TBD | TBD | TBD | No | Root-cause evidence | TBD | High | Required | |
| Finance / costing | TBD | TBD | TBD | No | ROI | TBD | Low | Required | |

Access must follow least privilege. Discovery should use the smallest representative sample that can answer feasibility questions.

---

## 5. Identifier linkage test

### Candidate canonical identifiers

- order number;
- production order / work order;
- article / product code;
- roll number;
- parent roll / child roll;
- batch / lot number;
- formulation or recipe version;
- line / machine;
- inspection timestamp;
- QC sample number;
- laboratory project/sample number;
- shipment / delivery number;
- complaint number.

### Linkage matrix

| From | To | Expected key | Actual key | Match rate | Ambiguity rate | Manual mapping needed? | Decision |
|---|---|---|---|---:|---:|---|---|
| INTEX order | Production record | Work order | TBD | TBD | TBD | TBD | Open |
| Production record | Roll | Roll ID | TBD | TBD | TBD | TBD | Open |
| Roll | ELSIS inspection | Roll ID / timestamp | TBD | TBD | TBD | TBD | Open |
| Roll | QC result | Roll ID / sample | TBD | TBD | TBD | TBD | Open |
| Roll | Rework/scrap | Roll / job | TBD | TBD | TBD | TBD | Open |
| Roll/order | Complaint | Delivery/order/roll | TBD | TBD | TBD | TBD | Open |

### Minimum linkage targets

These are initial targets to refine after discovery:

- ≥90% for order-to-roll linkage;
- ≥80% for roll-to-QC linkage;
- ≥70% for roll-to-inspection linkage if historical metadata is incomplete;
- 100% traceability for the new pilot data process after implementation.

A lower historical match rate does not automatically stop the pilot, but it must be quantified and a future-state capture process must be defined.

---

## 6. Data-quality assessment

Score each source from 0 to 5.

| Dimension | 0 | 3 | 5 |
|---|---|---|---|
| Completeness | Mostly missing | Important gaps | Required fields consistently present |
| Accuracy | Untrusted | Some validation | Validated against operational reality |
| Consistency | Conflicting definitions | Mixed conventions | Controlled definitions and units |
| Linkability | No stable identifiers | Partial/manual linkage | Stable machine-readable keys |
| Timeliness | Unknown/outdated | Delayed | Appropriate for intended decision |
| Granularity | Too aggregated | Mixed | Roll/batch/event level as needed |
| Interpretability | No definitions | Expert explanation needed | Documented fields, units, codes |
| Accessibility | Not exportable | Manual export | Approved repeatable read-only access |

For every source, document:

- total records/files;
- missingness by critical field;
- duplicates;
- invalid values;
- inconsistent units;
- inconsistent article/defect naming;
- date/time formats and time zones;
- identifier collisions;
- unmatched records;
- manual corrections currently performed;
- known changes in systems or processes over time.

---

## 7. System-specific audit questions

### INTEX / ERP

- Which modules are used for orders, articles, recipes/BOM, production, inventory, quality, costing, delivery, and complaints?
- Can data be exported by CSV, Excel, database view, API, scheduled report, or vendor interface?
- Are roll numbers generated and stored?
- Are parent/child roll relationships preserved?
- Are recipe versions, material batches, machine, operator, timestamps, quantities, scrap, and rework recorded?
- Which fields are free text versus controlled codes?
- Are historical changes/version histories available?
- Can a read-only technical account or approved export be created?

### ELSIS / inspection system

- Exact software and hardware version?
- Where are raw images, processed images, defect events, labels, severity, coordinates, timestamps, and decisions stored?
- Are image paths and database records exportable?
- Is there a roll/order identifier, encoder position, meter position, or timestamp?
- Are accepted, rejected, ignored, and manually overridden detections recorded?
- Is the defect taxonomy documented?
- What retention period applies to images and events?
- Can a representative export be produced without interrupting the line?
- Are vendor licenses or contractual restrictions relevant?

### QC and laboratory

- Which tests are performed, with what units, limits, methods, and instruments?
- How are results linked to product, roll, sample, recipe, order, customer specification, or project?
- Are failures, retests, deviations, and approvals recorded?
- Are PDFs generated from structured data or created manually?
- Which files contain images or handwritten annotations?
- Can result tables be exported directly instead of extracted from PDFs?

### Production/process

- Which setpoints and actual values are stored?
- Are line speed, temperatures, tension, coating gap, coating weight, viscosity, oven zones, curing, humidity, pressure, and energy available?
- Are values event-based, batch-based, or time series?
- Are recipe changes and operator adjustments recorded?
- Can timestamps be aligned with roll position or production order?

### Quality loss and complaints

- How are scrap and rework defined?
- Are meters, square meters, kilograms, labor hours, machine hours, material cost, and disposal cost available?
- Are downgraded products tracked?
- How long do quality holds and complaint investigations take?
- Can complaint records be linked to order, shipment, article, roll, batch, supplier lot, or process?

---

## 8. Interview guide

Ask every stakeholder:

1. Which decisions do you make repeatedly?
2. Which information do you need, and where do you find it?
3. Which recurring problem costs the most time, material, capacity, or customer trust?
4. Which data do you trust? Which data do you not trust?
5. Which important information exists only in people’s heads, emails, paper, or local files?
6. Which identifiers do you use to trace a product or problem?
7. Which workarounds are normal but undocumented?
8. What would make an AI or analytics tool genuinely useful?
9. What error would make the tool unacceptable?
10. What privacy, security, workload, or job concerns should be addressed?

Do not ask only what people want AI to do. Observe the current workflow and ask for real examples.

---

## 9. Pilot candidate scorecard

Score 1–5.

| Criterion | Weight | Candidate A | Candidate B | Candidate C |
|---|---:|---:|---:|---:|
| Annual quality cost / operational pain | 25% | | | |
| Data availability | 20% | | | |
| Identifier linkability | 15% | | | |
| Product volume / recurrence | 10% | | | |
| Management visibility | 10% | | | |
| Improvement actionability | 10% | | | |
| Cross-functional support | 5% | | | |
| Low operational risk | 5% | | | |
| **Weighted total** | **100%** | | | |

Selection rule: choose the candidate with the best combined value and feasibility, not simply the highest defect rate.

---

## 10. Discovery exit criteria

Discovery is complete only when the team has:

- a signed/approved source inventory;
- named data owners;
- at least one representative sample from every critical source;
- measured linkage rates;
- a data-quality score and known limitations;
- agreed KPI definitions and initial baseline ranges;
- selected one line/product family;
- documented architecture, security, privacy, and access approach;
- estimated implementation effort and cost;
- a clear go, revise, or stop recommendation.

## 11. Discovery final report structure

1. Executive recommendation
2. Business problem and baseline
3. Selected pilot scope
4. Data-source map
5. Linkage results
6. Data-quality results
7. Architecture and security
8. Risks and mitigations
9. Work plan and budget
10. Expected value and ROI scenarios
11. Gate decision requested
