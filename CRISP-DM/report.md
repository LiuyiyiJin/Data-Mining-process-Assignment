# CRISP-DM Project Report — Telecom Customer Churn

## Executive summary

This project develops a reproducible churn-risk workflow. The business decision is not simply whether a customer is likely to churn; it is whether a retention intervention is expected to be worthwhile. The notebook compares an interpretable baseline with a nonlinear model and evaluates the trade-off between missed churners and unnecessary outreach.

## Business understanding

The target is `Churn = Yes`. A false negative can represent lost recurring revenue; a false positive consumes retention budget. The final threshold should therefore be selected with stakeholder cost assumptions rather than accuracy alone.

## Data understanding and preparation

The Kaggle Telco Customer Churn dataset contains customer demographics, subscribed services, account information, monthly charges, and the churn label. The notebook checks duplicates, missing values, target balance, and suspicious numeric columns before fitting a leakage-safe preprocessing pipeline.

## Modeling and evaluation

The notebook compares logistic regression and a random forest. Primary metrics are ROC-AUC and PR-AUC; recall and precision are reported at the operating threshold. All final numbers must be regenerated after the CSV is downloaded.

The executed baseline shows churn recall of 0.78 for logistic regression and 0.62 for random forest at a 0.50 threshold. Supporting figures are in `artifacts/churn_class_balance.png` and `artifacts/monthly_charges_by_churn.png`.

## Deployment and monitoring

The proposed deployment is a weekly batch score sent to a retention queue. Monitor feature drift, score drift, recall on delayed labels, intervention rate, and calibration. Do not use the score as an automatic adverse decision; review fairness across relevant customer groups.

## Limitations

The data is observational, historical, and may encode past service or marketing policies. A prediction is not a causal estimate of which intervention will prevent churn.
