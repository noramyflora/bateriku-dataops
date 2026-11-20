
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/raw/sample_input.csv"
CONTRACT = ROOT / "contracts/warranty_claims_v1.json"
OUTPUT = ROOT / "data/processed/validated_claims.csv"


def validate():
    with CONTRACT.open(encoding="utf-8") as file:
        contract = json.load(file)

    with SOURCE.open(newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        expected = contract["required_columns"]

        if reader.fieldnames != expected:
            raise ValueError("CSV columns do not match contract")

        records = list(reader)

    seen_ids = set()
    errors = []

    for line, record in enumerate(records, start=2):
        for field, rules in contract["fields"].items():
            value = record[field].strip()

            if not value:
                if not rules.get("nullable", True):
                    errors.append(f"Line {line}: missing {field}")
                continue

            if rules["type"] == "integer":
                try:
                    number = int(value)
                    if number < rules.get("minimum", number):
                        errors.append(
                            f"Line {line}: invalid range for {field}"
                        )
                except ValueError:
                    errors.append(
                        f"Line {line}: invalid integer for {field}"
                    )

            if "min_length" in rules:
                if len(value) < rules["min_length"]:
                    errors.append(
                        f"Line {line}: {field} is too short"
                    )

            if "allowed_values" in rules:
                if value not in rules["allowed_values"]:
                    errors.append(
                        f"Line {line}: invalid {field}: {value}"
                    )

        claim_id = record["claim_id"].strip()
        if claim_id:
            if claim_id in seen_ids:
                errors.append(
                    f"Line {line}: duplicate claim_id {claim_id}"
                )
            seen_ids.add(claim_id)

    if errors:
        print("DATA VALIDATION FAILED")
        for error in errors:
            print(error)
        return 1

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=contract["required_columns"]
        )
        writer.writeheader()
        for record in records:
            writer.writerow({
                key: value.strip()
                for key, value in record.items()
            })

    print("DATA VALIDATION PASSED")
    print(f"Records validated: {len(records)}")
    print(f"Output: {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(validate())
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"DATA VALIDATION FAILED: {exc}")
        sys.exit(1)
