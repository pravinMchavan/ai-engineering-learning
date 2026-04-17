Handling Mixed Variables in a Dataset

1. What are Mixed Variables?
- A dataset containing different types of features:
  • Numerical (age, salary)
  • Categorical (gender, city)
  • Ordinal (low, medium, high)
  • Binary (yes/no)

--------------------------------------------------

2. Why Handling is Important?
- ML models require numerical input
- Different data types need different preprocessing
- Wrong handling → poor model performance

--------------------------------------------------

3. Step-by-Step Process

Step 1: Identify variable types
- Numerical → int, float
- Categorical → object/string
- Ordinal → ordered categories

--------------------------------------------------

Step 2: Handle Missing Values
- Numerical → fill with mean/median
- Categorical → fill with mode or "Unknown"

--------------------------------------------------

Step 3: Encode Categorical Variables

A. Nominal (no order)
→ Use One-Hot Encoding

B. Ordinal (has order)
→ Use Ordinal Encoding

--------------------------------------------------

Step 4: Scale Numerical Features

- No outliers → Min-Max Scaling
- Normal data → Standardization
- Outliers present → Robust Scaling

--------------------------------------------------

Step 5: Handle Skewness (if needed)
- Use log(x+1), sqrt, or Box-Cox

--------------------------------------------------

Step 6: Combine all features
- Merge processed numerical + encoded categorical data

--------------------------------------------------

4. Python Example (Basic Pipeline)

import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

# Example Data
df = pd.DataFrame({
    'Age': [25, 30, 35],
    'Gender': ['Male', 'Female', 'Male'],
    'Level': ['Low', 'Medium', 'High']
})

# One-Hot Encoding (Nominal)
df = pd.get_dummies(df, columns=['Gender'])

# Ordinal Encoding
ord_map = {'Low': 0, 'Medium': 1, 'High': 2}
df['Level'] = df['Level'].map(ord_map)

# Scaling
scaler = StandardScaler()
df['Age'] = scaler.fit_transform(df[['Age']])

print(df)

--------------------------------------------------

5. Advanced Method (Best Practice)

Use ColumnTransformer:

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

- Automatically handles mixed data types
- Clean and scalable

--------------------------------------------------

6. Key Points:
- Treat each variable type differently
- Never apply same method to all columns
- Encoding + Scaling are must steps

--------------------------------------------------

Quick Summary:
Mixed Data = Numerical + Categorical + Ordinal
→ Encode categorical
→ Scale numerical
→ Combine all features for ML