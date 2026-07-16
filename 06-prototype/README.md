# Roll Quality Passport Synthetic Prototype

This workspace now contains the first implementation artifact for the Darm AI Transformation Program: a machine-readable, synthetic-only Roll Quality Passport contract with validation code and tests.

The prototype proves structure and engineering discipline before any real company export is used.

## Current contents

```text
06-prototype/
├── README.md
├── schemas/
│   └── roll_quality_passport.schema.json
├── synthetic_data/
│   └── roll_quality_passports.jsonl
├── src/
│   └── validate_passports.py
└── tests/
    └── test_validate_passports.py
```

## Purpose

The prototype tests whether the proposed passport can represent:

- canonical and source roll identifiers;
- parent/child rolls;
- order and article context;
- materials and supplier lots;
- production times and parameters;
- ELSIS-style inspection events;
- controlled defect codes;
- severity, operator/system decisions, and cause confidence;
- QC/lab tests and release status;
- rework, scrap, shipment, and complaint disposition;
- source provenance, linkage level, missing domains, and confidence.

It is deliberately synthetic. Real INTEX, ELSIS, production, QC, formulation, customer, complaint, or employee records must not be added to this repository.

## Run validation

From the repository root:

```bash
python 06-prototype/src/validate_passports.py \
  06-prototype/synthetic_data/roll_quality_passports.jsonl
```

Expected core result:

```text
Validated 4 synthetic Roll Quality Passport record(s).
Errors: 0
Validation passed.
```

Warnings may be present for intentionally incomplete synthetic examples, such as a child roll whose parent record is outside the sample.

Treat warnings as failures:

```bash
python 06-prototype/src/validate_passports.py \
  06-prototype/synthetic_data/roll_quality_passports.jsonl \
  --warnings-as-errors
```

## Run tests

```bash
python -m unittest discover -s 06-prototype/tests -p 'test_*.py' -v
```

The tests cover:

- the bundled synthetic dataset;
- duplicate passport IDs;
- rejection of non-synthetic records;
- invalid held/ship combinations;
- unsupported cause assertions;
- malformed JSONL;
- missing parent IDs for child rolls.

## Validation scope

The standard-library validator checks:

- required sections;
- schema version;
- critical data types;
- enumerations;
- timezone-aware timestamps;
- production start/end order;
- duplicate passport, roll, event, test, and source IDs;
- parent/child rules;
- defect cause-status discipline;
- release/disposition consistency;
- quantity plausibility;
- synthetic-only provenance;
- linkage level and confidence.

The JSON Schema provides a machine-readable contract for later integration with approved tooling.

## Engineering quality rules

- Python code must be typed, documented, and tested.
- Use deterministic transformations where possible.
- Preserve source values and provenance.
- Never silently coerce invalid values.
- Validate units and controlled codes.
- Track data and transformation versions.
- Keep notebooks exploratory; move stable logic into `src/`.
- Every KPI must have a tested definition.
- Every model must beat a documented baseline and include error analysis.
- Every technical retrieval answer must retain source references.

## Data policy

### Allowed in GitHub

- schemas;
- synthetic or irreversibly anonymized examples approved for repository use;
- code and tests;
- empty configuration templates;
- non-sensitive metadata examples;
- documentation and architecture decisions.

### Not allowed in GitHub

- real ERP or INTEX exports;
- real ELSIS inspection images or event files;
- customer-identifiable data;
- employee emails or performance information;
- formulations, recipe percentages, or confidential process windows;
- supplier pricing;
- credentials, tokens, keys, passwords, certificates, or connection strings;
- unredacted complaints or quality records;
- local databases or model artifacts created from company data.

## What changes after discovery

The contract must be updated only through a reviewed version change after source owners validate real structures. Expected discovery-driven changes include:

- real INTEX field mapping;
- real ELSIS event and image metadata;
- actual parent/child roll logic;
- QC test and unit dictionaries;
- production parameter names and frequencies;
- approved defect taxonomy v1.0;
- customer and employee minimization rules;
- source-specific lineage and extraction metadata.

## Definition of done for the first prototype

The first prototype is complete when a synthetic or approved sample roll can be validated and displayed with:

- order and product context;
- roll identity and aliases;
- production context;
- inspection summary and controlled defect codes;
- QC/test results;
- release/rework status;
- source provenance;
- missing-data flags;
- reproducible tests.

The first prototype does not require machine learning.
