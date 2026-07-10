# Roll Quality Passport — Canonical Schema v0.1

## 1. Purpose

The Roll Quality Passport is the pilot's central traceability object. It provides one evidence-linked view of a physical roll from customer/order context through materials, production, inspection, QC, release, shipment, and post-delivery outcomes.

This document defines the logical model. It is not a production database specification and must be reconciled with real INTEX, ELSIS, QC, and production fields during discovery.

## 2. Design principles

- One canonical roll identifier with source-system aliases.
- Preserve source values and provenance; do not silently overwrite.
- Record uncertainty, missingness, and manual mappings.
- Separate facts, human judgments, and model outputs.
- Keep timestamps and units explicit.
- Support parent/child roll relationships.
- Store references to sensitive files rather than copying them into GitHub.
- Version taxonomies, recipes, specifications, and transformation logic.

## 3. Core entities

```text
CustomerRequirement
        |
SalesOrder / ProductionOrder
        |
Article / ProductSpecification
        |
ParentRoll -> Roll -> ChildRoll
        |
MaterialLots + RecipeVersion
        |
ProductionRun + ProcessEvents
        |
InspectionRun + DefectEvents
        |
QC/Lab Samples + TestResults
        |
Disposition / Rework / Release
        |
Shipment
        |
Complaint / FieldOutcome
```

## 4. Roll entity

| Field | Type | Required | Description |
|---|---|---:|---|
| `roll_id` | string | Yes | Canonical internal roll identifier |
| `source_roll_ids` | array | Yes | IDs used by ERP, inspection, labels, spreadsheets, or other sources |
| `parent_roll_id` | string/null | Conditional | Parent roll before slitting, cutting, coating, lamination, or rework |
| `child_roll_ids` | array | No | Derived rolls |
| `article_id` | string | Yes | Canonical article/product code |
| `product_family` | string | Yes | Controlled product-family label |
| `production_order_id` | string | Yes | Production/work-order reference |
| `sales_order_id` | string/null | No | Customer-order reference where allowed |
| `customer_id` | string/null | Restricted | Pseudonymized or role-protected customer identifier |
| `line_id` | string | Yes | Production line/machine |
| `production_start` | datetime | Yes | Start timestamp with time zone |
| `production_end` | datetime | Yes | End timestamp with time zone |
| `nominal_length_m` | decimal | No | Planned length |
| `actual_length_m` | decimal | No | Produced/measured length |
| `width_mm` | decimal | No | Measured or nominal width; distinguish source |
| `mass_kg` | decimal | No | Actual roll mass if available |
| `status` | enum | Yes | planned/in_process/hold/rework/released/downgraded/scrapped/shipped |
| `data_completeness_score` | decimal | Derived | Coverage of critical passport domains |
| `created_at` | datetime | Yes | Passport record creation |
| `updated_at` | datetime | Yes | Latest update |

## 5. Product and requirement context

| Field | Description |
|---|---|
| `article_id` | Internal article/product code |
| `article_revision` | Version/revision if used |
| `product_family` | Controlled family |
| `substrate_type` | Glass, aramid, silica, basalt, blend, etc. |
| `weave_or_structure` | Woven construction, needlemat, tape, hybrid, etc. |
| `finish_route` | Silicone, PU, vermiculite, graphite, lamination, appreture, hybrid, etc. |
| `customer_requirement_id` | Link to approved specification/requirement record |
| `target_temperature_c` | Application/test target, with context |
| `required_certifications` | Controlled list |
| `target_weight_g_m2` | Nominal requirement |
| `target_thickness_mm` | Nominal requirement |
| `quality_plan_id` | Required tests and acceptance limits |

## 6. Material and recipe context

### Material lot

| Field | Description |
|---|---|
| `material_id` | Canonical raw-material ID |
| `supplier_id` | Approved supplier ID |
| `supplier_material_code` | Supplier grade/code |
| `supplier_lot` | Supplier batch/lot |
| `internal_batch` | Internal batch ID |
| `quantity_used` | Value + unit |
| `coa_reference` | Controlled reference to CoA |
| `expiry_or_retest_date` | Where relevant |
| `deviation_status` | approved/deviation/unknown |

### Recipe/formulation

| Field | Description |
|---|---|
| `recipe_id` | Canonical recipe identifier |
| `recipe_version` | Immutable version |
| `recipe_effective_date` | Date version became effective |
| `formulation_batch_id` | Prepared mix/batch identifier |
| `target_solids_pct` | If relevant |
| `measured_viscosity` | Value, unit, temperature, method |
| `pot_life_context` | If relevant |
| `confidentiality_class` | Restricted/highly restricted |

Detailed formulation composition should remain in approved company systems and must not be exposed to unauthorized users or public AI services.

## 7. Process context

| Field | Description |
|---|---|
| `production_run_id` | Run/batch identifier |
| `line_id` | Machine/line |
| `operator_or_shift_id` | Pseudonymized/aggregated unless a documented purpose requires otherwise |
| `start_time` / `end_time` | Time zone explicit |
| `line_speed_m_min` | Setpoint and actual where available |
| `zone_temperatures_c` | Setpoints and actual values by zone |
| `web_tension` | Value + unit + sensor/source |
| `coating_gap` | Value + unit |
| `target_coating_weight_g_m2` | Target |
| `actual_coating_weight_g_m2` | Measured/estimated |
| `drying_or_curing_profile` | Structured reference |
| `ambient_temperature_c` | If available |
| `ambient_humidity_pct` | If available |
| `energy_kwh` | If available and allocable |
| `process_deviation_events` | Timestamped events with reason/action |
| `manual_adjustments` | Timestamped, purpose-defined, human-entered events |

