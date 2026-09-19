# Day 12 — NumPy Aggregations and Statistics

## Description
Use NumPy functions to calculate sum, mean, median, minimum, maximum, standard deviation, and variance.

## Objective
Build basic numerical analysis skills using NumPy.

## Tools
- Python
- NumPy
- Jupyter Notebook

## Deliverables
- Examples of at least seven aggregation functions
- Statistical analysis of a numerical dataset
- A short interpretation of the results

## Hints / Mini Guide
- Use functions such as `mean()`, `median()`, `std()`, and `var()`
- Experiment with `axis=0` and `axis=1`
- Compare results across different columns

## Suggested Datasets
- Student Performance Dataset
- Iris Dataset

## Approach
I used the `Iris_Dataset.csv` file, demonstrating eight aggregation functions on the real `petal length (cm)` column: `sum()`, `mean()`, `np.median()`, `min()`, `max()`, `std()`, `var()`, and `np.ptp()`/`np.percentile()`. I then built a 2D array from all four numeric feature columns and experimented with `axis=0` (which aggregates down each column, producing one result per feature) versus `axis=1` (which aggregates across each row, producing one result per flower), confirming the difference by checking the resulting shape each axis setting produces. For the statistical analysis, I built a full summary table of mean, median, standard deviation, variance, minimum, and maximum for all four columns at once, then compared their standard deviations directly to find the most and least variable features. Finally, I wrote a short interpretation of what those numbers actually mean for this dataset.

## Outcome
By the end of this task, I was comfortable using NumPy's core aggregation functions and understood how the `axis` parameter changes what gets summarized (i.e., `axis=0` for per-column results, `axis=1` for per-row results). Comparing standard deviations across the four columns showed that petal length is by far the most variable measurement in the dataset (std ≈ 1.76 cm) while sepal width is the most consistent (std ≈ 0.43 cm), which is a useful, concrete example of how a simple statistical comparison across columns can reveal which features carry the most distinguishing information in a dataset.

## Interview Questions
1. **What is the difference between mean and median?**
   The mean is the sum of all values divided by how many there are, and it is sensitive to extreme values (outliers) since one very large or very small number can pull it noticeably up or down. The median is the middle value when the data is sorted, but it is much less affected by outliers since it only depends on which value sits in the middle position, not on how far apart the values are.
2. **What does standard deviation measure?**
   Standard deviation measures how spread out a set of values is around its mean. A low standard deviation means values tend to cluster close to the mean (like sepal width in this dataset), while a high standard deviation means values are spread out over a wider range (like petal length). It's calculated as the square root of the variance.
3. **What does the `axis` parameter do in NumPy?**
   `axis` controls which direction an aggregation function collapses over in a multi-dimensional array. For a 2D array, `axis=0` aggregates down each column (collapsing the rows, so you get one result per column), and `axis=1` aggregates across each row (collapsing the columns, so you get one result per row).