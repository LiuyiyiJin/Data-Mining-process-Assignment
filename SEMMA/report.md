# SEMMA Project Report — Mall Customer Segmentation

## Objective

Segment customers using annual income and spending score so that marketing teams can tailor campaigns and measure segment-level outcomes.

## Sample and Explore

The Kaggle dataset contains customer identifiers, age, annual income, and spending score. The notebook checks schema, range validity, duplicates, distributions, and pairwise relationships.

## Modify and Model

The selected variables are standardized before K-Means. Candidate values of `k` are compared using inertia and silhouette score. The selected value must be justified by both metrics and business interpretability.

## Assess

Each cluster is profiled with count, mean age, income, and spending score. Recommendations are phrased as hypotheses for testing, not as guaranteed customer behavior. Stability across seeds and limitations are documented.

The executed run selected `k=5` by the highest silhouette score among candidates from 2 through 8. The segment table and plot are saved in `artifacts/customer_segments.csv` and `artifacts/customer_segments.png`; the model-selection table is `artifacts/k_selection_scores.csv`.
