Imputation Types + KNN Imputation Formula

1. What is Imputation?
- Imputation is the process of filling missing values in a dataset using statistical or machine learning methods.

--------------------------------------------------

2. Types of Imputation

A. Simple Imputation

1. Mean Imputation
   x_missing = mean(x)
   Use when:
   - Numerical data
   - No strong outliers

2. Median Imputation
   x_missing = median(x)
   Use when:
   - Numerical data with outliers

3. Mode Imputation
   x_missing = mode(x)
   Use when:
   - Categorical data

4. Constant Imputation
   x_missing = 0 or "Unknown"
   Use when:
   - Missing has meaning

--------------------------------------------------

B. Advanced Imputation

1. KNN Imputation
   - Uses nearest neighbors to fill missing values

2. Regression Imputation
   - Predict missing values using other variables

3. Multiple Imputation (MICE)
   - Repeats imputation multiple times for better accuracy

4. Interpolation
   - Used for time-series data

--------------------------------------------------

3. KNN Imputation Formula

Step 1: Compute distance (Euclidean distance)

For two rows (i, j):
d(i,j) = √[(x1 - y1)² + (x2 - y2)² + ... + (xn - yn)²]

--------------------------------------------------

Step 2: Find K nearest neighbors
- Select K rows with smallest distance

--------------------------------------------------

Step 3: Impute missing value

For numerical:
x_missing = (x1 + x2 + ... + xk) / k

For categorical:
x_missing = mode(x1, x2, ..., xk)

--------------------------------------------------

4. Important Notes:
- Always normalize data before KNN
- Choose K carefully (commonly 3 or 5)
- Works best when features are correlated

--------------------------------------------------

5. Quick Example

Neighbors' values: [10, 12, 14]

x_missing = (10 + 12 + 14) / 3 = 12

--------------------------------------------------

Quick Summary:
Imputation = filling missing data
KNN Imputation = use nearest neighbors + average/mode to fill values