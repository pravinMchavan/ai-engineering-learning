Outlier Detection (Definition + Methods + When to Use)

1. What is an Outlier?
- An outlier is a data point that is significantly different from other values in the dataset.
- It can be unusually high or low.

Example:
[10, 12, 14, 15, 18, 100] → 100 is an outlier

--------------------------------------------------

2. Why Detect Outliers?
- Can distort mean and standard deviation
- Can reduce model accuracy
- Important for data cleaning and analysis

--------------------------------------------------

3. Methods of Outlier Detection

A. IQR Method (Most Common)

Step 1: Calculate Q1 (25th percentile)
Step 2: Calculate Q3 (75th percentile)
Step 3: IQR = Q3 - Q1

Step 4: Define bounds
Lower Bound = Q1 - 1.5 * IQR
Upper Bound = Q3 + 1.5 * IQR

Step 5: Detect outliers
- Value < Lower Bound OR Value > Upper Bound

--------------------------------------------------

B. Z-Score Method

Formula:
Z = (x - mean) / std

Rule:
- |Z| > 3 → Outlier

Use when:
- Data is normally distributed

--------------------------------------------------

C. Modified Z-Score (Robust)

Formula:
Modified Z = 0.6745 * (x - median) / MAD

Rule:
- |Modified Z| > 3.5 → Outlier

Use when:
- Outliers present
- Data not normal

--------------------------------------------------

D. Isolation Forest (ML Method)

- Uses tree-based model to isolate outliers
- Works well for large datasets

--------------------------------------------------

E. DBSCAN (Clustering Method)

- Points far from clusters are outliers

--------------------------------------------------

4. Python Example (IQR Method)

import pandas as pd

data = [10, 12, 14, 15, 18, 100]
df = pd.DataFrame({'Value': data})

Q1 = df['Value'].quantile(0.25)
Q3 = df['Value'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df['Outlier'] = (df['Value'] < lower) | (df['Value'] > upper)

print(df)

--------------------------------------------------

5. What to Do After Detecting Outliers?

- Remove → if error or noise
- Cap (Winsorization) → limit extreme values
- Transform → log or scaling
- Keep → if meaningful (e.g., fraud detection)

--------------------------------------------------

6. Key Points:
- Always visualize data (boxplot, histogram)
- Choose method based on data distribution
- Not all outliers are bad

--------------------------------------------------

Quick Summary:
Outlier = extreme value
IQR, Z-score → common detection methods