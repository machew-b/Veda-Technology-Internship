# Day 08: Exception Handling for Data Programs

## Description
Learn how to handle common Python errors using try, except, else, and finally while processing data.

## Objective
Make data-processing programs more reliable and resistant to invalid input.

## Tools
- Python
- Jupyter Notebook

## Deliverables
- Examples of common Python exceptions
- A program using try-except
- A data conversion program that safely handles invalid values

## Hints / Mini Guide
- Practice handling `ValueError` and `TypeError`
- Keep error handling specific
- Use `finally` when cleanup is required

## Suggested Datasets
- Sample Customer Data
- Student Data

## Approach
I used the `Student_Performance_Dataset.csv` file, which contains real missing values across almost every column and one genuinely corrupted `math_score` entry (a garbled value containing stray tab/newline characters). I demonstrated five common exceptions with `try`/`except`, namely, `ValueError` (converting the corrupted value and a missing value to a number), `TypeError` (adding a number and a string together), `ZeroDivisionError` (dividing by zero), `KeyError` (accessing a missing dictionary key), and `IndexError` (accessing an out-of-range list position). I then wrote a `process_score()` program using `try`/`except`/`else` that only catches the specific exception it expects (`ValueError`), and a data conversion program that processed the entire `math_score` column, safely skipping invalid or missing values while counting how many conversions succeeded versus failed. Finally, I used `finally` in two places — once as a no-op placeholder to show where cleanup code would run on every attempt, and once to print a "Finished attempt" message after every single conversion, whether it succeeded or failed.

## Outcome
By the end of this task, I was comfortable catching specific exceptions with `try`/`except` rather than catching everything blindly, using `else` to run code only when no exception occurred, and using `finally` for cleanup that must always run regardless of outcome. Working with a dataset that had real missing values and one genuinely corrupted entry made it clear why this matters in practice: without exception handling, that single bad `math_score` value would have crashed the entire program the moment it was converted to a number. Instead, the program could catch the problem, skip or log it, and keep processing the remaining thousands of rows.

## Interview Questions
1. **Why is exception handling important?**
   Real-world data almost always contains unexpected or invalid values (missing data, corrupted entries, wrong types). Without exception handling, a single bad value (e.g., corrupted `math_score` entry in this dataset) would crash the entire program. `try`/`except` lets the program catch the problem, decide how to respond (skip it, log it, use a default value), and keep running instead of stopping completely.
2. **What is the difference between `ValueError` and `TypeError`?**
   A `ValueError` occurs when a value has the right type but an inappropriate value for the operation. For example, calling `float("\t41\n1")` fails because that text isn't a valid number, even though it's a string. A `TypeError` occurs when an operation is applied to an object of the wrong type entirely. For example, trying to add a number and a string together (`5.0 + "points"`) fails because addition isn't defined between those two types.
3. **What is the purpose of `finally`?**
   The `finally` block always runs after a `try`/`except`, whether an exception was raised or not, even if the `try` succeeded, even if an exception was caught, and even if an exception wasn't caught at all. It's used for cleanup code that must always happen, such as closing a file, releasing a resource, or logging that an attempt was made, regardless of whether that attempt succeeded.