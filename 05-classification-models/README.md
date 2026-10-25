# Classification Models

## Day 25: Logistic Regression Classification

### Description
Build a logistic regression model for binary classification and evaluate its predictions on unseen data.

### Objective
Understand one of the most important baseline classification algorithms.

### Tools
- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

### Deliverables
- Preprocessed dataset
- Logistic regression model
- Predictions
- Accuracy and classification report
- Short model interpretation

### Hints / Mini Guide
- Encode categorical variables when necessary
- Scale numerical features when appropriate
- Use `predict_proba()` to inspect predicted probabilities

### Suggested Datasets
- Breast Cancer Wisconsin Dataset
- Titanic Dataset
- Bank Marketing Dataset

### Approach
I used the `Bank_Marketing_Dataset.csv` file (11,162 customers, 17 columns), predicting whether a customer subscribed to a term `deposit` (yes/no). I encoded the target and three simple yes/no predictor columns (`default`, `housing`, `loan`) to 0/1, and one-hot encoded six multi-category text columns (`job`, `marital`, `education`, `contact`, `month`, `poutcome`). After a stratified 80/20 train-test split, I standardized the 7 numeric columns using a `StandardScaler` fit only on the training data, to avoid leaking test-set information. I trained a `LogisticRegression` model, generated predictions on the held-out test set, inspected the underlying predicted probabilities with `predict_proba()`, and evaluated the model with accuracy, a full classification report, and a confusion matrix. For interpretation, I examined the model's coefficients to see which features most strongly pushed predictions toward "yes" or "no".

### Outcome
The model reached about **82.5% accuracy** on the test set, with balanced precision and recall for both classes (0.82/0.85 for "no", 0.83/0.80 for "yes") on a dataset where the two classes are themselves fairly balanced (≈53% no / 47% yes). The strongest predictor was `poutcome_success` (a successful previous campaign outcome strongly predicts subscribing again), followed closely by `duration` (call duration), which comes with an important real-world caveat: a call's duration is only known *after* the call happens, so it wouldn't actually be available if predicting *before* calling a customer, and would typically be dropped in a genuine deployment to avoid this kind of data leakage even though it boosts this model's apparent accuracy. Several `month` dummy variables also showed a real seasonal pattern in subscription likelihood. This was a useful reminder that a strong-looking coefficient doesn't automatically mean a feature is safe or appropriate to use in practice.

### Interview Questions
1. **What is logistic regression?**
   Logistic regression is a statistical model used for binary (or multi-class) classification. Instead of predicting a continuous value directly like linear regression, it models the *probability* that an observation belongs to a particular class, by passing a weighted sum of the predictors through the sigmoid function, which squashes the output into a range between 0 and 1.
2. **Why is logistic regression used for classification?**
   Because its output is a probability between 0 and 1 (via the sigmoid function), rather than an unbounded number like plain linear regression would produce. That probability can be directly interpreted ("this customer has a 73% chance of subscribing") and converted into a class prediction by applying a threshold (commonly 0.5), making it a natural fit for classification problems.
3. **What does `predict_proba()` return?**
   `predict_proba()` returns the model's predicted probability for each possible class, for every row; for binary classification, an array with two columns per row: the probability of class 0 and the probability of class 1 (which always sum to 1). This is more informative than `predict()` alone, since it shows how confident the model actually is, rather than just the final thresholded class label.

---

## Day 26: Classification Metrics Deep Dive

### Description
Evaluate a classification model using accuracy, precision, recall, F1-score, and support, and determine when each metric is useful.

### Objective
Develop a deeper understanding of classification model evaluation.

### Tools
- Python
- Pandas
- Scikit-learn
- Jupyter Notebook

### Deliverables
- Classification report
- Metric comparison
- Business or practical interpretation of metrics
- Recommendation of the most suitable metric

### Hints / Mini Guide
- Understand false positives and false negatives
- Do not assume accuracy is always the best metric
- Consider the cost of different errors

### Suggested Datasets
- Breast Cancer Wisconsin Dataset
- Customer Churn Dataset

### Approach
I used the `Customer_Churn_Dataset.csv` file (64,374 customers), training a `LogisticRegression` model on an 80/20 stratified split to predict `Churn` (1 = yes, 0 = no) after encoding `Gender`, `Subscription Type`, and `Contract Length` and scaling the numeric columns. I pulled the confusion matrix counts (TN, FP, FN, TP) directly and used them to explain what a False Positive (predicting churn for a customer who stays) and a False Negative (missing a customer who actually churns) mean in this context. I calculated accuracy, precision, recall, and F1-score manually from those same counts and confirmed they matched `scikit-learn`'s built-in `classification_report`, then built a comparison table of each metric's formula and what it actually answers. To demonstrate why accuracy alone can mislead, I compared the trained model against a naive baseline that always predicts the majority class. Finally, I reasoned through the real business cost of each error type to recommend the most suitable metric for this specific problem.

