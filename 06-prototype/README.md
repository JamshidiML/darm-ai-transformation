# Prototype Workspace

This directory is reserved for implementation code, tests, schemas, synthetic data, and reproducible analytical prototypes for the Darm AI Transformation Program.

## Current status

No production code or real company data has been added. The first technical work begins after the two-week discovery sprint confirms approved sources, identifiers, architecture, and pilot scope.

## Planned structure

```text
06-prototype/
├── README.md
├── pyproject.toml              # add when implementation starts
├── src/
│   ├── ingestion/
│   ├── validation/
│   ├── identity_linkage/
│   ├── taxonomy/
│   ├── roll_passport/
│   ├── analytics/
│   ├── retrieval/
│   └── app/
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── data_quality/
│   └── evaluation/
├── schemas/
│   ├── data_contracts/
│   ├── roll_passport/
│   └── taxonomy/
├── synthetic_data/
├── notebooks/
└── docs/
```

## Technical priorities after discovery

1. Create machine-readable data contracts for approved sample exports.
2. Build schema and data-quality validation.
3. Implement canonical identifier mapping and linkage metrics.
4. Create a synthetic roll-passport dataset that mirrors structure but contains no real company information.
5. Build defect Pareto and recurrence analysis.
6. Build the first roll-quality passport API/view.
7. Add provenance and missing-data indicators.
8. Add tests for leakage, schema changes, unit conversion, and identifier ambiguity.
9. Add document retrieval only after the approved corpus and access controls are defined.
10. Add predictive modeling only when data quality, target definition, and evaluation design support it.

## Data policy

### Allowed in GitHub

- schemas;
- synthetic or irreversibly anonymized examples approved for repository use;
- code and tests;
- empty configuration templates;
- non-sensitive metadata examples;
- documentation and architecture decisions.

### Not allowed in GitHub

- real ERP exports;
- real ELSIS inspection images or event files;
- customer-identifiable data;
- employee emails or performance information;
- formulations, recipe percentages, confidential process windows;
- supplier pricing;
- credentials, tokens, keys, passwords, certificates, or connection strings;
- unredacted complaints or quality records.

## Engineering quality rules

- Python code should be typed, documented, and tested.
- Use deterministic transformations where possible.
- Preserve source values and provenance.
- Never silently coerce invalid values.
- Validate units and controlled codes.
- Track data and transformation versions.
- Keep notebooks exploratory; move stable logic into `src/`.
- Every KPI must have a tested definition.
- Every model must beat a documented baseline and include error analysis.
- Every technical retrieval answer must retain source references.

## Definition of done for the first prototype

The first prototype is complete when a synthetic or approved sample roll can be displayed with:

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