from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from types import ModuleType


REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "06-prototype" / "src" / "validate_passports.py"
SYNTHETIC_DATA_PATH = REPO_ROOT / "06-prototype" / "synthetic_data" / "roll_quality_passports.jsonl"


def load_validator_module() -> ModuleType:
    spec = importlib.util.spec_from_file_location("validate_passports", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load validator module from {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load_validator_module()


class PassportValidatorTests(unittest.TestCase):
    def test_synthetic_dataset_has_no_errors(self) -> None:
        records = validator.load_jsonl(SYNTHETIC_DATA_PATH)
        result = validator.validate_dataset(records)
        self.assertEqual([], result.errors)

    def test_duplicate_passport_id_is_rejected(self) -> None:
        records = validator.load_jsonl(SYNTHETIC_DATA_PATH)
        duplicate = json.loads(json.dumps(records[0]))
        duplicate["roll"]["canonical_roll_id"] = "ROLL-SYN-DUPLICATE"
        records.append(duplicate)
        result = validator.validate_dataset(records)
        self.assertTrue(any("duplicate passport_id" in error for error in result.errors))

    def test_non_synthetic_record_is_rejected(self) -> None:
        records = validator.load_jsonl(SYNTHETIC_DATA_PATH)
        record = json.loads(json.dumps(records[0]))
        record["provenance"]["synthetic"] = False
        result = validator.validate_dataset([record])
        self.assertTrue(any("accepts synthetic records only" in error for error in result.errors))

    def test_held_roll_cannot_ship(self) -> None:
        records = validator.load_jsonl(SYNTHETIC_DATA_PATH)
        record = json.loads(json.dumps(records[0]))
        record["quality"]["release_status"] = "held"
        record["disposition"]["final_disposition"] = "ship"
        result = validator.validate_dataset([record])
        self.assertTrue(any("held roll cannot" in error for error in result.errors))

    def test_observed_only_event_cannot_assert_cause(self) -> None:
        records = validator.load_jsonl(SYNTHETIC_DATA_PATH)
        record = json.loads(json.dumps(records[1]))
        record["inspection"]["events"][1]["suspected_cause"] = "Unsupported cause assertion"
        result = validator.validate_dataset([record])
        self.assertTrue(any("observed_only must not assert a cause" in error for error in result.errors))

    def test_invalid_jsonl_returns_parse_error(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "invalid.jsonl"
            path.write_text("{not valid json}\n", encoding="utf-8")
            with self.assertRaises(validator.RecordValidationError):
                validator.load_jsonl(path)

    def test_child_without_parent_is_rejected(self) -> None:
        records = validator.load_jsonl(SYNTHETIC_DATA_PATH)
        record = json.loads(json.dumps(records[2]))
        record["roll"]["parent_roll_id"] = None
        result = validator.validate_dataset([record])
        self.assertTrue(any("child roll requires a parent" in error for error in result.errors))


if __name__ == "__main__":
    unittest.main()
