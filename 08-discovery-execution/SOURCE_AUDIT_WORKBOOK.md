# Source Audit Workbook

Use one completed copy of this worksheet for each source: INTEX, ELSIS, QC/lab, production records, complaints/CAPA, Finance/costing, certificates/specifications, or other approved systems.

---

## A. Source identity

| Field | Entry |
|---|---|
| Source name | |
| System/version | |
| Department | |
| Business owner | |
| Technical owner | |
| Access approver | |
| Data steward | |
| Vendor/support contact | |
| Discovery date | |
| Auditor | |

## B. Business purpose

| Question | Entry |
|---|---|
| What business process does this source support? | |
| What decisions depend on it? | |
| Which users create or modify records? | |
| Which users consume the information? | |
| Is it a system of record or a secondary copy? | |
| What known problems exist? | |

## C. Access and extraction

| Field | Entry |
|---|---|
| Approved access mode | View / export / database view / API / vendor export / other |
| Read-only confirmed | Yes / No |
| Export formats | |
| Export frequency possible | |
| Historical depth | |
| Retention period | |
| Approximate volume | |
| Extraction affects production | Yes / No / Unknown |
| Vendor/license restrictions | |
| Repeatable extraction route | |
| Manual steps required | |

## D. Data classification

| Category | Present? | Notes/minimization rule |
|---|---:|---|
| Product/article data | | |
| Order/production-order data | | |
| Roll/batch data | | |
| Formulation/recipe data | | |
| Process parameters | | |
| Quality/test results | | |
| Inspection events/images | | |
| Supplier information | | |
| Customer information | | |
| Pricing/margin/cost | | |
| Employee/operator identity | | |
| Complaints/CAPA | | |
| Certificates/specifications | | |
| Credentials/secrets | | Must never be exported into analysis data |

## E. Identifiers

| Identifier | Exists? | Unique? | Stable? | Coverage | Example format | Notes |
|---|---:|---:|---:|---:|---|---|
| Sales order | | | | | | |
| Production order | | | | | | |
| Article/product | | | | | | |
| Roll | | | | | | |
| Parent roll | | | | | | |
| Child roll | | | | | | |
| Material batch/lot | | | | | | |
| Recipe/formulation version | | | | | | |
| Line/machine | | | | | | |
| Inspection event | | | | | | |
| QC sample/test | | | | | | |
| Shipment | | | | | | |
| Complaint | | | | | | |
| Customer specification | | | | | | |

## F. Time information

| Field | Entry |
|---|---|
| Creation timestamp | |
| Update timestamp | |
| Production start/end | |
| Inspection timestamp | |
| QC test timestamp | |
| Sampling interval | |
| Time zone | |
| Clock synchronization known | |
| Timestamp precision | |
| Historical timestamp reliability | |

## G. Field inventory

For each important field, record:

| Field name | Business meaning | Type | Unit/code list | Mandatory? | Missing % | Owner | Sensitive? | Source field or derived? |
|---|---|---|---|---:|---:|---|---:|---|
| | | | | | | | | |

## H. Quality checks

| Check | Result | Evidence/measurement |
|---|---|---|
| Record count reasonable | | |
| Primary identifiers complete | | |
| Duplicate identifiers | | |
| Invalid dates/times | | |
| Inconsistent units | | |
| Invalid code values | | |
| Free-text variants | | |
| Missing revision history | | |
| Orphan records | | |
| Manual corrections visible | | |
| Retests/rework represented | | |
| Source lineage available | | |

## I. Representative sample

| Field | Entry |
|---|---|
| Sample period | |
| Sample size | |
| Selection logic | |
| Approved by | |
| Storage location | |
| Pseudonymization applied | |
| Known limitations | |

## J. Feasibility assessment

Score 1–5.

| Dimension | Score | Rationale |
|---|---:|---|
| Business relevance | | |
| Owner availability | | |
| Read-only accessibility | | |
| Historical depth | | |
| Identifier quality | | |
| Timestamp quality | | |
| Field completeness | | |
| Repeatable export | | |
| Security/privacy feasibility | | |
| Pilot usefulness | | |

### Final rating

- [ ] Ready
- [ ] Feasible with limited cleanup
- [ ] Feasible with significant remediation
- [ ] Future capture required
- [ ] Blocked

### Required actions

| Action | Owner | Due date | Blocking? | Status |
|---|---|---|---:|---|
| | | | | |

### Evidence statement

Summarize only what was directly observed, what remains assumed, and what is blocked.
