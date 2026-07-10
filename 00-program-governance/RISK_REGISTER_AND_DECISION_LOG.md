# Risk Register and Decision Log

## Risk scoring

- Probability: 1 low — 5 very high
- Impact: 1 low — 5 critical
- Score: probability × impact
- Escalation: scores 15–25 require sponsor visibility and explicit mitigation ownership.

## Initial risk register

| ID | Risk | P | I | Score | Early warning | Mitigation | Owner | Status |
|---|---|---:|---:|---:|---|---|---|---|
| R-01 | Roll, order, process, inspection, and QC identifiers cannot be linked reliably | 4 | 5 | 20 | High unmatched-record rate | Run linkage audit before modeling; define canonical roll ID and reconciliation rules | AI Lead + IT + Quality | Open |
| R-02 | ELSIS data or images are not exportable or lack usable metadata | 3 | 5 | 15 | Local-only storage, proprietary format, missing timestamps | Technical audit, vendor documentation, read-only export test, fallback to existing defect summaries | Packaging + IT | Open |
| R-03 | Process parameters are not historically stored | 4 | 4 | 16 | Settings exist only on paper/HMI/operator memory | Start with available batch records and manual sample; define future capture requirements | Production + IT | Open |
| R-04 | Quality-cost baseline is unavailable or disputed | 3 | 5 | 15 | Scrap/rework definitions differ by department | Finance-approved KPI definitions and transparent assumption ranges | Finance + Quality | Open |
| R-05 | Defect labels are inconsistent or too subjective | 4 | 4 | 16 | Same defect appears under multiple names | Build controlled taxonomy, severity rules, examples, and human review | Quality + Packaging | Open |
| R-06 | Scope expands across too many lines, products, and systems | 4 | 4 | 16 | New requests added before first gate | Enforce one line, one product family, one historical window | Sponsor + AI Lead | Open |
| R-07 | Management expects predictive AI before data readiness | 3 | 4 | 12 | Pressure for a demo model without baseline | Communicate phase gates and show data-readiness evidence first | AI Lead | Open |
| R-08 | Confidential formulations or customer data are exposed to unapproved services | 2 | 5 | 10 | Ad hoc uploads to public tools | Approved tool list, data classification, DPA/security review, access logging | IT / Security | Open |
| R-09 | Employee data is interpreted as performance monitoring | 3 | 5 | 15 | Operator identifiers included without purpose | Data minimization, pseudonymization, transparency, works-council review where required | HR/IT/Employee Rep. | Open |
| R-10 | Technical assistant produces unsupported or unsafe claims | 3 | 5 | 15 | Answers without sources or uncertainty | Source-cited retrieval only; approved corpus; human sign-off; evaluation set | Quality + R&D + IT | Open |
| R-11 | Pilot creates a one-off dashboard with no maintainable data process | 3 | 4 | 12 | Manual files and undocumented transformations | Data contracts, owners, reproducible pipelines, architecture decisions | IT + AI Lead | Open |
| R-12 | External vendor lock-in limits control of data and models | 2 | 4 | 8 | Proprietary storage and no export rights | Open formats, export clauses, modular architecture, data ownership | IT + Procurement | Open |
| R-13 | Pilot produces insights but no operational action | 3 | 4 | 12 | Findings have no owner or due date | Action register linking each insight to owner, expected benefit, and verification date | Sponsor + Quality + Production | Open |
| R-14 | Funding applications delay execution | 3 | 3 | 9 | Work paused until grant decision | Start discovery internally; use grants for R&D-heavy scale-up | Sponsor + Finance | Open |
| R-15 | AI work conflicts with existing SmartCoat or other innovation initiatives | 2 | 4 | 8 | Duplicate schemas, platforms, or priorities | Define portfolio boundaries and reuse compatible data/knowledge standards | AI Lead + Sponsor | Open |

## Risk review cadence

- Review weekly during discovery and pilot.
- Re-score at every gate.
- Add evidence links to each risk.
- Close a risk only when the mitigation is implemented and verified.

---

# Decision Log

| Decision ID | Date | Decision | Options considered | Rationale | Owner | Consequence / follow-up |
|---|---|---|---|---|---|---|
| D-001 | 2026-07-10 | Use a phase-gated program model | Direct 12-week pilot; platform build; discovery-first | Reduces uncertainty and makes cost/value evidence credible | AI Lead | Prepare Gate 0 management ask |
| D-002 | 2026-07-10 | Narrow first operational scope to one line and one product family | Whole-company transformation; coating + packaging + R&D in parallel | Prevents scope overload and enables traceable results | AI Lead | Select candidate during discovery |
| D-003 | 2026-07-10 | Keep first phase read-only | Machine control; ERP writeback; analytics only | Protects operations, security, and management trust | AI Lead | No control-loop work in pilot |
| D-004 | 2026-07-10 | Treat original report as internal working source and create a corporate-facing strategy | Use original report unchanged | Separates company case from personal career planning | AI Lead | Use corporate version for management |
| D-005 | 2026-07-10 | Keep sensitive operational data outside GitHub | Store exports/images in repository; store only schemas/code/docs | Protects recipes, customer data, employee data, and production IP | AI Lead | Define approved data environment with IT |

## Decision template

```text
Decision ID:
Date:
Decision owner:
Context:
Decision:
Options considered:
Evidence:
Rationale:
Risks accepted:
Follow-up actions:
Review date:
```
