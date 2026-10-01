# Day 24: Regression Metrics

## Description
Evaluate regression models using MAE, MSE, RMSE, and R² and compare the interpretation of each metric.

## Objective
Understand how regression prediction errors are measured.

## Tools
- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

## Deliverables
- Calculation of MAE, MSE, RMSE, and R²
- Comparison table
- Model evaluation
- Explanation of the most appropriate metric

## Hints / Mini Guide
- Understand the units of each metric
- Remember that MSE penalizes larger errors more strongly
- Do not rely on R² alone

## Suggested Datasets
- California Housing Dataset
- Diabetes Dataset

## Approach
This `Diabetes_Dataset.csv` is a patient-level dataset (`Patient_ID`, `Age`, `Gender`, `BMI`, `Glucose_Level`, `Blood_Pressure`, `Insulin`, `Physical_Activity`, `Family_History`, `Diabetes_Outcome`) whose "natural" target, `Diabetes_Outcome`, is a binary 0/1 label rather than a continuous value. Since regression metrics specifically need a continuous target, I instead trained a `LinearRegression` model to predict `Glucose_Level` from the patient's other recorded health data (after dropping `Patient_ID` and encoding `Gender`/`Family_History` to 0/1). I calculated MAE, MSE, and RMSE manually with NumPy and confirmed each matched `scikit-learn`'s built-in functions, then calculated R² with `scikit-learn`. To concretely demonstrate the hint that MSE penalizes larger errors more strongly, I compared two toy error sets with identical MAE but different distributions, one with four consistent errors, one with three small errors and one large outlier, showing the outlier case produces a noticeably higher RMSE despite the identical MAE. I built a comparison table covering each metric's units and sensitivity to outliers, evaluated the trained model's actual results, and explained which metric is most appropriate to lead with for this problem.

## Outcome
The model reached **MAE ≈ 24.2**, **MSE ≈ 879.1**, **RMSE ≈ 29.6**, and **R² ≈ 0.31** on the test set, meaning predictions are typically off by about 24–30 mg/dL, and the model explains roughly 31% of the variance in Glucose_Level (the rest driven by factors not captured in this dataset, like diet or medication). I concluded that **RMSE is the most appropriate primary metric** for this problem: it's in Glucose_Level's own units (unlike MSE), and it penalizes large errors more heavily than MAE. This matters here since a badly wrong glucose prediction is a more serious problem than being slightly off on several patients. R² is valuable supporting context, but as the hint warns, relying on it alone would hide exactly the kind of real-world error-size information that MAE and RMSE make directly visible.

## Interview Questions
1. **What is MAE?**
   MAE (Mean Absolute Error) is the average of the absolute differences between actual and predicted values. It's expressed in the same units as the target variable, treats every error equally regardless of size, and is one of the most directly interpretable regression metrics, i.e., "on average, predictions are off by X units."
2. **Why is RMSE sensitive to large errors?**
   RMSE is the square root of MSE, which squares each individual error before averaging them. Squaring makes large errors contribute disproportionately more to the total than small errors do (a single error of 17 contributes 289 to the sum, compared to four errors of 5 contributing only 25 each). So, a model with one very large miss will have a much higher RMSE than a model whose errors are small but more consistent, even if both have the same MAE.
3. **What does R² measure?**
   R² (the coefficient of determination) measures the proportion of variance in the target variable that the model's predictions explain, on a scale typically between 0 and 1 (it can go negative for a model that performs worse than simply predicting the average every time). An R² of 0.31 means the model explains about 31% of the variability in the target. It says nothing on its own about how large the actual prediction errors are in real units, which is why it should be reported alongside MAE/RMSE rather than in place of them.