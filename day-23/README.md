# Day 23: Multiple Linear Regression

## Description
Build a multiple linear regression model using several numerical or encoded predictors to estimate a continuous target.

## Objective
Move beyond single-variable regression and understand multivariable prediction.

## Tools
- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

## Deliverables
- Multiple linear regression model
- Train-test evaluation
- Model coefficients
- Prediction results
- Interpretation of important features

## Hints / Mini Guide
- Separate predictors and target
- Check feature correlations
- Evaluate the model on unseen test data

## Suggested Datasets
- California Housing Dataset
- House Prices Dataset
- Diabetes Dataset

## Approach
I used the `House_Prices_Dataset.csv` file (545 houses, 13 columns), with `price` as the target. Six `yes`/`no` columns (`mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `prefarea`) were encoded to 1/0, and the three-category `furnishingstatus` column was one-hot encoded with `drop_first=True`, giving 13 numeric predictor columns in total. After checking each predictor's correlation with `price`, I split the data 80/20 into training and test sets, trained a `scikit-learn` `LinearRegression` model, and examined its coefficients. I generated predictions on the held-out test set and evaluated the model with MAE, RMSE, and R², comparing training R² against test R² to check for overfitting. Interpreting the coefficients surfaced an important nuance about feature scale: `area` had the strongest raw correlation with `price`, but a small-looking coefficient purely because of its large numeric scale compared to binary predictors like `bathrooms`.

## Outcome
The model achieved a test R² of about **0.653** (versus 0.686 on the training set — close enough to suggest reasonable generalization, not serious overfitting), an MAE of roughly 970,000, and an RMSE of roughly 1,325,000. `bathrooms` had the largest coefficient (≈+1,094,000 per additional bathroom), followed by `airconditioning` (≈+791,000) and `hotwaterheating` (≈+685,000). `area`'s coefficient looked small (≈+236 per square foot) purely because of scale — over a typical range of thousands of square feet, it still contributes substantially to predicted price, and its raw correlation with `price` (≈0.54) was actually the strongest of any single feature. This was a useful real-data lesson: a coefficient's raw size can be misleading when predictors sit on very different numeric scales, so correlation and coefficient magnitude both need to be considered together, not the coefficient alone.

## Interview Questions
1. **What is multiple linear regression?**
   Multiple linear regression is a statistical model that predicts a continuous target variable as a weighted sum of two or more predictor variables, plus an intercept, i.e., `y = b0 + b1*x1 + b2*x2 + ... + bn*xn`. It extends simple linear regression (which uses only one predictor) to account for several factors influencing the target at once.
2. **What does an individual regression coefficient represent?**
   A coefficient represents the expected change in the target variable for a one-unit increase in that specific predictor, **holding all other predictors constant**. For example, the `bathrooms` coefficient of about 1,094,000 means that, all else being equal, one additional bathroom is associated with a roughly 1,094,000 increase in predicted price.
3. **What assumptions are commonly associated with linear regression?**
   Common assumptions include: a roughly **linear relationship** between predictors and the target; **independence** of observations (errors); **homoscedasticity** (the errors have roughly constant variance across all predicted values, rather than fanning out); **normally distributed residuals**; and **low multicollinearity** among predictors (highly correlated predictors can make individual coefficients unstable and harder to interpret, even if the model's overall predictions are still fine).