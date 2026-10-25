# Pandas and Data Cleaning

## Day 15: Pandas DataFrame Basics

### Description
Create DataFrames from dictionaries and datasets and explore rows, columns, shape, and summary information.

### Objective
Learn the primary Pandas structure used for tabular data analysis.

### Tools
- Python
- Pandas
- Jupyter Notebook

### Deliverables
- Create a DataFrame manually
- Load a real dataset into a DataFrame
- Display shape, columns, data types, and summary statistics

### Hints / Mini Guide
- Use `pd.DataFrame()`
- Use `head()` and `info()` to inspect data
- Use `describe()` for numerical summaries

### Suggested Datasets
- Titanic Dataset
- Iris Dataset

### Approach
I built a small DataFrame manually from a Python dictionary using `pd.DataFrame()`, then loaded the real `Titanic_Dataset.csv` file (891 rows, 12 columns) with `pd.read_csv()`. I explored the loaded DataFrame's `shape`, `size`, `columns`, and `dtypes`, and used `info()` to see a combined summary including non-null counts per column, which revealed real missing data in `Age` (177 missing), `Cabin` (687 missing), and `Embarked` (2 missing). I used `describe()` to get numerical summary statistics (mean, min, max, quartiles) for the numeric columns like `Age` and `Fare`, and `describe(include="object")` to get a comparable summary for the text columns. I also looked more closely at one categorical column (`Embarked`) using `.unique()` and `.value_counts()` to see its distinct values and how often each appears.

### Outcome
By the end of this task, I was comfortable creating a DataFrame both manually and from a real CSV file, and knew which Pandas methods to reach for first when exploring any new dataset. `shape`, `columns`, and `dtypes` quickly answer "how big is this and what's in it," while `info()` and `describe()` go a step further, surfacing missing values and numerical summaries in a single call. Working with the real Titanic dataset made this concrete: `info()` immediately flagged that `Age`, `Cabin`, and `Embarked` had missing values, which is exactly the kind of thing that needs to be caught before any further analysis.

### Interview Questions
1. **What is a Pandas DataFrame?**
   A DataFrame is Pandas' core two-dimensional data structure — a table of rows and columns, similar to a spreadsheet or a SQL table, where each column can hold a different data type. It can be built manually (e.g. from a dictionary) or loaded from a file like a CSV, and comes with built-in methods for exploring, cleaning, and analyzing the data.
2. **What information does `info()` provide?**
   `info()` gives a combined summary of the DataFrame: the total number of rows, the list of columns, how many non-null (non-missing) values each column has, the data type of each column, and the DataFrame's overall memory usage. It's usually the fastest way to spot missing data and confirm each column loaded with the expected type.
3. **What is the difference between `shape` and `size`?**
   `shape` returns a tuple of `(number of rows, number of columns)`. For this dataset, `(891, 12)`. `size` returns a single number: the total count of individual cells in the DataFrame, which is rows × columns — for this dataset, `891 × 12 = 10,692`.

---

## Day 16: Selecting Rows and Columns with loc and iloc

### Description
Practice selecting rows and columns using Pandas loc[] and iloc[] and understand label-based versus position-based selection.

### Objective
Develop accurate DataFrame selection skills.

### Tools
- Python
- Pandas
- Jupyter Notebook

### Deliverables
- At least five loc[] examples
- At least five iloc[] examples
- A comparison of both methods

### Hints / Mini Guide
- `loc[]` uses labels
- `iloc[]` uses integer positions
- Practice selecting both rows and columns

### Suggested Datasets
- Titanic Dataset
- Iris Dataset

### Approach
I used the `Titanic_Dataset.csv` file, and also created a second version of it (`df_by_id`) indexed by `PassengerId` instead of the default 0, 1, 2, ... index, so that row labels and row positions would no longer be the same numbers — making the difference between `loc[]` and `iloc[]` genuinely visible rather than coincidentally identical. I wrote six `loc[]` examples covering single-row selection, inclusive range slicing, selecting specific columns by name, combined row-and-column selection, selecting a row by its real `PassengerId` label, and boolean filtering combined with column selection. I wrote six matching `iloc[]` examples covering single-row selection by position, exclusive range slicing, selecting columns by their numeric position, combined row-and-column selection by position, selecting a row by position on the re-indexed DataFrame, and negative positional indexing. For the comparison, I called `loc[3]` and `iloc[3]` on the same re-indexed DataFrame side by side to show they return two different passengers, and directly compared slice behavior to show `loc[]` includes its end label while `iloc[]` excludes its end position.

