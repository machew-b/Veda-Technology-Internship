# Day 25: Logistic Regression Classification

## Description
Build a logistic regression model for binary classification and evaluate its predictions on unseen data.

## Objective
Understand one of the most important baseline classification algorithms.

## Tools
- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

## Deliverables
- Preprocessed dataset
- Logistic regression model
- Predictions
- Accuracy and classification report
- Short model interpretation

## Hints / Mini Guide
- Encode categorical variables when necessary
- Scale numerical features when appropriate
- Use `predict_proba()` to inspect predicted probabilities

## Suggested Datasets
- Breast Cancer Wisconsin Dataset
- Titanic Dataset
- Bank Marketing Dataset

## Approach
I used the `Bank_Marketing_Dataset.csv` file (11,162 customers, 17 columns), predicting whether a customer subscribed to a term `deposit` (yes/no). I encoded the target and three simple yes/no predictor columns (`default`, `housing`, `loan`) to 0/1, and one-hot encoded six multi-category text columns (`job`, `marital`, `education`, `contact`, `month`, `poutcome`). After a stratified 80/20 train-test split, I standardized the 7 numeric columns using a `StandardScaler` fit only on the training data, to avoid leaking test-set information. I trained a `LogisticRegression` model, generated predictions on the held-out test set, inspected the underlying predicted probabilities with `predict_proba()`, and evaluated the model with accuracy, a full classification report, and a confusion matrix. For interpretation, I examined the model's coefficients to see which features most strongly pushed predictions toward "yes" or "no".

## Outcome
The model reached about **82.5% accuracy** on the test set, with balanced precision and recall for both classes (0.82/0.85 for "no", 0.83/0.80 for "yes") on a dataset where the two classes are themselves fairly balanced (≈53% no / 47% yes). The strongest predictor was `poutcome_success` (a successful previous campaign outcome strongly predicts subscribing again), followed closely by `duration` (call duration), which comes with an important real-world caveat: a call's duration is only known *after* the call happens, so it wouldn't actually be available if predicting *before* calling a customer, and would typically be dropped in a genuine deployment to avoid this kind of data leakage even though it boosts this model's apparent accuracy. Several `month` dummy variables also showed a real seasonal pattern in subscription likelihood. This was a useful reminder that a strong-looking coefficient doesn't automatically mean a feature is safe or appropriate to use in practice.

## Interview Questions
1. **What is logistic regression?**
   Logistic regression is a statistical model used for binary (or multi-class) classification. Instead of predicting a continuous value directly like linear regression, it models the *probability* that an observation belongs to a particular class, by passing a weighted sum of the predictors through the sigmoid function, which squashes the output into a range between 0 and 1.
2. **Why is logistic regression used for classification?**
   Because its output is a probability between 0 and 1 (via the sigmoid function), rather than an unbounded number like plain linear regression would produce. That probability can be directly interpreted ("this customer has a 73% chance of subscribing") and converted into a class prediction by applying a threshold (commonly 0.5), making it a natural fit for classification problems.
3. **What does `predict_proba()` return?**
   `predict_proba()` returns the model's predicted probability for each possible class, for every row; for binary classification, an array with two columns per row: the probability of class 0 and the probability of class 1 (which always sum to 1). This is more informative than `predict()` alone, since it shows how confident the model actually is, rather than just the final thresholded class label.