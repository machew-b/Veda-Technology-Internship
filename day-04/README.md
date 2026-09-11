# Day 4: Functions for Reusable Data Tasks

## Description
Create reusable Python functions for calculations, data transformation, and simple statistical operations.

## Objective
Learn how functions improve code organization and reusability.

## Tools
- Python
- Jupyter Notebook

## Deliverables
- At least five custom functions
- Functions for calculating mean, maximum, minimum, and percentage
- Examples showing function parameters and return values

## Hints / Mini Guide
- Use `def` to define functions
- Use parameters for reusable logic
- Return calculated values instead of only printing them

## Suggested Datasets
- Student Marks Dataset
- Employee Dataset

## Approach
I used the `Employee_Dataset.csv` file, which contains employee `Age`, `ExperienceInCurrentDomain`, `LeaveOrNot`, and other fields. I built seven custom functions with `def`: `calculate_mean`, `calculate_maximum`, `calculate_minimum`, and `calculate_percentage` (the four required calculations), plus `calculate_range` (which reuses `calculate_maximum` and `calculate_minimum` internally), `count_above_threshold` (which uses a default parameter value), and `summarize_column` (which combines several of the other functions and returns a dictionary of results). Every function takes one or more parameters and **returns** its result rather than only printing it, so the returned value could be stored in a variable and reused in later calculations. I then demonstrated calling the same function with different arguments (e.g., on the `Age` column versus the `ExperienceInCurrentDomain` column) and showed the difference between positional arguments and keyword arguments, as well as overriding a function's default parameter value.

## Outcome
By the end of this task, I was comfortable defining functions with `def`, using parameters to make the same logic reusable across different columns of data, and returning calculated values instead of just printing them. I saw how returning a value (rather than printing it) lets one function's output feed directly into another function or calculation, and how default parameter values and keyword arguments make functions more flexible to call. This showed why functions are central to organizing data science code since the same well-tested calculation can be reused everywhere it's needed instead of being rewritten each time.

## Interview Questions
1. **What is a function in Python?**
   A function is a named, reusable block of code defined with `def` that performs a specific task. It can accept input values (parameters), run some logic, and optionally `return` a result, so the same logic can be called multiple times without rewriting it.
2. **What is the difference between a parameter and an argument?**
   A parameter is the placeholder name listed in the function's definition (e.g. `def calculate_mean(values):` — `values` is the parameter). An argument is the actual value passed in when the function is called (e.g. `calculate_mean(ages)` — `ages` is the argument).
3. **Why are functions useful in data science projects?**
   Functions let you write a calculation or transformation once and reuse it across many columns, datasets, or projects, which reduces repeated code and bugs. They also make notebooks easier to read and test, since each function has a clear, single responsibility, and returning values (instead of just printing them) lets results be chained into further analysis.