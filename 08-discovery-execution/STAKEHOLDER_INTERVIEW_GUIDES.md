# Stakeholder Interview Guides

These interviews are evidence-gathering sessions, not generic discussions about AI. Ask participants to demonstrate real workflows, records, examples, decisions, and problems wherever permitted.

## Common opening

> The purpose is to understand how quality and process decisions are made today, where evidence is stored, which identifiers connect it, and which repeated problems could justify a narrow read-only pilot. This is not an employee-performance assessment and not a machine-control project.

## Common evidence rules

- Ask for approved representative examples, not broad uncontrolled exports.
- Record source, owner, date, and limitations.
- Separate observed workflow from assumptions.
- Do not capture passwords, secrets, or unnecessary personal data.
- Do not treat one person’s opinion as a verified system fact.

---

# 1. Management / Executive Sponsor

## Objectives

- Confirm the business problem and decision thresholds.
- Understand strategic priorities and political constraints.
- Establish sponsorship and escalation.

## Questions

1. Which quality, delivery, knowledge, or cost problems matter most this year?
2. Which recurring problem would management most value understanding or preventing?
3. Which product families or customers create disproportionate complexity or risk?
4. What result would make the discovery and pilot credible?
5. What result would make management stop the project?
6. Which costs are visible today and which are hidden?
7. Which departments must trust the outcome?
8. Which confidentiality, customer, employee, or operational concerns are non-negotiable?
9. Which budget and resource level could be considered after discovery?
10. Who owns the final Gate 1 decision?

## Required evidence

- Named sponsor.
- Strategic priorities.
- Approval constraints.
- Gate 1 decision criteria.

---

# 2. R&D / Product Development

## Objectives

- Understand formulation, testing, scale-up, failure-memory, and product-selection workflows.
- Identify which knowledge could later connect to roll quality.

## Questions

1. How is a new customer requirement converted into substrate, coating, lamination, and test choices?
2. Where are formulations, recipe versions, trials, and failures recorded?
3. How are lab trials linked to production trials and finished rolls?
4. Which fields distinguish two recipe versions?
5. How are supplier batches and raw-material substitutions tracked?
6. Which failures recur because old lessons are difficult to find?
7. How are scale-up deviations documented?
8. Which tests determine approval, rejection, or another experiment?
9. Which technical notes are structured and which are free text?
10. What evidence would help R&D explain a production or customer failure faster?
11. Which data must be restricted most strongly?
12. Which pilot product family has enough history and technical value?

## Demonstration request

Show one successful and one failed development path from requirement through lab, production, QC, and outcome.

---

# 3. Production

## Objectives

- Understand recipe execution, adjustments, process records, deviations, and practical constraints.

## Questions

1. How does an operator know which recipe and settings to run?
2. Which settings are setpoints and which are actual measured values?
3. Where are line speed, oven zones, tension, gap, coating weight, viscosity, solids, humidity, alarms, and adjustments recorded?
4. Which settings are changed manually and why?
5. Are recipe or parameter changes versioned?
6. How are start-up, changeover, cleaning, stoppage, and restart periods represented?
7. How are parent and child rolls handled?
8. When a defect appears later, how is the corresponding production context reconstructed?
9. Which operator observations are important but not recorded?
10. Which products are stable and which are highly sensitive?
11. Which repeated defects or rework activities consume the most time?
12. What would make a read-only analysis useful rather than burdensome?

## Demonstration request

Trace one recent production order from work instruction through settings, operator notes, produced rolls, and handoff to inspection/QC.

---

# 4. Packaging / Inspection / ELSIS Users

## Objectives

- Understand inspection events, images, defect labels, operator decisions, roll position, and release workflow.

## Questions

1. What system and version are used?
2. What does ELSIS detect automatically and what is still manual?
3. Which information is stored for every event?
4. Are original images retained? For how long?
5. Are meter position, coordinates, timestamp, roll ID, order ID, or encoder information available?
6. How are defect classes defined?
7. How are severity and disposition decided?
8. Are accepted, rejected, ignored, or reclassified events recorded?
9. Are human overrides captured?
10. Which defect labels are ambiguous or inconsistently used?
11. What information is sent upstream to Production or R&D?
12. What information is used for final release or customer evidence?
13. Can representative events/images be exported read-only?
14. What vendor or license restrictions exist?

