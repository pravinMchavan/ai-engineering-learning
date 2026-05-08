
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

### 1.2 MSE (Mean Squared Error)
**Meaning:** average squared error (penalizes big errors strongly).
$$
\mathrm{MSE} = \frac{1}{n}\sum_{i=1}^{n}\left(y^{(i)} - \hat{y}^{(i)}\right)^2
$$
**Use when:** you want to penalize large mistakes more.

### 1.3 RMSE (Root Mean Squared Error)
**Meaning:** square root of MSE (back to original units).
$$
\mathrm{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}\left(y^{(i)} - \hat{y}^{(i)}\right)^2}
$$
**Use when:** you want MSE-like penalty but interpretable units.

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
**Use when:** comparing models with different number of features.

### 1.6 MAPE (Mean Absolute Percentage Error)
$$
\mathrm{MAPE} = \frac{100}{n}\sum_{i=1}^{n}\left|\frac{y^{(i)} - \hat{y}^{(i)}}{y^{(i)}}\right|
$$
**Warning:** not stable when $y^{(i)} \approx 0$.

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

