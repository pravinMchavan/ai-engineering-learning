# What Is Gradient Descent? (House Price Example)

Gradient Descent is an **optimization algorithm** used to find the best model parameters by repeatedly making the **cost** smaller.

In our house-price model, we want a line that predicts price from size:

> **predicted_price = intercept + slope × size_sqft**

The **intercept** and **slope** are the two numbers we want to learn.

---

## Why we need Gradient Descent

When you pick a slope and intercept, you get predictions → errors → a cost value (like MSE).

- Bad line → high cost
- Better line → lower cost

### Cost function (MSE) formula

For $m$ training examples, with prediction $\hat{y}^{(i)}$ and actual $y^{(i)}$:

$$J(w,b) = \frac{1}{2m}\sum_{i=1}^{m}\left(\hat{y}^{(i)} - y^{(i)}\right)^2$$

For simple linear regression:

$$\hat{y}^{(i)} = w x^{(i)} + b$$

Gradient Descent is the method to automatically adjust slope/intercept to reduce cost.

---

## Intuition (no heavy theory)

Think of the cost function as a landscape:

- Height = cost (error)
- We want to reach the lowest point (minimum cost)

### Text graph: “walking downhill”

```
Cost (height)
	^
	|             o  (start)
	|          o
	|       o
	|    o
	| o   (minimum)
	+--------------------> steps
```

Each step moves parameters a bit in the direction that reduces cost.

---

## Global minimum vs local minimum

- **Global minimum:** the lowest possible cost value (the absolute best point).
- **Local minimum:** a point that looks “low” compared to nearby points, but there might be an even lower point elsewhere.

### Text graph idea

**Convex bowl (one global minimum)**

```
Cost
 ^
 |        \      /
 |         \    /
 |          \  /
 |           \/   <- global minimum
 +-----------------> parameter value
```

**Wavy landscape (can have local minima)**

```
Cost
 ^
 |    \_/\__
 |  _/      \_
 |_/          \__
 +-----------------> parameter value
	local     global
	min       min
```

**Important note for Simple Linear Regression:**
- With the usual cost (MSE), the cost surface is **convex**, which means there is **only one global minimum** (no “traps” of local minima).
- So Gradient Descent is mainly about choosing a good learning rate and stopping rule, not escaping local minima.

## What the “gradient” means

The **gradient** tells you which direction increases the cost the fastest.

So to reduce the cost, we move **in the opposite direction**.

You can remember it like this:

> Gradient points “uphill” → we step “downhill”.

---

## The update rule (simple)

At each step, update parameters:

- `slope = slope - learning_rate * gradient_wrt_slope`
- `intercept = intercept - learning_rate * gradient_wrt_intercept`

You don’t need to derive the gradients right now to understand the workflow.

---

## Learning rate (α): the step size

**Learning rate** controls how big each downhill step is.

### If learning rate is too small
- Training is very slow.

### If learning rate is too large
- You may overshoot the minimum and bounce around.

### Text graph: overshooting

```
Cost
 ^
 |      o     o     o
 |        o o   o o
 |          \_/
 +--------------------> steps
			 min
```

---

## Example: fitting house price line (concept)

Suppose your predictions are too high for small houses and too low for big houses.
That usually means your slope is too low or too high.

Gradient Descent uses the direction from the errors to adjust:

- If big houses are under-predicted → increase slope
- If all predictions are too high → decrease intercept

---

## Types of Gradient Descent (quick)

All do the same idea; they just differ in how much data they use per step:

1) **Batch Gradient Descent**: uses all training data per step (stable, slower per step)
2) **Stochastic Gradient Descent (SGD)**: uses 1 example per step (noisy, fast)
3) **Mini-batch Gradient Descent**: uses a small batch (most common in practice)

---

## What is “Convergence”?

**Convergence** means:

> The algorithm reaches a point where further updates don’t meaningfully reduce the cost.

So the parameters become **stable** and the cost stops improving.

---

## What is a “Convergence Algorithm”?

In ML practice, “convergence algorithm” usually means the **stopping rule** (the logic that decides when to stop iterating).

Because you can’t run gradient descent forever, you stop when one of these is true:

### Common convergence criteria (stopping conditions)

1) **Cost improvement is tiny**
- Stop if `|cost_new - cost_old| < ε`

2) **Gradient is near zero**
- Stop if the gradient magnitude is very small (you’re near the bottom)

3) **Parameters stop changing**
- Stop if `|w_new - w_old|` and `|b_new - b_old|` are tiny

4) **Maximum iterations reached**
- Safety stop: `iterations == max_iters`

### Simple convergence algorithm (pseudocode)

```text
set w, b (start values)
set alpha (learning rate)
set epsilon (small number)

repeat up to max_iters:
  compute predictions using w, b
  compute cost
  compute gradients for w and b
  update w and b (step downhill)

  if cost improvement < epsilon:
		stop (converged)
```

---

## Practical tips (so it works smoothly)

1) **Scale your feature (size_sqft)**
- If sizes are like 600–3000, scaling helps gradient descent converge faster.
- Example: standardization (mean 0, std 1).

2) **Watch the cost over steps**
- Cost should generally go down.
- If it increases or explodes → learning rate is too high.

3) **Use a baseline**
- Compare to a simple model (even average price) to sanity-check.

---

## Mini self-check

- If cost is not decreasing at all, what would you try first? (Usually lower learning rate.)
- If cost decreases but extremely slowly, what would you adjust? (Try higher learning rate or scale features.)
- If cost becomes stable, what does that mean? (Converged / stop.)

