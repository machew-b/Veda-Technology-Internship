# Day 33: Student Performance & Learning Analytics

## Description
Build a data science system that analyzes student academic and learning data to identify performance patterns, subject-wise strengths and weaknesses, attendance trends, and factors associated with successful outcomes.

## Objective
Learn the complete basic data science workflow from data cleaning and exploratory analysis to visualization, statistical analysis, and introductory predictive modeling.

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Excel
- Git/GitHub

## Deliverables
- Basic prediction model
- Model evaluation
- Final data science report
- GitHub documentation

## Hints / Mini Guide
- Use a public or synthetic student dataset.
- Handle missing values and inconsistent records.
- Analyze relationships between attendance, study time and performance.
- Start with linear regression or classification depending on the target variable.
- Clearly separate training and testing data.

## Approach
I used `Student_Learning_Analytics_Features.csv`, the dataset I saved on Day 32 with the engineered features. Before modeling, I picked 10 predictors (`attendance_percentage`, `study_hours_per_week`, `test_preparation_course`, `lunch`, `gender_female`, `parent_education_rank`, and the `race_group_B` to `race_group_E` dummies) and added an `assert` so that no column built from the scores, such as `average_score`, `grade`, or `high_performer`, could slip in as a predictor and cause data leakage. I left out `engagement_score` and `attendance_level` because they are rearranged versions of attendance and study hours. I used `train_test_split()` once with an 80/20 split, `random_state=42`, and `stratify` on `high_performer`, giving 7,992 training and 1,999 test students, and kept the test set untouched until each model was evaluated. For regression, I compared a `LinearRegression` predicting `average_score` against a `DummyRegressor` baseline that always predicts the mean, using R², MAE, and RMSE on both the training and test sets, plus 5-fold cross-validation on the training data, a coefficient table, and predicted-versus-actual and residual plots. For classification, I compared a `LogisticRegression` (inside a pipeline with `StandardScaler`, so the scaler is fitted on the training data only) predicting `high_performer` against a `DummyClassifier` that always predicts the most common class, using accuracy, precision, recall, F1, ROC AUC, a confusion matrix, an ROC curve, and standardized coefficients. As a check on model complexity, I repeated both tasks with a random forest. I also wrote the final data science report as `final_report.md`, which summarizes the whole three-day project and documents the repository structure and how to reproduce the results.

## Outcome
By the end of this task, I could build, evaluate, and interpret basic prediction models using a proper train/test separation and baselines to compare against. The linear regression reached a test R² of 0.27 and a mean absolute error of 7.3 points (versus 8.6 for the mean baseline), and the logistic regression reached 68.7% accuracy and a ROC AUC of 0.73 (versus 61.0% accuracy for the majority-class baseline). Both beat their baselines, with training and cross-validation scores that matched the test results, but the models explain only part of the variation, and the logistic regression finds about 49% of the real high performers. A random forest performed about the same, so the simpler and more explainable models were kept. The most useful lesson was the negative coefficient on `test_preparation_course` (-2.5): on its own the course goes with a gain of +0.9 points, and the negative sign only appears because study hours were simulated to be higher for students who took the course. That showed me that a coefficient depends on which other predictors are in the model and should not be read in isolation. Since attendance and study hours were simulated on Day 31, the model results demonstrate the workflow rather than real findings about students.

## Interview Questions
1. **Why do you separate training and testing data?**
   The training data is used to fit the model, and the test data is kept aside to measure how well the model works on students it has never seen. If a model were evaluated on the same data it learned from, the score would only show how well it memorized, not how well it generalizes, i.e., an overfit model can look excellent on training data and perform poorly on new data. Keeping the test set untouched until the end, and fitting steps like scaling on the training data only, keeps the evaluation honest.
2. **What are precision and recall, and why is accuracy alone not enough for classification?**
   Precision is the share of predicted positives that are truly positive, and recall is the share of real positives that the model manages to find. Accuracy can hide problems, especially when the classes are imbalanced, e.g., a model that always predicts the majority class can still score 61% accuracy here while finding none of the high performers. In this project the logistic regression had a precision of 62% but a recall of only 49%, which an accuracy of 69% alone would not have shown.
3. **What is a baseline model, and why compare against one?**
   A baseline is a deliberately simple model, such as always predicting the mean (regression) or the most common class (classification). It sets the minimum bar that a real model has to beat, so a score is only meaningful relative to it. For example, an R² of 0.27 sounds weak by itself, but it reflects a mean absolute error of 7.3 points compared to 8.6 for the baseline, which shows the model is learning something real, if modest.