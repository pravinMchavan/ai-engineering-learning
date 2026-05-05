# First Step Before Any Machine Learning Project

## The first step: define the problem (not the model)

Before picking an algorithm or writing training code, write a **problem statement** that is clear enough that a non-ML teammate could agree/disagree with it.

**Why this is the “first step”**
- If the problem, label, and success metric are unclear, you can build a “great model” that solves the wrong thing.
- Most ML failures are not algorithm failures—they’re **data/label/goal** mismatches.

### Key questions (quick checklist)

1) **What decision will this support?**
- Example: “Approve or reject a loan application” (decision), not “predict default” (model output).

2) **What exactly are we predicting? (target)**
- **Target/label**: the thing you want to predict (e.g., `will_churn_in_30_days`).
- Write the label definition in one sentence with a time window.

3) **What type of ML problem is it?**
- **Classification**: predict a category (e.g., spam vs not spam).
- **Regression**: predict a number (e.g., house price).
- **Ranking**: order items (e.g., search results).

4) **How will we measure success? (metric + baseline)**
- Choose a metric that matches the business goal (e.g., precision/recall, ROC-AUC, MAE).
- Define a **baseline** (a simple rule or simple model) to beat.

5) **What data is available at prediction time?**
- List input features/sources.
- Avoid **data leakage**: using information that wouldn’t exist when you make the real prediction.

6) **Constraints and risks**
- Constraints: latency, cost, privacy, regulations, interpretability.
- Risks: bias/fairness issues, feedback loops, label noise.

---

## Copy/paste: 1-page ML Project Note

Use this as your “First Step” note at the start of every project.

**Project name:**

**Problem (1 sentence):**

**Who uses the prediction?**

**Decision being supported:**

**Prediction target (label):**
- Definition:
- Time window:

**Inputs available at prediction time:**

**Success metric(s):**

**Baseline to beat:**

**How we will evaluate (split strategy):**
- Random split or time-based split?
- What is the test set representing?

**Constraints:**

**Risks / assumptions:**

**Next step after this note:**
- Do quick EDA (Exploratory Data Analysis) and validate label quality.

---

## Mini-sanity checks
- Can you explain the goal without ML words?
- If the model is wrong 10% of the time, what happens?
- Are you sure every feature is known at prediction time?
- Is your metric aligned with the real-world cost of mistakes?

