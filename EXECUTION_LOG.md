# Execution log

Date: 2026-11-03

All three notebooks were executed locally with the downloaded datasets and saved with outputs.

| Project | Dataset rows | Dataset status | Notebook status |
|---|---:|---|---|
| CRISP-DM | 7,043 | Loaded from Telco Customer Churn CSV | Passed |
| KDD | 284,807 | Loaded from Credit Card Fraud CSV; 492 fraud cases | Passed |
| SEMMA | 200 | Loaded from Mall Customers CSV | Passed |

## Verified model outputs

### CRISP-DM

The notebook reports churn-class precision/recall for logistic regression and random forest. Logistic regression recall for churn is 0.78; random forest recall for churn is 0.62 at the demonstrated 0.50 threshold.

### KDD

The notebook reports PR-AUC and ROC-AUC. Logistic regression: PR-AUC 0.703857, ROC-AUC 0.972638. Random forest: PR-AUC 0.848219, ROC-AUC 0.959794. Because the class is extremely rare, PR-AUC and threshold-specific precision/recall are emphasized over accuracy.

### SEMMA

The notebook evaluates K-Means values of k from 2 through 8 with inertia and silhouette score, selects the best silhouette candidate, profiles the resulting clusters, and displays the segmentation plot.

## Reproducibility note

Raw CSV files are excluded from Git by `.gitignore`. A reviewer should download the credited Kaggle datasets and place them in the documented project `data/` directories before rerunning the notebooks.
