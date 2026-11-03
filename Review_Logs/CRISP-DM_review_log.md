# CRISP-DM review and revision log

## Revision 1 — business objective

- Draft issue: treating churn prediction as an accuracy contest.
- Critique: the business decision is retention prioritization; false negatives and false positives have different costs.
- Revision: define the output as a ranked retention queue and report recall, precision, ROC-AUC, and PR-AUC.
- Manual check: verified that the notebook reports both classes and uses a stated threshold.

## Revision 2 — leakage and reproducibility

- Draft issue: cleaning and encoding could be performed before the split.
- Critique: fitting transformations before the split can leak test information.
- Revision: use a scikit-learn `ColumnTransformer` inside a `Pipeline` and fit it only on training data.
- Manual check: inspected the notebook order and confirmed the split precedes model fitting.

## Revision 3 — deployment claims

- Draft issue: describing the classifier as an automatic churn decision.
- Critique: predictions do not establish which intervention will cause retention.
- Revision: describe weekly batch scoring, monitoring, human review, and causal limitations.
- Manual check: deployment section contains drift, calibration, fairness, and retraining considerations.
