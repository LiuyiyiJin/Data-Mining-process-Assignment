# KDD review and revision log

## Revision 1 — metric choice

- Draft issue: reporting accuracy as the main success criterion.
- Critique: with a 0.172% fraud rate, accuracy can be misleading.
- Revision: prioritize PR-AUC, recall, precision, and threshold-specific error analysis.
- Manual check: notebook prints the class distribution and classification report.

## Revision 2 — transformation order

- Draft issue: scaling the complete dataset before the holdout split.
- Critique: preprocessing must be learned from training data only.
- Revision: use a pipeline with imputation, scaling, and model fitting after the stratified split.
- Manual check: executed notebook successfully on the 284,807-row dataset.

## Revision 3 — interpretation

- Draft issue: presenting the model as an automatic fraud adjudicator.
- Critique: anonymized features and delayed labels limit causal and operational interpretation.
- Revision: frame the output as an analyst investigation queue and document temporal drift limitations.
- Manual check: report includes limitations and monitoring requirements.
