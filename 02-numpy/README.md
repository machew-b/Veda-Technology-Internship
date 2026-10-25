# NumPy

## Day 09: NumPy Array Creation and Data Types

### Description
Create NumPy arrays and explore their shape, dimensions, size, data types, and basic operations.

### Objective
Learn the fundamentals of NumPy, a core Python library for data science.

### Tools
- Python
- NumPy
- Jupyter Notebook

### Deliverables
- Examples of one-dimensional and two-dimensional arrays
- Demonstration of array attributes
- Examples of numerical operations

### Hints / Mini Guide
- Use `np.array()` to create arrays
- Explore `shape`, `ndim`, `size`, and `dtype`
- Compare NumPy arrays with Python lists

### Suggested Datasets
- Iris Dataset
- Student Marks Dataset

### Approach
I used the `Iris_Dataset.csv` file, which contains four numeric measurement columns (`sepal length (cm)`, `sepal width (cm)`, `petal length (cm)`, `petal width (cm)`) and a categorical `target` column identifying each flower's species. I created one-dimensional arrays with `np.array()` from single real columns, and a two-dimensional array by combining all four numeric columns into one array of features. I then explored the `shape`, `ndim`, `size`, and `dtype` attributes on both the 1D and 2D arrays, and showed that an array can also hold string data (the species column) rather than just numbers. For numerical operations, I used summary statistics (`mean()`, `max()`, `min()`, `sum()`, `std()`), element-wise arithmetic, operations between two full arrays, boolean masking to filter values by a condition, and per-column statistics on the 2D array using `axis=0`. Finally, I directly compared NumPy arrays against plain Python lists, showing that the same `*` and `+` operators behave completely differently on each.

### Outcome
By the end of this task, I was comfortable creating both 1D and 2D NumPy arrays from real data and reading their `shape`, `ndim`, `size`, and `dtype` attributes to understand their structure. I learned that NumPy arrays support fast, element-wise numerical operations directly with standard operators, while the equivalent operators on a plain Python list either repeat (`*`) or concatenate (`+`) instead of performing math. This is the core reason NumPy is used throughout data science: it lets you apply a calculation to an entire column, or even an entire table, of data at once, without writing a loop.

### Interview Questions
1. **What is NumPy?**
   NumPy is a core Python library for numerical computing. Its main feature is the array object (`ndarray`), which stores data efficiently and supports fast, element-wise mathematical operations across an entire collection of values at once. Ultimately, it is the foundation that most data science and machine learning libraries in Python are built on top of.
2. **What is the difference between a NumPy array and a Python list?**
   A Python list can hold mixed data types and supports general-purpose operations, but arithmetic operators don't work element-wise on it (`list * 2` repeats the list, `list + list` concatenates them). A NumPy array is designed specifically for numerical data: all elements typically share one `dtype`, and operators like `*` and `+` apply element-wise across the whole array, which also makes NumPy arrays much faster for large-scale numerical work.
3. **What does the `shape` attribute represent?**
   `shape` is a tuple showing the size of an array along each of its dimensions. For a 1D array of 150 values, `shape` is `(150,)`. For a 2D array with 150 rows and 4 columns, `shape` is `(150, 4)`, where the first number is the row count, and the second is the column count.

---

## Day 10: NumPy Indexing and Slicing

### Description
Practice selecting individual elements, rows, columns, and ranges from NumPy arrays using indexing and slicing.

### Objective
Develop the ability to efficiently access numerical data stored in arrays.

### Tools
- Python
- NumPy
- Jupyter Notebook

### Deliverables
- Examples of one-dimensional indexing
- Examples of two-dimensional indexing
- At least five slicing examples

### Hints / Mini Guide
- Remember that Python indexing starts at zero
- Use `array[row, column]` for two-dimensional arrays
- Practice positive and negative indexing

### Suggested Datasets
- Iris Dataset
- Wine Dataset

### Approach
I used the `Wine_Dataset.csv` file, creating a 1D array from the real `Alcohol` column and a 2D array from five real feature columns (`Alcohol`, `Malic acid`, `Ash`, `Magnesium`, `Color intensity`). For one-dimensional indexing, I practiced accessing elements with positive indices (the first and fifth values) and negative indices (the last and second-to-last values), reinforcing that indexing starts at zero. For two-dimensional indexing, I used `array[row, column]` to select individual elements, an entire row, an entire column, and an element using negative indices on both axes at once. For slicing, I wrote eight examples covering basic `start:stop` ranges, open-ended slices, negative slicing from the end, stepped slices, and three 2D slices selecting a range of rows, a range of columns, and a rectangular sub-block of both.

