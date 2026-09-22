# Day 14: NumPy Array Reshaping and Stacking

## Description
Reshape arrays into different dimensions and combine multiple arrays using stacking and concatenation.

## Objective
Learn how to restructure and combine array data for different analysis needs.

## Tools
- Python
- NumPy
- Jupyter Notebook

## Deliverables
- Examples of reshaping a 1D array into 2D (and back)
- At least three examples combining arrays (stacking or concatenation)
- A short explanation of when reshaping is useful

## Hints / Mini Guide
- Use `reshape()`, `flatten()`, and `ravel()`
- Use `np.vstack()`, `np.hstack()`, and `np.concatenate()`
- Check that the total number of elements matches before reshaping

## Suggested Datasets
- Iris Dataset
- Student Marks Dataset

## Approach
I used the `Iris_Dataset.csv` file, reshaping the real `petal length (cm)` column from a 1D array of 150 values into a `(150, 1)` 2D column, then into a `(15, 10)` grid, using both explicit dimensions and `-1` to let NumPy infer one dimension automatically. I converted a reshaped 2D array back into 1D using both `flatten()` and `ravel()`, confirmed they produce identical values, and demonstrated that an invalid reshape (one where the total element count doesn't match) raises a `ValueError`. For combining arrays, I wrote four examples: `np.vstack()` to stack two columns as new rows, `np.hstack()` to join two 1D arrays end-to-end, `np.concatenate()` with `axis=1` to join two reshaped column vectors side-by-side into a feature matrix, and `np.hstack()` again to add a newly computed `sepal_area` column onto the full `features` array. I finished with a short written explanation of where reshaping is actually useful in practice, grounded in the examples above, particularly preparing a single column for machine learning models that expect two-dimensional input.

## Outcome
By the end of this task, I was comfortable reshaping arrays between dimensions with `reshape()`, converting back to 1D with `flatten()`/`ravel()`, and combining arrays with `vstack()`, `hstack()`, and `concatenate()`. Seeing the `ValueError` raised by an invalid reshape reinforced that the total element count must always match. The clearest practical takeaway was that reshaping a single column into `(-1, 1)` is a small but essential step for combining separate columns into one dataset or feeding a single feature into tools that expect two-dimensional input.

## Interview Questions
1. **What does `reshape()` do?**
   `reshape()` returns a new view of the same data, rearranged into a different shape (number of dimensions and sizes), without changing the actual values or copying them. The new shape's total element count must exactly match the original array's total element count, or NumPy raises a `ValueError`.
2. **What is the difference between `flatten()` and `ravel()`?**
   Both convert a multi-dimensional array into a 1D array, and in most everyday cases they produce the same result. The key difference is that `flatten()` always returns a copy of the data (so changing the flattened array never affects the original), while `ravel()` returns a view whenever possible (so changing it can sometimes change the original array too). Note that `ravel()` is generally faster since it usually avoids copying data.
3. **What is the difference between `vstack()` and `hstack()`?**
   `np.vstack()` stacks arrays **vertically**, adding them as new rows (combining along `axis=0`). `np.hstack()` stacks arrays **horizontally**, joining them side-by-side into a longer row or adding new columns (combining along `axis=1`, or concatenating 1D arrays end to end).