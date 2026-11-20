# Reproducibility Guide – Bateriku.com DataOps Engineering

**Course:** MCI1014 – Artificial Intelligence in Software Engineering

**Assignment:** Assignment 2 – DataOps Engineering

**Project:** AI-Assisted Battery Warranty Verification and Claim Management System for Bateriku.com

## 1. Purpose

This document provides instructions for reproducing the DataOps validation and automated testing workflow for the Bateriku.com synthetic battery warranty claims dataset.

## 2. Execution Environment

The project uses the following technologies:

- Python 3
- GitHub repository
- Google Colab
- pytest
- GitHub Actions

## 3. Repository Setup

Clone the repository:

```bash
git clone https://github.com/noramyflora/bateriku-dataops.git
```

Navigate to the project directory:

```bash
cd bateriku-dataops
```

Install the testing framework if it is not available:

```bash
python -m pip install pytest
```

## 4. Dataset and Data Contract

The project uses a synthetic battery warranty claims dataset.

**Input dataset:**

`data/raw/sample_input.csv`

**Data contract:**

`contracts/warranty_claims_v1.json`

**Dataset manifest:**

`metadata/dataset_manifest.json`

**Data lineage:**

`metadata/lineage.json`

The dataset is intended for academic validation and testing rather than real customer warranty processing.

## 5. Execute Data Validation

From the repository root directory, run:

```bash
python src/validate_data.py
```

The validation script is intended to check the dataset against the defined data quality rules.

The documented processed dataset location is:

`data/processed/validated_claims.csv`

Confirm the actual output after execution.

## 6. Execute Automated Tests

Run the following command from the repository root:

```bash
python -m pytest -v
```

The previously recorded verification evidence reported:

**4 tests passed.**

The result should be reproduced in the current environment before submission.

## 7. Continuous Integration Verification

The project uses GitHub Actions for automated data quality verification.

Workflow configuration:

`.github/workflows/data-quality.yml`

Verification procedure:

1. Open the GitHub repository.
2. Select the Actions tab.
3. Open the Data Quality CI workflow.
4. Select the latest workflow run.
5. Confirm that all required jobs completed successfully.

A successful workflow run provides evidence that the automated checks passed for the corresponding repository revision.

## 8. Dataset Versioning and Integrity

Dataset versioning information is maintained in:

`metadata/dataset_manifest.json`

The manifest includes:

- Dataset release identifier
- Schema version
- Source dataset reference
- Row count
- SHA-256 checksum

The checksum can be recalculated to verify that the dataset contents match the documented release.

## 9. Evidence

Execution and verification screenshots are stored in:

`evidence/`

Evidence includes data validation, automated testing, negative testing, and GitHub Actions workflow results.

## 10. Reproducibility Limitations

The project uses synthetic data for academic testing.

The current workflow demonstrates data validation and automated testing. It does not establish the accuracy of an AI model for real-world warranty claim decisions.

Any future production deployment would require additional security, data governance, operational testing, and human oversight.
