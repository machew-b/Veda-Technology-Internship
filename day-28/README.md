# Day 28: Decision Tree Classifier

## Description
Train a decision tree classifier and explore how tree depth and other parameters influence model performance.

## Objective
Understand tree-based classification and model complexity.

## Tools
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Jupyter Notebook

## Deliverables
- Decision tree model
- Visualization of the tree
- Performance comparison across tree depths
- Overfitting analysis

## Hints / Mini Guide
- Experiment with `max_depth`
- Compare training and testing performance
- Use feature importance to understand splits

## Suggested Datasets
- Iris Dataset
- Breast Cancer Wisconsin Dataset

## Approach
I used the `Iris_Dataset.csv` file, splitting it 80/20 (stratified) and training a `DecisionTreeClassifier`. I visualized the resulting tree structure with `plot_tree()`, then systematically compared training vs. test accuracy across seven `max_depth` settings (1, 2, 3, 4, 5, 10, and unlimited) to see how model complexity affects generalization. I built a comparison table and a line chart tracking both training and test accuracy against depth, used the widening gap between them to analyze overfitting, and examined `feature_importances_` on the best-performing tree to see which features actually drove its splitting decisions.

## Outcome
A single-split tree (`max_depth=1`) underfit badly, with only 66.7% accuracy on both training and test data. `max_depth=3` struck the best balance: 98.3% training accuracy and 96.7% test accuracy, close together, meaning the model learned the real pattern without memorizing noise. Letting the tree grow deeper (`max_depth=5` or unlimited) reached a perfect 100% training accuracy, but test accuracy actually *dropped* to 93.3%, a textbook overfitting signature where the deeper tree used its extra complexity to memorize training-set quirks rather than learn anything that generalizes. Feature importance confirmed that `petal length (cm)` and `petal width (cm)` together drove almost all of the tree's decisions, while the sepal measurements contributed very little, matching the tree's very first split, which was on petal length. This made it concrete that more training accuracy doesn't mean a better model; what matters is performance on unseen data.

## Interview Questions
1. **How does a decision tree make predictions?**
   A decision tree makes predictions by asking a sequence of yes/no questions about a sample's features, starting at the root node and following the branch that matches the sample's values at each step, until it reaches a leaf node. That leaf's majority class (for classification) becomes the tree's prediction. Each split is chosen during training to best separate the classes at that point, typically measured using a metric like Gini impurity.
2. **What is overfitting in decision trees?**
   Overfitting happens when a tree grows complex enough to essentially memorize the training data, including its noise and quirks, rather than learning the broader pattern that generalizes to new data. It shows up as a large gap between training accuracy (very high, sometimes 100%) and test accuracy (noticeably lower), since the tree's extra splits are tailored to specifics of the training set that don't hold up on unseen examples.
3. **What does `max_depth` control?**
   `max_depth` limits how many levels of splits a decision tree is allowed to make, which directly controls the tree's complexity. A small `max_depth` produces a simple tree that may underfit; an unlimited or very large `max_depth` lets the tree keep splitting until it perfectly separates the training data, which risks overfitting. Tuning `max_depth` is one of the main ways to control the trade-off between underfitting and overfitting in a decision tree.