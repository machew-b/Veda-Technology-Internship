# A/B Testing and Regression

## Day 22: A/B Test Analysis

### Description
Analyze an A/B test comparing two groups and determine whether observed differences in a selected metric are statistically meaningful.

### Objective
Apply statistical testing to a practical experimentation problem.

### Tools
- Python
- Pandas
- NumPy
- SciPy
- Jupyter Notebook

### Deliverables
- A/B test dataset analysis
- Descriptive statistics for both groups
- Appropriate statistical test
- Final recommendation based on evidence

### Hints / Mini Guide
- Clearly define the control and treatment groups
- Compare both effect size and statistical significance
- Avoid making decisions based only on p-values

### Suggested Datasets
- A/B Testing Sample Dataset
- Marketing Campaign Dataset

### Approach
I used the `AB_Testing_Sample_Dataset.csv` file (294,478 users), clearly defining the `control` group (shown the `old_page`) and `treatment` group (shown the `new_page`), and confirming the groups matched their landing pages with a crosstab. I computed descriptive statistics for both groups on the primary metric (`converted`) and a secondary metric (`purchase_amount`). For `converted`, a binary outcome, I ran a two-proportion z-test, and computed the absolute difference, relative lift, and a 95% confidence interval for the difference in conversion rates. For `purchase_amount`, a continuous metric, I ran a Welch's t-test and computed Cohen's d as the effect size. I specifically compared the two results to demonstrate why a p-value alone isn't sufficient evidence, since both metrics came back statistically significant despite having very different effect sizes.

### Outcome
The conversion rate was 11.87% in the control group versus 17.95% in the treatment group — a ~6.1 percentage point absolute lift, a ~51% relative lift, and a 95% confidence interval of roughly (5.8, 6.3) percentage points that clearly excludes zero (z ≈ 46, p ≈ 0). Purchase amount was also significantly higher in the treatment group (p ≈ 0), but with a Cohen's d of only about 0.15 — a small effect by Cohen's own convention, despite the p-value looking just as extreme as the conversion result. This was a direct, real demonstration of why effect size matters alongside significance: with almost 300,000 users, even a small, possibly unimportant difference will register as "statistically significant," so the p-value alone can't distinguish a strong result from a weak one. **Final recommendation: launch the new page** — the conversion rate improvement is both statistically significant and practically large, which is a much stronger basis for the decision than the p-value alone would suggest.

### Interview Questions
1. **What is A/B testing?**
   A/B testing is a controlled experiment that compares two versions of something, typically a "control" (the existing version) and a "treatment" (a new version being tested), by randomly splitting users between them and measuring whether a chosen metric (like conversion rate) differs meaningfully between the two groups. It's used to make evidence-based decisions about changes before rolling them out to everyone.
2. **What is the control group?**
   The control group is the baseline group in an experiment. They are the users who experience the existing, unchanged version (in this dataset, the `old_page`). It's what the treatment group's results are compared against to determine whether the new version actually made a difference.
3. **Why should effect size be considered alongside statistical significance?**
   A p-value only tells you how likely the observed difference would be if there were truly no difference between groups (i.e., it doesn't tell you how *large* or *practically meaningful* that difference actually is). With a large enough sample size, even a tiny, unimportant difference can become "statistically significant." Effect size (like a percentage-point lift, relative lift, or Cohen's d) measures the actual magnitude of the difference, which is what ultimately matters for deciding whether a change is worth making.

---

## Day 23: Multiple Linear Regression

### Description
Build a multiple linear regression model using several numerical or encoded predictors to estimate a continuous target.

### Objective
Move beyond single-variable regression and understand multivariable prediction.

### Tools
- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

### Deliverables
- Multiple linear regression model
- Train-test evaluation
- Model coefficients
- Prediction results
- Interpretation of important features

### Hints / Mini Guide
- Separate predictors and target
- Check feature correlations
- Evaluate the model on unseen test data

### Suggested Datasets
- California Housing Dataset
- House Prices Dataset
- Diabetes Dataset

