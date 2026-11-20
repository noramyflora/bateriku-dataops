
# Data Card – Bateriku.com Synthetic Warranty Claims

## 1. Dataset Overview

Dataset Name: Bateriku Synthetic Warranty Claims

Project: AI-Assisted Battery Warranty Verification and Claim Management System for Bateriku.com

Course: MCI1014 – Artificial Intelligence in Software Engineering

Dataset Version: v1.0.0

Data Type: Synthetic

Source File: data/raw/sample_input.csv

## 2. Dataset Purpose

The dataset supports the development and evaluation of a reproducible DataOps workflow for battery warranty claim records.

The main purposes are:
- Validate warranty claim data quality.
- Detect incomplete and duplicate records.
- Identify invalid warranty and inspection values.
- Support automated testing and continuous integration.
- Provide structured data for future AI research.

## 3. Dataset Description

The dataset contains six synthetic battery warranty claim records.

The dataset includes six fields:

1. claim_id
2. battery_brand
3. warranty_months
4. battery_age_months
5. inspection_status
6. claim_status

Field definitions and constraints are documented in docs/data_dictionary.md.

## 4. Data Collection and Origin

The dataset is synthetically constructed for academic testing.

It does not contain actual customer warranty claims.

No real customer personal information is included.

## 5. Intended Uses

The dataset is intended for:
- Academic DataOps experimentation.
- Data contract validation.
- Automated data quality testing.
- Reproducibility demonstrations.
- CI pipeline verification.

## 6. Limitations

The dataset contains only six synthetic records.

Therefore:
- It is not representative of real-world claim distributions.
- It is insufficient for reliable AI model training.
- It cannot establish production-level model accuracy.
- It cannot demonstrate real-world fairness.
- It must not be used to make actual warranty decisions.

## 7. Ethical Considerations

The dataset excludes customer names, telephone numbers, identification numbers and other personal information.

Synthetic data is used to reduce privacy risks.

Any future use of real operational data would require appropriate authorization, access controls and privacy safeguards.

AI-generated recommendations must remain subject to human review.

## 8. Data Quality

The DataOps workflow is intended to evaluate:

- Schema compliance
- Completeness
- Uniqueness
- Validity
- Distribution or class balance
- Domain and ethical constraints

Automated test results and supporting evidence are maintained separately.

## 9. Dataset Versioning and Traceability

The dataset is associated with:

- contracts/warranty_claims_v1.json
- metadata/dataset_manifest.json
- metadata/lineage.json

Dataset modifications should be documented and reviewed before release.

## 10. Responsible Use

This dataset is intended exclusively for academic research, demonstration and software engineering experimentation.

It must not be treated as verified operational evidence or used for automated approval or rejection of real customer warranty claims.
