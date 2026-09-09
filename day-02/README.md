# Day 02: Conditional Statements for Data Decisions

## Description
Use if, elif, and else statements to make decisions based on numerical and categorical data.

## Objective
Learn how conditional logic can be used to classify and process data.

## Tools
- Python
- Jupyter Notebook

## Deliverables
- A notebook containing at least 10 conditional examples
- A simple classification program using conditions
- Examples using multiple conditions

## Hints / Mini Guide
- Use comparison operators such as `>`, `<`, and `==`
- Combine conditions using `and` and `or`
- Create categories such as Pass/Fail or Low/Medium/High

## Suggested Datasets
- Student Performance Dataset
- Employee Salary Dataset

## Approach
I used the `Employee_Salary_Dataset.csv` file, which contains employee `Experience_Years`, `Age`, `Gender`, and `Salary` data. First, I loaded the dataset with pandas and explored it using `.head()`, `.info()`, and `.describe()`. Then I wrote more than 10 single-condition `if`/`elif`/`else` examples on numerical fields (experience, age, salary) and a categorical field (gender) — such as checking salary thresholds, age groups, and experience levels. Next, I combined multiple conditions using `and`/`or` operators (e.g., flagging employees who are both highly experienced and well-paid, or highly experienced but underpaid). Finally, I used plain `if`/`elif`/`else` statements to classify a few individual employees into a salary tier and experience level, one record at a time.

## Outcome
By the end of this task, I was able to classify individual employees into a salary tier (Low, Medium, High, Very High) and an experience level (Entry-level, Mid-level, Senior-level) using conditional statements. I learned how `if`/`elif`/`else` logic — including compound conditions with `and`/`or` — can turn raw numerical and categorical data into meaningful, human-readable categories.

## Interview Questions
1. **What is the difference between `if` and `elif`?**
   `if` is the first condition checked in a chain. `elif` ("else if") lets you check an additional condition only if the conditions above it were `False`. Python evaluates them in order and runs the first matching branch, then skips the rest — so `elif` is used for extra conditions after the initial `if`.
2. **How do you combine multiple conditions in Python?**
   By using the logical operators `and` and `or` inside a single condition — `and` requires every condition to be `True`, while `or` requires at least one to be `True`. For example: `if experience_years > 10 and salary > 500000:` only runs when both conditions hold.
3. **What is the purpose of the `else` statement?**
   `else` is the fallback branch at the end of an `if`/`elif` chain. It runs whenever none of the conditions above it were `True`, making sure every possible case is handled instead of being silently skipped.