EDA vs Feature Engineering

1. EDA (Exploratory Data Analysis)
- Purpose: Understand the data
- Focus: Analysis, visualization, patterns

What you do in EDA:
- Check missing values
- Detect outliers
- Analyze distribution (skewness)
- Find relationships (correlation)
- Use graphs (histogram, boxplot, scatter)

Goal:
→ Understand data before making changes

--------------------------------------------------

2. Feature Engineering
- Purpose: Improve model performance
- Focus: Creating and transforming features

What you do in Feature Engineering:
- Create new features (Total = Price × Quantity)
- Encode categorical data (One-Hot, Ordinal)
- Scale data (Min-Max, Standardization)
- Transform variables (log, sqrt)
- Handle missing values (imputation)

Goal:
→ Prepare data for machine learning

--------------------------------------------------

3. Key Differences

EDA:
- Understand data
- No major changes
- Visualization + analysis
- Helps in decision making

Feature Engineering:
- Modify data
- Create new features
- Apply transformations
- Improves model accuracy

--------------------------------------------------

4. Simple Example

Dataset:
Age, Salary

EDA:
- Check distribution of Age
- Find correlation between Age & Salary

Feature Engineering:
- Create new feature: Salary_per_Age
- Scale Age and Salary

--------------------------------------------------

5. Relationship

EDA → Feature Engineering

- First understand data (EDA)
- Then modify data (Feature Engineering)

--------------------------------------------------

6. Key Points:
- EDA is analysis
- Feature Engineering is transformation
- Both are essential steps in ML pipeline

--------------------------------------------------

Quick Summary:
EDA = Understand Data
Feature Engineering = Improve Data