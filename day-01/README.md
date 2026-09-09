# Day 01: Python Variables and Data Types

## Description
Practice Python variables and fundamental data types such as integers, floats, strings, booleans, lists, tuples, sets, and dictionaries using simple data science examples.

## Objective
Build a strong Python foundation required for data science.

## Tools
- Python
- Jupyter Notebook

## Deliverables
1. A Jupyter Notebook demonstrating different Python data types
2. Examples of type conversion and basic operations
3. A short README explaining the examples

## Approach
I used the `Student_Performance_Dataset.csv` file to demonstrate each of Python's fundamental data types: `int`, `float`, `str`, `bool`, `list`, `tuple`, `set`, and `dict` where every example uses a real value pulled directly from the dataset. For each type I used `type()` to confirm the variable's data type, and along the way I noticed the `math_score` column loads in as text, which required converting it to a number with `int()` before it could be used in calculations. I then practiced converting between types with `int()`, `float()`, `str()`, and `bool()`, including turning the dataset's `lunch` and `test_preparation_course` columns (stored as `1`/`0`) into real booleans, and performed basic operations on each type, such as arithmetic on scores, string concatenation, list functions like `max()`/`min()`/`sum()`, tuple indexing, set operations like `union()`, and dictionary key/value access.

## Outcome
By the end of this task, I could confidently identify and work with all of Python's core data types using `type()`, convert dataset values between types (including handling a real column that loaded in as text instead of numbers), and perform basic operations on numbers, strings, lists, tuples, sets, and dictionaries, all using real values from the Student Performance dataset. This gave me a solid Python foundation to build on for future data science tasks.

## Interview Questions
1. **What are the main built-in data types in Python?**
   The core built-in types are `int`, `float`, `str`, `bool`, `list`, `tuple`, `set`, and `dict`.
2. **What is the difference between a list and a tuple?**
   A list (`[]`) is ordered and mutable — items can be added, removed, or changed after creation. A tuple (`()`) is ordered but immutable, i.e., once created, its contents cannot be changed.
3. **Why is Python widely used in data science?**
   Python has a simple, readable syntax and a rich ecosystem of libraries (like pandas, NumPy, and matplotlib) built specifically for loading, cleaning, analyzing, and visualizing data, which makes it fast to go from raw data to insights.