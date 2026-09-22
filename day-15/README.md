# Day 15: Pandas DataFrame Basics

## Description
Create DataFrames from dictionaries and datasets and explore rows, columns, shape, and summary information.

## Objective
Learn the primary Pandas structure used for tabular data analysis.

## Tools
- Python
- Pandas
- Jupyter Notebook

## Deliverables
- Create a DataFrame manually
- Load a real dataset into a DataFrame
- Display shape, columns, data types, and summary statistics

## Hints / Mini Guide
- Use `pd.DataFrame()`
- Use `head()` and `info()` to inspect data
- Use `describe()` for numerical summaries

## Suggested Datasets
- Titanic Dataset
- Iris Dataset

## Approach
I built a small DataFrame manually from a Python dictionary using `pd.DataFrame()`, then loaded the real `Titanic_Dataset.csv` file (891 rows, 12 columns) with `pd.read_csv()`. I explored the loaded DataFrame's `shape`, `size`, `columns`, and `dtypes`, and used `info()` to see a combined summary including non-null counts per column, which revealed real missing data in `Age` (177 missing), `Cabin` (687 missing), and `Embarked` (2 missing). I used `describe()` to get numerical summary statistics (mean, min, max, quartiles) for the numeric columns like `Age` and `Fare`, and `describe(include="object")` to get a comparable summary for the text columns. I also looked more closely at one categorical column (`Embarked`) using `.unique()` and `.value_counts()` to see its distinct values and how often each appears.

## Outcome
By the end of this task, I was comfortable creating a DataFrame both manually and from a real CSV file, and knew which Pandas methods to reach for first when exploring any new dataset. `shape`, `columns`, and `dtypes` quickly answer "how big is this and what's in it," while `info()` and `describe()` go a step further, surfacing missing values and numerical summaries in a single call. Working with the real Titanic dataset made this concrete: `info()` immediately flagged that `Age`, `Cabin`, and `Embarked` had missing values, which is exactly the kind of thing that needs to be caught before any further analysis.

## Interview Questions
1. **What is a Pandas DataFrame?**
   A DataFrame is Pandas' core two-dimensional data structure — a table of rows and columns, similar to a spreadsheet or a SQL table, where each column can hold a different data type. It can be built manually (e.g. from a dictionary) or loaded from a file like a CSV, and comes with built-in methods for exploring, cleaning, and analyzing the data.
2. **What information does `info()` provide?**
   `info()` gives a combined summary of the DataFrame: the total number of rows, the list of columns, how many non-null (non-missing) values each column has, the data type of each column, and the DataFrame's overall memory usage. It's usually the fastest way to spot missing data and confirm each column loaded with the expected type.
3. **What is the difference between `shape` and `size`?**
   `shape` returns a tuple of `(number of rows, number of columns)`. For this dataset, `(891, 12)`. `size` returns a single number: the total count of individual cells in the DataFrame, which is rows × columns — for this dataset, `891 × 12 = 10,692`.