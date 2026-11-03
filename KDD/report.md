# KDD Project Report — Credit Card Fraud Detection

## Problem and knowledge goal

The goal is to identify suspicious transactions for analyst review while controlling false alarms. Because fraud is rare, accuracy is not an appropriate primary metric.

## Selection and preprocessing

The Kaggle dataset contains anonymized transaction features, time, amount, and a binary class label. The notebook verifies the target distribution, checks missingness and duplicates, and uses a stratified holdout. Preprocessing is fitted only on training data.

## Transformation and mining

Amount and time are standardized. A class-weighted logistic regression provides a transparent baseline; a random forest captures nonlinear interactions. The notebook reports PR-AUC and threshold-specific recall/precision.

## Interpretation

The deliverable is an investigation queue, not an automatic account action. Threshold selection should reflect analyst capacity and the relative cost of missed fraud versus false alarms.

## Limitations

Anonymized variables limit domain explanation. Historical labels may be delayed or incomplete, and temporal drift may make a random split optimistic. A production system should use time-based validation and drift monitoring.