### Outcome
The model reached **82.7% accuracy**, **81% precision** and **82% recall** for the Churn class, and **83%/85%** precision/recall for No Churn — a solid, fairly balanced result (TN=5,628, FP=1,148, FN=1,077, TP=5,022). The naive always-predict-majority-class baseline scored a deceptively reasonable **52.6% accuracy** while catching **zero** actual churners (0% recall for Churn) — a direct demonstration of why accuracy alone can hide a model with no real skill. Reasoning through the business cost of each error — a False Positive wastes a retention offer on a customer who was never leaving, while a False Negative loses that customer and their future revenue entirely — led to recommending **recall** as the primary metric for this problem, with F1-score tracked alongside it as a safeguard against chasing recall at the expense of precision. This made concrete why the "right" metric depends on which kind of mistake actually costs the business more, not on which metric simply looks the highest.

### Interview Questions
1. **What is precision?**
   Precision measures, out of everyone the model predicted as positive (e.g., predicted to churn), what fraction actually were positive: `TP / (TP + FP)`. High precision means few False Positives, i.e., when the model says "churn," it's usually right.
2. **What is recall?**
   Recall measures, out of everyone who actually was positive (e.g., actually churned), what fraction the model correctly identified: `TP / (TP + FN)`. High recall means few False Negatives, i.e., the model misses very few of the actual positive cases.
3. **When is F1-score useful?**
   F1-score is the harmonic mean of precision and recall, giving a single number that balances both. It's especially useful when you need one overall metric to compare models (rather than tracking precision and recall separately), when the classes are imbalanced (making plain accuracy unreliable), or when there isn't a clear reason to prioritize one of precision/recall heavily over the other. Note that F1 penalizes a model that's very strong in one but very weak in the other, unlike a simple average would.

---

## Day 27: Confusion Matrix and Threshold Tuning

### Description
Analyze classification predictions using a confusion matrix and investigate how changing the classification threshold affects precision and recall.

### Objective
Understand the relationship between probability thresholds and classification performance.

### Tools
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

### Deliverables
- Confusion matrix visualization
- Results for multiple probability thresholds
- Precision-recall comparison
- Recommended threshold with justification

### Hints / Mini Guide
- Use `predict_proba()`
- Test several thresholds
- Consider the cost of false positives and false negatives

### Suggested Datasets
- Breast Cancer Wisconsin Dataset
- Customer Churn Dataset

### Approach
I rebuilt the same logistic regression churn model from Day 26 on `Customer_Churn_Dataset.csv`, using `predict_proba()` to get each test customer's probability of churning instead of jumping straight to a 0/1 label. I visualized the confusion matrix at the default 0.5 threshold with a Seaborn heatmap, then tested five thresholds (0.3, 0.4, 0.5, 0.6, 0.7), calculating precision, recall, F1-score, and the full confusion matrix breakdown at each one. I compared the results both as a line chart of precision/recall/F1 against threshold, and as a full precision-recall curve using `scikit-learn`'s `precision_recall_curve()`. Finally, applying the same business reasoning from Day 26 — a missed churner (False Negative) typically costs more than an unnecessary retention offer (False Positive) — I recommended a specific threshold and quantified exactly what trade-off it makes compared to the default.

### Outcome
As the threshold increased from 0.3 to 0.7, precision rose steadily (0.729 → 0.878) while recall fell (0.919 → 0.656) — the classic precision-recall trade-off, visible in both the line chart and the precision-recall curve. I recommended lowering the threshold from the default **0.5 to 0.4**: this catches **325 more actual churners** (missed churners drop from 1,077 to 752) at the cost of **409 more false alarms** (unnecessary retention offers). This is a trade worth making given a lost customer is typically far more costly than a wasted retention offer. As a bonus, 0.4 also produced the **best F1-score of any threshold tested** (0.822 vs. 0.819 at 0.5), so this wasn't a case of sacrificing overall balance just to chase recall; rather, it was a genuine improvement on both fronts. This showed that the default 0.5 threshold is just a starting point, not automatically the right choice for a specific business problem.

### Interview Questions
1. **What is a confusion matrix?**
   A confusion matrix is a table that breaks down a classification model's predictions against the actual outcomes, showing counts of True Positives, True Negatives, False Positives, and False Negatives. It gives a much more detailed picture of model performance than accuracy alone, since it shows exactly what kinds of mistakes the model is making, not just how many.
2. **How does changing the threshold affect recall?**
   Lowering the classification threshold makes the model predict the positive class more readily (since a lower probability is now enough to count as a positive prediction), which generally **increases recall** (i.e., more of the actual positive cases get caught) but tends to **decrease precision**, since the model is also now flagging more cases that turn out to be negative. Raising the threshold has the opposite effect: recall drops, precision rises.
