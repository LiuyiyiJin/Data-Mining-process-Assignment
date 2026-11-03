# SEMMA: Mall Customer Segmentation

## Objective

Create interpretable customer segments to support differentiated marketing, while avoiding claims that clusters are automatically causal or stable.

## SEMMA stages

1. **Sample** — load the Kaggle mall-customer sample and define the analysis population.
2. **Explore** — inspect distributions, outliers, correlations, and candidate segmentation variables.
3. **Modify** — select annual income and spending score, standardize features, and document exclusions.
4. **Model** — fit K-Means for a range of `k` values and compare silhouette scores and inertia.
5. **Assess** — profile each cluster, visualize the segments, test sensitivity to random seed, and translate findings into cautious marketing recommendations.

The workflow is compatible with Python/Colab and mirrors the SAS SEMMA logic. SAS use is optional.
