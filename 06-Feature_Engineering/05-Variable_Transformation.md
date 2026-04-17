Variable Transformation (Definition + Types + When to Use)

1. What is Variable Transformation?
- Variable Transformation means changing the scale or distribution of data to improve model performance.
- It helps in handling skewness, outliers, and non-linear relationships.

--------------------------------------------------

2. Why use Variable Transformation?
- To make data more normal (Gaussian distribution)
- To reduce skewness
- To handle outliers
- To improve model accuracy
- To meet assumptions of ML models (like Linear Regression)

--------------------------------------------------

3. Types of Variable Transformation:

A. Log Transformation
Formula:
   x' = log(x) or log(x + 1)

Use when:
- Data is right-skewed
- Large values need compression

Note:
- Use log(x+1) if zeros are present

--------------------------------------------------

B. Square Root Transformation
Formula:
   x' = √x

Use when:
- Moderate skewness
- Data has small values

--------------------------------------------------

C. Square Transformation
Formula:
   x' = x²

Use when:
- Left-skewed data
- Want to increase differences between values

--------------------------------------------------

D. Reciprocal Transformation
Formula:
   x' = 1/x

Use when:
- Highly skewed data
- Large values need strong reduction

Note:
- Cannot use when x = 0

--------------------------------------------------

E. Box-Cox Transformation
- Automatically finds best transformation

Use when:
- Data is positive (>0)
- Want near-normal distribution

--------------------------------------------------

F. Yeo-Johnson Transformation
- Extension of Box-Cox

Use when:
- Data includes zero or negative values

--------------------------------------------------

G. Scaling (Normalization & Standardization)

1. Min-Max Scaling:
   x' = (x - min) / (max - min)

Use when:
- No outliers
- Need values between 0 and 1

2. Standardization (Z-score):
   x' = (x - mean) / std

Use when:
- Data is normally distributed
- Used in ML algorithms like SVM, Logistic Regression

3. Robust Scaling:
   x' = (x - median) / IQR

Use when:
- Outliers are present

--------------------------------------------------

4. Quick Decision Guide:

- Right skewed → Log / Root
- Left skewed → Square
- Heavy outliers → Robust Scaling
- Need normal distribution → Box-Cox / Yeo-Johnson
- Zeros present → log(x+1) or Yeo-Johnson
- No outliers → Min-Max Scaling

--------------------------------------------------

5. Key Points:
- Always visualize data before transformation
- Choose transformation based on data distribution
- Different models may require different transformations

--------------------------------------------------

Quick Summary:
Variable Transformation = changing data to improve model performance