3. **Why might the default 0.5 threshold not be optimal?**
   A 0.5 threshold treats a False Positive and a False Negative as equally costly mistakes, which is rarely true in a real business problem. In this churn example, missing an actual churner is more expensive than wasting a retention offer on someone who wasn't leaving, so a lower threshold that favors recall over precision can produce a better real-world outcome than the default. That is, even if 0.5 isn't technically "wrong" in a vacuum, it's not tailored to the specific costs involved in this decision.

---

## Day 28: Decision Tree Classifier

### Description
Train a decision tree classifier and explore how tree depth and other parameters influence model performance.

### Objective
Understand tree-based classification and model complexity.

### Tools
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Jupyter Notebook

### Deliverables
- Decision tree model
- Visualization of the tree
- Performance comparison across tree depths
- Overfitting analysis

### Hints / Mini Guide
- Experiment with `max_depth`
- Compare training and testing performance
- Use feature importance to understand splits

### Suggested Datasets
- Iris Dataset
- Breast Cancer Wisconsin Dataset

### Approach
I used the `Iris_Dataset.csv` file, splitting it 80/20 (stratified) and training a `DecisionTreeClassifier`. I visualized the resulting tree structure with `plot_tree()`, then systematically compared training vs. test accuracy across seven `max_depth` settings (1, 2, 3, 4, 5, 10, and unlimited) to see how model complexity affects generalization. I built a comparison table and a line chart tracking both training and test accuracy against depth, used the widening gap between them to analyze overfitting, and examined `feature_importances_` on the best-performing tree to see which features actually drove its splitting decisions.

### Outcome
A single-split tree (`max_depth=1`) underfit badly, with only 66.7% accuracy on both training and test data. `max_depth=3` struck the best balance: 98.3% training accuracy and 96.7% test accuracy, close together, meaning the model learned the real pattern without memorizing noise. Letting the tree grow deeper (`max_depth=5` or unlimited) reached a perfect 100% training accuracy, but test accuracy actually *dropped* to 93.3%, a textbook overfitting signature where the deeper tree used its extra complexity to memorize training-set quirks rather than learn anything that generalizes. Feature importance confirmed that `petal length (cm)` and `petal width (cm)` together drove almost all of the tree's decisions, while the sepal measurements contributed very little, matching the tree's very first split, which was on petal length. This made it concrete that more training accuracy doesn't mean a better model; what matters is performance on unseen data.

### Interview Questions
1. **How does a decision tree make predictions?**
   A decision tree makes predictions by asking a sequence of yes/no questions about a sample's features, starting at the root node and following the branch that matches the sample's values at each step, until it reaches a leaf node. That leaf's majority class (for classification) becomes the tree's prediction. Each split is chosen during training to best separate the classes at that point, typically measured using a metric like Gini impurity.
2. **What is overfitting in decision trees?**
   Overfitting happens when a tree grows complex enough to essentially memorize the training data, including its noise and quirks, rather than learning the broader pattern that generalizes to new data. It shows up as a large gap between training accuracy (very high, sometimes 100%) and test accuracy (noticeably lower), since the tree's extra splits are tailored to specifics of the training set that don't hold up on unseen examples.
3. **What does `max_depth` control?**
   `max_depth` limits how many levels of splits a decision tree is allowed to make, which directly controls the tree's complexity. A small `max_depth` produces a simple tree that may underfit; an unlimited or very large `max_depth` lets the tree keep splitting until it perfectly separates the training data, which risks overfitting. Tuning `max_depth` is one of the main ways to control the trade-off between underfitting and overfitting in a decision tree.

---

## Day 29: Random Forest Classifier

### Description
Build a random forest classification model and compare its performance with a single decision tree.

### Objective
Understand ensemble learning and why combining multiple trees can improve generalization.

### Tools
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Jupyter Notebook

### Deliverables
- Random forest model
- Decision tree baseline
- Performance comparison
- Feature importance analysis

### Hints / Mini Guide
- Experiment with `n_estimators`
- Compare training and testing scores
- Inspect `feature_importances_`

### Suggested Datasets
- Breast Cancer Wisconsin Dataset
- Titanic Dataset
- Bank Marketing Dataset

### Approach
I used the `Titanic_Dataset.csv` file, filling missing `Age` with the median and missing `Embarked` with the mode, dropping identifier and text columns, and encoding `Sex` and `Embarked`. I trained a single decision tree baseline and a random forest on the same 80/20 split and compared their accuracy. On that one split the two models looked surprisingly close, so rather than stop there, I repeated the comparison across 20 different random splits to see which model was actually more reliable. I swept `n_estimators` from 10 to 300 to see how the forest's accuracy changes as more trees are added, and examined `feature_importances_` from the final model to see which features drove most of its predictions.