### Outcome
By the end of this task, I could confidently choose between `loc[]` and `iloc[]` depending on whether I needed to select by a meaningful label or by raw position, and I understood exactly why the two can silently disagree once a DataFrame's index isn't just 0, 1, 2, .... The side-by-side `loc[3]` vs `iloc[3]` comparison on `df_by_id` made this concrete: they returned different passengers entirely. I also learned to watch out for the inclusive-vs-exclusive slicing difference between the two, since that's an easy source of off-by-one bugs if `loc[]` and `iloc[]` are used interchangeably without thinking about it.

### Interview Questions
1. **What is the difference between `loc[]` and `iloc[]`?**
   `loc[]` selects data using **labels**, whether it is the actual index value(s) and column name(s), whatever they are. `iloc[]` selects data using **integer positions**, counting from 0, regardless of what the labels actually are. When a DataFrame's index happens to be the default 0, 1, 2, ..., they often look interchangeable. But as soon as the index is anything else (like `PassengerId`), `df.loc[3]` and `df.iloc[3]` can return completely different rows.
2. **When should you use `loc[]`?**
   Use `loc[]` when you want to select data by a meaningful label, whether it is a specific index value (like a `PassengerId`), a named column, or a condition (boolean filtering), especially when the DataFrame's index isn't just its row position. It's also the more readable choice when the labels themselves are meaningful, since the code says exactly what row or column is being selected.
3. **Can `iloc[]` use column names?**
   No, `iloc[]` only accepts integer positions for both rows and columns, never names or labels. To select a column by name, `loc[]` (or plain `df["column_name"]`) is required instead; if you only know a column's position, you'd need to look up its integer index first (e.g. with `df.columns.get_loc("Name")`) before `iloc[]` could use it.

---

## Day 17: Filtering and Sorting DataFrames

### Description
Filter rows using conditions and sort DataFrame values in ascending and descending order.

### Objective
Learn fundamental techniques for retrieving specific records from datasets.

### Tools
- Python
- Pandas
- Jupyter Notebook

### Deliverables
- At least five filtering examples
- Multiple sorting examples
- A short analysis of filtered records

### Hints / Mini Guide
- Use boolean conditions
- Use `sort_values()`
- Combine multiple conditions when required

### Suggested Datasets
- Titanic Dataset
- Superstore Dataset

### Approach
I used the `Superstore_Dataset.csv` file (9,994 orders across 21 columns), writing six filtering examples: orders with Sales over 500, orders in the Furniture category, loss-making orders (Profit < 0), loss-making Technology orders combined with `&` (AND), orders from the West or East region combined with `|` (OR), and orders in specific sub-categories using `.isin()`. For sorting, I used `sort_values()` to sort by Sales descending, by Profit ascending (to surface the biggest losses first), by two columns at once (Category ascending, then Sales descending within each category), and to sort the already-filtered loss-making orders by loss size. For the analysis, I took a closer look at the loss-making orders using `.value_counts()` and `.groupby()`, finding that 1,871 of the 9,994 orders (about 19%) lost money, totaling roughly -$156,131 in lost profit, with Office Supplies having the most loss-making orders overall.

### Outcome
By the end of this task, I was comfortable filtering DataFrame rows with single and combined boolean conditions, and sorting by one or multiple columns with independent ascending/descending directions. Filtering down to the loss-making orders and analyzing them further showed that filtering isn't just an isolated skill. That is, it's usually the first step toward answering a real question about the data, like which product category is losing the most money and whether that's explained by order volume or something else worth investigating further.

### Interview Questions
1. **How do you filter rows in Pandas?**
   By placing a boolean condition inside `df[...]`, such as `df[df["Sales"] > 500]`. Pandas evaluates the condition for every row, producing a Series of `True`/`False` values, and then returns only the rows where the result was `True`. `df.loc[condition]` works the same way and also lets you select specific columns at the same time.
