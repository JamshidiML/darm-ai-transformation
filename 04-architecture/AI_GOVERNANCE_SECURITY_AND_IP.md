# AI Governance, Security, Privacy, and IP Controls

## 1. Purpose

This document defines mandatory controls for the Darm AI Transformation Program. It applies to data discovery, prototypes, knowledge retrieval, analytics, machine learning, external partners, and future production deployment.

The goal is to enable innovation without exposing formulations, process know-how, customer information, employee data, quality evidence, or regulated technical claims.

## 2. AI governance model

### Decision rights

| Decision | Required approver(s) |
|---|---|
| Add a new data source | Data owner + IT/security + use-case owner |
| Use customer-identifiable data | Business owner + IT/security + privacy/legal review as required |
| Use employee-related data | Business owner + IT/security + HR/employee representative review as required |
| Upload data to an external AI service | IT/security + data owner + contractual/privacy approval |
| Release an internal knowledge assistant | Use-case owner + IT + Quality/R&D validation |
| Use a predictive model in a workflow | Business owner + technical/model owner + Quality/IT approval |
| Send AI-generated content to a customer | Authorized human owner; AI cannot self-send |
| Change process settings based on AI | Separate approved project, validated model, human authority, operational safety review |
| Automate quality release/certification | Not permitted in initial phases; requires separate governance and validation |

## 3. Risk classification of AI use cases

| Level | Example | Minimum controls |
|---|---|---|
| G0 — Low | Drafting internal non-sensitive text | Approved tool, user review |
| G1 — Moderate | Search across approved SOPs/TDS | Access control, citations, evaluation, logging |
| G2 — High | Quality/root-cause support, supplier substitution, formulation support | Source evidence, expert validation, strict permissions, audit, uncertainty, test set |
| G3 — Critical | Process recommendation, safety/compliance decisions, quality release | Formal validation, change control, human approval, monitoring, rollback, legal/safety review |
| G4 — Prohibited in current program | Autonomous machine control, autonomous release, hidden employee scoring | Not allowed without a future separately approved program |

## 4. Data classification

| Class | Examples | Handling |
|---|---|---|
| Public | Approved website and published product information | May be used in approved public tools |
| Internal | General procedures, non-sensitive project plans | Company-approved tools; no public disclosure |
| Confidential | QC results, internal reports, non-public product information, supplier documents | Restricted role access, approved storage, controlled external use |
| Highly Restricted | Formulations, recipe percentages, proprietary process windows, customer secrets, sensitive complaints, pricing, employee data | Named access, encryption, logging, no public AI, contractual and technical controls |

Every source in discovery must receive a classification and owner.

## 5. Approved-use principles

- Use only the minimum data needed for the approved purpose.
- Prefer aggregation or pseudonymization for employee and customer fields.
- Do not use employee identifiers for performance ranking in the pilot.
- Do not infer sensitive personal characteristics.
- Do not train external models on confidential data unless explicitly approved contractually and technically.
- Preserve source ownership and deletion/retention obligations.
- Keep real operational data outside GitHub unless a formal exception is approved.

## 6. Security controls

### Identity and access

- single sign-on where available;
- role-based access control;
- least privilege;
- separate roles for raw data, curated data, administration, and business use;
- periodic access review;
- immediate removal when role or project participation ends;
- no shared accounts.

### Secrets

- no secrets in source code or notebooks;
- use approved secret management;
- rotate credentials;
- restrict service accounts to read-only where possible;
- log and monitor authentication failures.

### Data protection

- encryption in transit and at rest;
- approved company/EU hosting where required;
- backups and tested recovery;
- retention and secure deletion;
- environment separation for development, test, and production;
- malware scanning and file validation for document ingestion;
- network segmentation where machine/OT systems are involved.

### Logging and audit

Log at minimum:

- user and service access;
- data ingestion events;
- data export/download where feasible;
- model/prompt/version used;
- sources retrieved;
- user approval/override for high-risk outputs;
- administrative changes;
- security incidents.

Logs must not expose sensitive content unnecessarily.

## 7. OT and machine-system boundaries

The initial program must not:

- write to PLC, HMI, machine recipes, ELSIS control, or ERP;
- connect unapproved cloud services directly to production networks;
- bypass machine-vendor or IT security requirements;
- introduce uncontrolled USB/file-transfer processes.