### Outcome
By the end of this task, I was comfortable using both indexing and slicing to pull exactly the data I needed out of a NumPy array, whether that was a single value, an entire row or column, or any rectangular sub-section, without writing a loop. Working through positive and negative indices on both 1D and 2D arrays made the zero-based indexing rule and the `array[row, column]` pattern feel natural, and practicing slicing showed how a single `start:stop:step` expression can replace what would otherwise take several lines of manual selection.

### Interview Questions
1. **What is zero-based indexing?**
   Zero-based indexing means the first element in a sequence is at position `0`, not `1`. So in an array of 178 wines, the first wine is `array[0]` and the last is `array[177]` (or equivalently `array[-1]`).
2. **How do you select a column from a two-dimensional NumPy array?**
   By using `array[:, column_index]`, where the colon (`:`) before the comma means "all rows" and the number after the comma selects that specific column. For example, `features[:, 2]` selects every row's value in column index 2.
3. **What is slicing?**
   Slicing is selecting a range of elements from an array using the `start:stop` (and optional `:step`) syntax, instead of a single index. It returns every element from `start` up to, but not including, `stop`, stepping by `step` if one is given (e.g. `alcohol[0:10:2]` returns every second value from index 0 up to index 9).

---

## Day 11: NumPy Vectorization and Broadcasting

### Description
Perform arithmetic operations on complete NumPy arrays and explore broadcasting between arrays of compatible shapes.

### Objective
Understand efficient numerical computation without explicit Python loops.

### Tools
- Python
- NumPy
- Jupyter Notebook

### Deliverables
- Examples of vectorized arithmetic
- At least three broadcasting examples
- A comparison between loop-based and vectorized calculations

### Hints / Mini Guide
- Try adding a scalar to an array
- Experiment with arrays of different compatible shapes
- Avoid unnecessary Python loops

### Suggested Datasets
- Student Marks Dataset
- Iris Dataset

### Approach
I used the `Iris_Dataset.csv` file, working with a 1D array of `petal length (cm)` values and a 2D array built from all four numeric feature columns. For vectorized arithmetic, I added and multiplied the array by a scalar, performed element-wise arithmetic between two real feature arrays (`sepal length` × `sepal width`), and applied NumPy math functions (`np.square()`, `np.sqrt()`) across the whole array at once. For broadcasting, I wrote three examples: a scalar broadcast across a 1D array, a 1D array of column means (shape `(4,)`) broadcast across every row of the `(150, 4)` feature array, and a reshaped column vector (shape `(150, 1)`) broadcast across every column of that same array. Finally, I compared a loop-based calculation with its vectorized equivalent, first using the real 150-row dataset and then using the same data repeated 10,000 times, resulting in 1.5 million values. I timed both approaches to measure the actual speed difference.

### Outcome
By the end of this task, I was comfortable performing vectorized arithmetic directly on NumPy arrays and understood how broadcasting lets operations work between arrays of different but compatible shapes without manually reshaping or looping. Timing the loop-based versus vectorized calculation made the benefit concrete: on the small 150-row array the difference was negligible, but on the 1.5-million-value array, the vectorized version ran roughly 36 times faster than the equivalent Python `for` loop, while producing an identical result. This showed exactly why vectorization matters as data size grows.

### Interview Questions
1. **What is vectorization?**
   Vectorization is applying an operation to an entire array at once, instead of looping through each element individually in Python. NumPy performs the operation internally using optimized, compiled code, which is both faster and results in shorter, more readable code than the equivalent explicit loop.
2. **What is broadcasting in NumPy?**
   Broadcasting is NumPy's rule for performing operations between arrays of different but compatible shapes, without needing to manually copy or reshape one of them first. For example, a single row of 4 values can be broadcast across all 150 rows of a `(150, 4)` array, applying that row's values to every row automatically.
