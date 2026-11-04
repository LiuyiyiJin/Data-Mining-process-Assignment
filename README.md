# Three Data Science Methodologies

This repository contains three reproducible data-science projects implemented with three different process methodologies:

| Methodology | Project | Task | Dataset |
|---|---|---|---|
| CRISP-DM | Telecom Customer Churn | Binary classification | [IBM Telco Customer Churn on Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) |
| KDD | Credit Card Fraud Detection | Imbalanced classification | [Credit Card Fraud Detection on Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) |
| SEMMA | Mall Customer Segmentation | Unsupervised clustering | [Mall Customer Segmentation Data on Kaggle](https://www.kaggle.com/datasets/shwetabh123/mall-customers) |

## Medium articles

These project articles are published as unlisted stories on Medium and can be read through the links below.

- [CRISP-DM — From Business Question to Retention Queue](https://medium.com/p/b1f56b4e2bd3)
- [KDD — Credit-Card Fraud: From Selection to Actionable Investigation](https://medium.com/p/b8e3f5852888)
- [SEMMA — Customer Segmentation with K-Means](https://medium.com/p/47372649a12e)

## Open in Google Colab

- [CRISP-DM — Telecom Customer Churn](https://colab.research.google.com/github/LiuyiyiJin/Data-Mining-process-Assignment/blob/master/CRISP-DM/crisp_dm_project.ipynb)
- [KDD — Credit Card Fraud Detection](https://colab.research.google.com/github/LiuyiyiJin/Data-Mining-process-Assignment/blob/master/KDD/kdd_project.ipynb)
- [SEMMA — Mall Customer Segmentation](https://colab.research.google.com/github/LiuyiyiJin/Data-Mining-process-Assignment/blob/master/SEMMA/semma_project.ipynb)

Before running in Colab, upload the relevant CSV into the project's `data/` directory as documented in `data/README.md`. Raw datasets are excluded from GitHub to avoid committing large files.

## Execution screenshots

Screenshots captured from the executed Colab notebooks are organized by methodology:

- `screenshots/CRISP-DM/` — data understanding and model evaluation.
- `screenshots/KDD/` — data preview, class distribution, and model evaluation.
- `screenshots/SEMMA/` — data preview, exploration, k-selection, and final clusters.

## Repository map

- `CRISP-DM/` — business-to-deployment workflow for churn prediction.
- `KDD/` — knowledge-discovery workflow from selection through interpretation.
- `SEMMA/` — SAS-inspired Sample, Explore, Modify, Model, Assess workflow.
- `data/README.md` — dataset download and licensing notes.

Each project contains a Colab-ready notebook, a detailed report, a data dictionary, and an artifact directory.

## Reproducibility

1. Download the dataset described in the relevant project's `data/README.md`.
2. Put the CSV in that project's `data/` directory.
3. Open the `.ipynb` file in Google Colab and run all cells from top to bottom.
4. Review the generated figures and metrics in the corresponding `artifacts/` directory.

The notebooks include assertions, fixed random seeds, explicit evaluation metrics, and a limitations section. Results must be checked against the data downloaded by the student before final submission.

## Status

The repository includes executed notebooks, reports, figures, Colab execution screenshots, and links to the three published Medium articles. Walkthrough video links will be added when available.
