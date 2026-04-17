Ordinal Encoding (Definition + Process)

1. What is Ordinal Encoding?
- Ordinal Encoding is a technique used to convert categorical data into numerical data when the categories have a natural order (ranking).
- It assigns integers to categories based on their order or priority.

👉 Example:
Low < Medium < High
Low = 0, Medium = 1, High = 2

--------------------------------------------------

2. When to use Ordinal Encoding?
Use it when:
- Categories have meaningful order
- Rank matters

Examples:
- Education level: School < College < Degree < Masters
- Size: Small < Medium < Large
- Ratings: Poor < Average < Good < Excellent

❌ Do NOT use when:
- Categories have no order (e.g., colors, cities)

--------------------------------------------------

3. Process of Converting Categorical Data into Numerical Data:

Step 1: Identify ordered categories
Example: ["Low", "Medium", "High"]

Step 2: Define mapping based on order
Low → 0
Medium → 1
High → 2

Step 3: Replace categories with numbers in dataset

Original Data:
["Low", "High", "Medium", "Low"]

Encoded Data:
[0, 2, 1, 0]

--------------------------------------------------

4. Python Example:

from sklearn.preprocessing import OrdinalEncoder

data = [["Low"], ["High"], ["Medium"], ["Low"]]

encoder = OrdinalEncoder(categories=[["Low", "Medium", "High"]])
encoded_data = encoder.fit_transform(data)

print(encoded_data)

--------------------------------------------------

5. Key Points:
- Preserves order information
- Simple and fast
- Can mislead ML models if used on non-ordinal data

--------------------------------------------------

Quick Summary:
Ordinal Encoding = converting ordered categories into numbers based on rank
Example: Low=0, Medium=1, High=2