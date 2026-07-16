#!/usr/bin/env python3
"""Validate synthetic Roll Quality Passport JSONL records.

The validator intentionally uses only the Python standard library so it can run
in restricted company environments. It is a prototype contract check, not a
replacement for approved production data validation or JSON Schema tooling.

Usage:
    python 06-prototype/src/validate_passports.py \
        06-prototype/synthetic_data/roll_quality_passports.jsonl
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = "0.1.0"
LINKAGE_LEVELS = {"A", "B", "C", "D"}
ROLL_TYPES = {"parent", "child", "standalone", "rework"}
SEVERITIES = {"S0", "S1", "S2", "S3", "S4"}
CAUSE_STATUSES = {"observed_only", "suspected", "supported", "confirmed"}
INSPECTION_DECISIONS = {"accepted", "rejected", "ignored", "reclassified", "review"}
TEST_STATUSES = {"pass", "fail", "retest", "not_applicable", "unknown"}
RELEASE_STATUSES = {
    "released",
    "held",
    "reworked",
    "scrapped",
    "conditionally_released",
    "unknown",
}
FINAL_DISPOSITIONS = {"ship", "hold", "rework", "scrap", "downgrade", "investigate", "unknown"}
KNOWN_DEFECT_CODES = {
    "COAT-THIN",
    "COAT-THICK",
    "COAT-UNEVEN",
    "COAT-PINHOLE",
    "COAT-FOAM",
    "COAT-STREAK",
    "COAT-BLOCKING",
    "ADH-DELAM",
    "ADH-LOW",
    "CURE-UNDER",
    "CURE-OVER",
    "LAM-WRINKLE",
    "LAM-BUBBLE",
    "LAM-MISALIGN",
    "DIM-WIDTH",
    "DIM-THICKNESS",
    "THERM-BRITTLE",
    "THERM-GLASSY",
    "WIND-TELESCOPE",
    "WIND-CREASE",
    "PACK-DAMAGE",
    "TRACE-LABEL",
    "UNK",
}


@dataclass
class ValidationResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)


class RecordValidationError(ValueError):
    """Raised when the JSONL input cannot be parsed as records."""


def _require_mapping(value: Any, path: str, result: ValidationResult) -> dict[str, Any]:
    if not isinstance(value, dict):
        result.error(f"{path}: expected object, got {type(value).__name__}")
        return {}
    return value


def _require_list(value: Any, path: str, result: ValidationResult) -> list[Any]:
    if not isinstance(value, list):
        result.error(f"{path}: expected array, got {type(value).__name__}")
        return []
    return value


def _require_string(value: Any, path: str, result: ValidationResult, *, allow_none: bool = False) -> str | None:
    if value is None and allow_none:
        return None
    if not isinstance(value, str) or not value.strip():
        result.error(f"{path}: expected non-empty string")
        return None
    return value


def _require_number(
    value: Any,
    path: str,
    result: ValidationResult,
    *,
    allow_none: bool = False,
    minimum: float | None = None,
    maximum: float | None = None,
) -> float | int | None:
    if value is None and allow_none:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        result.error(f"{path}: expected number")
        return None
    if minimum is not None and value < minimum:
        result.error(f"{path}: value {value} is below minimum {minimum}")
    if maximum is not None and value > maximum:
        result.error(f"{path}: value {value} is above maximum {maximum}")
    return value


def _parse_datetime(value: Any, path: str, result: ValidationResult, *, allow_none: bool = False) -> datetime | None:
    if value is None and allow_none:
        return None
    text = _require_string(value, path, result)
    if text is None:
        return None
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        result.error(f"{path}: invalid ISO-8601 datetime {text!r}")
        return None
    if parsed.tzinfo is None:
        result.error(f"{path}: timezone offset is required")
    return parsed


def _require_keys(mapping: dict[str, Any], keys: Iterable[str], path: str, result: ValidationResult) -> None:
    for key in keys:
        if key not in mapping:
            result.error(f"{path}: missing required key {key!r}")


def validate_record(record: Any, index: int) -> ValidationResult:
    result = ValidationResult()
    root = _require_mapping(record, f"record[{index}]", result)
    _require_keys(
        root,
        [
            "schema_version",
            "passport_id",
            "roll",
            "order_context",
            "production",
            "inspection",
            "quality",
            "disposition",
            "provenance",
        ],
        f"record[{index}]",
        result,
    )

    passport_id = _require_string(root.get("passport_id"), f"record[{index}].passport_id", result)
    prefix = passport_id or f"record[{index}]"

    if root.get("schema_version") != SCHEMA_VERSION:
        result.error(f"{prefix}: schema_version must be {SCHEMA_VERSION!r}")

    roll = _require_mapping(root.get("roll"), f"{prefix}.roll", result)
    _require_keys(roll, ["canonical_roll_id", "source_roll_ids", "roll_type"], f"{prefix}.roll", result)
    _require_string(roll.get("canonical_roll_id"), f"{prefix}.roll.canonical_roll_id", result)
    roll_type = roll.get("roll_type")
    if roll_type not in ROLL_TYPES:
        result.error(f"{prefix}.roll.roll_type: invalid value {roll_type!r}")
    parent_roll_id = roll.get("parent_roll_id")
    if roll_type == "child" and not isinstance(parent_roll_id, str):
        result.error(f"{prefix}.roll.parent_roll_id: child roll requires a parent roll ID")
    if roll_type != "child" and parent_roll_id not in (None, ""):
        result.warning(f"{prefix}.roll.parent_roll_id: set for non-child roll")
    _require_number(roll.get("length_m"), f"{prefix}.roll.length_m", result, allow_none=True, minimum=0)
    _require_number(roll.get("width_mm"), f"{prefix}.roll.width_mm", result, allow_none=True, minimum=0)

    source_ids = _require_list(roll.get("source_roll_ids"), f"{prefix}.roll.source_roll_ids", result)
    if not source_ids:
        result.error(f"{prefix}.roll.source_roll_ids: at least one source ID is required")
    seen_source_ids: set[tuple[str, str]] = set()
    for source_index, raw_source_id in enumerate(source_ids):
        source_id = _require_mapping(raw_source_id, f"{prefix}.roll.source_roll_ids[{source_index}]", result)
        source = _require_string(source_id.get("source"), f"{prefix}.roll.source_roll_ids[{source_index}].source", result)
        value = _require_string(source_id.get("value"), f"{prefix}.roll.source_roll_ids[{source_index}].value", result)
        if source and value:
            key = (source, value)
            if key in seen_source_ids:
                result.error(f"{prefix}.roll.source_roll_ids: duplicate source/value pair {key!r}")
            seen_source_ids.add(key)

    order_context = _require_mapping(root.get("order_context"), f"{prefix}.order_context", result)
    _require_keys(
        order_context,
        ["sales_order_id", "production_order_id", "article_id", "product_family"],
        f"{prefix}.order_context",
        result,
    )
    _require_string(order_context.get("article_id"), f"{prefix}.order_context.article_id", result)
    _require_string(order_context.get("product_family"), f"{prefix}.order_context.product_family", result)

    production = _require_mapping(root.get("production"), f"{prefix}.production", result)
    _require_keys(
        production,
        ["line_id", "started_at", "ended_at", "recipe_version", "parameters"],
        f"{prefix}.production",
        result,
    )
    _require_string(production.get("line_id"), f"{prefix}.production.line_id", result)
    started_at = _parse_datetime(production.get("started_at"), f"{prefix}.production.started_at", result)
    ended_at = _parse_datetime(production.get("ended_at"), f"{prefix}.production.ended_at", result)
    if started_at and ended_at and ended_at < started_at:
        result.error(f"{prefix}.production: ended_at precedes started_at")

    parameters = _require_list(production.get("parameters"), f"{prefix}.production.parameters", result)
    seen_parameters: set[tuple[str, str]] = set()
    for parameter_index, raw_parameter in enumerate(parameters):
        parameter = _require_mapping(raw_parameter, f"{prefix}.production.parameters[{parameter_index}]", result)
        name = _require_string(parameter.get("name"), f"{prefix}.production.parameters[{parameter_index}].name", result)
        value_kind = parameter.get("value_kind")
        if value_kind not in {"setpoint", "actual", "manual", "derived"}:
            result.error(f"{prefix}.production.parameters[{parameter_index}].value_kind: invalid value {value_kind!r}")
        if name and isinstance(value_kind, str):
            parameter_key = (name, value_kind)
            if parameter_key in seen_parameters:
                result.warning(f"{prefix}.production.parameters: duplicate name/value_kind {parameter_key!r}")
            seen_parameters.add(parameter_key)

    inspection = _require_mapping(root.get("inspection"), f"{prefix}.inspection", result)
    events = _require_list(inspection.get("events"), f"{prefix}.inspection.events", result)
    seen_event_ids: set[str] = set()
    for event_index, raw_event in enumerate(events):
        event = _require_mapping(raw_event, f"{prefix}.inspection.events[{event_index}]", result)
        _require_keys(
            event,
            ["event_id", "defect_code", "severity", "decision", "cause_status"],
            f"{prefix}.inspection.events[{event_index}]",
            result,
        )
        event_id = _require_string(event.get("event_id"), f"{prefix}.inspection.events[{event_index}].event_id", result)
        if event_id:
            if event_id in seen_event_ids:
                result.error(f"{prefix}.inspection.events: duplicate event ID {event_id!r}")
            seen_event_ids.add(event_id)
        defect_code = event.get("defect_code")
        if defect_code not in KNOWN_DEFECT_CODES:
            result.warning(f"{prefix}.inspection.events[{event_index}].defect_code: unknown draft taxonomy code {defect_code!r}")
        severity = event.get("severity")
        if severity not in SEVERITIES:
            result.error(f"{prefix}.inspection.events[{event_index}].severity: invalid value {severity!r}")
        decision = event.get("decision")
        if decision not in INSPECTION_DECISIONS:
            result.error(f"{prefix}.inspection.events[{event_index}].decision: invalid value {decision!r}")
        cause_status = event.get("cause_status")
        if cause_status not in CAUSE_STATUSES:
            result.error(f"{prefix}.inspection.events[{event_index}].cause_status: invalid value {cause_status!r}")
        suspected_cause = event.get("suspected_cause")
        if cause_status == "observed_only" and suspected_cause not in (None, ""):
            result.error(f"{prefix}.inspection.events[{event_index}]: observed_only must not assert a cause")
        if cause_status in {"supported", "confirmed"} and not isinstance(suspected_cause, str):
            result.error(f"{prefix}.inspection.events[{event_index}]: {cause_status} requires a cause statement")
        _require_number(event.get("position_m"), f"{prefix}.inspection.events[{event_index}].position_m", result, allow_none=True, minimum=0)
        _parse_datetime(event.get("recorded_at"), f"{prefix}.inspection.events[{event_index}].recorded_at", result, allow_none=True)

    quality = _require_mapping(root.get("quality"), f"{prefix}.quality", result)
    release_status = quality.get("release_status")
    if release_status not in RELEASE_STATUSES:
        result.error(f"{prefix}.quality.release_status: invalid value {release_status!r}")
    tests = _require_list(quality.get("tests"), f"{prefix}.quality.tests", result)
    seen_test_ids: set[str] = set()
    for test_index, raw_test in enumerate(tests):
        test = _require_mapping(raw_test, f"{prefix}.quality.tests[{test_index}]", result)
        test_id = _require_string(test.get("test_id"), f"{prefix}.quality.tests[{test_index}].test_id", result)
        if test_id:
            if test_id in seen_test_ids:
                result.error(f"{prefix}.quality.tests: duplicate test ID {test_id!r}")
            seen_test_ids.add(test_id)
        _require_string(test.get("method"), f"{prefix}.quality.tests[{test_index}].method", result)
        status = test.get("result_status")
        if status not in TEST_STATUSES:
            result.error(f"{prefix}.quality.tests[{test_index}].result_status: invalid value {status!r}")
        lower_limit = _require_number(test.get("lower_limit"), f"{prefix}.quality.tests[{test_index}].lower_limit", result, allow_none=True)
        upper_limit = _require_number(test.get("upper_limit"), f"{prefix}.quality.tests[{test_index}].upper_limit", result, allow_none=True)
        if lower_limit is not None and upper_limit is not None and lower_limit > upper_limit:
            result.error(f"{prefix}.quality.tests[{test_index}]: lower_limit exceeds upper_limit")
        _parse_datetime(test.get("tested_at"), f"{prefix}.quality.tests[{test_index}].tested_at", result, allow_none=True)

    disposition = _require_mapping(root.get("disposition"), f"{prefix}.disposition", result)
    final_disposition = disposition.get("final_disposition")
    if final_disposition not in FINAL_DISPOSITIONS:
        result.error(f"{prefix}.disposition.final_disposition: invalid value {final_disposition!r}")
    rework_quantity = _require_number(
        disposition.get("rework_quantity_m"),
        f"{prefix}.disposition.rework_quantity_m",
        result,
        allow_none=True,
        minimum=0,
    )
    scrap_quantity = _require_number(
        disposition.get("scrap_quantity_m"),
        f"{prefix}.disposition.scrap_quantity_m",
        result,
        allow_none=True,
        minimum=0,
    )
    length_m = roll.get("length_m")
    if isinstance(length_m, (int, float)):
        total_loss = sum(value for value in (rework_quantity, scrap_quantity) if isinstance(value, (int, float)))
        if total_loss > length_m:
            result.error(f"{prefix}.disposition: rework + scrap quantity exceeds roll length")

    if release_status == "released" and final_disposition not in {"ship", "downgrade"}:
        result.warning(f"{prefix}: released status is unusual with disposition {final_disposition!r}")
    if release_status == "held" and final_disposition == "ship":
        result.error(f"{prefix}: held roll cannot have final disposition 'ship'")
    if release_status == "scrapped" and final_disposition != "scrap":
        result.warning(f"{prefix}: scrapped release status should normally have scrap disposition")

    provenance = _require_mapping(root.get("provenance"), f"{prefix}.provenance", result)
    if provenance.get("synthetic") is not True:
        result.error(f"{prefix}.provenance.synthetic: prototype repository accepts synthetic records only")
    linkage_level = provenance.get("linkage_level")
    if linkage_level not in LINKAGE_LEVELS:
        result.error(f"{prefix}.provenance.linkage_level: invalid value {linkage_level!r}")
    confidence = _require_number(
        provenance.get("linkage_confidence"),
        f"{prefix}.provenance.linkage_confidence",
        result,
        minimum=0,
        maximum=1,
    )
    if linkage_level == "A" and isinstance(confidence, (int, float)) and confidence < 0.85:
        result.warning(f"{prefix}: Level A linkage has unexpectedly low confidence {confidence}")
    if linkage_level == "D" and isinstance(confidence, (int, float)) and confidence > 0.5:
        result.warning(f"{prefix}: Level D linkage has unexpectedly high confidence {confidence}")
    _parse_datetime(provenance.get("generated_at"), f"{prefix}.provenance.generated_at", result)
    source_systems = _require_list(provenance.get("source_systems"), f"{prefix}.provenance.source_systems", result)
    if not source_systems:
        result.error(f"{prefix}.provenance.source_systems: at least one source is required")

    return result


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise RecordValidationError(f"Input file does not exist: {path}")
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                value = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise RecordValidationError(
                    f"{path}:{line_number}: invalid JSON: {exc.msg} at column {exc.colno}"
                ) from exc
            if not isinstance(value, dict):
                raise RecordValidationError(f"{path}:{line_number}: each JSONL line must contain an object")
            records.append(value)
    if not records:
        raise RecordValidationError(f"Input file contains no records: {path}")
    return records


def validate_dataset(records: list[dict[str, Any]]) -> ValidationResult:
    combined = ValidationResult()
    passport_ids: set[str] = set()
    roll_ids: set[str] = set()
    all_roll_ids: set[str] = {
        record.get("roll", {}).get("canonical_roll_id")
        for record in records
        if isinstance(record.get("roll"), dict)
        and isinstance(record.get("roll", {}).get("canonical_roll_id"), str)
    }

    for index, record in enumerate(records, start=1):
        record_result = validate_record(record, index)
        combined.errors.extend(record_result.errors)
        combined.warnings.extend(record_result.warnings)

        passport_id = record.get("passport_id")
        if isinstance(passport_id, str):
            if passport_id in passport_ids:
                combined.error(f"dataset: duplicate passport_id {passport_id!r}")
            passport_ids.add(passport_id)

        roll = record.get("roll")
        if isinstance(roll, dict):
            roll_id = roll.get("canonical_roll_id")
            if isinstance(roll_id, str):
                if roll_id in roll_ids:
                    combined.error(f"dataset: duplicate canonical_roll_id {roll_id!r}")
                roll_ids.add(roll_id)
            if roll.get("roll_type") == "child":
                parent_roll_id = roll.get("parent_roll_id")
                if isinstance(parent_roll_id, str) and parent_roll_id not in all_roll_ids:
                    combined.warning(
                        f"dataset: child roll {roll_id!r} references parent {parent_roll_id!r} not present in this sample"
                    )

    return combined


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Path to the JSONL passport file")
    parser.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="Return a failing exit code when warnings are present",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        records = load_jsonl(args.input)
    except RecordValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    result = validate_dataset(records)

    print(f"Validated {len(records)} synthetic Roll Quality Passport record(s).")
    print(f"Errors: {len(result.errors)}")
    print(f"Warnings: {len(result.warnings)}")

    for message in result.errors:
        print(f"ERROR: {message}")
    for message in result.warnings:
        print(f"WARNING: {message}")

    if result.errors:
        return 1
    if args.warnings_as_errors and result.warnings:
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