### Outcome
On a single split, the decision tree's test accuracy (0.821) was close to the random forest's (0.810), which on its own would be a misleading basis for comparing the two models. Across 20 different splits, the real pattern became clear: the random forest's average test accuracy (0.822) was higher than the single tree's (0.782), and the forest was also more consistent, with a lower standard deviation (0.022 versus 0.028). Sweeping `n_estimators` showed accuracy stabilizing after roughly 50 trees, with little further benefit from adding more. Feature importance identified `Fare`, `Sex_male`, and `Age` as the strongest predictors of survival, consistent with well-known patterns from the real Titanic disaster. This made the core benefit of a random forest concrete: averaging many trees smooths out the randomness that makes any single tree's performance swing from one train-test split to the next.

### Interview Questions
1. **What is a random forest?**
   A random forest is an ensemble of many decision trees, each trained on a random subset of the training data and a random subset of features at each split. Its final prediction is the majority vote (for classification) across all the individual trees. Combining many trees this way reduces the risk of any single tree's quirks or overfitting dominating the final result.
2. **Why does random forest usually generalize better than one decision tree?**
   A single decision tree, especially an unconstrained one, can easily overfit to the specific training data it saw, and its performance can vary a lot depending on which rows happened to be in that training set. A random forest trains many such trees on different random subsets of the data and features, then averages their predictions together. That averaging cancels out much of each individual tree's noise and overfitting, producing a model whose performance is both typically higher and more stable across different data splits.
3. **What is ensemble learning?**
   Ensemble learning is the general technique of combining multiple models together to produce a single prediction that's usually better than any individual model could achieve alone. A random forest is one specific example, an ensemble of many decision trees, but the same idea applies broadly: combining diverse models tends to reduce error and variance compared to relying on just one model.

---

## Day 30: K-Nearest Neighbors

### Description
Build a KNN classification model and evaluate how different values of K influence prediction performance.

### Objective
Understand distance-based classification and the importance of feature scaling.

### Tools
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook

### Deliverables
- KNN model
- Feature scaling workflow
- Performance comparison for multiple K values
- Best-K selection analysis

### Hints / Mini Guide
- Scale features before using distance-based KNN
- Test several K values
- Compare training and testing performance

### Suggested Datasets
- Iris Dataset
- Wine Dataset
- Breast Cancer Wisconsin Dataset

### Approach
I used the `Wine_Dataset.csv` file, where raw feature ranges vary enormously (`Proline` runs from about 278 to 1680, while `Hue` only runs from about 0.48 to 1.71). I trained a KNN model (K=5) on the raw, unscaled features first, then fit a `StandardScaler` on the training data only and trained an identical KNN model on the scaled version, to directly measure how much scaling matters for a distance-based method. I swept K from 1 to 30, comparing training and test accuracy at each value. Since the 36-row test set made raw test accuracy noisy between nearby K values, I used 5-fold cross-validation on the training set instead to choose the final K more reliably, then evaluated that chosen model on the held-out test set.

### Outcome
Scaling improved test accuracy from 80.6% (unscaled) to 97.2% (scaled), a large, direct demonstration of why feature scaling is essential before using KNN. Sweeping K from 1 to 30 showed the classic pattern: `K=1` achieves perfect training accuracy (each point is its own nearest neighbor, a sign of high variance) while larger K produces a smoother, more stable model. Cross-validation accuracy climbed from about 94% at `K=1` to a consistently high plateau of roughly 97 to 98% from about `K=11` onward, with no real benefit to going higher. I selected **K=11** as the best choice, since it sits at the start of that stable plateau, stays small enough to remain locally sensitive, and is odd to avoid tie votes between the three wine classes. The final model reached strong training and test accuracy at that setting.

### Interview Questions
1. **How does KNN classify observations?**
   KNN classifies a new point by looking at the K training points closest to it (by distance, typically Euclidean distance) and assigning the majority class among those K neighbors. There's no real "training" step beyond storing the data; all the work happens at prediction time, when distances to every stored training point are calculated.
2. **Why is scaling important for KNN?**
   KNN relies entirely on distance calculations between points, and features with larger raw numeric ranges will dominate that distance regardless of how informative they actually are. In this dataset, an unscaled `Proline` value (hundreds to thousands) would completely overwhelm a feature like `Hue` (under 2) in the distance calculation, even if `Hue` is just as useful for distinguishing wine classes. Scaling puts every feature on a comparable range so each one contributes fairly.
3. **What happens when K is too small or too large?**
   A very small K (like K=1) makes the model highly sensitive to individual points and noise, since a single unusual neighbor can flip the prediction; this leads to high variance and a model that fits the training data very closely but may not generalize well. A very large K smooths predictions over a wide neighborhood, which can wash out genuine local patterns and push every prediction toward the overall majority class, leading to high bias and underfitting. Choosing K is about finding the balance between these two extremes.
