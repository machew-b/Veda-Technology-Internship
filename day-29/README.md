# Day 29: Random Forest Classifier

## Description
Build a random forest classification model and compare its performance with a single decision tree.

## Objective
Understand ensemble learning and why combining multiple trees can improve generalization.

## Tools
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Jupyter Notebook

## Deliverables
- Random forest model
- Decision tree baseline
- Performance comparison
- Feature importance analysis

## Hints / Mini Guide
- Experiment with `n_estimators`
- Compare training and testing scores
- Inspect `feature_importances_`

## Suggested Datasets
- Breast Cancer Wisconsin Dataset
- Titanic Dataset
- Bank Marketing Dataset

## Approach
I used the `Titanic_Dataset.csv` file, filling missing `Age` with the median and missing `Embarked` with the mode, dropping identifier and text columns, and encoding `Sex` and `Embarked`. I trained a single decision tree baseline and a random forest on the same 80/20 split and compared their accuracy. On that one split the two models looked surprisingly close, so rather than stop there, I repeated the comparison across 20 different random splits to see which model was actually more reliable. I swept `n_estimators` from 10 to 300 to see how the forest's accuracy changes as more trees are added, and examined `feature_importances_` from the final model to see which features drove most of its predictions.

## Outcome
On a single split, the decision tree's test accuracy (0.821) was close to the random forest's (0.810), which on its own would be a misleading basis for comparing the two models. Across 20 different splits, the real pattern became clear: the random forest's average test accuracy (0.822) was higher than the single tree's (0.782), and the forest was also more consistent, with a lower standard deviation (0.022 versus 0.028). Sweeping `n_estimators` showed accuracy stabilizing after roughly 50 trees, with little further benefit from adding more. Feature importance identified `Fare`, `Sex_male`, and `Age` as the strongest predictors of survival, consistent with well-known patterns from the real Titanic disaster. This made the core benefit of a random forest concrete: averaging many trees smooths out the randomness that makes any single tree's performance swing from one train-test split to the next.

## Interview Questions
1. **What is a random forest?**
   A random forest is an ensemble of many decision trees, each trained on a random subset of the training data and a random subset of features at each split. Its final prediction is the majority vote (for classification) across all the individual trees. Combining many trees this way reduces the risk of any single tree's quirks or overfitting dominating the final result.
2. **Why does random forest usually generalize better than one decision tree?**
   A single decision tree, especially an unconstrained one, can easily overfit to the specific training data it saw, and its performance can vary a lot depending on which rows happened to be in that training set. A random forest trains many such trees on different random subsets of the data and features, then averages their predictions together. That averaging cancels out much of each individual tree's noise and overfitting, producing a model whose performance is both typically higher and more stable across different data splits.
3. **What is ensemble learning?**
   Ensemble learning is the general technique of combining multiple models together to produce a single prediction that's usually better than any individual model could achieve alone. A random forest is one specific example, an ensemble of many decision trees, but the same idea applies broadly: combining diverse models tends to reduce error and variance compared to relying on just one model.