For time-series data, store references to a time-series store and summarize roll-level features rather than duplicating all raw points in the passport.

## 8. Inspection and defect context

### Inspection run

| Field | Description |
|---|---|
| `inspection_run_id` | Inspection-system run |
| `system_name_version` | ELSIS and relevant software/model version |
| `inspection_start` / `inspection_end` | Timestamps |
| `image_or_event_store_reference` | Approved location reference |
| `meters_inspected` | Coverage |
| `inspection_completeness` | Complete/partial/unknown |

### Defect event

| Field | Description |
|---|---|
| `defect_event_id` | Unique event |
| `defect_taxonomy_version` | Version used |
| `defect_code` | Controlled code |
| `source_label` | Original ELSIS/operator label |
| `severity` | 0–4 or approved scale |
| `confidence` | System confidence where relevant |
| `meter_position` | Longitudinal position |
| `cross_web_position_mm` | Lateral position |
| `length_mm` / `width_mm` / `area_mm2` | Geometry if available |
| `timestamp` | Detection timestamp |
| `image_reference` | Controlled path/ID |
| `human_decision` | accepted/rejected/ignored/reclassified/unknown |
| `disposition` | no_action/mark/cut/rework/downgrade/scrap/hold |
| `reviewer_role` | Role, not personal identity unless required |
| `root_cause_status` | unknown/hypothesis/confirmed |
| `root_cause_reference` | Link to approved investigation record |

## 9. QC and laboratory context

### Sample

| Field | Description |
|---|---|
| `sample_id` | Canonical sample ID |
| `roll_id` | Roll link |
| `sample_position_m` | Position if known |
| `sampling_time` | Timestamp |
| `sampling_method` | Controlled code |
| `laboratory_or_qc` | Source function |

### Test result

| Field | Description |
|---|---|
| `test_result_id` | Unique result |
| `test_code` | Controlled method/test |
| `method_revision` | Version |
| `value` | Numeric/text result |
| `unit` | Explicit standardized unit |
| `lower_limit` / `upper_limit` | Applicable acceptance limits |
| `result_status` | pass/fail/conditional/not_applicable/unknown |
| `test_date` | Timestamp/date |
| `instrument_id` | If relevant |
| `analyst_role` | Minimized/pseudonymized |
| `report_reference` | Approved document/record link |
| `retest_of` | Previous result ID if applicable |
| `deviation_reference` | Approved deviation record |

## 10. Disposition and release

| Field | Description |
|---|---|
| `quality_status` | pending/hold/rework/retest/released/conditional/downgraded/rejected |
| `release_date` | Timestamp |
| `release_authority_role` | Role responsible |
| `release_basis` | Quality plan/test/deviation references |
| `nonconformance_id` | Link to NCR if applicable |
| `rework_actions` | Structured action list |
| `scrap_quantity` | Value + unit |
| `downgrade_reason` | Controlled reason |
| `capa_reference` | CAPA link |

## 11. Shipment and complaint outcome

| Field | Description |
|---|---|
| `shipment_id` | Delivery/shipment reference |
| `ship_date` | Date |
| `delivered_quantity` | Value + unit |
| `customer_id` | Restricted/pseudonymized |
| `complaint_id` | Link if complaint exists |
| `complaint_category` | Controlled category |
| `complaint_date` | Date |
| `customer_symptom` | Approved/minimized description |
| `investigation_status` | open/closed |
| `confirmed_cause` | Controlled cause/reference |
| `customer_action` | replacement/credit/information/none/etc. |
| `field_outcome` | accepted/repeat_order/complaint/unknown |

## 12. Provenance and data quality

Every field should support metadata:

```json
{
  "value": "example",
  "source_system": "INTEX",
  "source_record_id": "...",
  "source_timestamp": "2026-07-10T12:00:00+02:00",
  "ingested_at": "...",
  "transformation_version": "...",
  "quality_flag": "verified|inferred|manual|conflicting|missing",
  "confidence": 1.0
}
```

## 13. Passport views

### Executive view

- roll status;
- major quality risk;
- defects and cost impact;
- release/hold/rework;
- missing critical evidence.

### Quality view

- test results versus limits;
- defects by position and severity;
- deviations, NCR, rework, and release evidence;
- comparable historical cases.

### Production view

- recipe/version;
- process timeline;
- setpoint/actual deviations;
- defects mapped to roll position/time where feasible;
- operator observations and corrective actions.

### R&D view

- material/formulation/process context;
- relevant historical experiments;
- scale-up deviations;
- technical lessons and future experiment opportunities.

## 14. Minimum viable passport

The pilot MVP requires only:

- roll ID and source aliases;
- article/product family;
- production order;
- line and production time;
- available recipe/material references;
- inspection summary and defects;
- QC results and release status;
- rework/scrap status;
- source provenance and missing-data flags.

Do not delay the pilot waiting for every future field.