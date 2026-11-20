
# DataOps Change Record – Bateriku.com

## 1. Project Information

Project: AI-Assisted Battery Warranty Verification and Claim Management System for Bateriku.com

Course: MCI1014 – Artificial Intelligence in Software Engineering

Repository: bateriku-dataops

Dataset Type: Synthetic Warranty Claims

Baseline Dataset Version: v1.0.0

## 2. Purpose

This document records changes to the DataOps workflow, dataset, data contract, validation rules and supporting documentation.

It supports change control, reproducibility, impact analysis and traceability.

## 3. Baseline Configuration

The initial DataOps baseline includes:

- Synthetic warranty claims dataset
- Versioned data contract
- Data ingestion and validation script
- Automated data quality tests
- GitHub Actions CI workflow
- Dataset manifest
- Data lineage documentation
- Data governance documentation

The baseline must be verified using a recorded commit or release tag before a reviewed change is claimed.

## 4. Change Log

| Change ID | Description | Affected Component | Status |
|---|---|---|---|
| CR-001 | Establish initial synthetic dataset | data/raw/sample_input.csv | Implemented |
| CR-002 | Introduce versioned data contract | contracts/warranty_claims_v1.json | Implemented |
| CR-003 | Add data validation script | src/validate_data.py | Implemented |
| CR-004 | Add automated data quality testing | tests/ | Implemented |
| CR-005 | Integrate GitHub Actions CI | .github/workflows/ | Implemented |
| CR-006 | Document dataset manifest and lineage | metadata/ | Implemented |
| CR-007 | Add governance and reproducibility documentation | docs/ | Implemented |

## 5. Proposed Controlled Change

Change ID: CR-008

Change Title: Extend Data Quality Coverage

Change Type: Validation and testing improvement

Proposed Change:
Introduce additional automated tests to cover distribution or class balance and domain or ethics-related validation.

Reason:
Improve alignment with the six required data quality dimensions in Assignment 2.

Affected Components:
- tests/
- src/validate_data.py (if necessary)
- README.md
- evidence/

Expected Impact:
- Improved data quality coverage
- Stronger automated verification
- Better traceability of validation requirements

Status: Proposed – not yet implemented or approved.

## 6. Impact Analysis

The proposed change should be assessed for:

1. Compatibility with the existing data contract.
2. Effects on valid and invalid input records.
3. Changes to automated test outcomes.
4. Effects on CI execution.
5. Updates required to documentation and evidence.

## 7. Verification and Approval

Before closing CR-008:

- Implement the additional tests.
- Execute the complete test suite.
- Verify the GitHub Actions result.
- Record the baseline and updated commit IDs.
- Document test results and any failures.
- Record reviewer approval or academic self-review.

## 8. Traceability

Each implemented change should be linked to:

- The relevant assignment requirement
- The affected repository file
- The corresponding automated test
- The GitHub commit
- The supporting evidence

## 9. Change Control Statement

A proposed change is not considered completed until implementation, verification and documentation are recorded.

This document must be updated when new changes are introduced.
