# Day 18: Missing Values in Pandas

## Description
Identify missing values in a dataset and practice handling them using techniques such as dropping and filling missing values.

## Objective
Understand one of the most common data preprocessing problems.

## Tools
- Python
- Pandas
- Jupyter Notebook

## Deliverables
- Missing-value summary
- Examples using isna() and notna()
- A cleaned version of the dataset

## Hints / Mini Guide
- Use `isna().sum()` to count missing values
- Compare dropping and filling strategies
- Use mean or median carefully for numerical columns

## Suggested Datasets
- Titanic Dataset
- House Prices Dataset

## Approach
The real `House_Prices_Dataset.csv` file turned out to have **zero missing values** across all 545 rows and 13 columns, confirmed with `isna().sum()`. Since this task is specifically about missing-value handling, I created a clearly-labeled working copy of the dataset with a small, reproducible set of values (about 5% each) set to `NaN` across the `price`, `area`, `bedrooms`, and `furnishingstatus` columns, leaving the original real data untouched. I built a missing-value summary table showing both the count and percentage missing per column, and demonstrated `isna()`/`notna()` on individual columns and across the whole DataFrame to filter rows with and without missing data. I then compared dropping strategies (`dropna()` on all columns vs. `dropna(subset=["price"])` for one specific column) against filling strategies (`fillna()` with a constant placeholder, the column median, and the column mode), including a direct comparison of `price`'s mean vs. median to show why median is the safer choice when a column has outliers. Finally, I combined median filling for the numeric columns and mode filling for the categorical column to produce a fully cleaned dataset with zero missing values and no rows lost.

## Outcome
By the end of this task, I could confidently build a missing-value summary, use `isna()`/`notna()` to inspect and filter data by missingness, and choose between dropping and filling based on the situation. Comparing `dropna()` against `fillna()` on the same simulated data made the tradeoff concrete: dropping is simple but throws away every other value in that row, while filling preserves all rows but requires picking a sensible replacement. Comparing the mean and median for `price` specifically reinforced why median is generally the safer default for skewed numeric columns. That is, a few expensive houses pull the mean upward, while the median stays representative of a "typical" value.

## Interview Questions
1. **What are missing values?**
   Missing values are entries in a dataset where no data was recorded for a particular row and column, represented in Pandas as `NaN` (Not a Number) for numeric and object columns, or `NaT` for missing dates. They can occur for many reasons, for instance, in a field wasn't collected, a value was lost during data entry or merging, or a question simply didn't apply to that row.
2. **What are common ways to handle missing values?**
   The two main approaches are **dropping** (removing rows or columns that contain missing values, using `dropna()`) and **filling** (replacing missing values with a substitute, using `fillna()` which commonly a constant, the column's mean or median for numeric data, the mode for categorical data, or a value carried forward/backward from a nearby row).
3. **When should you avoid simply dropping missing rows?**
   You should avoid dropping rows when missing values are common enough that dropping them all would lose a large, potentially meaningful portion of the dataset, when the missing rows aren't randomly distributed (e.g. certain groups are more likely to have missing data, which would bias the remaining dataset), or when there just isn't much data to begin with and every row matters. In those cases, filling in a reasonable estimate usually preserves more useful information than deleting the row entirely.