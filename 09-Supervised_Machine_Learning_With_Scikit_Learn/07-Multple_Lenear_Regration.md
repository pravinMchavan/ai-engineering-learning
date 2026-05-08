

# Multiple Linear Regression (MLR) — Notes (Theory + Formulas)

## 1) What it is
**Multiple Linear Regression** predicts a continuous target $y$ using **two or more** input features ($x_1, x_2, \dots, x_p$) with a linear relationship.

**Linear** means: the model is linear in the parameters (coefficients), not necessarily that each feature is “straight-line” in raw form (you can add polynomial features, interactions, log transforms, etc., and it is still linear in parameters).

---

## 2) Model (hypothesis) formula

For one example (row) $i$:
$$
\hat{y}^{(i)} = \beta_0 + \beta_1 x_1^{(i)} + \beta_2 x_2^{(i)} + \cdots + \beta_p x_p^{(i)}
$$

- $\hat{y}^{(i)}$: predicted value
- $\beta_0$: intercept (bias)
- $\beta_j$: coefficient (weight) for feature $x_j$
- $p$: number of features

### Vector / matrix form (compact)
Let:
- $\mathbf{x}^{(i)} = [1, x_1^{(i)}, x_2^{(i)}, \dots, x_p^{(i)}]^\top$ (the leading 1 is for intercept)
- $\boldsymbol{\beta} = [\beta_0, \beta_1, \dots, \beta_p]^\top$

Then:
$$
\hat{y}^{(i)} = (\mathbf{x}^{(i)})^\top \boldsymbol{\beta}
$$

For a whole dataset with $n$ examples:
- $\mathbf{X}$ is an $n \times (p+1)$ matrix (first column all 1s)
- $\mathbf{y}$ is an $n \times 1$ vector

$$
\hat{\mathbf{y}} = \mathbf{X} \boldsymbol{\beta}
$$

---

## 3) Error / noise model
We often assume:
$$
y = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}
$$
where $\boldsymbol{\varepsilon}$ is the error (noise) term.

---

## 4) Objective (loss) function: Least Squares
To fit $\boldsymbol{\beta}$, we minimize **Sum of Squared Errors** (SSE) or **Mean Squared Error** (MSE).

### SSE
$$
\mathrm{SSE}(\boldsymbol{\beta}) = \sum_{i=1}^{n}\left(y^{(i)} - \hat{y}^{(i)}\right)^2
$$

**Advantages:**
- Simple and convex for linear regression (single global minimum).
- Strongly penalizes large errors.

**Disadvantages:**
- Depends on dataset size $n$ (bigger $n$ usually means bigger SSE), so it’s harder to compare across datasets.
- Sensitive to outliers.

### MSE
$$
\mathrm{MSE}(\boldsymbol{\beta}) = \frac{1}{n}\sum_{i=1}^{n}\left(y^{(i)} - \hat{y}^{(i)}\right)^2
$$

**Advantages:**
- Normalized by $n$ (easier to compare than SSE).
- Differentiable and convex (good for gradient descent).

**Disadvantages:**
- Sensitive to outliers.
- Error is in squared units (less interpretable).

In matrix form (SSE):
$$
\mathrm{SSE}(\boldsymbol{\beta}) = \|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|_2^2
$$

---

## 5) How we estimate coefficients

### A) Closed-form solution (Normal Equation)
If $\mathbf{X}^\top\mathbf{X}$ is invertible:
$$
\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top \mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}
$$

Notes:
- Works well for smaller feature sets.
- In practice, libraries often use numerically stable methods (QR / SVD) even if the formula above is the “theory”.

### B) Gradient Descent (iterative)
Update rule (for learning rate $\alpha$):
$$
\boldsymbol{\beta} \leftarrow \boldsymbol{\beta} - \alpha\, \nabla_{\boldsymbol{\beta}}\mathrm{MSE}(\boldsymbol{\beta})
$$

Gradient for MSE:
$$
\nabla_{\boldsymbol{\beta}}\mathrm{MSE} = -\frac{2}{n}\mathbf{X}^\top(\mathbf{y}-\mathbf{X}\boldsymbol{\beta})
$$

So one common form:
$$
\boldsymbol{\beta} \leftarrow \boldsymbol{\beta} + \frac{2\alpha}{n}\mathbf{X}^\top(\mathbf{y}-\mathbf{X}\boldsymbol{\beta})
$$

