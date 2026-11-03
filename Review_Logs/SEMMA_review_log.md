# SEMMA review and revision log

## Revision 1 — sample definition

- Draft issue: clustering every column, including the customer identifier.
- Critique: identifiers do not represent customer behavior and can distort distance calculations.
- Revision: use annual income and spending score as documented segmentation variables.
- Manual check: notebook defines the feature list explicitly.

## Revision 2 — scale and model selection

- Draft issue: choosing `k` from a visual impression alone.
- Critique: cluster count should be supported by quantitative diagnostics and interpretability.
- Revision: standardize features and compare inertia plus silhouette score for k=2..8.
- Manual check: the executed run selected k=5 and saved the selection table.

## Revision 3 — business interpretation

- Draft issue: treating clusters as permanent customer identities.
- Critique: clusters are descriptive and may be unstable or non-causal.
- Revision: present campaign ideas as testable hypotheses and recommend stability checks.
- Manual check: report includes seed sensitivity and experimentation limitations.
