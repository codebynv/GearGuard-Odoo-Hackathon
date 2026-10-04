# Testing Guide

## Core scenarios

- Equipment creation and identifier validation
- Maintenance request creation
- Valid and invalid workflow transitions
- Repair resolution requirements
- Preventive maintenance generation
- Dashboard metric accuracy

## Regression rule

When business logic changes, test both the successful path and at least one invalid input or transition.

## Demo preparation

Run the main workflow from equipment creation through repair and confirm the dashboard reflects the resulting state.
