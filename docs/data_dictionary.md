
# Data Dictionary – Bateriku.com Warranty Claims

## 1. Overview

This document defines the fields, meanings, constraints, and validation rules for the synthetic battery warranty claims dataset used in Assignment 2 – MCI1014 DataOps Engineering.

Dataset: `data/raw/sample_input.csv`  
Data contract: `contracts/warranty_claims_v1.json`  
Schema version: `1.0.0`  
Data classification: Synthetic

## 2. Data Dictionary

| Field | Data Type | Required | Description | Constraints |
|---|---|---|---|---|
| claim_id | String | Yes | Unique identifier for each warranty claim | Non-null; unique |
| battery_brand | String | Yes | Brand of the battery involved in the claim | Non-null; minimum length 1 |
| warranty_months | Integer | Yes | Warranty coverage duration in months | Non-null; minimum 1 |
| battery_age_months | Integer | Yes | Battery age in months at the time of the claim | Non-null; minimum 0 |
| inspection_status | String | Yes | Status of battery inspection | Completed or Pending |
| claim_status | String | Yes | Recorded warranty claim outcome | Approved, Rejected, or Pending |

## 3. Validation Rules

- Every required field must be present and non-null.
- Claim IDs must be unique.
- Numeric fields must contain valid integers within their defined ranges.
- Inspection and claim statuses must use the allowed values in the data contract.
- Unexpected columns and invalid records must be rejected according to the data contract.

## 4. Target / Label Definition

`claim_status` is the recorded claim outcome and a potential target label for future AI analysis. It is not an automatically generated decision or proof that a claim was correctly approved or rejected.

## 5. Sensitive Data

The dataset is synthetic and intended for academic validation and testing. No customer names, telephone numbers, identification numbers, or other personal customer details should be included.

## 6. Data Quality and Limitations

Data quality checks must cover schema, completeness, uniqueness, validity, distribution or class balance, and a domain or ethics-related rule. The data dictionary defines the field-level rules; automated tests must independently demonstrate enforcement.

The synthetic sample does not establish real-world claim frequencies, model fairness, or production readiness.

## 7. Schema Change Control

Changes to field names, types, allowed values, or constraints must be reviewed, approved, versioned, and documented before adoption. Breaking changes require impact assessment and updated validation tests.
