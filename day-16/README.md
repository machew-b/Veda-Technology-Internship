# Day 16: Selecting Rows and Columns with loc and iloc

## Description
Practice selecting rows and columns using Pandas loc[] and iloc[] and understand label-based versus position-based selection.

## Objective
Develop accurate DataFrame selection skills.

## Tools
- Python
- Pandas
- Jupyter Notebook

## Deliverables
- At least five loc[] examples
- At least five iloc[] examples
- A comparison of both methods

## Hints / Mini Guide
- `loc[]` uses labels
- `iloc[]` uses integer positions
- Practice selecting both rows and columns

## Suggested Datasets
- Titanic Dataset
- Iris Dataset

## Approach
I used the `Titanic_Dataset.csv` file, and also created a second version of it (`df_by_id`) indexed by `PassengerId` instead of the default 0, 1, 2, ... index, so that row labels and row positions would no longer be the same numbers — making the difference between `loc[]` and `iloc[]` genuinely visible rather than coincidentally identical. I wrote six `loc[]` examples covering single-row selection, inclusive range slicing, selecting specific columns by name, combined row-and-column selection, selecting a row by its real `PassengerId` label, and boolean filtering combined with column selection. I wrote six matching `iloc[]` examples covering single-row selection by position, exclusive range slicing, selecting columns by their numeric position, combined row-and-column selection by position, selecting a row by position on the re-indexed DataFrame, and negative positional indexing. For the comparison, I called `loc[3]` and `iloc[3]` on the same re-indexed DataFrame side by side to show they return two different passengers, and directly compared slice behavior to show `loc[]` includes its end label while `iloc[]` excludes its end position.

## Outcome
By the end of this task, I could confidently choose between `loc[]` and `iloc[]` depending on whether I needed to select by a meaningful label or by raw position, and I understood exactly why the two can silently disagree once a DataFrame's index isn't just 0, 1, 2, .... The side-by-side `loc[3]` vs `iloc[3]` comparison on `df_by_id` made this concrete: they returned different passengers entirely. I also learned to watch out for the inclusive-vs-exclusive slicing difference between the two, since that's an easy source of off-by-one bugs if `loc[]` and `iloc[]` are used interchangeably without thinking about it.

## Interview Questions
1. **What is the difference between `loc[]` and `iloc[]`?**
   `loc[]` selects data using **labels**, whether it is the actual index value(s) and column name(s), whatever they are. `iloc[]` selects data using **integer positions**, counting from 0, regardless of what the labels actually are. When a DataFrame's index happens to be the default 0, 1, 2, ..., they often look interchangeable. But as soon as the index is anything else (like `PassengerId`), `df.loc[3]` and `df.iloc[3]` can return completely different rows.
2. **When should you use `loc[]`?**
   Use `loc[]` when you want to select data by a meaningful label, whether it is a specific index value (like a `PassengerId`), a named column, or a condition (boolean filtering), especially when the DataFrame's index isn't just its row position. It's also the more readable choice when the labels themselves are meaningful, since the code says exactly what row or column is being selected.
3. **Can `iloc[]` use column names?**
   No, `iloc[]` only accepts integer positions for both rows and columns, never names or labels. To select a column by name, `loc[]` (or plain `df["column_name"]`) is required instead; if you only know a column's position, you'd need to look up its integer index first (e.g. with `df.columns.get_loc("Name")`) before `iloc[]` could use it.