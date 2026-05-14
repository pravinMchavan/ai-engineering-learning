# Polynomial Regression

Polynomial Regression is used when the relationship between input and output is not a straight line.

## Simple Idea

In linear regression, we assume the output changes in a straight-line pattern:

$$
y = b_0 + b_1x
$$

But in many real datasets, the pattern is curved. Polynomial regression adds powers of the input variable so the model can fit a curve.

## Formula

For one input variable $x$, the polynomial regression model is:

$$
y = b_0 + b_1x + b_2x^2 + b_3x^3 + \cdots + b_nx^n
$$

Where:
- $y$ = predicted output
- $x$ = input feature
- $b_0, b_1, b_2, \dots, b_n$ = model coefficients
- $n$ = degree of the polynomial

## Common Degrees

### Degree 2

$$
y = b_0 + b_1x + b_2x^2
$$

This can form a U-shaped or inverted U-shaped curve.

### Degree 3

$$
y = b_0 + b_1x + b_2x^2 + b_3x^3
$$

This can fit more complex curved patterns.

## Why It Works

Polynomial regression is still based on linear regression, but it first converts the original feature $x$ into new features like $x^2$, $x^3$, and so on.

The model then learns a linear relationship using those transformed features.

## Example

Suppose:

$$
x = 2
$$

For a degree 3 polynomial:

$$
x,\; x^2,\; x^3 = 2,\; 4,\; 8
$$

So the model can use these values to fit a curve instead of only a straight line.

## Python Example

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Input data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 4, 9, 16, 25])

# Create polynomial features up to degree 2
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Fit linear regression on transformed features
model = LinearRegression()
model.fit(X_poly, y)

# Predict
predictions = model.predict(X_poly)
```

## Key Point

Polynomial regression helps when the data is curved, while linear regression is better when the data is close to a straight line.
