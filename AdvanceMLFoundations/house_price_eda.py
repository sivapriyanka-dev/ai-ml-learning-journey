# Step 1 — Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_california_housing

# Step 2 — Load Data
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# Step 3 — Basic Inspection
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

# Step 4 — Statistical Summary Look for: min, max, mean, std, suspicious values
print(df.describe())

# Step 5 — Missing Values - missing data - which columns
print(df.isnull().sum())

# Step 6 — Duplicate Check
print("Number of duplicate rows:", df.duplicated().sum())

# Step 7 — Target Variable Distribution
# normal, skewed,uniform
plt.figure(figsize=(8, 5))

df["MedHouseVal"].hist(bins=30)

plt.title("Target Distribution")
plt.xlabel("House Price")
plt.ylabel("Count")

plt.show()

# Step 8 — Feature Distributions
plt.figure(figsize=(8, 5))
df["MedInc"].hist(bins=30)
plt.show()

# Step 9 — Boxplots (Outlier Detection)
# extremely large room counts
# huge population
sns.boxplot(x=df["AveRooms"])
plt.show()

# Step 10 — Correlation Matrix
# Strong positive: feature increases → target increases
# Negative: feature increases → target decreases
corr = df.corr()

plt.figure(figsize=(10, 8))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.show()

# Step 11 — Scatter Relationships
plt.scatter(
    df["MedInc"],
    df["MedHouseVal"],
    alpha=0.3
)

plt.xlabel("Median Income")
plt.ylabel("House Price")

plt.show()

# Strongest correlated feature? MedInc (0.69)
# Biggest outlier? AveOccup
# Target skewed? Yes, right-skewed and capped at 5.0

# ✅ target is right-skewed
# ✅ target capped at 5.0
# ✅ huge outliers (AveOccup, AveRooms)
# ✅ strong predictor (MedInc)
# ✅ multicollinearity (AveRooms ↔ AveBedrms)
# ✅ nonlinear relationships
