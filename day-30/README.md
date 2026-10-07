# Day 30: K-Nearest Neighbors

## Description
Build a KNN classification model and evaluate how different values of K influence prediction performance.

## Objective
Understand distance-based classification and the importance of feature scaling.

## Tools
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook

## Deliverables
- KNN model
- Feature scaling workflow
- Performance comparison for multiple K values
- Best-K selection analysis

## Hints / Mini Guide
- Scale features before using distance-based KNN
- Test several K values
- Compare training and testing performance

## Suggested Datasets
- Iris Dataset
- Wine Dataset
- Breast Cancer Wisconsin Dataset

## Approach
I used the `Wine_Dataset.csv` file, where raw feature ranges vary enormously (`Proline` runs from about 278 to 1680, while `Hue` only runs from about 0.48 to 1.71). I trained a KNN model (K=5) on the raw, unscaled features first, then fit a `StandardScaler` on the training data only and trained an identical KNN model on the scaled version, to directly measure how much scaling matters for a distance-based method. I swept K from 1 to 30, comparing training and test accuracy at each value. Since the 36-row test set made raw test accuracy noisy between nearby K values, I used 5-fold cross-validation on the training set instead to choose the final K more reliably, then evaluated that chosen model on the held-out test set.

## Outcome
Scaling improved test accuracy from 80.6% (unscaled) to 97.2% (scaled), a large, direct demonstration of why feature scaling is essential before using KNN. Sweeping K from 1 to 30 showed the classic pattern: `K=1` achieves perfect training accuracy (each point is its own nearest neighbor, a sign of high variance) while larger K produces a smoother, more stable model. Cross-validation accuracy climbed from about 94% at `K=1` to a consistently high plateau of roughly 97 to 98% from about `K=11` onward, with no real benefit to going higher. I selected **K=11** as the best choice, since it sits at the start of that stable plateau, stays small enough to remain locally sensitive, and is odd to avoid tie votes between the three wine classes. The final model reached strong training and test accuracy at that setting.

## Interview Questions
1. **How does KNN classify observations?**
   KNN classifies a new point by looking at the K training points closest to it (by distance, typically Euclidean distance) and assigning the majority class among those K neighbors. There's no real "training" step beyond storing the data; all the work happens at prediction time, when distances to every stored training point are calculated.
2. **Why is scaling important for KNN?**
   KNN relies entirely on distance calculations between points, and features with larger raw numeric ranges will dominate that distance regardless of how informative they actually are. In this dataset, an unscaled `Proline` value (hundreds to thousands) would completely overwhelm a feature like `Hue` (under 2) in the distance calculation, even if `Hue` is just as useful for distinguishing wine classes. Scaling puts every feature on a comparable range so each one contributes fairly.
3. **What happens when K is too small or too large?**
   A very small K (like K=1) makes the model highly sensitive to individual points and noise, since a single unusual neighbor can flip the prediction; this leads to high variance and a model that fits the training data very closely but may not generalize well. A very large K smooths predictions over a wide neighborhood, which can wash out genuine local patterns and push every prediction toward the overall majority class, leading to high bias and underfitting. Choosing K is about finding the balance between these two extremes.