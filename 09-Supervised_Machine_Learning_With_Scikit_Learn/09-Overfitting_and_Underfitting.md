
# Overfitting and Underfitting — Notes

## 1) Basic definitions

### Underfitting
When a model is **too simple** to learn the true pattern in the data.

**Common signs:**
- Training error is high
- Validation/Test error is also high
- Model performs poorly everywhere

### Overfitting
When a model learns the training data **too well**, including noise (random fluctuations), and fails to generalize.

**Common signs:**
- Training error is very low
- Validation/Test error is high
- Big gap between training and validation performance

### Good fit (balanced)
Model captures the real pattern and generalizes well.

**Common signs:**
- Training error is low
- Validation/Test error is also low and close to training

---

## 2) Bias and Variance (core theory)

### Bias (systematic error)
**Bias** means the error from **wrong assumptions** in the model.
Example: fitting a straight line to data that is actually curved.

### Variance (sensitivity to data)
**Variance** means how much the model changes if you train it on a different sample from the same dataset.
High variance models “change a lot” with small changes in data.

---

## 3) What is low bias, low variance, high variance?

### Low bias
The model can represent the true relationship reasonably well.

**Typical result:** good training performance (low training error).

### Low variance
The model is stable: if the training data changes a little, predictions don’t change much.

**Typical result:** training and validation performance are close.

### High variance
The model is too sensitive to the training data.

**Typical result:** excellent training performance, but poor validation/test performance.

Quick mapping:
- **Underfitting** → usually **high bias**, **low variance**
- **Overfitting** → usually **low bias**, **high variance**

---

## 4) Bias–Variance tradeoff (one line idea)
When model complexity increases:
- Bias usually decreases (model can fit more patterns)
- Variance usually increases (model becomes more sensitive)

The goal is to choose a model/complexity that minimizes generalization error.

### (Optional) Expected error decomposition idea
For many problems, the expected prediction error can be thought of as:
$$
	ext{Generalization Error} \approx \text{Bias}^2 + \text{Variance} + \text{Irreducible Noise}
$$
*(You don’t always need the math, but the idea is important.)*

---

## 5) How to detect underfitting vs overfitting

### Quick cheat-sheet (easy to remember)
If you are using **accuracy** (classification):
- **Train: very good**, **Test: very good** → **Low bias + Low variance** → good generalization
- **Train: very good**, **Test: very bad** → **Low bias + High variance** → overfitting
- **Train: very bad**, **Test: very bad** → **High bias + (usually) low variance** → underfitting

If you are using **error** (regression) like MAE/RMSE (lower is better):
- **Train error: low**, **Test error: low** → Low bias + Low variance
- **Train error: low**, **Test error: high** → Low bias + High variance (overfitting)
- **Train error: high**, **Test error: high** → High bias (underfitting)

### A) Train vs Validation comparison
- If **train is bad** and **validation is bad** → underfitting
- If **train is good** and **validation is bad** → overfitting
- If **both are good and close** → good fit

### B) Learning curves (error vs training size)
If you plot error as you increase training data size:
- **Underfitting:** both curves are high and close together (adding more data doesn’t help much)
- **Overfitting:** training curve low, validation curve high (gap reduces when adding more data)

---

## 6) How to fix underfitting (reduce bias)
- Use a more complex model (e.g., polynomial features, more depth, more estimators)
- Add more useful features (feature engineering)
- Reduce regularization (smaller $\lambda$ in Ridge/Lasso)
- Train longer / tune optimization (if using gradient-based models)

---

## 7) How to fix overfitting (reduce variance)
- Get more training data (often the best fix)
- Simplify the model (reduce complexity)
- Increase regularization (Ridge/Lasso, dropout, etc.)
- Use cross-validation to choose hyperparameters
- Early stopping (stop training when validation error starts increasing)
- Feature selection (remove noisy/irrelevant features)

---

## 8) Real-life examples (easy to remember)

### Example: Polynomial regression
- Degree 1 (line): may underfit curved data → high bias
- Degree 10: may fit noise → high variance
- Degree 3–4: often a better tradeoff

### Example: Decision trees
- Very shallow tree: underfits (high bias)
- Very deep tree: overfits (high variance)

---

## 9) Quick revision (3 lines)
- Underfitting: **high bias**, model too simple, train/test both poor.
- Overfitting: **high variance**, model too complex, train good but test poor.
- Best model: good performance on unseen data (train ≈ validation).

