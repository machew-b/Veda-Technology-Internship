# Day 26: Classification Metrics Deep Dive

## Description
Evaluate a classification model using accuracy, precision, recall, F1-score, and support, and determine when each metric is useful.

## Objective
Develop a deeper understanding of classification model evaluation.

## Tools
- Python
- Pandas
- Scikit-learn
- Jupyter Notebook

## Deliverables
- Classification report
- Metric comparison
- Business or practical interpretation of metrics
- Recommendation of the most suitable metric

## Hints / Mini Guide
- Understand false positives and false negatives
- Do not assume accuracy is always the best metric
- Consider the cost of different errors

## Suggested Datasets
- Breast Cancer Wisconsin Dataset
- Customer Churn Dataset

## Approach
I used the `Customer_Churn_Dataset.csv` file (64,374 customers), training a `LogisticRegression` model on an 80/20 stratified split to predict `Churn` (1 = yes, 0 = no) after encoding `Gender`, `Subscription Type`, and `Contract Length` and scaling the numeric columns. I pulled the confusion matrix counts (TN, FP, FN, TP) directly and used them to explain what a False Positive (predicting churn for a customer who stays) and a False Negative (missing a customer who actually churns) mean in this context. I calculated accuracy, precision, recall, and F1-score manually from those same counts and confirmed they matched `scikit-learn`'s built-in `classification_report`, then built a comparison table of each metric's formula and what it actually answers. To demonstrate why accuracy alone can mislead, I compared the trained model against a naive baseline that always predicts the majority class. Finally, I reasoned through the real business cost of each error type to recommend the most suitable metric for this specific problem.

## Outcome
The model reached **82.7% accuracy**, **81% precision** and **82% recall** for the Churn class, and **83%/85%** precision/recall for No Churn — a solid, fairly balanced result (TN=5,628, FP=1,148, FN=1,077, TP=5,022). The naive always-predict-majority-class baseline scored a deceptively reasonable **52.6% accuracy** while catching **zero** actual churners (0% recall for Churn) — a direct demonstration of why accuracy alone can hide a model with no real skill. Reasoning through the business cost of each error — a False Positive wastes a retention offer on a customer who was never leaving, while a False Negative loses that customer and their future revenue entirely — led to recommending **recall** as the primary metric for this problem, with F1-score tracked alongside it as a safeguard against chasing recall at the expense of precision. This made concrete why the "right" metric depends on which kind of mistake actually costs the business more, not on which metric simply looks the highest.

## Interview Questions
1. **What is precision?**
   Precision measures, out of everyone the model predicted as positive (e.g., predicted to churn), what fraction actually were positive: `TP / (TP + FP)`. High precision means few False Positives, i.e., when the model says "churn," it's usually right.
2. **What is recall?**
   Recall measures, out of everyone who actually was positive (e.g., actually churned), what fraction the model correctly identified: `TP / (TP + FN)`. High recall means few False Negatives, i.e., the model misses very few of the actual positive cases.
3. **When is F1-score useful?**
   F1-score is the harmonic mean of precision and recall, giving a single number that balances both. It's especially useful when you need one overall metric to compare models (rather than tracking precision and recall separately), when the classes are imbalanced (making plain accuracy unreliable), or when there isn't a clear reason to prioritize one of precision/recall heavily over the other. Note that F1 penalizes a model that's very strong in one but very weak in the other, unlike a simple average would.