# Day 09: NumPy Array Creation and Data Types

## Description
Create NumPy arrays and explore their shape, dimensions, size, data types, and basic operations.

## Objective
Learn the fundamentals of NumPy, a core Python library for data science.

## Tools
- Python
- NumPy
- Jupyter Notebook

## Deliverables
- Examples of one-dimensional and two-dimensional arrays
- Demonstration of array attributes
- Examples of numerical operations

## Hints / Mini Guide
- Use `np.array()` to create arrays
- Explore `shape`, `ndim`, `size`, and `dtype`
- Compare NumPy arrays with Python lists

## Suggested Datasets
- Iris Dataset
- Student Marks Dataset

## Approach
I used the `Iris_Dataset.csv` file, which contains four numeric measurement columns (`sepal length (cm)`, `sepal width (cm)`, `petal length (cm)`, `petal width (cm)`) and a categorical `target` column identifying each flower's species. I created one-dimensional arrays with `np.array()` from single real columns, and a two-dimensional array by combining all four numeric columns into one array of features. I then explored the `shape`, `ndim`, `size`, and `dtype` attributes on both the 1D and 2D arrays, and showed that an array can also hold string data (the species column) rather than just numbers. For numerical operations, I used summary statistics (`mean()`, `max()`, `min()`, `sum()`, `std()`), element-wise arithmetic, operations between two full arrays, boolean masking to filter values by a condition, and per-column statistics on the 2D array using `axis=0`. Finally, I directly compared NumPy arrays against plain Python lists, showing that the same `*` and `+` operators behave completely differently on each.

## Outcome
By the end of this task, I was comfortable creating both 1D and 2D NumPy arrays from real data and reading their `shape`, `ndim`, `size`, and `dtype` attributes to understand their structure. I learned that NumPy arrays support fast, element-wise numerical operations directly with standard operators, while the equivalent operators on a plain Python list either repeat (`*`) or concatenate (`+`) instead of performing math. This is the core reason NumPy is used throughout data science: it lets you apply a calculation to an entire column, or even an entire table, of data at once, without writing a loop.

## Interview Questions
1. **What is NumPy?**
   NumPy is a core Python library for numerical computing. Its main feature is the array object (`ndarray`), which stores data efficiently and supports fast, element-wise mathematical operations across an entire collection of values at once. Ultimately, it is the foundation that most data science and machine learning libraries in Python are built on top of.
2. **What is the difference between a NumPy array and a Python list?**
   A Python list can hold mixed data types and supports general-purpose operations, but arithmetic operators don't work element-wise on it (`list * 2` repeats the list, `list + list` concatenates them). A NumPy array is designed specifically for numerical data: all elements typically share one `dtype`, and operators like `*` and `+` apply element-wise across the whole array, which also makes NumPy arrays much faster for large-scale numerical work.
3. **What does the `shape` attribute represent?**
   `shape` is a tuple showing the size of an array along each of its dimensions. For a 1D array of 150 values, `shape` is `(150,)`. For a 2D array with 150 rows and 4 columns, `shape` is `(150, 4)`, where the first number is the row count, and the second is the column count.