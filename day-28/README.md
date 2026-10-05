# Day 28: Decision Tree Classifier

## Description
Train a decision tree classifier and explore how tree depth affects model performance and complexity.

## Objective
Understand tree-based classification, model complexity, and the trade-off between fitting the training data and generalizing to unseen data.

## Tools
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

## Deliverables
- Trained decision tree classifier
- Visualization of the decision tree
- Performance comparison across tree depths
- Confusion matrix, classification report, and feature importances
- Discussion of overfitting

## Hints / Mini Guide
- Experiment with `max_depth`
- Compare training and testing performance
- Use feature importance to understand which measurements influence splits

## Suggested Datasets
- Iris Dataset
- Breast Cancer Wisconsin Dataset

## Approach
I used the `Iris_Dataset.csv` file (150 flowers, four measurements, and three species), separating the sepal and petal measurements from the `target` column. I split the data into training and testing sets using an 80/20 stratified split so each species stayed equally represented in both sets. I trained decision tree models with maximum depths of 1, 2, 3, 4, 5, and no limit, then compared their training and testing accuracy, train-test gap, and number of leaf nodes. Finally, I evaluated and visualized a depth-3 tree using a confusion matrix, classification report, and feature importances.

## Outcome
The depth comparison shows how changing `max_depth` affects both model complexity and accuracy. A shallow tree is easier to follow but may miss useful patterns, while a deeper tree can fit the training data more closely and may perform less well on unseen flowers. The depth-3 tree gives me a concrete set of splits to interpret, and the confusion matrix and classification report show which Iris species it predicts correctly or mixes up. The feature-importance chart also shows which measurements the fitted tree relied on most.

## Interview Questions
1. **How does a decision tree make predictions?**
   A decision tree makes predictions by applying a series of feature-based rules. Each rule sends an observation down one branch, and the class at the final leaf is the prediction.
2. **What does `max_depth` control?**
   `max_depth` controls how many levels of splits the tree can make. A smaller depth makes a simpler tree, while a deeper tree can learn more detailed rules but may overfit the training data.
3. **How can you tell if a decision tree is overfitting?**
   Compare its training and testing performance. If training accuracy keeps improving as the tree gets deeper but testing accuracy does not, the tree may be learning patterns that do not generalize to new data.
