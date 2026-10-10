# Student Performance & Learning Analytics: Final Data Science Report

**Project:** a three-day project (Days 31 to 33) from the Veda Technology Internship, Data Science track.
**Goal:** analyze student academic and learning data to identify performance patterns, subject-wise strengths and weaknesses, attendance trends, and factors associated with successful outcomes, then build introductory prediction models.

## 1. Summary

A messy student dataset of 10,000 records was cleaned into 9,991 reliable records, explored by subject, attendance, and background, and used to train two simple prediction models. The main results:

- Math is the weakest subject (average 57.2, pass rate 63.8%), and it is also the subject that separates high and low performers the most.
- Female students average about 6.1 points higher than male students overall, leading in math and writing, while male students lead slightly in reading.
- Attendance and study time are the strongest links to performance in this data (correlations of 0.37 and 0.36 with average score), **but both columns were simulated**, so these links are partly built in.
- A linear regression explains 27% of the variation in average score (test R² = 0.27, mean error 7.3 points), and a logistic regression identifies high performers with 68.7% accuracy (ROC AUC 0.73). Both beat their baselines, and a random forest performed about the same.

## 2. Data

| Item | Detail |
|------|--------|
| Source | `Student_Performance_Dataset.csv`, 10,000 rows and 12 columns (four subject scores, `total_score`, `grade`, and background columns) |
| Data quality problems | 213 rows with missing values, inconsistent `gender` and `race_ethnicity` labels, a text-typed `math_score` column |
| After cleaning | 9,991 rows, with all validation checks passing |
| Added columns | `attendance_percentage` and `study_hours_per_week`, **simulated** because the source data has neither |
| Engineered features | 13 columns on Day 32 (analysis features, encoded predictors, `engagement_score`, and the `high_performer` target) |

## 3. Methods

| Day | Focus | What was done |
|-----|-------|---------------|
| 31 | Cleaning, EDA, attendance | Built a three-step cleaning pipeline that recovered 80 subject scores, 16 totals, 3 grades, and 1 roll number from the data itself, and dropped only 9 rows. Explored distributions, grades, and group averages, and analyzed attendance by grade and by band. |
| 32 | Subjects, correlation, features | Compared the four subjects, built a correlation matrix and heatmap with p-values, made five visualizations, and engineered 13 features, with a table of which columns must stay out of the model to avoid leakage. |
| 33 | Modeling | Split the data 80/20 once, trained a linear regression and a logistic regression against baselines, validated with 5-fold cross-validation, and compared against a random forest. |

## 4. Key Findings

1. **Math is the weak spot.** Average scores are 57.2 for math, compared with 71.4 for writing, and only 39.9% of students passed all four subjects at a 50-point mark (an assumed cutoff).
2. **Attendance tracks performance.** Average attendance falls from 85.9% for grade A to 69.0% for Fail, and average scores rise from 55.9 to 71.9 across the attendance bands. About 30% of students are below a 75% attendance line.
3. **Background matters little, with one exception.** Test preparation, lunch type, and parental education barely move scores, but the gender gap is clear.
4. **The subject scores are almost uncorrelated with each other** (-0.04 to 0.10). In real student data they would normally move together, which suggests the scores were generated independently.
5. **Coefficients need care.** In the regression, `test_preparation_course` has a negative coefficient (-2.5) even though the course alone goes with a gain of +0.9 points, because study hours were simulated to be higher for students who took the course. The sign is an artifact of overlapping predictors, not evidence that the course hurts.

## 5. Model Results (test set of 1,999 students)

| Task | Model | Result | Baseline |
|------|-------|--------|----------|
| Predict `average_score` | Linear regression | R² 0.27, MAE 7.3, RMSE 9.1 | MAE 8.6 (predict the mean) |
| Predict `high_performer` | Logistic regression | Accuracy 68.7%, precision 62%, recall 49%, F1 0.55, ROC AUC 0.73 | Accuracy 61.0% (most common class) |
| Both | Random forest | R² 0.26, accuracy 69.2% | About the same as the simple models |

Cross-validation on the training data gave R² between 0.26 and 0.31 and accuracy between 67.5% and 69.4%, matching the test results, so the models are not overfit. The strongest drivers in both models were study hours, attendance, and gender. The logistic regression is cautious: at the default 0.5 cutoff it finds 383 of the 779 real high performers and misses 396.

## 6. Limitations

- **Two key columns are simulated.** Attendance and study hours were generated with a built-in link to performance, so the relationships and the model coefficients involving them demonstrate the workflow and are not findings about real students.
- **The dataset appears synthetic.** The near-zero correlations between subjects and the weak effect of background columns are unusual for real data.
- **Modest predictive power.** The models explain only part of the variation, and the classifier misses about half of the real high performers at the default cutoff.
- **Assumed thresholds.** The 50-point pass mark, the 70-point `high_performer` cutoff, and the 75% attendance line were chosen for analysis and are not official.
- **Not for decisions about students.** The gender and background patterns are descriptive patterns in this dataset. These models are a learning exercise and should not be used to make decisions about individual students.

## 7. Recommendations and Next Steps

1. Replace the simulated columns with real attendance and study-time records (for example, the UCI Student Performance dataset includes absences and study time) and repeat the analysis.
2. Tune the classification cutoff to trade precision against recall, depending on whether missing a high performer or flagging the wrong student is the bigger problem.
3. Add features that carry real signal, such as prior-term grades or assignment submission rates.
4. Collect more than one measurement per student over time, so that trends, not just snapshots, can be analyzed.

## 8. Repository Documentation

**Repository:** `Veda-Technology-Internship`

```
Veda-Technology-Internship/
├── datasets/
│   ├── Student_Performance_Dataset.csv          # raw data (Day 31 input)
│   ├── Student_Learning_Analytics_Cleaned.csv   # created by Day 31, read by Day 32
│   └── Student_Learning_Analytics_Features.csv  # created by Day 32, read by Day 33
├── day-31/   # cleaning pipeline, EDA, attendance analysis
├── day-32/   # subject analysis, correlation, visualizations, feature engineering
└── day-33/   # prediction models, evaluation, this report
```

Each day folder contains a `README.md` and a notebook named `student_performance_and_learning_analytics.ipynb`.

**How to reproduce:**

1. Install Python 3 with `pandas`, `numpy`, `matplotlib`, `scipy`, `scikit-learn`, and `jupyter`.
2. Run the notebooks in order: `day-31`, then `day-32`, then `day-33`. Each notebook reads its input from `../datasets/` and, for Days 31 and 32, writes the file the next day needs.
3. The simulated columns use a fixed random seed (`42`) and the train/test split uses `random_state=42`, so the results are reproducible.
