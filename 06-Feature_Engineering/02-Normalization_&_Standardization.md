## Feature Scaling

Feature scaling is used to bring all values to a similar scale so that no feature dominates due to large numbers.

--------------------------------------------------

## 1. Normalization (Min-Max Scaling)

Formula:
(value - x1-xmin) / (xmax - xmin)

Example:
Marks range: 0 to 100
Student score: 50
Result = 0.5

Use when:
- Data has fixed range (like 0–255 images)
- No extreme outliers

Avoid when:
- Data has outliers (it compresses other values)

--------------------------------------------------

## 2. Standardization (Z-score Scaling)

Formula:
(value - mean) / standard deviation

Example:
Average marks = 50
Score 70 → positive value
Score 30 → negative value

Use when:
- Data has outliers
- Used in ML algorithms like Regression, SVM, KNN

Avoid when:
- You need values in a fixed range (0–1)

--------------------------------------------------

## Key Difference

Normalization:
- Range: 0 to 1
- Sensitive to outliers

Standardization:
- Range: no fixed range
- Less affected by outliers

--------------------------------------------------

## Important Notes

Scaling is important for:
- KNN
- SVM
- Linear Regression
- Neural Networks

Scaling not required for:
- Decision Trees
- Random Forest

--------------------------------------------------



Normalization (Outliers & Zeros)

1. Outliers Problem:
- Min-Max scaling fails because extreme values compress all other data.
- Z-score is also affected by outliers.

Best Solution:
- Robust Scaling:
  x' = (x - median) / IQR
  → Not affected by outliers

Alternative:
- Log Transform (for skewed data):
  x' = log(x)
  → Reduces large values
  → Not valid for x = 0

--------------------------------------------------

2. Zeros Problem:
- log(0) is undefined

Solutions:
1. Add constant:
   x' = log(x + 1)

2. Use Min-Max (if no outliers):
   x' = (x - min) / (max - min)

3. If zero has meaning:
   - Create extra feature:
     is_zero = 1 if x == 0 else 0

--------------------------------------------------

3. Best Practical Approach:

If dataset has BOTH outliers + zeros:

Step 1: Handle zeros
   → use log(x + 1)

Step 2: Handle outliers
   → use Robust Scaling

--------------------------------------------------

Quick Summary:
- Outliers → Robust Scaling
- Skewed data → Log Transform
- Zeros → log(x+1)
- Important zeros → add binary feature