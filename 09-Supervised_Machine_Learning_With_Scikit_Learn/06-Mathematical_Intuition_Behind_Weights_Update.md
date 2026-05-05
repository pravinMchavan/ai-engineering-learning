# Mathematical Intuition Behind Weights Update (Gradient Descent)

This note explains **why** the parameters (weights) update the way they do, using real math symbols.

**How it connects to previous notes**
- Cost function $J$: see [03-What_is-Cost_Function.md](03-What_is-Cost_Function.md)
- Gradient Descent overview + convergence: see [04-What_is_Gradient-Descent.md](04-What_is_Gradient-Descent.md)

---

## 1) Model (simple linear regression)

For one feature $x$ and target $y$:

$$\hat{y}^{(i)} = w x^{(i)} + b$$

Equivalent theta notation (common in ML):

$$\hat{y}^{(i)} = \theta_1 x^{(i)} + \theta_0$$

So $\theta_1 \equiv w$ and $\theta_0 \equiv b$.

Where:
- $w$ = weight (slope)
- $b$ = bias (intercept)
- $\hat{y}^{(i)}$ = predicted output for example $i$

---

## 2) Error (residual)

For a single data point:

$$e^{(i)} = \hat{y}^{(i)} - y^{(i)}$$

If $e^{(i)} > 0$, prediction is too high. If $e^{(i)} < 0$, prediction is too low.

---

## 3) Cost function (Mean Squared Error)

For $m$ training examples:

$$J(w,b) = \frac{1}{2m}\sum_{i=1}^{m} \left(\hat{y}^{(i)} - y^{(i)}\right)^2$$

Why the factor $\frac{1}{2m}$?
- $\frac{1}{m}$ makes it an average.
- $\frac{1}{2}$ cancels a $2$ during differentiation.

---

## 4) Goal

We want:

$$\min_{w,b} \; J(w,b)$$

So we adjust $w$ and $b$ to make $J$ smaller.

---

## 5) Gradient Descent idea

The gradient $\nabla J$ points in the direction of **steepest increase** of $J$.

To decrease $J$, move in the opposite direction:

$$w \leftarrow w - \alpha\,\frac{\partial J}{\partial w}$$
$$b \leftarrow b - \alpha\,\frac{\partial J}{\partial b}$$

Where $\alpha > 0$ is the **learning rate**.

---

## 6) Derivative w.r.t. $w$ (weight update)

Start with:

$$J(w,b) = \frac{1}{2m}\sum_{i=1}^{m} (w x^{(i)} + b - y^{(i)})^2$$

Differentiate:

$$\frac{\partial J}{\partial w}
= \frac{1}{2m}\sum_{i=1}^{m} 2(w x^{(i)} + b - y^{(i)})\,\frac{\partial}{\partial w}(w x^{(i)} + b - y^{(i)})$$

But:

$$\frac{\partial}{\partial w}(w x^{(i)} + b - y^{(i)}) = x^{(i)}$$

So:

$$\frac{\partial J}{\partial w} = \frac{1}{m}\sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})\,x^{(i)}$$

**Update rule:**

$$w \leftarrow w - \alpha\left(\frac{1}{m}\sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})x^{(i)}\right)$$

### Intuition for the sign

- If $\hat{y}^{(i)} > y^{(i)}$ (positive error) and $x^{(i)} > 0$, then $(\hat{y}^{(i)} - y^{(i)})x^{(i)} > 0$.
	- That makes $\frac{\partial J}{\partial w} > 0$.
	- Update subtracts it → $w$ decreases → predictions go down.

### Why does $x^{(i)}$ multiply the error?

The gradient contains $x^{(i)}$ because the prediction changes with $w$ according to:

$$\frac{\partial \hat{y}^{(i)}}{\partial w} = x^{(i)}$$

Using the chain rule (sketch):

$$\frac{\partial}{\partial w}(\hat{y}^{(i)}-y^{(i)})^2 = 2(\hat{y}^{(i)}-y^{(i)})\,\frac{\partial \hat{y}^{(i)}}{\partial w} = 2(\hat{y}^{(i)}-y^{(i)})x^{(i)}$$

So:
- Larger $|x^{(i)}|$ means that point is **more sensitive** to changes in $w$.
- Therefore it contributes more to the direction/magnitude of the $w$ update.

---

## 7) Derivative w.r.t. $b$ (bias update)

Similarly:

$$\frac{\partial J}{\partial b} = \frac{1}{m}\sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})$$

**Update rule:**

