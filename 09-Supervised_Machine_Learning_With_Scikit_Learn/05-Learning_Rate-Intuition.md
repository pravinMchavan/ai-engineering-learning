# Learning Rate (α) — Theory Note

## Definition

The **learning rate** (often written as $\alpha$ or `lr`) is a positive scalar that controls the **step size** of each update in gradient-based optimization.

In Gradient Descent, parameters $\theta$ are updated as:

$$\theta_{t+1} = \theta_t - \alpha\,\nabla J(\theta_t)$$

Where:
- $\theta$ = model parameters (e.g., slope and intercept)
- $J(\theta)$ = cost/loss function
- $\nabla J(\theta)$ = gradient (direction of steepest increase)
- $\alpha$ = learning rate (how far we move per step)

---

## Why learning rate matters

Learning rate is the main knob that trades off:

- **Speed** of convergence (how fast cost decreases)
- **Stability** of updates (whether the algorithm overshoots or diverges)

Even with the same data and the same cost function, different $\alpha$ can lead to:
- slow progress
- good convergence
- oscillation
- divergence (cost explodes)

---

## Behavior for different α values

### 1) α too small → very slow convergence

Updates are tiny, so you need many iterations.

```
Cost
 ^
 | o
 |  o
 |   o
 |    o
 |     o
 +-----------------> iterations
```

### 2) α reasonable → fast and stable convergence

Cost decreases quickly and smoothly.

```
Cost
 ^
 | o
 |  \
 |   \
 |    \
 |     o (near minimum)
 +-----------------> iterations
```

### 3) α too large → overshoot / oscillation

Steps jump over the minimum repeatedly.

```
Cost
 ^
 | o   o   o
 |  o o o o
 |    o o
 +-----------------> iterations
```

### 4) α far too large → divergence

Cost increases instead of decreasing.

```
Cost
 ^
 | o
 |  o
 |    o
 |       o
 |           o
 +-----------------> iterations
```

---

## Convergence (theory perspective)

For many common cases (especially convex, smooth objectives), learning rate affects whether the sequence $\{\theta_t\}$ converges.

High-level idea:

- If $\alpha$ is small enough, updates are stable and $J(\theta_t)$ tends to decrease.
- If $\alpha$ is too large, the method can overshoot the minimum and may not converge.

In convex optimization with a smooth objective, there are known bounds that relate a safe step size to the curvature of $J$ (how sharply it bends). Intuitively:

> higher curvature ⇒ smaller safe learning rate.

---

## Learning rate in different Gradient Descent variants

### Batch Gradient Descent
- Uses the full dataset to compute $\nabla J(\theta)$.
- Gradient is stable → learning rate can be chosen more predictably.

### Stochastic / Mini-batch Gradient Descent
- Gradient estimates are noisy.
- Too large $\alpha$ amplifies noise → instability.
- Often uses decreasing learning rate schedules.

---

## Learning rate schedules (theory + purpose)

Instead of a constant $\alpha$, you can use $\alpha_t$ that changes with time/iteration.

Why schedule it?
- larger steps early to move quickly
- smaller steps later to settle near the minimum

Common schedules:

1) **Step decay**
- Drop $\alpha$ by a factor after some epochs.

2) **Exponential decay**
$$\alpha_t = \alpha_0\,\gamma^t\quad (0<\gamma<1)$$

3) **Inverse time decay**
$$\alpha_t = \frac{\alpha_0}{1 + k t}$$

---

## Practical theory notes (still conceptual)

- Learning rate interacts with **feature scaling**. Poorly scaled features make the cost surface “stretched”, which typically requires smaller $\alpha$ for stability.
- If the objective has a narrow valley, large steps can bounce across the valley.
- A good stopping rule (convergence criterion) typically checks improvement in $J(\theta)$ or the norm of $\nabla J(\theta)$.

---

## Summary (one paragraph)

The learning rate $\alpha$ controls how aggressively Gradient Descent updates parameters: too small slows convergence, too large causes oscillation or divergence. For smooth convex objectives, convergence is guaranteed only when $\alpha$ is within a stable range related to the curvature of the loss; for stochastic methods, schedules that reduce $\alpha$ over time help stabilize convergence.

