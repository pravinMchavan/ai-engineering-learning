# Simple Linear Regression (Not Theoretical) — House Price Example

This note avoids heavy theory. We’ll use one simple idea:

> Use **one input** (house size) to predict **one output** (house price).

## Definition (Simple Linear Regression)

**Simple Linear Regression** is a supervised learning method that predicts a numeric value (like house price) using **one** input feature (like house size) by fitting a **straight-line relationship** between them.

---

## What we’re building

**Goal:** predict a house’s price from its size.

- **Feature (X):** house size (e.g., square feet)
- **Target (y):** price (e.g., in lakhs or dollars)

Example dataset (toy numbers):

| size_sqft | price_lakh |
|---:|---:|
| 600 | 22 |
| 800 | 28 |
| 1000 | 35 |
| 1200 | 42 |
| 1500 | 55 |

---

## What “linear regression” does (in plain words)

It draws the **best-fitting straight line** through your data so you can:

1) **Predict** price for a new size (e.g., 1100 sqft)
2) **Estimate trend** (how much price increases when size increases)

You don’t need to memorize formulas. Just remember:

- The model learns **two numbers**:
	- a starting value (base price)
	- an “increase per sqft” value

---

## Step-by-step workflow (what you actually do)

### Step 1: Prepare your data

Make sure:

- Size is numeric (no commas, no “sqft” text)
- Price is numeric
- Units are consistent

**Tip:** If your dataset has many columns, start with just one: `size_sqft`.

---

### Step 2: Split data (train vs test)

Why split?

- **Train set:** the model learns from this.
- **Test set:** you check if it works on new (unseen) houses.

Common split: 80% train / 20% test.

---

### Step 3: Train the model

Training means: the model picks the line that makes prediction errors as small as possible on the training data.

**Error (residual):**

> actual price − predicted price

---

### Step 4: Predict on test set

Use the trained model to predict prices for the test houses.

---

### Step 5: Evaluate (use a metric you understand)

Use at least one of these:

- **MAE (Mean Absolute Error):** average absolute mistake. Easy to read.
	- Example: MAE = 3 lakh means “on average we’re off by 3 lakh”.
- **RMSE (Root Mean Squared Error):** punishes big mistakes more.

---

### Step 6: Interpret what the model learned

Two things to check:

1) **Slope (increase per sqft):**
	 - If slope is `0.03 lakh/sqft`, then +100 sqft ≈ +3 lakh.
2) **Intercept (base):**
	 - The “starting value” when size is 0.
	 - In real estate it’s not physically meaningful, but it’s part of the math.

---

## Minimal scikit-learn example (copy/paste)

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 1) Data: size (X) and price (y)
X = np.array([600, 800, 1000, 1200, 1500]).reshape(-1, 1)  # must be 2D
y = np.array([22, 28, 35, 42, 55])  # 1D

# 2) Split
X_train, X_test, y_train, y_test = train_test_split(
		X, y, test_size=0.2, random_state=42
)

# 3) Train
model = LinearRegression()
model.fit(X_train, y_train)

# 4) Predict
y_pred = model.predict(X_test)

# 5) Evaluate
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5

print("Intercept (base price):", model.intercept_)
print("Slope (lakh per sqft):", model.coef_[0])
print("MAE:", mae)
print("RMSE:", rmse)

# Predict a new house
new_size = np.array([[1100]])
print("Predicted price for 1100 sqft:", model.predict(new_size)[0])
```

---

## What can go wrong (common beginner mistakes)

1) **Data leakage**
- Using a feature that includes the future (e.g., “final negotiated price”).

2) **Outliers**
- A luxury villa can pull the line up and worsen normal-house predictions.

3) **Non-linear pattern**
- If prices rise faster after a certain size, a straight line may underfit.
- Fix later with more features or non-linear models—but first learn the baseline.

4) **Too few features**
- Size alone ignores location, age, condition.
- That’s okay for learning—just don’t expect production accuracy.

---

## Quick self-check

- If size increases, does predicted price increase? (It should.)
- Is MAE small enough to be useful for your decision?
- Plot size vs price: does a straight line roughly make sense?

