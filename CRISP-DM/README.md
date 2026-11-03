# CRISP-DM: Telecom Customer Churn

## Objective

Predict whether a telecom customer will churn, then translate model results into retention actions.

## CRISP-DM stages

1. **Business understanding** — define churn, costs of false negatives, and a retention decision threshold.
2. **Data understanding** — inspect schema, missing values, class balance, and relationships with churn.
3. **Data preparation** — clean `TotalCharges`, encode categorical variables, split data without leakage, and build a preprocessing pipeline.
4. **Modeling** — compare a transparent logistic regression with a tree-based model.
5. **Evaluation** — report ROC-AUC, PR-AUC, recall, precision, calibration, and a confusion matrix at a stated threshold.
6. **Deployment** — document a batch-scoring design, monitoring metrics, retraining trigger, and ethical limitations.

Open `crisp_dm_project.ipynb` in Colab. The full narrative is in `report.md`.
