# Stakeholder Nomination and Controlled Access Request

**Program:** Darmstädter + Klevers AI Transformation  
**Phase:** Gate 0 / Two-week Discovery Sprint  
**Purpose:** nominate the minimum cross-functional team and request only the access required to assess feasibility.

## 1. Nomination request

The discovery sprint needs a small working group with decision access and operational knowledge. The expected contribution is focused and time-bounded.

| Function | Nominee | Expected contribution | Estimated discovery involvement |
|---|---|---|---:|
| Executive Sponsor | | Decisions, escalation, cross-functional support | 30 min kickoff + 30 min Gate 1 + brief updates |
| AI Transformation Lead | Mohsen Jamshidi (proposed) | Coordination, interviews, analysis, documentation, synthesis | Lead role |
| R&D | | Data sources, technical context, experiment/knowledge requirements | 2–4 hours |
| Production | | Line workflow, records, process parameters, operator context | 3–5 hours |
| Quality | | Tests, limits, defects, release, complaints, validation | 4–6 hours |
| Packaging / Inspection | | ELSIS workflow, labels, images/events, operator decisions | 3–5 hours |
| IT / Security | | Access, architecture, systems, storage, security, retention | 4–8 hours |
| Finance / Controlling | | KPI definitions, cost baseline, ROI validation | 2–4 hours |
| HR / Employee Representative | | Privacy, transparency, employee-impact review if required | As required |
| INTEX key user/vendor contact | | Export/report/interface knowledge | 1–3 hours |
| ELSIS key user/vendor contact | | Database/export/image/event knowledge | 1–3 hours |

The discovery should not create a large committee. Additional specialists are invited only for specific questions.

## 2. Working agreement

Each representative agrees to:

- explain the actual workflow rather than only the documented process;
- provide or authorize the smallest representative sample needed;
- identify known data limitations and manual workarounds;
- review interpretations in their domain;
- distinguish fact, assumption, and expert hypothesis;
- protect confidential information;
- avoid adding unrelated scope before Gate 1;
- nominate a substitute if unavailable.

## 3. Controlled data-access request

### General rule

Discovery access is:

- read-only;
- purpose-limited;
- time-limited;
- minimum necessary;
- role-based;
- auditable where feasible;
- stored only in an approved company environment.

The preference is an approved representative export rather than direct production-system access.

### Requested source assessment

| Source | Requested information | Preferred access | Not requested |
|---|---|---|---|
| INTEX | Field list, report/export options, representative order/article/roll/production/quality/rework/cost records | Approved export or read-only report | Write access, unrestricted customer/pricing data, full database copy |
| ELSIS | Schema/metadata, representative defect events, labels, positions, timestamps, decisions, selected images if approved | Vendor-supported/read-only export | Control access, production configuration changes, unrestricted image dump |
| QC | Test dictionary, limits, representative results, release/deviation links | Approved table/file sample | Unnecessary personal data or unrelated product families |
| Laboratory | Method/result structure, sample/project/roll linkage, representative reports | Approved sample/export | Full confidential R&D archive before scope approval |
| Production | Available settings/actuals, timestamps, IDs, representative logs | Approved export or supervised review | PLC/HMI write access or uncontrolled network connection |
| Rework/scrap/hold | Definitions, quantities, reasons, time/cost fields | Aggregated or approved sample | Individual performance analysis |
| Complaints | Minimized selected cases and linkage fields | Redacted/pseudonymized sample | Unnecessary customer/person identifiers |
| Finance | Aggregated cost components and approved rates | Controlled summary | Unrestricted pricing, payroll, or unrelated financial records |

## 4. Data minimization checklist

Before transfer, ask:

- Is the field necessary to answer a discovery question?
- Can it be aggregated?
- Can customer identity be replaced by a controlled ID?
- Can employee identity be removed or replaced by role/shift?
- Can a small representative sample replace a full export?
- Can the file remain in place and be reviewed under supervision?
- Is the retention period defined?
- Is the deletion/return process clear?

## 5. Representative sample guidance

The ideal first sample contains a small number of selected rolls with enough context to test linkage:

- 10–30 rolls across at least two dates/batches;
- at least one normal case;
- at least one defect/rework case;
- at least one QC failure/retest or quality-hold case if available;
- at least one roll with ELSIS data;
- one product family candidate;
- source identifiers preserved;
- customer and employee fields minimized.

The exact sample should be approved by the relevant data owners.

## 6. Questions for each data owner

1. What is the authoritative source?
2. What business process creates the data?
3. What does each critical field mean?
4. Which identifiers are stable and unique?
5. Which values are manually entered?
6. Which known errors or workarounds exist?
7. How far back is data available?
8. How often does the structure change?
9. What confidentiality, retention, contractual, or legal restrictions apply?
10. Who may approve future repeatable access?

## 7. Approval table

| Source/domain | Business owner | Technical owner | Approved purpose | Approved sample/scope | Access method | Expiry | Conditions |
|---|---|---|---|---|---|---|---|
| INTEX | | | Discovery | | | | |
| ELSIS | | | Discovery | | | | |
| QC | | | Discovery | | | | |
| Laboratory | | | Discovery | | | | |
| Production | | | Discovery | | | | |
| Rework/scrap/hold | | | Baseline | | | | |
| Complaints | | | Linkage/root-cause feasibility | | | | |
| Finance | | | KPI/ROI baseline | | | | |

## 8. Discovery communication

Recommended message to participating colleagues:

> We are conducting a short, read-only discovery to understand whether existing data and technical knowledge can be connected to improve quality, traceability, and problem solving. The objective is not to monitor individual performance or control machines. We will use the minimum necessary data, involve the responsible experts, make limitations visible, and return to management with a Go, Revise, or Stop recommendation before any larger implementation.

## 9. Completion criteria

This nomination/access package is complete when:

- all core representatives are named;
- each critical source has an owner;
- approved access/sample method is recorded;
- the secure workspace is known;
- privacy/employee requirements are addressed;
- discovery kickoff and Gate 1 review dates are scheduled.