### Approach
I used the `House_Prices_Dataset.csv` file (545 houses, 13 columns), with `price` as the target. Six `yes`/`no` columns (`mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `prefarea`) were encoded to 1/0, and the three-category `furnishingstatus` column was one-hot encoded with `drop_first=True`, giving 13 numeric predictor columns in total. After checking each predictor's correlation with `price`, I split the data 80/20 into training and test sets, trained a `scikit-learn` `LinearRegression` model, and examined its coefficients. I generated predictions on the held-out test set and evaluated the model with MAE, RMSE, and R², comparing training R² against test R² to check for overfitting. Interpreting the coefficients surfaced an important nuance about feature scale: `area` had the strongest raw correlation with `price`, but a small-looking coefficient purely because of its large numeric scale compared to binary predictors like `bathrooms`.

### Outcome
The model achieved a test R² of about **0.653** (versus 0.686 on the training set — close enough to suggest reasonable generalization, not serious overfitting), an MAE of roughly 970,000, and an RMSE of roughly 1,325,000. `bathrooms` had the largest coefficient (≈+1,094,000 per additional bathroom), followed by `airconditioning` (≈+791,000) and `hotwaterheating` (≈+685,000). `area`'s coefficient looked small (≈+236 per square foot) purely because of scale — over a typical range of thousands of square feet, it still contributes substantially to predicted price, and its raw correlation with `price` (≈0.54) was actually the strongest of any single feature. This was a useful real-data lesson: a coefficient's raw size can be misleading when predictors sit on very different numeric scales, so correlation and coefficient magnitude both need to be considered together, not the coefficient alone.

### Interview Questions
1. **What is multiple linear regression?**
   Multiple linear regression is a statistical model that predicts a continuous target variable as a weighted sum of two or more predictor variables, plus an intercept, i.e., `y = b0 + b1*x1 + b2*x2 + ... + bn*xn`. It extends simple linear regression (which uses only one predictor) to account for several factors influencing the target at once.
2. **What does an individual regression coefficient represent?**
   A coefficient represents the expected change in the target variable for a one-unit increase in that specific predictor, **holding all other predictors constant**. For example, the `bathrooms` coefficient of about 1,094,000 means that, all else being equal, one additional bathroom is associated with a roughly 1,094,000 increase in predicted price.
3. **What assumptions are commonly associated with linear regression?**
   Common assumptions include: a roughly **linear relationship** between predictors and the target; **independence** of observations (errors); **homoscedasticity** (the errors have roughly constant variance across all predicted values, rather than fanning out); **normally distributed residuals**; and **low multicollinearity** among predictors (highly correlated predictors can make individual coefficients unstable and harder to interpret, even if the model's overall predictions are still fine).

---

## Day 24: Regression Metrics

### Description
Evaluate regression models using MAE, MSE, RMSE, and R² and compare the interpretation of each metric.

### Objective
Understand how regression prediction errors are measured.

### Tools
- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

### Deliverables
- Calculation of MAE, MSE, RMSE, and R²
- Comparison table
- Model evaluation
- Explanation of the most appropriate metric

### Hints / Mini Guide
- Understand the units of each metric
- Remember that MSE penalizes larger errors more strongly
- Do not rely on R² alone

### Suggested Datasets
- California Housing Dataset
- Diabetes Dataset

### Approach
This `Diabetes_Dataset.csv` is a patient-level dataset (`Patient_ID`, `Age`, `Gender`, `BMI`, `Glucose_Level`, `Blood_Pressure`, `Insulin`, `Physical_Activity`, `Family_History`, `Diabetes_Outcome`) whose "natural" target, `Diabetes_Outcome`, is a binary 0/1 label rather than a continuous value. Since regression metrics specifically need a continuous target, I instead trained a `LinearRegression` model to predict `Glucose_Level` from the patient's other recorded health data (after dropping `Patient_ID` and encoding `Gender`/`Family_History` to 0/1). I calculated MAE, MSE, and RMSE manually with NumPy and confirmed each matched `scikit-learn`'s built-in functions, then calculated R² with `scikit-learn`. To concretely demonstrate the hint that MSE penalizes larger errors more strongly, I compared two toy error sets with identical MAE but different distributions, one with four consistent errors, one with three small errors and one large outlier, showing the outlier case produces a noticeably higher RMSE despite the identical MAE. I built a comparison table covering each metric's units and sensitivity to outliers, evaluated the trained model's actual results, and explained which metric is most appropriate to lead with for this problem.

### Outcome
The model reached **MAE ≈ 24.2**, **MSE ≈ 879.1**, **RMSE ≈ 29.6**, and **R² ≈ 0.31** on the test set, meaning predictions are typically off by about 24–30 mg/dL, and the model explains roughly 31% of the variance in Glucose_Level (the rest driven by factors not captured in this dataset, like diet or medication). I concluded that **RMSE is the most appropriate primary metric** for this problem: it's in Glucose_Level's own units (unlike MSE), and it penalizes large errors more heavily than MAE. This matters here since a badly wrong glucose prediction is a more serious problem than being slightly off on several patients. R² is valuable supporting context, but as the hint warns, relying on it alone would hide exactly the kind of real-world error-size information that MAE and RMSE make directly visible.

### Interview Questions
1. **What is MAE?**
   MAE (Mean Absolute Error) is the average of the absolute differences between actual and predicted values. It's expressed in the same units as the target variable, treats every error equally regardless of size, and is one of the most directly interpretable regression metrics, i.e., "on average, predictions are off by X units."
2. **Why is RMSE sensitive to large errors?**
   RMSE is the square root of MSE, which squares each individual error before averaging them. Squaring makes large errors contribute disproportionately more to the total than small errors do (a single error of 17 contributes 289 to the sum, compared to four errors of 5 contributing only 25 each). So, a model with one very large miss will have a much higher RMSE than a model whose errors are small but more consistent, even if both have the same MAE.
3. **What does R² measure?**
   R² (the coefficient of determination) measures the proportion of variance in the target variable that the model's predictions explain, on a scale typically between 0 and 1 (it can go negative for a model that performs worse than simply predicting the average every time). An R² of 0.31 means the model explains about 31% of the variability in the target. It says nothing on its own about how large the actual prediction errors are in real units, which is why it should be reported alongside MAE/RMSE rather than in place of them.
