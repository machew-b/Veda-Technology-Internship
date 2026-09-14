# Day 07: String Processing for Data Cleaning

## Description
Practice string operations such as trimming spaces, changing case, replacing characters, splitting text, and extracting information.

## Objective
Build basic text-cleaning skills needed for real-world datasets.

## Tools
- Python
- Jupyter Notebook

## Deliverables
- A notebook demonstrating common string methods
- A small text-cleaning function
- Examples of cleaning names, emails, and categories

## Hints / Mini Guide
- Use `strip()`, `lower()`, `upper()`, `replace()`, and `split()`
- Check whether strings contain unwanted spaces
- Create standardized categorical values

## Suggested Datasets
- Customer Dataset
- Employee Dataset

## Approach
I used the `Customer_Dataset.csv` file, which is an intentionally messy customer records dataset containing inconsistent name casing, extra spaces, mixed gender labels (`"M"`, `"male"`, `"Female"`), city values with different casing and abbreviations (`"LA"`, `"new york"`, `"Los Angeles"`), missing values, invalid emails (`"bad-email"`, blanks), and purchase amounts formatted as text with `$` signs and commas. I demonstrated `strip()`, `lower()`, `upper()`, `replace()`, and `split()` directly on real values from the dataset, including splitting three different real date formats (`/`, `-`, and `.` separators) found in the `Signup Date` column. I wrote a `has_unwanted_spaces()` check, a reusable `clean_text()` function that trims whitespace while safely handling missing values, and an `extract_amount()` function that strips `$` and `,` characters from purchase amounts and converts them to numbers. For the names/emails/categories deliverable, I built `clean_email()` (trims, lowercases, and flags values without an `@` as invalid), `standardize_gender()`, and `standardize_city()` functions that map inconsistent raw text down to one clean, standardized label, and combined everything into a set of fully cleaned customer records.

## Outcome
By the end of this task, I was comfortable using `strip()`, `lower()`, `upper()`, `replace()`, and `split()` to clean and standardize real, messy text data, and could write small reusable functions to apply that cleaning consistently and safely (including handling missing values without errors). I learned that checking for unwanted spaces is as simple as comparing a string to its own `.strip()`'d version, that `replace()` is useful for stripping out formatting characters like `$` and `,` before converting text to numbers, and that mapping inconsistent category text (`"LA"`, `"Los Angeles"`, `"la"`) down to one standardized label is essential before any grouping or analysis can be trusted.

## Interview Questions
1. **Why is string cleaning important in data science?**
   Real-world text data is rarely consistent, i.e., the same value can show up with extra spaces, mixed casing, or different spellings (e.g. `"LA"`, `"Los Angeles"`, `"la"`). If it isn't cleaned first, operations like grouping, filtering, or joining on that text will silently treat those as different values, leading to incorrect counts and analysis. Cleaning strings early ensures the data is consistent and reliable before anything else is built on top of it.
2. **What does `strip()` do?**
   `strip()` removes any leading and trailing whitespace (spaces, tabs, newlines) from a string, without touching whitespace in the middle. For example, `" miami ".strip()` returns `"miami"`.
3. **How can you convert a string to lowercase?**
   By calling the `.lower()` method on it, e.g. `"JOHN.SMITH@EXAMPLE.COM".lower()` returns `"john.smith@example.com"`. This is especially useful for emails and categories, where case shouldn't matter but inconsistent casing is common in raw data.