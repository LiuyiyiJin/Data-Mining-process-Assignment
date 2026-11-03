# From Business Question to Retention Queue: A CRISP-DM Telco Churn Project

## Abstract

This project applies the complete CRISP-DM lifecycle to telecom customer churn. The emphasis is on connecting model metrics to a retention decision rather than treating accuracy as the business objective.

## Business framing

The practical question is which customers should be prioritized for retention outreach. False negatives represent missed churn risk, while false positives consume limited outreach capacity.

## Method

The project moves through business understanding, data understanding, data preparation, modeling, evaluation, and deployment planning. A leakage-safe preprocessing pipeline compares logistic regression and random forest.

## Results and lessons

At the demonstrated threshold, logistic regression recalls more churners than the random forest baseline. The choice of final threshold should be made using intervention cost, calibration, and capacity—not accuracy alone.

## Reproducibility

The Colab notebook, report, figures, data instructions, and limitations are available in the project repository.
