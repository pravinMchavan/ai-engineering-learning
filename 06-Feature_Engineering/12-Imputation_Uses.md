Imputation: which to use (quick guide)

 Mean:
 - Use for numerical data
 - When data is normally distributed (no outliers)

 Median:
 - Use for numerical data with outliers
 - Robust to skewed data

 Mode:
 - Use for categorical data
 - Fills with most frequent value

 KNN Imputation:
 - Use when data has patterns/relationships
 - Works for numerical data, but slower

 MICE (Iterative Imputer):
 - Use for complex datasets with multiple features
 - Gives more accurate results but computationally expensive

 Constant (0, "Unknown"):
 - Use when missing has meaning or as placeholder

 Forward/Backward Fill:
 - Use for time-series data

 Rule of thumb:
 - Simple data → Mean/Median/Mode
 - Complex data → KNN or MICE