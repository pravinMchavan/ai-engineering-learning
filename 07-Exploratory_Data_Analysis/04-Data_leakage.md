## Data Leakage (ML / EDA)

**Data leakage** happens when information that would *not be available at prediction time* (real world / production) accidentally influences the model during training.

Result: unrealistically high offline scores, followed by poor real-world performance.

---

## Why it happens

- Splitting the dataset **after** doing transformations (scaling, imputation, encoding) on the full data.
- Using features that are **proxies for the target** (created after the outcome is known).
- Mixing future and past in time-based problems.
- Duplicates / near-duplicates across train and test.
- Using group-specific signals that appear in both train and test (customer id, device id, patient id).

---

## Common types of leakage

### 1) Target leakage (the feature “knows the answer”)

- Feature is computed using the target, or using information that happens after the target event.
- Example: predicting loan default with a feature like `collection_call_made` (only happens after default risk is detected).

**Rule:** if a feature would not exist at prediction time, it must not be used.

### 2) Train–test contamination (preprocessing leakage)

- You fit preprocessing on the full dataset, then split.
- Example: scaling with mean/std computed from *all rows*.

**Fix:** split first, then fit transformers only on train (or use a pipeline).

### 3) Time leakage

- Using future information to predict past.
- Example: predicting next month sales but using `rolling_mean` computed with future dates, or random split on a time series.

**Fix:** time-based split (train on past, validate on future).

### 4) Duplicate / entity leakage

- Same user/patient/product appears in both train and test.
- Example: multiple rows per customer; random split leaks customer-specific patterns.

**Fix:** group-aware split (GroupKFold / GroupShuffleSplit).

---

## Red flags (quick diagnostics)

- Validation score is “too good to be true” very early.
- Huge gap: offline metric high, production metric low.
- A single feature shows extremely high importance and seems suspicious.
- Model performance collapses when you remove an ID-like column.

---

## Prevention workflow (recommended)

### Step 1 — Define prediction moment

Write down:

- **When** do we make the prediction?
- **What information is available at that moment?**

Anything not available at that moment is a leakage risk.

### Step 2 — Split first (before feature engineering)

- Tabular (i.i.d): use train/valid/test split.
- Time series: split by time (past → future).
- Multi-row per entity: split by group (customer/patient/product).

### Step 3 — Use pipelines for preprocessing

In scikit-learn, keep preprocessing + model in a single pipeline so transforms are fit only on training folds.

```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

numeric_features = ["age", "income"]
categorical_features = ["city", "job"]

numeric_transformer = Pipeline([
	("imputer", SimpleImputer(strategy="median")),
	("scaler", StandardScaler()),
])

categorical_transformer = Pipeline([
	("imputer", SimpleImputer(strategy="most_frequent")),
	("onehot", OneHotEncoder(handle_unknown="ignore")),
])

preprocess = ColumnTransformer([
	("num", numeric_transformer, numeric_features),
	("cat", categorical_transformer, categorical_features),
])

model = Pipeline([
	("preprocess", preprocess),
	("clf", LogisticRegression(max_iter=200)),
])
```

### Step 4 — Validate with the right split strategy

- If entities repeat: GroupKFold
- If time: TimeSeriesSplit (or custom walk-forward)

### Step 5 — Do a “leakage review” of features

For each feature, ask:

- Is this available at prediction time?
- Is it derived from the target or post-outcome events?
- Does it contain IDs, timestamps, or aggregates that could include future rows?

### Step 6 — Run sanity checks

- Baseline model (simple) vs complex model: if complex is *massively* better, re-check leakage.
- Train on shuffled targets: metric should drop near random.
- Check duplicates between splits (exact or near-duplicate).

---

## Quick checklist (before you trust your score)

- [ ] Split strategy matches the problem (random vs time vs group)
- [ ] Split done **before** any fit/transform step
- [ ] All preprocessing is inside a pipeline
- [ ] No post-outcome / future-derived features
- [ ] No duplicates or same-entity overlap across splits
- [ ] Cross-validation uses the correct splitter