2. **How do you sort a DataFrame?**
   Using `sort_values()`, passing the column name (or a list of column names) to sort by, e.g. `df.sort_values("Sales", ascending=False)`. Sorting is ascending by default; passing `ascending=False` reverses it, and passing a list for both the column names and the `ascending` parameter lets you sort by multiple columns with different directions at once.
3. **How do you combine multiple filtering conditions?**
   By wrapping each condition in parentheses and joining them with `&` for AND or `|` for OR, for example, `df[(df["Category"] == "Technology") & (df["Profit"] < 0)]`. The parentheses are required because Python's operator precedence would otherwise evaluate `&`/`|` before the comparison operators, causing an error or an incorrect result.

---

## Day 18: Missing Values in Pandas

### Description
Identify missing values in a dataset and practice handling them using techniques such as dropping and filling missing values.

### Objective
Understand one of the most common data preprocessing problems.

### Tools
- Python
- Pandas
- Jupyter Notebook

### Deliverables
- Missing-value summary
- Examples using isna() and notna()
- A cleaned version of the dataset

### Hints / Mini Guide
- Use `isna().sum()` to count missing values
- Compare dropping and filling strategies
- Use mean or median carefully for numerical columns

### Suggested Datasets
- Titanic Dataset
- House Prices Dataset

### Approach
The real `House_Prices_Dataset.csv` file turned out to have **zero missing values** across all 545 rows and 13 columns, confirmed with `isna().sum()`. Since this task is specifically about missing-value handling, I created a clearly-labeled working copy of the dataset with a small, reproducible set of values (about 5% each) set to `NaN` across the `price`, `area`, `bedrooms`, and `furnishingstatus` columns, leaving the original real data untouched. I built a missing-value summary table showing both the count and percentage missing per column, and demonstrated `isna()`/`notna()` on individual columns and across the whole DataFrame to filter rows with and without missing data. I then compared dropping strategies (`dropna()` on all columns vs. `dropna(subset=["price"])` for one specific column) against filling strategies (`fillna()` with a constant placeholder, the column median, and the column mode), including a direct comparison of `price`'s mean vs. median to show why median is the safer choice when a column has outliers. Finally, I combined median filling for the numeric columns and mode filling for the categorical column to produce a fully cleaned dataset with zero missing values and no rows lost.

### Outcome
By the end of this task, I could confidently build a missing-value summary, use `isna()`/`notna()` to inspect and filter data by missingness, and choose between dropping and filling based on the situation. Comparing `dropna()` against `fillna()` on the same simulated data made the tradeoff concrete: dropping is simple but throws away every other value in that row, while filling preserves all rows but requires picking a sensible replacement. Comparing the mean and median for `price` specifically reinforced why median is generally the safer default for skewed numeric columns. That is, a few expensive houses pull the mean upward, while the median stays representative of a "typical" value.

### Interview Questions
1. **What are missing values?**
   Missing values are entries in a dataset where no data was recorded for a particular row and column, represented in Pandas as `NaN` (Not a Number) for numeric and object columns, or `NaT` for missing dates. They can occur for many reasons, for instance, in a field wasn't collected, a value was lost during data entry or merging, or a question simply didn't apply to that row.
