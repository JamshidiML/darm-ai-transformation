# Cross-System Roll Linkage Test Specification

## Purpose

Measure whether representative production rolls can be traced reliably across INTEX, production records, ELSIS inspection, QC/laboratory evidence, rework/scrap, shipment, and complaints.

This is the central feasibility test for the Roll Quality Intelligence pilot.

---

## 1. Scope

Test at least two candidate product families or lines where feasible.

Recommended sample per candidate:

- 30–50 rolls minimum for initial linkage testing;
- include normal, reworked, rejected, complaint-linked, and unusual rolls;
- include parent/child roll cases;
- include at least two production dates or campaigns;
- include more than one operator/shift only when permitted and without employee-performance analysis.

The sample must be approved, representative, and stored in the approved company environment.

---

## 2. Required source domains

| Domain | Minimum evidence |
|---|---|
| INTEX | order, production order, article, roll, quantity, dates, status |
| Production | line, recipe/version, settings or production sheet, start/end |
| ELSIS | roll reference, events, labels, positions/timestamps, decisions |
| QC/lab | sample/test identifier, method, value, unit, limits, decision |
| Rework/scrap | roll/order reference, reason, quantity, disposition |
| Shipment | shipment/delivery reference, customer/order link |
| Complaints | complaint ID, order/shipment/roll link where available |

A missing domain is not silently excluded. It is recorded as unavailable, not applicable, or blocked.

---

## 3. Canonical linkage model

The initial canonical model should support:

```text
sales_order
  └── production_order
        └── parent_roll
              ├── child_roll_A
              ├── child_roll_B
              └── child_roll_C
```

Each roll may connect to:

- article/product;
- material lots;
- recipe/formulation version;
- line/machine;
- production interval;
- inspection events/images;
- QC samples/tests;
- rework/scrap records;
- release status;
- shipment;
- complaint/CAPA.

Do not assume `roll_id` is globally unique until measured.

---

## 4. Identifier normalization

For every source identifier, preserve:

- source system;
- original value;
- normalized value;
- normalization rule;
- parent/child relationship;
- confidence;
- manual or automatic match flag.

Allowed normalization examples:

- trim leading/trailing whitespace;
- normalize case where business rules confirm case-insensitivity;
- remove formatting separators only when documented;
- map known prefixes/suffixes;
- map parent/child identifiers using approved production logic.

Prohibited:

- guessing identifiers from approximate text without a documented rule;
- overwriting original values;
- silently merging ambiguous records;
- using customer or employee names as primary linkage keys.

---

## 5. Matching hierarchy

### Level A — deterministic exact match

Examples:

- exact roll ID + source-approved normalization;
- exact production order + child-roll sequence;
- exact inspection roll reference;
- exact QC roll/sample mapping.

### Level B — deterministic composite match

Examples:

- production order + article + date/time window;
- parent roll + cut/slit child sequence;
- line + campaign + roll sequence.

### Level C — supported temporal/contextual match

Examples:

- production interval aligned with inspection start/end;
- QC sample time and article aligned with a unique candidate roll.

Level C requires documented evidence and confidence. It cannot be treated as an exact match.

### Level D — unresolved/ambiguous

More than one plausible match or insufficient evidence.

Never force Level D into a matched record.

---

## 6. Linkage table

Create one row per canonical roll.

| canonical_roll_id | source_roll_ids | production_order | article | parent_roll | production_record | elsis_record | qc_record | rework_scrap_record | shipment_record | complaint_record | match_level | confidence | unresolved_reason |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Preserve source-level lineage in a separate mapping table where one source contains multiple records per roll.

---

## 7. Metrics

Calculate separately for each candidate scope.

### Core linkage rates

```text
order_to_roll_rate = rolls linked to an order / sampled rolls
roll_to_production_rate = rolls linked to production context / sampled rolls
roll_to_inspection_rate = rolls linked to ELSIS / sampled rolls
roll_to_qc_rate = rolls linked to QC/lab evidence / sampled rolls
roll_to_rework_scrap_rate = applicable rolls linked to rework/scrap / applicable rolls
roll_to_shipment_rate = shipped rolls linked to shipment / shipped rolls
complaint_traceability_rate = complaints linked to order/roll / sampled complaints
complete_passport_rate = rolls with all required applicable domains / sampled rolls
```

### Quality metrics

- duplicate source identifiers;
- ambiguous matches;
- unmatched records;
- orphan records;
- manual match percentage;
- Level A/B/C/D distribution;
- average manual minutes per roll;
- missing critical-field percentage;
- timestamp alignment error where measurable.

---

## 8. Initial feasibility thresholds

These are decision aids, not universal truth. Gate 1 may adjust them based on business context.

| Metric | Strong | Workable with remediation | Weak/blocking |
|---|---:|---:|---:|
| Order-to-roll linkage | ≥95% | 80–94% | <80% |
| Roll-to-inspection linkage | ≥90% | 70–89% | <70% |
| Roll-to-QC linkage | ≥85% | 60–84% | <60% |
| Core production context | ≥85% | 60–84% | <60% |
| Exact/composite matches (A+B) | ≥85% | 65–84% | <65% |
| Manual reconciliation | ≤10% | 11–30% | >30% |
| Complete required passport | ≥75% | 50–74% | <50% |

A candidate may still be selected with weak historical process data when future capture is inexpensive and the near-term analytics value remains strong.

---

## 9. Parent/child roll test

Explicitly verify:

- whether parent and child roll IDs are stored;
- whether quantities reconcile;
- whether inspection occurs before or after splitting;
- whether QC samples refer to parent or child;
- whether rework creates new roll identities;
- whether shipment uses parent, child, or packaging labels;
- whether complaints reference a delivered child roll.

Document any one-to-many and many-to-one relationships.

---

## 10. Timestamp alignment test

For sources that lack direct identifiers:

1. confirm source clock/time zone;
2. compare production start/end with inspection start/end;
3. compare line speed, roll length, and event position where possible;
4. identify clock drift or manual time entry;
5. calculate plausible alignment tolerance;
6. label matches as contextual rather than exact.

Do not use timestamps alone when overlapping jobs or parallel lines create ambiguity.

---

## 11. Data-quality scorecard

Score 1–5:

| Dimension | Weight |
|---|---:|
| Identifier completeness | 20% |
| Identifier uniqueness/stability | 15% |
| Cross-source linkage | 20% |
| Timestamp quality | 10% |
| Process-context availability | 10% |
| Inspection/QC availability | 10% |
| Repeatable extraction | 10% |
| Manual effort | 5% |

Calculate weighted score, but retain individual weak dimensions. A high average must not hide a critical identifier failure.

---

## 12. Required outputs

- canonical identifier recommendation;
- source alias and normalization table;
- parent/child roll model;
- measured linkage rates;
- ambiguous/unmatched examples;
- manual-reconciliation rules;
- data-quality scorecard;
- remediation backlog;
- recommended pilot scope and fallback;
- evidence supporting go/revise/stop.

---

## 13. Acceptance criteria

The linkage test is complete when:

- the sample selection is documented;
- original identifiers are preserved;
- matching rules are reproducible;
- ambiguity is not hidden;
- all metrics are calculated by candidate scope;
- results are validated by source owners;
- the recommended canonical key strategy is documented;
- the pilot-selection decision can be defended with evidence.
