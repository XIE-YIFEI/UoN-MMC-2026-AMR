# UoN-MMC-2026-AMR
# UoN MMC 2026: Antimicrobial Resistance Dynamics in a Hospital Network

## Researcher
* Xie Yifei (Nottingham ID: 20796507)

## Project Overview
This repository contains the mathematical modeling and simulation code for the 2026 University of Nottingham Mathematical Modeling Competition. This project models the transmission dynamics of antimicrobial-resistant (AMR) bacteria across a two-ward hospital network: the Intensive Care Unit (ICU) and General Medicine, using deterministic compartmental models.

## Compartmental Model Definitions
For each ward $i \in \{1, 2\}$ (where 1 = ICU, 2 = General Medicine):

### Patient Compartments
* `PU_i`: Uncolonized / Susceptible patients
* `PN_i`: Patients colonized with non-resistant bacteria
* `PR_i`: Patients colonized with AMR bacteria

### Key Parameters
* `\lambda_i`: Daily admission rate
* `\delta_i`: Daily discharge rate
* `\tau_i`: Antibiotic prescribing rate (Selection pressure)
* `\beta_i`: Transmission rate (inversely related to hand hygiene compliance)
* `\gamma`: Natural bacterial clearance rate
* `\nu_{1 \to 2}`: Transfer rate from ICU to General Medicine