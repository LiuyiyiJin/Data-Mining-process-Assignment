# KDD: Credit Card Fraud Detection

## Objective

Discover a reliable fraud-detection model under extreme class imbalance and explain the operational precision/recall trade-off.

## KDD stages

1. **Selection** — select transaction amount, anonymized principal components, time, and the fraud label.
2. **Preprocessing** — validate types, inspect missingness and duplicates, split before fitting transformations, and preserve the rare-class signal.
3. **Transformation** — scale amount/time and prepare a stratified modeling matrix.
4. **Data mining** — compare a class-weighted logistic model with a tree-based model.
5. **Interpretation/evaluation** — use PR-AUC, recall at a precision target, confusion matrix, and error analysis to turn patterns into actionable knowledge.

See `kdd_project.ipynb` and `report.md`.
