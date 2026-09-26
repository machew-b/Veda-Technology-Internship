# Day 19: Duplicate Records and Data Validation

## Description
Detect duplicate rows and perform simple validation checks to identify inconsistent or invalid records.

## Objective
Learn basic data-quality practices before analysis or modeling.

## Tools
- Python
- Pandas
- Jupyter Notebook

## Deliverables
- Duplicate record analysis
- Cleaned dataset without unwanted duplicates
- At least five data validation checks

## Hints / Mini Guide
- Use `duplicated()` to identify duplicates
- Use `drop_duplicates()` carefully
- Check ranges and expected categories

## Suggested Datasets
- Customer Dataset
- Sales Dataset

## Approach
I used the same intentionally messy `Customer_Dataset.csv` file from Day 7, which turned out to contain 3 exact full-row duplicates (confirmed to be the same 3 `Order ID`s duplicated as well). I used `duplicated()` to flag the duplicate rows, viewed both just the later copies and, with `keep=False`, every row involved in a duplicate group side by side, then used `drop_duplicates()` to remove them while keeping the first occurrence of each. I ran six data validation checks on the deduplicated data: `Age` within a realistic 0–120 range, `Gender` matching one of the expected category labels (case-insensitive), `Purchase Amount` not being negative, `Email` containing an "@" symbol and not being blank, `Order ID` being unique after cleaning, and `City` matching a known set of expected city names. I combined the results of all six checks into a single validation summary table showing how many rows failed each one.

## Outcome
By the end of this task, I was comfortable identifying and removing exact duplicate rows with `duplicated()`/`drop_duplicates()`, and understood that whole-row duplicate detection alone won't catch subtler issues like a repeated key with slightly different details (i.e., checking `subset=` on a key column is often necessary too). Running the six validation checks surfaced real data-quality problems in this dataset: a negative age (-5), an unrealistic age (150), inconsistent gender casing, a negative purchase amount, missing/malformed emails, and inconsistent city name casing and abbreviations. Building the validation summary table made it clear that combining several targeted, specific checks gives a much more complete picture of a dataset's quality than any single check (or eyeballing rows) could on its own.

## Interview Questions
1. **What is a duplicate record?**
   A duplicate record is a row in a dataset that repeats information already present in another row, either an exact copy of every column's value, or (more subtly) a repeated key value like an Order ID or customer that shouldn't logically appear more than once, even if some of the other columns differ slightly.
2. **How do you identify duplicates in Pandas?**
   `df.duplicated()` returns a boolean Series marking every row that exactly matches an earlier row as `True` (by default, keeping the first occurrence as `False`). Passing `subset=["column_name"]` checks for duplicates based on just one or more specific columns instead of the whole row, and `keep=False` marks every row involved in a duplicate group (not just the later copies), which is useful for reviewing them side by side before deciding what to remove.
3. **Why is data validation important?**
   Data validation catches records that are technically present but logically wrong or inconsistent. That is, a negative age, an amount that shouldn't be negative, or a category value that doesn't match any expected option. Without validation, these bad records can silently distort summary statistics, break downstream calculations, or produce misleading results in an analysis or a model, long before anyone notices something is wrong.