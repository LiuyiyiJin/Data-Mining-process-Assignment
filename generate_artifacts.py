from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

ROOT = Path(__file__).resolve().parent
sns.set_theme(style="whitegrid")

# CRISP-DM: target balance and monthly charges by churn.
crisp = ROOT / "CRISP-DM"
crisp_art = crisp / "artifacts"
crisp_art.mkdir(exist_ok=True)
telco = pd.read_csv(crisp / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv")
telco["TotalCharges"] = pd.to_numeric(telco["TotalCharges"], errors="coerce")
fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(data=telco, x="Churn", ax=ax)
ax.set_title("Telco churn class balance")
fig.tight_layout(); fig.savefig(crisp_art / "churn_class_balance.png", dpi=160); plt.close(fig)
fig, ax = plt.subplots(figsize=(7, 4))
sns.boxplot(data=telco, x="Churn", y="MonthlyCharges", ax=ax)
ax.set_title("Monthly charges by churn outcome")
fig.tight_layout(); fig.savefig(crisp_art / "monthly_charges_by_churn.png", dpi=160); plt.close(fig)

# KDD: extreme class imbalance.
kdd = ROOT / "KDD"
kdd_art = kdd / "artifacts"
kdd_art.mkdir(exist_ok=True)
fraud = pd.read_csv(kdd / "data" / "creditcard.csv", usecols=["Class"])
counts = fraud["Class"].value_counts().sort_index()
pd.DataFrame({"class": counts.index, "count": counts.values}).to_csv(kdd_art / "class_counts.csv", index=False)
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(["Legitimate", "Fraud"], counts.values, color=["#4c78a8", "#e45756"])
ax.set_yscale("log"); ax.set_ylabel("Transactions (log scale)"); ax.set_title("Credit-card class imbalance")
fig.tight_layout(); fig.savefig(kdd_art / "class_imbalance.png", dpi=160); plt.close(fig)

# SEMMA: model-selection table and selected clustering plot.
semma = ROOT / "SEMMA"
semma_art = semma / "artifacts"
semma_art.mkdir(exist_ok=True)
mall = pd.read_csv(semma / "data" / "Mall_Customers.csv")
features = ["Annual Income (k$)", "Spending Score (1-100)"]
X = mall[features].dropna()
Z = StandardScaler().fit_transform(X)
rows = []
for k in range(2, 9):
    model = KMeans(n_clusters=k, n_init=20, random_state=42).fit(Z)
    rows.append({"k": k, "inertia": model.inertia_, "silhouette": silhouette_score(Z, model.labels_)})
scores = pd.DataFrame(rows)
scores.to_csv(semma_art / "k_selection_scores.csv", index=False)
best_k = int(scores.loc[scores["silhouette"].idxmax(), "k"])
model = KMeans(n_clusters=best_k, n_init=20, random_state=42).fit(Z)
seg = X.copy(); seg["cluster"] = model.labels_
seg.to_csv(semma_art / "customer_segments.csv", index=False)
fig, ax = plt.subplots(figsize=(7, 5))
sns.scatterplot(data=seg, x=features[0], y=features[1], hue="cluster", palette="tab10", ax=ax)
ax.set_title(f"Mall customer segments (k={best_k})")
fig.tight_layout(); fig.savefig(semma_art / "customer_segments.png", dpi=160); plt.close(fig)

print("Artifacts generated")
print(f"SEMMA selected k={best_k}")