## Demonstration request

Show one accepted roll and one problematic roll, including event list, images, classification, operator action, and final decision.

---

# 5. Quality Control / Laboratory

## Objectives

- Understand tests, specifications, units, retests, release decisions, deviations, and record linkage.

## Questions

1. Which tests are performed routinely and which are product/customer specific?
2. Where are methods, limits, units, and method revisions controlled?
3. How are samples linked to order, roll, batch, recipe, project, and customer specification?
4. How are failures, retests, conditional approvals, deviations, and waivers recorded?
5. Which results are entered manually?
6. Which PDFs originate from structured instrument data?
7. Are raw values retained or only final pass/fail?
8. How are certificates and COAs generated?
9. What delays release?
10. Which tests are repeated because previous evidence is difficult to find?
11. Which defects or complaints require the most investigation?
12. Which quality terms differ from ELSIS or Production terminology?
13. What information would make root-cause work faster?

## Demonstration request

Show one normal release, one retest, and one deviation/failed release with all linked evidence.

---

# 6. IT / Security / Data Protection

## Objectives

- Establish safe access, approved infrastructure, retention, identity, and technical boundaries.

## Questions

1. Which systems and owners are involved?
2. Which read-only interfaces or export routes are approved?
3. Which systems are in OT, IT, vendor-managed, or isolated networks?
4. What data classifications apply?
5. Where may discovery data be stored and processed?
6. Which services are approved for document or AI processing?
7. What encryption, backup, retention, deletion, and audit requirements apply?
8. Which fields must be removed or pseudonymized?
9. Is employee or personal data present?
10. Is works-council or data-protection review required?
11. What vendor contracts or licenses restrict export or model use?
12. How will access be revoked after discovery?
13. What is the incident route for accidental exposure?
14. How should future production deployment be segmented from machine control?

## Required evidence

- Approved workspace.
- Approved transfer routes.
- Named access approvers.
- Data classification and retention rules.

---

# 7. Finance / Controlling

## Objectives

- Define auditable quality-cost baselines and prevent inflated ROI claims.

## Questions

1. How are scrap quantities and values recorded?
2. How are rework labor, machine hours, energy, and materials costed?
3. How are downgraded goods, credits, replacements, and complaint costs recorded?
4. Which costs are actual postings and which require estimates?
5. Which period is representative?
6. How should standard cost and actual cost be used?
7. Where could double counting occur?
8. Can cost be analyzed by article, order, product family, line, defect, or customer?
9. How are quality holds and lost capacity valued?
10. What confidence level is required before management accepts a benefit claim?
11. What payback period is acceptable?
12. Which pilot costs must be included beyond external invoices?

## Demonstration request

Reconcile one scrap event, one rework event, and one complaint/replacement from physical evidence to financial impact.

---

# 8. Sales / Customer Service / Complaints

## Objectives

- Understand complaint linkage, customer specifications, response effort, and repeated-case value.

## Questions

1. How are complaints registered and categorized?
2. Which identifiers connect complaints to order, shipment, article, and roll?
3. Are photos, samples, customer specifications, and correspondence retained together?
4. How is root cause investigated?
5. How are CAPA and customer responses approved?
6. Which complaints recur?
7. How much time is spent assembling evidence?
8. Are credits, replacements, returns, and lost orders visible?
9. Which customer-specific limits or approvals affect the decision?
10. Which complaint information is sensitive or personal?
11. Which evidence would improve response speed and credibility?

## Demonstration request

Trace one resolved complaint and one unresolved or repeated complaint through evidence, decision, cost, and corrective action.

---

# Interview Record Template

| Field | Entry |
|---|---|
| Interview | |
| Date | |
| Participants | |
| Department | |
| Systems demonstrated | |
| Documents/examples shown | |
| Observed facts | |
| Supported findings | |
| Assumptions to verify | |
| Blockers | |
| Candidate identifiers | |
| Data-quality concerns | |
| High-value pain points | |
| Security/privacy concerns | |
| Decisions needed | |
| Actions, owners, due dates | |
