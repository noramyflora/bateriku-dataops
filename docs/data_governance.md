# Data Governance – Bateriku.com DataOps Engineering

**Course:** MCI1014 – Artificial Intelligence in Software Engineering

**Assignment:** Assignment 2 – DataOps Engineering

**Project:** AI-Assisted Battery Warranty Verification and Claim Management System for Bateriku.com

## 1. Purpose

This document defines the data governance principles for the Bateriku.com DataOps Engineering project, focusing on data quality, privacy, integrity, traceability, and reproducibility.

## 2. Data Classification

The project uses a synthetic battery warranty claims dataset for academic development and testing.

No actual customer names, contact details, identification numbers, or confidential warranty records should be included in the public GitHub repository.

## 3. Data Ownership and Responsibility

The project developer is responsible for maintaining the dataset, validating its structure, documenting changes, and ensuring that test data complies with the defined data contract.

## 4. Data Quality Management

Data quality is governed by the versioned data contract:

`contracts/warranty_claims_v1.json`

The validation process checks:

- Required fields and missing values.
- Duplicate claim identifiers.
- Invalid data types.
- Warranty duration and battery age constraints.
- Permitted inspection and claim statuses.

Invalid records must be rejected according to the data contract.

## 5. Data Privacy and Security

Only synthetic data is permitted in the public repository.

Real customer information must not be uploaded or included in screenshots, logs, test files, or documentation.

## 6. Data Lineage and Traceability

The data processing workflow is documented in:

`metadata/lineage.json`

The workflow follows:

Raw Synthetic Dataset → Data Validation → Validated Dataset → Automated Testing → Continuous Integration Verification

## 7. Dataset Versioning

Dataset metadata is maintained in:

`metadata/dataset_manifest.json`

The manifest records the dataset release identifier, schema version, source reference, row count, and checksum.

Changes to the dataset should be documented and verified before a new release is declared.

## 8. Reproducibility and Continuous Integration

The project uses Python 3, pytest, and GitHub Actions.

Automated testing helps verify that the data validation workflow continues to operate consistently following repository changes.

## 9. Human Oversight

Data validation supports the technical reliability of the proposed AI-assisted warranty claim system.

Final warranty decisions should remain subject to authorised human review and applicable business warranty policies.

## 10. Governance Review

Data governance documentation should be reviewed whenever the dataset structure, validation rules, processing workflow, or data contract changes.
