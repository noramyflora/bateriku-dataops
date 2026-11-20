
import csv
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/raw/sample_input.csv"
CONTRACT = ROOT / "contracts/warranty_claims_v1.json"
SCRIPT = ROOT / "src/validate_data.py"


@pytest.fixture
def test_project(tmp_path):
    """Create an isolated copy of the project for testing."""
    for folder in ["data/raw", "contracts", "src"]:
        (tmp_path / folder).mkdir(parents=True, exist_ok=True)

    shutil.copy(CONTRACT, tmp_path / "contracts")
    shutil.copy(SCRIPT, tmp_path / "src")

    return tmp_path


def prepare_data(project, change=None):
    with SOURCE.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames
        rows = list(reader)

    if change:
        change(rows)

    destination = project / "data/raw/sample_input.csv"

    with destination.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def run_validation(project):
    return subprocess.run(
        [sys.executable, str(project / "src/validate_data.py")],
        cwd=project,
        capture_output=True,
        text=True
    )


def test_valid_dataset(test_project):
    prepare_data(test_project)
    result = run_validation(test_project)

    assert result.returncode == 0
    assert "DATA VALIDATION PASSED" in result.stdout
    assert (
        test_project / "data/processed/validated_claims.csv"
    ).exists()


@pytest.mark.parametrize(
    "change,expected_error",
    [
        (
            lambda rows: rows[0].update({"claim_id": ""}),
            "missing claim_id"
        ),
        (
            lambda rows: rows[1].update(
                {"claim_id": rows[0]["claim_id"]}
            ),
            "duplicate claim_id"
        ),
        (
            lambda rows: rows[0].update(
                {"warranty_months": "-5"}
            ),
            "invalid range for warranty_months"
        ),
    ]
)
def test_invalid_dataset(
    test_project, change, expected_error
):
    prepare_data(test_project, change)
    result = run_validation(test_project)

    assert result.returncode != 0
    assert "DATA VALIDATION FAILED" in result.stdout
    assert expected_error in result.stdout
