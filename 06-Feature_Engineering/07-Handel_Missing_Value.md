Handling Missing Data in a Dataset

1. What is Missing Data?
- Missing data occurs when no value is stored for a variable.
- Represented as NaN, NULL, or empty cells.

--------------------------------------------------

2. Why Handling is Important?
- ML models cannot handle missing values directly
- Can reduce accuracy and create bias

--------------------------------------------------

3. Types of Missing Data

1. MCAR (Missing Completely at Random)
   → No pattern in missing data

2. MAR (Missing at Random)
   → Missing depends on other variables

3. MNAR (Missing Not at Random)
   → Missing depends on the value itself

--------------------------------------------------

4. Methods to Handle Missing Data

A. Deletion Methods

1. Row Deletion (Drop rows)
   df.dropna()

   Use when:
   - Very few missing values
   - Dataset is large

2. Column Deletion (Drop columns)
   df.dropna(axis=1)

   Use when:
   - Column has too many missing values

--------------------------------------------------

B. Imputation Methods

1. Mean Imputation (Numerical)
   df['col'].fillna(df['col'].mean())

   Use when:
   - Data is normally distributed
   - No strong outliers

2. Median Imputation (Numerical)
   df['col'].fillna(df['col'].median())

   Use when:
   - Outliers present

3. Mode Imputation (Categorical)
   df['col'].fillna(df['col'].mode()[0])

   Use when:
   - Categorical data

4. Constant Value
   df['col'].fillna(0) or "Unknown"

   Use when:
   - Missing has meaning

--------------------------------------------------

C. Advanced Methods

1. KNN Imputation
   - Uses nearest neighbors

2. Regression Imputation
   - Predict missing values using other features

3. Interpolation
   - Used for time-series data

--------------------------------------------------

5. Python Example

import pandas as pd

df = pd.DataFrame({
    'Age': [25, None, 30, 35],
    'City': ['Mumbai', None, 'Pune', 'Delhi']
})

# Fill numerical with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill categorical with mode
df['City'] = df['City'].fillna(df['City'].mode()[0])

print(df)

--------------------------------------------------

6. Best Practice Strategy

- Small missing → Drop rows
- Many missing → Impute
- Numerical + outliers → Median
- Categorical → Mode
- Time series → Interpolation

--------------------------------------------------

7. Key Points:
- Always analyze missing pattern first
- Avoid blindly dropping data
- Choose method based on data type

--------------------------------------------------

Quick Summary:
Missing Data → Detect → Analyze → Impute or Delete → Use clean data