# Day 20: Data Types and Type Conversion

## Description
Inspect DataFrame data types and convert columns between strings, integers, floats, booleans, and dates.

## Objective
Understand how correct data types affect data processing and analysis.

## Tools
- Python
- Pandas
- Jupyter Notebook

## Deliverables
- Data-type inspection report
- Examples of converting at least four column types
- A cleaned dataset with appropriate data types

## Hints / Mini Guide
- Use `dtypes` to inspect column types
- Use `astype()` where appropriate
- Use `pd.to_numeric()` for numeric conversion

## Suggested Datasets
- Titanic Dataset
- Customer Dataset

## Approach
I used the `Titanic_Dataset.csv` file, first building a data-type inspection report combining `dtypes`, `info()`, non-null counts, and unique-value counts per column, which highlighted that `Survived` and `Pclass` are stored as plain integers despite really being categories. I then converted four column types: `Survived` from integer to boolean, `PassengerId` from integer to string (since it's an identifier, not a quantity meant for arithmetic), `Fare` from float to a formatted string and back to numeric using `pd.to_numeric()` (including a demonstration of `errors="coerce"` on an invalid value), and `Embarked`'s port codes into real historical embarkation dates using `pd.to_datetime()` — Southampton and Cherbourg both departed April 10, 1912, and Queenstown April 11, 1912. I combined all of this, plus converting `Sex`, `Pclass`, and `Embarked` to the memory-efficient `category` dtype, into one final cleaned DataFrame where each column's dtype matches what it actually represents.

## Outcome
By the end of this task, I was comfortable inspecting column dtypes and choosing the right conversion tool for the situation — `astype()` for direct, general conversions, and `pd.to_numeric()` when a string column might contain values that need safe handling (`errors="coerce"`) rather than crashing outright. Working through real Titanic columns made the reasoning behind each choice concrete: `Survived` is really a yes/no flag (boolean), `PassengerId` is an identifier that should never be summed (string), and `Embarked`'s port codes carry an actual date behind them once you know the ship's real 1912 sailing schedule. This reinforced that choosing the right dtype isn't just a formality; rather, this this keeps later calculations and analysis meaningful.

## Interview Questions
1. **Why are correct data types important?**
   The dtype of a column determines what operations make sense on it and how much memory it uses. Treating a category like `Pclass` as a plain integer risks someone accidentally averaging it, which produces a number with no real meaning; storing a low-cardinality text column as `category` instead of a general string saves memory; and converting text that represents dates or numbers into their proper dtype (`datetime64`, `int`/`float`) is required before any date arithmetic or numeric calculation can work correctly.
2. **What does `astype()` do?**
   `astype()` converts a Series (or a whole DataFrame) to a specified data type, such as `astype(bool)`, `astype(str)`, `astype("category")`, or `astype(int)`. It's a direct, general-purpose conversion, i.e., if the existing values can't be validly converted to the target type, it raises an error rather than silently producing a wrong result.
3. **How can you convert a string column to numeric?**
   Using `pd.to_numeric()`, e.g. `pd.to_numeric(df["column"])`. Unlike `astype(float)`, it has an `errors` parameter, i.e., `errors="raise"` (the default) stops on an invalid value, `errors="coerce"` converts anything unparseable into `NaN` instead of crashing, and `errors="ignore"` leaves the original values unchanged if conversion fails, which makes it a safer choice than `astype()` when a text column might contain some invalid entries.