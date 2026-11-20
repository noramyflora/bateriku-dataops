# Bateriku.com DataOps Engineering

**Assignment 2 – MCI1014 Artificial Intelligence in Software Engineering**

**Project:** AI-Assisted Battery Warranty Verification and Claim Management System for Bateriku.com

## 1. Project Overview

This repository implements a DataOps engineering workflow to support the development of an AI-assisted battery warranty verification and claim management system for Bateriku.com.

The project focuses on data quality, reproducibility, automated validation, and continuous integration (CI).

The implementation uses a synthetic battery warranty claims dataset for academic testing.

## 2. Project Objectives

The objectives of this DataOps implementation are to:

1. Establish a structured and reproducible data processing workflow.
2. Validate battery warranty claim records before further processing.
3. Detect missing, duplicate, and invalid data.
4. Implement automated data quality tests using pytest.
5. Integrate automated testing with GitHub Actions.
6. Maintain documentation, traceability, and verification evidence.

## 3. Repository Structure

The repository contains the following components:

- `.github/workflows/data-quality.yml` – Automated continuous integration workflow.
- `contracts/` – Data contracts defining expected dataset requirements.
- `data/` – Raw and processed warranty claims data.
- `docs/data_scope.md` – Data scope, assumptions, limitations, and traceability documentation.
- `src/validate_data.py` – Python script for validating warranty claim records.
- `tests/test_data_quality.py` – Automated data quality tests.
- `evidence/` – Screenshots documenting validation and testing results.
- `README.md` – Project overview and reproducibility instructions.

## 4. Dataset Description

The project uses six synthetic battery warranty claim records.

The dataset includes the following fields:

- `claim_id`
- `battery_brand`
- `warranty_months`
- `battery_age_months`
- `inspection_status`
- `claim_status`

Synthetic data is used to demonstrate the validation workflow without exposing confidential customer information.

## 5. Data Validation

The Python validation script checks the dataset for:

- Missing claim identifiers.
- Duplicate claim identifiers.
- Invalid warranty duration values.
- Compliance with the implemented data quality rules.

The validation process successfully processed six synthetic warranty claim records.

**Validation result:** PASSED

**Output:** `data/processed/validated_claims.csv`

## 6. Reproducibility Instructions

The repository can be executed in Google Colab or a compatible Python environment.

### Step 1: Clone the repository

```bash
git clone https://github.com/noramyflora/bateriku-dataops.git
cd bateriku-dataops
```

### Step 2: Install pytest

```bash
python -m pip install pytest
```

### Step 3: Run data validation

```bash
python src/validate_data.py
```

### Step 4: Run automated tests

```bash
python -m pytest tests/test_data_quality.py -v
```

These commands assume the required input dataset and data contract files are present in their expected repository locations.

## 7. Automated Data Quality Testing

Six automated data quality tests were implemented using pytest to verify the reliability and integrity of the synthetic battery warranty claims dataset.

The automated tests include:

1. Valid dataset verification.
2. Missing claim ID detection.
3. Duplicate claim ID detection.
4. Invalid warranty duration detection.
5. Claim status distribution validation.
6. Approved claim within warranty validation.

**Test Result: 6 PASSED**

All six automated tests were successfully executed through GitHub Actions CI.

The tests demonstrate that the implemented DataOps workflow can detect selected data quality issues and validate predefined warranty-related business rules.

## 8. Continuous Integration

GitHub Actions is configured to execute the Data Quality CI workflow.

The workflow includes:

1. Repository checkout.
2. Python environment setup.
3. pytest installation.
4. Dataset validation.
5. Automated data quality testing.

The workflow is defined in:

`.github/workflows/data-quality.yml`

**Observed CI execution status: SUCCESS**

The successful workflow demonstrates that the implemented validation and testing steps can run in an automated environment.

## 9. Requirements Traceability and Risk Management

Assignment 2 extends the requirements and risk management activities established in Assignment 1.

The relationship between the assignments is documented in:

`docs/data_scope.md`

The DataOps implementation addresses data quality requirements including required claim information, missing identifiers, duplicate records, and preliminary warranty duration validation.

Risk mitigation activities include the use of synthetic data, automated validation, and CI testing.

## 10. Verification Evidence

Execution evidence is stored in the `evidence/` directory.

The evidence includes:

- `data-validation-success.png`
- `validated-dataset-output.png`
- `data-quality-negative-tests.png`
- `automated-pytest-results.png`
- `github-actions-test-results1.png`
- `github-actions-data-quality-success1.png`

Additional screenshots are retained in the same directory.

## 11. Data Governance and Limitations

This implementation uses synthetic records for academic demonstration.

No confidential or personal customer information should be committed to the repository.

The current validation workflow verifies selected data quality requirements. It does not establish the accuracy of AI predictions or determine actual customer warranty eligibility.

Final warranty decisions may require purchase verification, technician inspection findings, applicable warranty terms, and human review.

## 12. Implementation Status

The following activities have been completed and demonstrated:

- Synthetic warranty claims dataset preparation.
- Python-based data validation.
- Validation of six synthetic records.
- Automated data quality testing.
- Six successful pytest test cases, including distribution and warranty domain quality tests.
- Successful GitHub Actions CI execution.
- Requirements and risk traceability documentation.
- Collection of execution evidence.

**Overall status: Implemented and verified for the demonstrated DataOps scope.**