3. **Why is vectorization useful for data science?**
   Data science regularly involves applying the same calculation to every row or column of a large dataset. Vectorized NumPy operations perform this far faster than a Python `for` loop, since the looping happens in optimized low-level code rather than in Python itself, which matters enormously as dataset size grows (in this task's timing test, roughly 36x faster on 1.5 million values), and also makes the code shorter and easier to read.

---

## Day 12: NumPy Aggregations and Statistics

### Description
Use NumPy functions to calculate sum, mean, median, minimum, maximum, standard deviation, and variance.

### Objective
Build basic numerical analysis skills using NumPy.

### Tools
- Python
- NumPy
- Jupyter Notebook

### Deliverables
- Examples of at least seven aggregation functions
- Statistical analysis of a numerical dataset
- A short interpretation of the results

### Hints / Mini Guide
- Use functions such as `mean()`, `median()`, `std()`, and `var()`
- Experiment with `axis=0` and `axis=1`
- Compare results across different columns

### Suggested Datasets
- Student Performance Dataset
- Iris Dataset

### Approach
I used the `Iris_Dataset.csv` file, demonstrating eight aggregation functions on the real `petal length (cm)` column: `sum()`, `mean()`, `np.median()`, `min()`, `max()`, `std()`, `var()`, and `np.ptp()`/`np.percentile()`. I then built a 2D array from all four numeric feature columns and experimented with `axis=0` (which aggregates down each column, producing one result per feature) versus `axis=1` (which aggregates across each row, producing one result per flower), confirming the difference by checking the resulting shape each axis setting produces. For the statistical analysis, I built a full summary table of mean, median, standard deviation, variance, minimum, and maximum for all four columns at once, then compared their standard deviations directly to find the most and least variable features. Finally, I wrote a short interpretation of what those numbers actually mean for this dataset.

### Outcome
By the end of this task, I was comfortable using NumPy's core aggregation functions and understood how the `axis` parameter changes what gets summarized (i.e., `axis=0` for per-column results, `axis=1` for per-row results). Comparing standard deviations across the four columns showed that petal length is by far the most variable measurement in the dataset (std ≈ 1.76 cm) while sepal width is the most consistent (std ≈ 0.43 cm), which is a useful, concrete example of how a simple statistical comparison across columns can reveal which features carry the most distinguishing information in a dataset.

### Interview Questions
1. **What is the difference between mean and median?**
   The mean is the sum of all values divided by how many there are, and it is sensitive to extreme values (outliers) since one very large or very small number can pull it noticeably up or down. The median is the middle value when the data is sorted, but it is much less affected by outliers since it only depends on which value sits in the middle position, not on how far apart the values are.
2. **What does standard deviation measure?**
   Standard deviation measures how spread out a set of values is around its mean. A low standard deviation means values tend to cluster close to the mean (like sepal width in this dataset), while a high standard deviation means values are spread out over a wider range (like petal length). It's calculated as the square root of the variance.
3. **What does the `axis` parameter do in NumPy?**
   `axis` controls which direction an aggregation function collapses over in a multi-dimensional array. For a 2D array, `axis=0` aggregates down each column (collapsing the rows, so you get one result per column), and `axis=1` aggregates across each row (collapsing the columns, so you get one result per row).

---

## Day 13: NumPy Random Sampling

### Description
Generate random numbers and samples using NumPy and explore reproducibility using random seeds.

### Objective
Understand random data generation and its importance in data science experiments.

### Tools
- Python
- NumPy
- Jupyter Notebook

### Deliverables
- Examples of random integers and floating-point numbers
- Random samples from an array
- A demonstration of reproducible results using a seed

### Hints / Mini Guide
- Use NumPy random functions
- Set a random seed for reproducibility
- Generate a small simulated dataset

### Suggested Datasets
- Generated Random Dataset
- Student Marks Dataset

### Approach
Since this task is about generating data rather than working with an existing file, I used NumPy's random functions to build the dataset myself. I generated random integers with `np.random.randint()` (a single value, an array, and a 2D grid), and random floats with `np.random.rand()`, `np.random.uniform()`, and `np.random.randn()`. I then used `np.random.choice()` to randomly sample from an array of grade labels, both with and without replacement, and with custom probability weights favoring certain values. To demonstrate reproducibility, I first showed that two calls to a random function without a seed produce different results, then showed that setting `np.random.seed()` to the same value before each call produces an identical sequence every time, and that a different seed produces a different (but still repeatable) sequence. Finally, I generated a small simulated dataset of 20 students, combining random study hours, scores, and weighted grade sampling, using a fixed seed, and confirmed that resetting the same seed regenerates the exact same data.

### Outcome
By the end of this task, I was comfortable generating random integers, random floats from multiple distributions, and random samples from an array using NumPy. Demonstrating the seed behavior directly, where unseeded calls differing, seeded calls matching exactly, made it clear why random seeds matter: they turn an otherwise unpredictable process into something that can be exactly reproduced. Building the small simulated student dataset with a fixed seed showed how this applies in practice, i.e., anyone re-running the same seeded code gets the identical dataset, which is essential for debugging, sharing results, and letting others verify a data science experiment.

### Interview Questions
1. **Why are random numbers useful in data science?**
   Random numbers are used to simulate data for testing, to randomly split data into training and test sets, to shuffle data before training a model, to generate synthetic datasets when real data isn't available, and to sample a smaller subset from a large dataset for quicker experimentation. They're a core building block for experiments where controlled randomness is needed.
2. **What is a random seed?**
   A random seed is a starting value passed to `np.random.seed()` that initializes NumPy's random number generator. Once a seed is set, every "random" number generated afterward follows a fixed, predetermined sequence. So, setting the same seed again will always reproduce the exact same sequence of "random" values.
3. **Why is reproducibility important?**
   Reproducibility means someone else (or you, later) can re-run the exact same code and get the exact same results. This is essential for debugging (so a bug can be reliably reproduced), for verifying results (so others can check your work produces what you claim), and for fair comparisons between experiments (so any difference in outcome is due to an actual change, not just different random luck).

---

## Day 14: NumPy Array Reshaping and Stacking

### Description
Reshape arrays into different dimensions and combine multiple arrays using stacking and concatenation.

### Objective
Learn how to restructure and combine array data for different analysis needs.

### Tools
- Python
- NumPy
- Jupyter Notebook

### Deliverables
- Examples of reshaping a 1D array into 2D (and back)
- At least three examples combining arrays (stacking or concatenation)
- A short explanation of when reshaping is useful

### Hints / Mini Guide
- Use `reshape()`, `flatten()`, and `ravel()`
- Use `np.vstack()`, `np.hstack()`, and `np.concatenate()`
- Check that the total number of elements matches before reshaping

### Suggested Datasets
- Iris Dataset
- Student Marks Dataset

### Approach
I used the `Iris_Dataset.csv` file, reshaping the real `petal length (cm)` column from a 1D array of 150 values into a `(150, 1)` 2D column, then into a `(15, 10)` grid, using both explicit dimensions and `-1` to let NumPy infer one dimension automatically. I converted a reshaped 2D array back into 1D using both `flatten()` and `ravel()`, confirmed they produce identical values, and demonstrated that an invalid reshape (one where the total element count doesn't match) raises a `ValueError`. For combining arrays, I wrote four examples: `np.vstack()` to stack two columns as new rows, `np.hstack()` to join two 1D arrays end-to-end, `np.concatenate()` with `axis=1` to join two reshaped column vectors side-by-side into a feature matrix, and `np.hstack()` again to add a newly computed `sepal_area` column onto the full `features` array. I finished with a short written explanation of where reshaping is actually useful in practice, grounded in the examples above, particularly preparing a single column for machine learning models that expect two-dimensional input.

### Outcome
By the end of this task, I was comfortable reshaping arrays between dimensions with `reshape()`, converting back to 1D with `flatten()`/`ravel()`, and combining arrays with `vstack()`, `hstack()`, and `concatenate()`. Seeing the `ValueError` raised by an invalid reshape reinforced that the total element count must always match. The clearest practical takeaway was that reshaping a single column into `(-1, 1)` is a small but essential step for combining separate columns into one dataset or feeding a single feature into tools that expect two-dimensional input.

### Interview Questions
1. **What does `reshape()` do?**
   `reshape()` returns a new view of the same data, rearranged into a different shape (number of dimensions and sizes), without changing the actual values or copying them. The new shape's total element count must exactly match the original array's total element count, or NumPy raises a `ValueError`.
2. **What is the difference between `flatten()` and `ravel()`?**
   Both convert a multi-dimensional array into a 1D array, and in most everyday cases they produce the same result. The key difference is that `flatten()` always returns a copy of the data (so changing the flattened array never affects the original), while `ravel()` returns a view whenever possible (so changing it can sometimes change the original array too). Note that `ravel()` is generally faster since it usually avoids copying data.
3. **What is the difference between `vstack()` and `hstack()`?**
   `np.vstack()` stacks arrays **vertically**, adding them as new rows (combining along `axis=0`). `np.hstack()` stacks arrays **horizontally**, joining them side-by-side into a longer row or adding new columns (combining along `axis=1`, or concatenating 1D arrays end to end).
