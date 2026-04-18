MICE Imputation (Definition + Process + Formula)

1. What is MICE Imputation?
- MICE = Multiple Imputation by Chained Equations
- It fills missing values by modeling each variable as a function of other variables.
- Performs multiple iterations to improve accuracy.

--------------------------------------------------

2. Key Idea:
- Instead of filling missing values once,
  MICE fills them multiple times using predictions.

--------------------------------------------------

3. How MICE Works (Step-by-Step)

Step 1: Initialize missing values
- Fill with simple method (mean/median)

Step 2: Select one variable with missing values
- Treat it as target variable (Y)
- Other variables become input (X)

Step 3: Train a model
- Predict missing values using X → Y

Step 4: Replace missing values with predicted values

Step 5: Repeat for all variables with missing data

Step 6: Repeat entire cycle multiple times (iterations)

--------------------------------------------------

4. Formula (Conceptual)

For a variable X₁:
X₁_missing = f(X₂, X₃, X₄, ...)

Example (Regression):
X₁ = β₀ + β₁X₂ + β₂X₃ + ... + ε

--------------------------------------------------

5. Python Example

import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# Sample Data
df = pd.DataFrame({
    'Age': [25, 30, None, 35],
    'Salary': [50000, None, 55000, 65000]
})

# Apply MICE
imputer = IterativeImputer(max_iter=10, random_state=0)
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

print(df_imputed)

--------------------------------------------------

6. When to Use MICE?
- Multiple columns have missing values
- Variables are correlated
- Need high accuracy

--------------------------------------------------

7. Advantages:
- More accurate than mean/KNN
- Uses relationships between variables
- Handles multiple missing columns

--------------------------------------------------

8. Disadvantages:
- Computationally expensive
- Complex to implement
- May overfit if data is small

--------------------------------------------------

9. Important Tips:
- Works best with numerical data
- Requires proper scaling (optional but recommended)
- More iterations → better results (but slower)

--------------------------------------------------

Quick Summary:
MICE = Iterative imputation using ML models for each variable