2. **What are common ways to handle missing values?**
   The two main approaches are **dropping** (removing rows or columns that contain missing values, using `dropna()`) and **filling** (replacing missing values with a substitute, using `fillna()` which commonly a constant, the column's mean or median for numeric data, the mode for categorical data, or a value carried forward/backward from a nearby row).
3. **When should you avoid simply dropping missing rows?**
   You should avoid dropping rows when missing values are common enough that dropping them all would lose a large, potentially meaningful portion of the dataset, when the missing rows aren't randomly distributed (e.g. certain groups are more likely to have missing data, which would bias the remaining dataset), or when there just isn't much data to begin with and every row matters. In those cases, filling in a reasonable estimate usually preserves more useful information than deleting the row entirely.

---

## Day 19: Duplicate Records and Data Validation

### Description
Detect duplicate rows and perform simple validation checks to identify inconsistent or invalid records.

### Objective
Learn basic data-quality practices before analysis or modeling.

### Tools
- Python
- Pandas
- Jupyter Notebook

### Deliverables
- Duplicate record analysis
- Cleaned dataset without unwanted duplicates
- At least five data validation checks

### Hints / Mini Guide
- Use `duplicated()` to identify duplicates
- Use `drop_duplicates()` carefully
- Check ranges and expected categories

### Suggested Datasets
- Customer Dataset
- Sales Dataset

### Approach
I used the same intentionally messy `Customer_Dataset.csv` file from Day 7, which turned out to contain 3 exact full-row duplicates (confirmed to be the same 3 `Order ID`s duplicated as well). I used `duplicated()` to flag the duplicate rows, viewed both just the later copies and, with `keep=False`, every row involved in a duplicate group side by side, then used `drop_duplicates()` to remove them while keeping the first occurrence of each. I ran six data validation checks on the deduplicated data: `Age` within a realistic 0–120 range, `Gender` matching one of the expected category labels (case-insensitive), `Purchase Amount` not being negative, `Email` containing an "@" symbol and not being blank, `Order ID` being unique after cleaning, and `City` matching a known set of expected city names. I combined the results of all six checks into a single validation summary table showing how many rows failed each one.

### Outcome
By the end of this task, I was comfortable identifying and removing exact duplicate rows with `duplicated()`/`drop_duplicates()`, and understood that whole-row duplicate detection alone won't catch subtler issues like a repeated key with slightly different details (i.e., checking `subset=` on a key column is often necessary too). Running the six validation checks surfaced real data-quality problems in this dataset: a negative age (-5), an unrealistic age (150), inconsistent gender casing, a negative purchase amount, missing/malformed emails, and inconsistent city name casing and abbreviations. Building the validation summary table made it clear that combining several targeted, specific checks gives a much more complete picture of a dataset's quality than any single check (or eyeballing rows) could on its own.

### Interview Questions
1. **What is a duplicate record?**
   A duplicate record is a row in a dataset that repeats information already present in another row, either an exact copy of every column's value, or (more subtly) a repeated key value like an Order ID or customer that shouldn't logically appear more than once, even if some of the other columns differ slightly.
2. **How do you identify duplicates in Pandas?**
   `df.duplicated()` returns a boolean Series marking every row that exactly matches an earlier row as `True` (by default, keeping the first occurrence as `False`). Passing `subset=["column_name"]` checks for duplicates based on just one or more specific columns instead of the whole row, and `keep=False` marks every row involved in a duplicate group (not just the later copies), which is useful for reviewing them side by side before deciding what to remove.
3. **Why is data validation important?**
   Data validation catches records that are technically present but logically wrong or inconsistent. That is, a negative age, an amount that shouldn't be negative, or a category value that doesn't match any expected option. Without validation, these bad records can silently distort summary statistics, break downstream calculations, or produce misleading results in an analysis or a model, long before anyone notices something is wrong.

---

## Day 20: Data Types and Type Conversion

### Description
Inspect DataFrame data types and convert columns between strings, integers, floats, booleans, and dates.

### Objective
Understand how correct data types affect data processing and analysis.

### Tools
- Python
- Pandas
- Jupyter Notebook

### Deliverables
- Data-type inspection report
- Examples of converting at least four column types
- A cleaned dataset with appropriate data types

### Hints / Mini Guide
- Use `dtypes` to inspect column types
- Use `astype()` where appropriate
- Use `pd.to_numeric()` for numeric conversion

### Suggested Datasets
- Titanic Dataset
- Customer Dataset

### Approach
I used the `Titanic_Dataset.csv` file, first building a data-type inspection report combining `dtypes`, `info()`, non-null counts, and unique-value counts per column, which highlighted that `Survived` and `Pclass` are stored as plain integers despite really being categories. I then converted four column types: `Survived` from integer to boolean, `PassengerId` from integer to string (since it's an identifier, not a quantity meant for arithmetic), `Fare` from float to a formatted string and back to numeric using `pd.to_numeric()` (including a demonstration of `errors="coerce"` on an invalid value), and `Embarked`'s port codes into real historical embarkation dates using `pd.to_datetime()` — Southampton and Cherbourg both departed April 10, 1912, and Queenstown April 11, 1912. I combined all of this, plus converting `Sex`, `Pclass`, and `Embarked` to the memory-efficient `category` dtype, into one final cleaned DataFrame where each column's dtype matches what it actually represents.

### Outcome
By the end of this task, I was comfortable inspecting column dtypes and choosing the right conversion tool for the situation — `astype()` for direct, general conversions, and `pd.to_numeric()` when a string column might contain values that need safe handling (`errors="coerce"`) rather than crashing outright. Working through real Titanic columns made the reasoning behind each choice concrete: `Survived` is really a yes/no flag (boolean), `PassengerId` is an identifier that should never be summed (string), and `Embarked`'s port codes carry an actual date behind them once you know the ship's real 1912 sailing schedule. This reinforced that choosing the right dtype isn't just a formality; rather, this this keeps later calculations and analysis meaningful.

### Interview Questions
1. **Why are correct data types important?**
   The dtype of a column determines what operations make sense on it and how much memory it uses. Treating a category like `Pclass` as a plain integer risks someone accidentally averaging it, which produces a number with no real meaning; storing a low-cardinality text column as `category` instead of a general string saves memory; and converting text that represents dates or numbers into their proper dtype (`datetime64`, `int`/`float`) is required before any date arithmetic or numeric calculation can work correctly.
2. **What does `astype()` do?**
   `astype()` converts a Series (or a whole DataFrame) to a specified data type, such as `astype(bool)`, `astype(str)`, `astype("category")`, or `astype(int)`. It's a direct, general-purpose conversion, i.e., if the existing values can't be validly converted to the target type, it raises an error rather than silently producing a wrong result.
3. **How can you convert a string column to numeric?**
   Using `pd.to_numeric()`, e.g. `pd.to_numeric(df["column"])`. Unlike `astype(float)`, it has an `errors` parameter, i.e., `errors="raise"` (the default) stops on an invalid value, `errors="coerce"` converts anything unparseable into `NaN` instead of crashing, and `errors="ignore"` leaves the original values unchanged if conversion fails, which makes it a safer choice than `astype()` when a text column might contain some invalid entries.

---

## Day 21: Date Parsing and Datetime Basics

### Description
Convert text-based dates into Pandas datetime values, extract calendar information, validate dates, and use dates to analyze orders.

### Objective
Learn how to work with date and time data in data science.

### Tools
- Python
- Pandas
- Jupyter Notebook

### Deliverables
- Parsed `Order Date` and `Ship Date` columns
- New columns for order year, month, day, and weekday
- A check for missing or invalid dates
- A short analysis based on dates

### Hints / Mini Guide
- Use `pd.to_datetime()` to convert text into datetime values.
- Use `errors="coerce"` to convert invalid values to `NaT`.
- Use the `.dt` accessor to extract `.year`, `.month`, `.day`, and `.day_name()`.
- Subtract datetime columns to calculate elapsed time.

### Suggested Datasets
- Superstore Dataset
- Online Retail Dataset

### Approach
I used `Superstore_Dataset.csv`, specifying its `cp1252` text encoding while loading it. I converted `Order Date` and `Ship Date` with `pd.to_datetime()` and the explicit `%m/%d/%Y` format, using `errors="coerce"` so unparseable values would be visible as `NaT`. I created order year, month, day, and weekday columns with `.dt`, then calculated shipping duration by subtracting the order date from the ship date. Finally, I checked for missing or invalid dates and ship dates earlier than order dates, and grouped sales by year and month while counting unique orders by weekday.

### Outcome
The date-quality checks found no missing or invalid dates and no ship-before-order records. 2017 had the highest annual sales at `$733,215.26`; November 2017 was the highest-sales month at `$118,447.82`. Average shipping time was about `3.96` days. Converting the text columns into datetimes made date arithmetic and calendar-based summaries straightforward.

### Interview Questions
1. **Why should dates be converted from text to datetime?**
	Datetime values support chronological sorting, date arithmetic, filtering by time period, and extracting calendar fields. Text values do not reliably support these operations.
2. **What does `errors="coerce"` do in `pd.to_datetime()`?**
	It converts values that cannot be parsed into `NaT` (Not a Time), allowing the invalid values to be identified and handled without stopping the conversion.
3. **What is the `.dt` accessor used for?**
	It provides vectorized datetime properties and methods for a datetime Series, such as `.dt.year`, `.dt.month`, `.dt.day`, and `.dt.day_name()`.