$$b \leftarrow b - \alpha\left(\frac{1}{m}\sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})\right)$$

### Intuition

- If predictions are mostly too high, average error is positive → $b$ decreases.
- If predictions are mostly too low, average error is negative → $b$ increases.

---

## 8) Worked numeric mini-example (one step)

Take $m=2$ points:

$$\{(x^{(1)},y^{(1)}),(x^{(2)},y^{(2)})\} = \{(1,1),(2,2)\}$$

Start with $w_0=0$, $b_0=0$.

Predictions:

$$\hat{y}^{(1)} = 0\cdot 1 + 0 = 0,\quad \hat{y}^{(2)} = 0\cdot 2 + 0 = 0$$

Errors:

$$e^{(1)} = \hat{y}^{(1)}-y^{(1)}=-1,\quad e^{(2)} = \hat{y}^{(2)}-y^{(2)}=-2$$

Gradients:

$$\frac{\partial J}{\partial w} = \frac{1}{m}\sum_{i=1}^{m} e^{(i)}x^{(i)} = \frac{1}{2}\big[(-1)\cdot 1 + (-2)\cdot 2\big] = -\frac{5}{2}$$

$$\frac{\partial J}{\partial b} = \frac{1}{m}\sum_{i=1}^{m} e^{(i)} = \frac{1}{2}(-1-2) = -\frac{3}{2}$$

With learning rate $\alpha=0.1$:

$$w_1 = w_0 - \alpha\frac{\partial J}{\partial w} = 0 - 0.1\left(-\frac{5}{2}\right)=0.25$$
$$b_1 = b_0 - \alpha\frac{\partial J}{\partial b} = 0 - 0.1\left(-\frac{3}{2}\right)=0.15$$

One step increases $w$ and $b$ because the errors were negative (predictions too low).

---

## 9) Vector form (multiple features)

Now let $\mathbf{x}^{(i)} \in \mathbb{R}^{n}$ and $\mathbf{w} \in \mathbb{R}^{n}$.

Model:

$$\hat{y}^{(i)} = \mathbf{w}^\top \mathbf{x}^{(i)} + b$$

Cost:

$$J(\mathbf{w}, b) = \frac{1}{2m}\sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})^2$$

Gradients:

$$\nabla_{\mathbf{w}} J = \frac{1}{m}\sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})\,\mathbf{x}^{(i)}$$
$$\frac{\partial J}{\partial b} = \frac{1}{m}\sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})$$

Updates:

$$\mathbf{w} \leftarrow \mathbf{w} - \alpha\,\nabla_{\mathbf{w}}J$$
$$b \leftarrow b - \alpha\,\frac{\partial J}{\partial b}$$

### Matrix (design matrix) form

Let:
- $X \in \mathbb{R}^{m\times n}$ be the design matrix (rows are $\mathbf{x}^{(i)\top}$)
- $\mathbf{y} \in \mathbb{R}^{m}$ be the target vector
- $\mathbf{1} \in \mathbb{R}^{m}$ be the all-ones vector

Predictions:

$$\hat{\mathbf{y}} = X\mathbf{w} + b\mathbf{1}$$

Cost:

$$J(\mathbf{w},b) = \frac{1}{2m}\|X\mathbf{w} + b\mathbf{1} - \mathbf{y}\|^2$$

Gradients:

$$\nabla_{\mathbf{w}}J = \frac{1}{m}X^\top\left(X\mathbf{w} + b\mathbf{1} - \mathbf{y}\right)$$
$$\frac{\partial J}{\partial b} = \frac{1}{m}\mathbf{1}^\top\left(X\mathbf{w} + b\mathbf{1} - \mathbf{y}\right)$$

---

## 10) Why updates reduce the cost (one-line intuition)

For small enough $\alpha$, the first-order approximation says:

$$J(\theta - \alpha\nabla J(\theta)) \approx J(\theta) - \alpha\,\|\nabla J(\theta)\|^2$$

Since $\alpha>0$ and $\|\nabla J(\theta)\|^2 \ge 0$, the cost tends to go down.

---

## 11) Quick checklist

- $\hat{y} = wx + b$
- $J(w,b) = \frac{1}{2m}\sum (\hat{y}-y)^2$
- $\frac{\partial J}{\partial w} = \frac{1}{m}\sum (\hat{y}-y)x$
- $\frac{\partial J}{\partial b} = \frac{1}{m}\sum (\hat{y}-y)$
- Update: parameter $\leftarrow$ parameter $-\alpha\times$ gradient

