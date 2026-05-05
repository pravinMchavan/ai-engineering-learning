# What Is a Cost Function? (House Price Example)

In linear regression, a **cost function** is just a single number that tells you:

> “How wrong are our predictions overall?”

The model training process tries to **minimize** this number.

---

## Key words (simple definitions)

- **Actual (y):** real house price from data
- **Predicted (ŷ):** model’s predicted price
- **Error / Residual (e):** difference between actual and predicted
	- $e = y - \hat{y}$
- **Cost:** one number that summarizes all errors

### Notation you will see in ML

For linear regression, parameters are often written as $\theta_0$ (intercept) and $\theta_1$ (slope):

$$\hat{y}^{(i)} = \theta_0 + \theta_1 x^{(i)}$$

A very common cost function is MSE written as $J(\theta_0,\theta_1)$:

$$J(\theta_0,\theta_1) = \frac{1}{2m}\sum_{i=1}^{m}\left(\hat{y}^{(i)} - y^{(i)}\right)^2$$

---

## Tiny dataset (size → price)

Let’s pretend we trained a model and got predictions like this:

| size_sqft | actual price (lakh) | predicted price (lakh) | error $e = y-\hat{y}$ |
|---:|---:|---:|---:|
| 800  | 28 | 30 | -2 |
| 1000 | 35 | 34 |  1 |
| 1200 | 42 | 40 |  2 |
| 1500 | 55 | 52 |  3 |

### Text graph: actual vs predicted

```
Price (lakh)
55 |                         A
52 |                        P
42 |                A
40 |               P
35 |          A
34 |         P
30 |    P
28 |   A
	 +--------------------------------
			 800   1000   1200   1500   size (sqft)

Legend: A = Actual, P = Predicted
```

---

## Common cost functions (what you’ll actually use)

### 1) MAE (Mean Absolute Error)

MAE takes absolute error (ignores +/− sign) and averages it.

$$\text{MAE} = \frac{1}{n}\sum_{i=1}^{n} |y_i - \hat{y}_i|$$

Why people like it:
- Easy meaning: “On average, we miss by ___ lakh.”

For the table above:
- Absolute errors: 2, 1, 2, 3 → average = $\frac{2+1+2+3}{4} = 2.0$ lakh

So: **MAE = 2 lakh**.

---

### 2) MSE (Mean Squared Error) and RMSE

**MSE** squares the errors (big mistakes become much bigger).

$$\text{MSE} = \frac{1}{n}\sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

**RMSE** is the square-root of MSE so it goes back to the original unit (lakh).

$$\text{RMSE} = \sqrt{\text{MSE}}$$

Why squared error is used a lot in linear regression:
- It strongly punishes large mistakes.
- It’s smooth and works well with gradient-based optimization.

For the table above:
- Squared errors: $(-2)^2, 1^2, 2^2, 3^2 = 4, 1, 4, 9$
- MSE = $\frac{4+1+4+9}{4} = 4.5$
- RMSE = $\sqrt{4.5} \approx 2.12$ lakh

---

## Why we “minimize cost” (intuition)

Imagine trying different lines (different models). Each line gives different errors.

- A good line → small errors → smaller cost
- A bad line → large errors → bigger cost

### Text graph: cost vs slope (just intuition)

```
Cost
 ^
 |            *
 |         *     *
 |      *           *
 |   *                 *
 | *                     *
 +-----------------------------> slope (line steepness)
							 best
```

The lowest point is the “best” slope (and intercept) for this dataset.

---

## Quick Python: compute MAE, MSE, RMSE

```python
import numpy as np

y_true = np.array([28, 35, 42, 55])
y_pred = np.array([30, 34, 40, 52])

errors = y_true - y_pred

mae = np.mean(np.abs(errors))
mse = np.mean(errors ** 2)
rmse = np.sqrt(mse)

print("Errors:", errors)
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
```

---

## Which one should you use?

- Start with **MAE** if you want an easy-to-explain “average mistake”.
- Use **RMSE** if large mistakes are especially bad and you want to punish them.
- In basic linear regression training, you’ll often see **MSE** as the cost function.

---

## Mini self-check

- Can you compute one residual: $e = y - \hat{y}$?
- If one house is off by 20 lakh, which metric increases more: MAE or RMSE?
- Does your metric match the real-world cost of being wrong?

  