---

## 6) Interpretation of coefficients (important theory)
If all other features are held constant:
- $\beta_j$ is the expected change in $\hat{y}$ when $x_j$ increases by 1 unit.

Example: If $\beta_2 = 3.5$, then increasing $x_2$ by 1 increases the prediction by 3.5 (assuming other features unchanged).

---

## 7) Key assumptions (classical linear regression)
These assumptions matter mainly for **statistical inference** (p-values, confidence intervals), and for model reliability:

1. **Linearity**: relationship is linear in parameters.
2. **Independence**: errors are independent (often violated in time series).
3. **Homoscedasticity**: constant error variance.
4. **No perfect multicollinearity**: features aren’t exact linear combinations of each other.
5. **Normality of errors** (optional for prediction, more for inference): errors are approximately normal.

If multicollinearity is strong (features highly correlated), coefficients can become unstable (large magnitude, sensitive to small data changes).

---

## 8) Model evaluation formulas

### MAE (Mean Absolute Error)
$$
\mathrm{MAE} = \frac{1}{n}\sum_{i=1}^{n}|y^{(i)} - \hat{y}^{(i)}|
$$

### RMSE (Root Mean Squared Error)
$$
\mathrm{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y^{(i)} - \hat{y}^{(i)})^2}
$$

### $R^2$ (Coefficient of Determination)
Define:
$$
\mathrm{SST} = \sum_{i=1}^{n}(y^{(i)}-\bar{y})^2,\quad
\mathrm{SSE} = \sum_{i=1}^{n}(y^{(i)}-\hat{y}^{(i)})^2
$$
Then:
$$
R^2 = 1 - \frac{\mathrm{SSE}}{\mathrm{SST}}
$$

### Adjusted $R^2$ (penalizes many features)
$$
\bar{R}^2 = 1 - (1 - R^2)\frac{n-1}{n-p-1}
$$
where $p$ is number of features (not counting the intercept).

Notes (interpretation):
- Adjusted $R^2$ is used to compare models with **different number of features**.
- It increases only when the new feature improves the model enough; otherwise it can decrease.
- Typically $\bar{R}^2 \le R^2$, and it can be negative for a weak model.

---

## 9) Regularization (when MLR overfits / multicollinearity)
Regularization adds a penalty to shrink coefficients.

### Ridge Regression (L2)
$$
\min_{\boldsymbol{\beta}}\; \frac{1}{n}\|\mathbf{y}-\mathbf{X}\boldsymbol{\beta}\|_2^2 + \lambda\|\boldsymbol{\beta}\|_2^2
$$

**Advantages:**
- Reduces overfitting by shrinking coefficients (lower variance).
- Works well when features are correlated (multicollinearity).

**Disadvantages:**
- Does not set coefficients exactly to 0 (no automatic feature selection).
- Adds bias; $\lambda$ must be tuned.

### Lasso Regression (L1)
$$
\min_{\boldsymbol{\beta}}\; \frac{1}{n}\|\mathbf{y}-\mathbf{X}\boldsymbol{\beta}\|_2^2 + \lambda\|\boldsymbol{\beta}\|_1
$$

**Advantages:**
- Can set some coefficients to exactly 0 (feature selection).
- Helps produce simpler, more interpretable models.

**Disadvantages:**
- Can be unstable when features are strongly correlated (may pick one and drop others).
- Like Ridge, needs tuning of $\lambda$; can underfit if $\lambda$ is too large.

- Ridge reduces coefficient size (keeps all features).
- Lasso can push some coefficients to exactly 0 (feature selection).

---

## 10) Very small Scikit-learn mapping (what to use)
- Multiple Linear Regression: `LinearRegression`
- Ridge: `Ridge`
- Lasso: `Lasso`
- Scale features (important for Ridge/Lasso/GD-based solvers): `StandardScaler`

Minimal workflow:
1. Split: train/test
2. Fit on train
3. Predict on test
4. Evaluate with MAE/RMSE/$R^2$

---

## 11) Quick summary (1-minute revision)
- Model: $\hat{y} = \beta_0 + \sum_{j=1}^{p}\beta_j x_j$
- Fit by minimizing squared errors (least squares)
- Solution: Normal Equation or Gradient Descent
- Metrics: MAE, RMSE, $R^2$, Adjusted $R^2$
- If multicollinearity/overfitting: use Ridge/Lasso

