# Day 27: Confusion Matrix and Threshold Tuning

## Description
Analyze classification predictions using a confusion matrix and investigate how changing the classification threshold affects precision and recall.

## Objective
Understand the relationship between probability thresholds and classification performance.

## Tools
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

## Deliverables
- Confusion matrix visualization
- Results for multiple probability thresholds
- Precision-recall comparison
- Recommended threshold with justification

## Hints / Mini Guide
- Use `predict_proba()`
- Test several thresholds
- Consider the cost of false positives and false negatives

## Suggested Datasets
- Breast Cancer Wisconsin Dataset
- Customer Churn Dataset

## Approach
I rebuilt the same logistic regression churn model from Day 26 on `Customer_Churn_Dataset.csv`, using `predict_proba()` to get each test customer's probability of churning instead of jumping straight to a 0/1 label. I visualized the confusion matrix at the default 0.5 threshold with a Seaborn heatmap, then tested five thresholds (0.3, 0.4, 0.5, 0.6, 0.7), calculating precision, recall, F1-score, and the full confusion matrix breakdown at each one. I compared the results both as a line chart of precision/recall/F1 against threshold, and as a full precision-recall curve using `scikit-learn`'s `precision_recall_curve()`. Finally, applying the same business reasoning from Day 26 — a missed churner (False Negative) typically costs more than an unnecessary retention offer (False Positive) — I recommended a specific threshold and quantified exactly what trade-off it makes compared to the default.

## Outcome
As the threshold increased from 0.3 to 0.7, precision rose steadily (0.729 → 0.878) while recall fell (0.919 → 0.656) — the classic precision-recall trade-off, visible in both the line chart and the precision-recall curve. I recommended lowering the threshold from the default **0.5 to 0.4**: this catches **325 more actual churners** (missed churners drop from 1,077 to 752) at the cost of **409 more false alarms** (unnecessary retention offers). This is a trade worth making given a lost customer is typically far more costly than a wasted retention offer. As a bonus, 0.4 also produced the **best F1-score of any threshold tested** (0.822 vs. 0.819 at 0.5), so this wasn't a case of sacrificing overall balance just to chase recall; rather, it was a genuine improvement on both fronts. This showed that the default 0.5 threshold is just a starting point, not automatically the right choice for a specific business problem.

## Interview Questions
1. **What is a confusion matrix?**
   A confusion matrix is a table that breaks down a classification model's predictions against the actual outcomes, showing counts of True Positives, True Negatives, False Positives, and False Negatives. It gives a much more detailed picture of model performance than accuracy alone, since it shows exactly what kinds of mistakes the model is making, not just how many.
2. **How does changing the threshold affect recall?**
   Lowering the classification threshold makes the model predict the positive class more readily (since a lower probability is now enough to count as a positive prediction), which generally **increases recall** (i.e., more of the actual positive cases get caught) but tends to **decrease precision**, since the model is also now flagging more cases that turn out to be negative. Raising the threshold has the opposite effect: recall drops, precision rises.
3. **Why might the default 0.5 threshold not be optimal?**
   A 0.5 threshold treats a False Positive and a False Negative as equally costly mistakes, which is rarely true in a real business problem. In this churn example, missing an actual churner is more expensive than wasting a retention offer on someone who wasn't leaving, so a lower threshold that favors recall over precision can produce a better real-world outcome than the default. That is, even if 0.5 isn't technically "wrong" in a vacuum, it's not tailored to the specific costs involved in this decision.