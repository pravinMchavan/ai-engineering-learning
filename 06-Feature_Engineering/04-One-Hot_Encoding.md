One-Hot Encoding (Definition + Process)

1. What is One-Hot Encoding?
- One-Hot Encoding is a technique used to convert categorical data into numerical data when categories have NO natural order.
- It creates separate binary (0/1) columns for each category.

👉 Example:
Color = [Red, Blue, Green]

After Encoding:
Red   → [1, 0, 0]
Blue  → [0, 1, 0]
Green → [0, 0, 1]

--------------------------------------------------

2. When to use One-Hot Encoding?
Use it when:
- Categories have no order
- Each category is independent

Examples:
- Colors (Red, Blue, Green)
- Cities (Mumbai, Delhi, Pune)
- Gender (Male, Female)

❌ Do NOT use when:
- Data has natural ranking (use Ordinal Encoding instead)

--------------------------------------------------

3. Process of Converting Categorical Data into Numerical Data:

Step 1: Identify unique categories
Example: ["Red", "Blue", "Green"]

Step 2: Create new columns for each category
Columns → Red, Blue, Green

Step 3: Assign binary values (1 or 0)
- If category present → 1
- Else → 0

Original Data:
["Red", "Blue", "Green", "Red"]

Encoded Data:
Red   Blue   Green
1     0      0
0     1      0
0     0      1
1     0      0

--------------------------------------------------

4. Python Example:

from sklearn.preprocessing import OneHotEncoder

data = [["Red"], ["Blue"], ["Green"], ["Red"]]

encoder = OneHotEncoder(sparse=False)
encoded_data = encoder.fit_transform(data)

print(encoded_data)

--------------------------------------------------

5. Key Points:
- No order is assumed
- Prevents model from misunderstanding relationships
- Increases number of columns (can cause high dimensionality)

--------------------------------------------------

Quick Summary:
One-Hot Encoding = converting categories into binary columns (0/1)
Example: Red=[1,0,0], Blue=[0,1,0], Green=[0,0,1]