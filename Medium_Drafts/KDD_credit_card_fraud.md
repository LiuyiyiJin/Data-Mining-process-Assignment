# KDD for Credit-Card Fraud: From Selection to Actionable Investigation

## Abstract

This project uses the KDD process to build a fraud-screening baseline under extreme class imbalance.

## KDD workflow

Selection defines the transaction fields and fraud label. Preprocessing checks quality and preserves the rare class. Transformation scales numeric variables. Data mining compares class-weighted logistic regression and random forest. Interpretation focuses on PR-AUC and threshold-specific precision/recall.

## Results

The random forest baseline achieves higher PR-AUC than logistic regression in the executed split. This does not mean automatic approval or rejection is safe; the model is a prioritization tool for analyst review.

## Limitations

The features are anonymized, labels may be delayed, and the dataset covers a short historical period. Time-based validation and drift monitoring are required before production use.
