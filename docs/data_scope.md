# Data Scope and Requirements

## 1. Project Overview

**Project Title:** AI-Assisted Battery Warranty Verification and Claim Management System for Bateriku.com

**Course:** MCI1014 – Artificial Intelligence in Software Engineering

**Assignment:** Assignment 2 – DataOps Engineering

The project aims to establish a controlled, reproducible and reliable data foundation for an AI-assisted battery warranty verification and claim management system.

The proposed system supports administrative staff and technicians in reviewing battery warranty claims by providing structured data for warranty verification and claim assessment.

## 2. Data Purpose

The dataset is intended to support the following activities:

1. Verify battery warranty information.
2. Identify incomplete or invalid warranty claim records.
3. Support consistent assessment of warranty claims.
4. Prepare structured data for future AI-assisted decision support.
5. Evaluate data quality before the information is used by the proposed system.

## 3. Data Source

The initial dataset is a synthetic sample created specifically for academic purposes.

The sample represents hypothetical battery warranty claims and does not contain actual customer records.

**Source identifier:** `synthetic-battery-warranty-v1`

**Source file:** `data/raw/sample_input.csv`

**Data classification:** Synthetic, non-confidential data.

## 4. Data Ownership and Permitted Use

**Proposed accountable owner:** Bateriku.com operations management, subject to organizational confirmation.

**Academic dataset custodian:** Student researcher.

**Permitted use:** Academic development, testing, data validation, preprocessing and evaluation of the proposed DataOps pipeline.

**Prohibited use:** Making real customer warranty decisions or representing synthetic records as actual operational data.

## 5. Data Consumers

The intended consumers include:

- Administrative staff reviewing warranty claim information.
- Battery technicians providing inspection results.
- The proposed AI-assisted warranty verification system.
- The student researcher responsible for developing and validating the DataOps pipeline.

## 6. Initial Required Fields

| Field | Description |
|---|---|
| claim_id | Unique identifier for each warranty claim |
| battery_brand | Brand of the battery |
| warranty_months | Warranty duration in months |
| battery_age_months | Battery age in months at the time of claim |
| inspection_status | Status of the battery inspection |
| claim_status | Recorded warranty claim status |

The exact data types, allowed values, missing-value rules and uniqueness constraints will be specified in the versioned data contract.

## 7. Target or Label Definition

The initial target field is `claim_status`, with three possible values:

- Approved
- Rejected
- Pending

For the initial dataset, these values are illustrative labels rather than verified warranty outcomes.

A future AI model would require a clearly defined and validated decision policy, together with appropriately reviewed training labels.

## 8. Assumptions and Limitations

- The dataset contains synthetic records.
- The sample does not represent actual warranty claim frequencies.
- Battery age and warranty duration alone are insufficient to determine claim eligibility.
- Final warranty decisions may depend on purchase verification, inspection findings and applicable warranty terms.
- The initial sample is intended to test data-processing functionality, not AI prediction accuracy.

## 9. Relationship to Assignment 1

The DataOps package supports the data completeness, validation and traceability needs identified in Assignment 1.

At least two exact requirement or risk identifiers from the Assignment 1 repository must be inserted and linked to the relevant data contract rules and tests.

**Status:** Pending verification of Assignment 1 requirement and risk identifiers.

## 10. Expected Outcome

The expected outcome is a documented and reproducible data foundation that enables an engineer to identify the source dataset, validate its structure, process it consistently and trace changes between dataset versions.
