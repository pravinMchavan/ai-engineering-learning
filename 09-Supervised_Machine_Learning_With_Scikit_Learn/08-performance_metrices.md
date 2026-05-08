
# Performance Metrics — Notes (Theory + Formulas)

Performance metrics tell us **how good** a model’s predictions are. The best metric depends on:
- Task type: **Regression** (continuous output) vs **Classification** (class labels)
- Goal: minimize average error, avoid false negatives, rank probabilities, etc.

---

## 1) Regression metrics
Assume true values $y^{(i)}$ and predictions $\hat{y}^{(i)}$ for $i=1..n$.

### 1.1 MAE (Mean Absolute Error)
**Meaning:** average absolute error.
$$
\mathrm{MAE} = \frac{1}{n}\sum_{i=1}^{n}\left|y^{(i)} - \hat{y}^{(i)}\right|
$$
**Use when:** you want an error in original units and less sensitivity to outliers than MSE.

**Advantages:**
- More robust to outliers (errors grow linearly).
- Easy to interpret (same units as $y$).

**Disadvantages:**
- Not differentiable at 0 (can be slightly harder for gradient-based optimization).
- Doesn’t penalize large errors as strongly as MSE.

### 1.2 MSE (Mean Squared Error)
**Meaning:** average squared error (penalizes big errors strongly).
$$
\mathrm{MSE} = \frac{1}{n}\sum_{i=1}^{n}\left(y^{(i)} - \hat{y}^{(i)}\right)^2
$$
**Use when:** you want to penalize large mistakes more.

**Advantages:**
- Strongly penalizes large errors (good when big mistakes are costly).
- Smooth and differentiable (works well with gradient methods).

**Disadvantages:**
- Very sensitive to outliers.
- Error is in squared units (less interpretable than MAE/RMSE).

### 1.3 RMSE (Root Mean Squared Error)
**Meaning:** square root of MSE (back to original units).
$$
\mathrm{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}\left(y^{(i)} - \hat{y}^{(i)}\right)^2}
$$
**Use when:** you want MSE-like penalty but interpretable units.

**Advantages:**
- Same units as $y$ (interpretable).
- Still penalizes large errors more than small ones.

**Disadvantages:**
- Sensitive to outliers (because it comes from MSE).
- Often models are fit by minimizing MSE/SSE; RMSE is usually reported, not optimized directly.

### 1.4 $R^2$ (Coefficient of Determination)
Let $\bar{y}$ be the mean of $y$.
$$
\mathrm{SSE} = \sum_{i=1}^{n}(y^{(i)}-\hat{y}^{(i)})^2,\quad
\mathrm{SST} = \sum_{i=1}^{n}(y^{(i)}-\bar{y})^2
$$
$$
R^2 = 1 - \frac{\mathrm{SSE}}{\mathrm{SST}}
$$
**Meaning:** proportion of variance explained by the model.

**Important:** $R^2$ is used for **regression problems only** (continuous $y$). For classification, use metrics like accuracy, precision/recall, F1, ROC-AUC, PR-AUC.

### 1.5 Adjusted $R^2$
For $p$ features (not counting intercept):
$$
\bar{R}^2 = 1 - (1 - R^2)\frac{n-1}{n-p-1}
$$
**Meaning:** like $R^2$, but it **penalizes adding extra features**.

**Key points:**
- $\bar{R}^2$ increases **only if** a new feature improves the model more than expected by chance.
- $\bar{R}^2 \le R^2$.
- It can be **negative** for a poor model.

**Use when:** comparing regression models with different number of features.

### 1.6 MAPE (Mean Absolute Percentage Error)
$$
\mathrm{MAPE} = \frac{100}{n}\sum_{i=1}^{n}\left|\frac{y^{(i)} - \hat{y}^{(i)}}{y^{(i)}}\right|
$$
**Warning:** not stable when $y^{(i)} \approx 0$.

**Advantages:**
- Scale-free (percentage), easy to compare across datasets.

**Disadvantages:**
- Undefined / unstable when $y$ is 0 or near 0.
- Can over-penalize errors when true values are small.

---

## 2) Classification metrics (binary)
Assume positive class = 1, negative class = 0.

### 2.1 Confusion Matrix

|                | Predicted + | Predicted - |
|---|---:|---:|
| **Actual +**   | TP          | FN          |
| **Actual -**   | FP          | TN          |

- **TP**: True Positive
- **TN**: True Negative
- **FP**: False Positive
- **FN**: False Negative

### 2.2 Accuracy
$$
\mathrm{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
$$
**Use when:** classes are balanced.
**Bad when:** data is imbalanced (e.g., 99% negatives).

### 2.3 Precision (Positive Predictive Value)
**Meaning:** of predicted positives, how many are actually positive?
$$
\mathrm{Precision} = \frac{TP}{TP + FP}
$$
**High precision:** few false positives.

### 2.4 Recall (Sensitivity / True Positive Rate)
**Meaning:** of actual positives, how many did we catch?
$$
\mathrm{Recall} = \frac{TP}{TP + FN}
$$
**High recall:** few false negatives.

### 2.5 F1-score
Harmonic mean of precision and recall.
$$
F_1 = 2\cdot\frac{\mathrm{Precision}\cdot\mathrm{Recall}}{\mathrm{Precision}+\mathrm{Recall}}
$$
**Use when:** you care about both FP and FN, especially with imbalance.

### 2.6 Specificity (True Negative Rate)
$$
\mathrm{Specificity} = \frac{TN}{TN + FP}
$$
**Use when:** negatives are important to classify correctly.

### 2.7 ROC curve and AUC
- **ROC** plots: TPR (Recall) vs FPR.
$$
\mathrm{TPR} = \frac{TP}{TP+FN},\quad \mathrm{FPR} = \frac{FP}{FP+TN}
$$
- **AUC** is the area under the ROC curve.
**Meaning:** probability the model ranks a random positive higher than a random negative.

### 2.8 PR curve (Precision-Recall)
Better than ROC when the positive class is rare.

---

## 3) Multiclass classification (quick notes)
- **Macro average:** average metric across classes (treat all classes equally).
- **Weighted average:** average weighted by class support (class counts).
- **Micro average:** global TP/FP/FN totals (good for overall performance).

---

## 4) Choosing the right metric (rules of thumb)
- **Imbalanced classes:** use F1, PR-AUC, precision/recall (not accuracy).
- **Cost of FN is high** (missed disease/fraud): focus on **recall**.
- **Cost of FP is high** (wrongly flagging user): focus on **precision**.
- **$R^2$:** use only for **regression**, not classification.
- **Regression with outliers:** MAE is more robust than RMSE.
- **Want large errors punished:** RMSE.

### Quick guide (Uniform error vs Outliers)
Think about how your errors look:

1) **Uniform errors (no big outliers)**
- Use **MSE/RMSE** (good default; smooth; penalizes larger errors more).

2) **Mild outliers (few larger errors, but not extreme)**
- Use **RMSE** if you *want* to penalize those bigger errors.
- Use **MAE** if you *don’t want* outliers to dominate the score.

3) **Serious outliers (extreme values present)**
- Prefer **MAE** (much more robust than MSE/RMSE).
- Also consider cleaning/handling outliers (capping/winsorizing) before training/evaluation.

---

## 5) Scikit-learn metric functions (names)

### Regression
- `mean_absolute_error`
- `mean_squared_error` (set `squared=False` for RMSE in some versions)
- `r2_score`

### Classification
- `accuracy_score`
- `precision_score`
- `recall_score`
- `f1_score`
- `confusion_matrix`
- `roc_auc_score`
- `classification_report`