Any future OT integration requires:

- architecture and cyber risk assessment;
- network segmentation;
- approved protocol/gateway;
- change-management process;
- operational testing;
- fail-safe behavior;
- rollback;
- vendor and maintenance ownership.

## 8. Knowledge assistant controls

A technical knowledge assistant must:

- use an approved source corpus;
- show sources at document/page/record level;
- identify uncertainty and conflicting evidence;
- refuse or escalate when evidence is absent;
- respect document permissions;
- avoid using superseded documents without warning;
- log retrieval and model version;
- be evaluated before release.

It must not:

- invent test results, standards, certifications, or product approvals;
- issue customer-facing claims without human approval;
- reveal restricted formulations or customer information to unauthorized users;
- treat model fluency as evidence.

## 9. Model governance

Every model requires a model card containing:

- intended use and prohibited use;
- business owner and technical owner;
- training/evaluation data period and scope;
- target definition;
- baseline comparison;
- performance metrics and subgroup results;
- false-positive and false-negative consequences;
- known limitations;
- explainability approach;
- human review point;
- monitoring and drift plan;
- retraining criteria;
- rollback/retirement process;
- approval record.

No model should be deployed solely because it has a high aggregate score.

## 10. IP protection

The program's strategic IP includes:

- formulations and recipe versions;
- process windows and scale-up knowledge;
- relationships between materials, process, tests, defects, applications, and customer outcomes;
- historical experiments, including failed trials;
- defect and root-cause knowledge;
- supplier performance and substitution logic;
- trained models, features, ontologies, knowledge graphs, and evaluation datasets;
- proprietary workflows and decision rules.

Protection measures:

- explicit ownership in contracts;
- no vendor right to reuse confidential data or outputs without written approval;
- export rights for data, embeddings, metadata, model artifacts, logs, and configurations;
- avoid architecture that traps knowledge in a proprietary UI;
- use confidentiality labels and role-based access;
- separate company IP from personal/startup repositories unless formally authorized;
- document inventorship and patentable developments when relevant.

## 11. External partner requirements

Before sharing data or access:

- NDA and appropriate data-processing terms;
- defined purpose and data scope;
- hosting/subprocessor disclosure;
- security controls and incident notification;
- deletion/return obligations;
- no secondary model training or reuse without permission;
- IP ownership and licensing terms;
- audit/evidence rights where proportionate;
- exit and data-export plan.

## 12. Privacy and employee trust

The program should communicate clearly:

- what data is used;
- why it is used;
- who can access it;
- what decisions AI can and cannot make;
- how long data is kept;
- how employees can report concerns or errors.

Initial employee-related design:

- prefer shift/role/process context over individual identity;
- pseudonymize identifiers where individual identity is not required;
- do not build productivity rankings;
- do not use hidden behavioral monitoring;
- involve employee representatives where legally or organizationally required.

## 13. AI output labels

Every high-risk AI output should show:

- `AI-generated assistance — human review required`;
- source references;
- generation/model version;
- date/time;
- confidence/uncertainty or evidence coverage;
- responsible reviewer status.

## 14. Incident process

Report immediately:

- unauthorized data exposure;
- prompt or retrieval leakage;
- incorrect technical, quality, certification, or safety output with potential impact;
- access-control failure;
- unapproved external tool usage;
- model behavior that creates systematic risk;
- operational disruption connected to the system.

Response steps:

1. contain and disable affected access/workflow;
2. preserve logs and evidence;
3. notify IT/security and business owner;
4. assess data, operational, customer, legal, and employee impact;
5. correct and validate;
6. document root cause and preventive action;
7. approve restart.

## 15. Gate checklist

Before discovery:

- owners identified;
- approved purpose;
- access route approved;
- secure workspace available;
- data classification started.

Before pilot:

- source inventory and data owners complete;
- security/privacy review complete;
- approved architecture and retention;
- risk register updated;
- employee communication completed where needed.

Before scale:

- measurable value demonstrated;
- model/retrieval evaluation complete;
- support and ownership defined;
- monitoring and incident process tested;
- contracts and IP terms approved;
- operational rollback available.
