# Day 06: List and Dictionary Comprehensions

## Description
Use list and dictionary comprehensions to create collections efficiently from existing data.

## Objective
Learn concise Python techniques commonly used in data preprocessing.

## Tools
- Python
- Jupyter Notebook

## Deliverables
- At least five list comprehension examples
- At least three dictionary comprehension examples
- Examples involving filtering and transformation

## Hints / Mini Guide
- Use `[expression for item in iterable]`
- Add conditions using `if`
- Compare comprehension with traditional loops

## Suggested Datasets
- Student Marks Dataset
- Product Dataset

## Approach
I used the `Student_Marks_Dataset.csv` file to build six list comprehension examples and four dictionary comprehension examples, covering plain transformation (rounding marks), filtering (`if mark >= 40`), combined filtering-and-transformation, conditional expressions (`"Pass" if ... else "Fail"`), comprehensions built from `range()`, and comprehensions built by iterating two lists together with `zip()`. For dictionaries, I built examples that map a student's position to their mark, filter down to only passing students, label each student Pass/Fail, and count how many students took each number of courses. For one list example and one dictionary example, I wrote the equivalent traditional `for` loop right alongside the comprehension to directly compare the two approaches.

## Outcome
By the end of this task, I was comfortable writing both list and dictionary comprehensions to filter and transform data in a single line. Comparing each comprehension to its traditional loop equivalent made it clear that comprehensions produce the exact same result in far fewer lines, which is why they're such a common technique for cleaning and preparing data before analysis. I also learned that a comprehension can include a filtering condition, a transformation expression, or both at once, and that the same `for ... in ...` pattern works whether you're building a list or a dictionary.

## Interview Questions
1. **What is list comprehension?**
   List comprehension is a concise way to build a new list from an existing iterable in a single line, using the form `[expression for item in iterable]`. It replaces the more verbose pattern of creating an empty list and appending to it inside a `for` loop.
2. **How can you filter values using list comprehension?**
   By adding an `if` condition at the end of the comprehension, e.g. `[mark for mark in marks if mark >= 40]`. Only items where the condition evaluates to `True` are included in the resulting list.
3. **What is dictionary comprehension?**
   Dictionary comprehension is the same idea as list comprehension, but it builds a dictionary instead of a list, using the form `{key_expression: value_expression for item in iterable}`. It can also include an `if` condition to filter which items are included, just like a list comprehension.