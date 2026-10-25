# Python Fundamentals

## Day 01: Python Variables and Data Types

### Description
Practice Python variables and fundamental data types such as integers, floats, strings, booleans, lists, tuples, sets, and dictionaries using simple data science examples.

### Objective
Build a strong Python foundation required for data science.

### Tools
- Python
- Jupyter Notebook

### Deliverables
1. A Jupyter Notebook demonstrating different Python data types
2. Examples of type conversion and basic operations
3. A short README explaining the examples

### Approach
I used the `Student_Performance_Dataset.csv` file to demonstrate each of Python's fundamental data types: `int`, `float`, `str`, `bool`, `list`, `tuple`, `set`, and `dict` where every example uses a real value pulled directly from the dataset. For each type I used `type()` to confirm the variable's data type, and along the way I noticed the `math_score` column loads in as text, which required converting it to a number with `int()` before it could be used in calculations. I then practiced converting between types with `int()`, `float()`, `str()`, and `bool()`, including turning the dataset's `lunch` and `test_preparation_course` columns (stored as `1`/`0`) into real booleans, and performed basic operations on each type, such as arithmetic on scores, string concatenation, list functions like `max()`/`min()`/`sum()`, tuple indexing, set operations like `union()`, and dictionary key/value access.

### Outcome
By the end of this task, I could confidently identify and work with all of Python's core data types using `type()`, convert dataset values between types (including handling a real column that loaded in as text instead of numbers), and perform basic operations on numbers, strings, lists, tuples, sets, and dictionaries, all using real values from the Student Performance dataset. This gave me a solid Python foundation to build on for future data science tasks.

### Interview Questions
1. **What are the main built-in data types in Python?**
   The core built-in types are `int`, `float`, `str`, `bool`, `list`, `tuple`, `set`, and `dict`.
2. **What is the difference between a list and a tuple?**
   A list (`[]`) is ordered and mutable, where items can be added, removed, or changed after creation. A tuple (`()`) is ordered but immutable, i.e., once created, its contents cannot be changed.
3. **Why is Python widely used in data science?**
   Python has a simple, readable syntax and a rich ecosystem of libraries (like pandas, NumPy, and matplotlib) built specifically for loading, cleaning, analyzing, and visualizing data, which makes it fast to go from raw data to insights.

---

## Day 02: Conditional Statements for Data Decisions

### Description
Use if, elif, and else statements to make decisions based on numerical and categorical data.

### Objective
Learn how conditional logic can be used to classify and process data.

### Tools
- Python
- Jupyter Notebook

### Deliverables
- A notebook containing at least 10 conditional examples
- A simple classification program using conditions
- Examples using multiple conditions

### Hints / Mini Guide
- Use comparison operators such as `>`, `<`, and `==`
- Combine conditions using `and` and `or`
- Create categories such as Pass/Fail or Low/Medium/High

### Suggested Datasets
- Student Performance Dataset
- Employee Salary Dataset

### Approach
I used the `Employee_Salary_Dataset.csv` file, which contains employee `Experience_Years`, `Age`, `Gender`, and `Salary` data. First, I loaded the dataset with pandas and explored it using `.head()`, `.info()`, and `.describe()`. Then I wrote more than 10 single-condition `if`/`elif`/`else` examples on numerical fields (experience, age, salary) and a categorical field (gender), such as checking salary thresholds, age groups, and experience levels. Next, I combined multiple conditions using `and`/`or` operators (e.g., flagging employees who are both highly experienced and well-paid, or highly experienced but underpaid). Finally, I used plain `if`/`elif`/`else` statements to classify a few individual employees into a salary tier and experience level, one record at a time.

### Outcome
By the end of this task, I was able to classify individual employees into a salary tier (Low, Medium, High, Very High) and an experience level (Entry-level, Mid-level, Senior-level) using conditional statements. I learned how `if`/`elif`/`else` logic,  including compound conditions with `and`/`or`, can turn raw numerical and categorical data into meaningful, human-readable categories.

### Interview Questions
1. **What is the difference between `if` and `elif`?**
   `if` is the first condition checked in a chain. `elif` ("else if") lets you check an additional condition only if the conditions above it were `False`. Python evaluates them in order and runs the first matching branch, then skips the rest. Thus, `elif` is used for extra conditions after the initial `if`.
2. **How do you combine multiple conditions in Python?**
   By using the logical operators `and` and `or` inside a single condition. Note that `and` requires every condition to be `True`, while `or` requires at least one to be `True`. For example: `if experience_years > 10 and salary > 500000:` only runs when both conditions hold.
3. **What is the purpose of the `else` statement?**
   `else` is the fallback branch at the end of an `if`/`elif` chain. It runs whenever none of the conditions above it were `True`, making sure every possible case is handled instead of being silently skipped.

---

## Day 03: Loops for Dataset Processing

### Description
Practice for loops and while loops to process collections of values and perform repetitive data operations.

### Objective
Understand iteration and how loops can be used for basic data processing.

### Tools
- Python
- Jupyter Notebook

### Deliverables
- Examples using for loops and while loops
- A program that processes a list of numerical values
- A program that calculates summary statistics using loops

### Hints / Mini Guide
- Use `range()` for controlled iteration
- Practice iterating through lists and dictionaries
- Use accumulators for totals and averages

### Suggested Datasets
- Student Marks Dataset
- Sales Sample Dataset

### Approach
I used the `Student_Marks_Dataset.csv` file, which contains `number_courses`, `time_study`, and `Marks` data for 99 students. I loaded the dataset with pandas and converted the `Marks` and `number_courses` columns into plain Python lists to loop over. I then wrote several `for` loop examples — looping through a list directly, looping with `range()` (including a stepped range), looping through two lists together with `zip()`, and looping through a dictionary's key-value pairs — followed by `while` loop examples, including one that searches for the first student who scored above 50 and one that counts down remaining items to process. For the two required programs, I used a `for` loop with accumulator variables to count how many students passed versus failed (marks >= 40), and a second program that manually calculated the total, average, highest, and lowest marks using accumulators rather than built-in functions like `sum()` or `max()`. Finally, I built and looped through a dictionary that tallies how many students took each number of courses.

### Outcome
By the end of this task, I was comfortable using both `for` and `while` loops to iterate over lists, paired lists, and dictionaries, using `range()` for controlled iteration, and using accumulator variables to build up totals, averages, and running counts. I learned how loops let a program repeat the same operation across every item in a dataset — one value at a time — which is the foundation for processing much larger datasets before moving on to more efficient, vectorized approaches.

### Interview Questions
1. **What is the difference between a `for` loop and a `while` loop?**
   A `for` loop iterates over a known collection or a fixed range of values. It runs once for each item and stops automatically when the collection is exhausted. A `while` loop instead repeats for as long as a condition stays `True`, which is useful when you don't know in advance exactly how many times you'll need to loop (e.g., searching for a value or counting down).
2. **What does `range()` do?**
   `range()` generates a sequence of numbers, typically used to control how many times a loop runs. `range(5)` produces `0, 1, 2, 3, 4`, and `range(start, stop, step)` lets you control the starting point and the step size between numbers, such as `range(0, 100, 10)` for every 10th value.
3. **Why are vectorized operations generally preferred over loops in data science?**
   Vectorized operations (like pandas/NumPy operations that act on an entire column at once) are implemented in optimized, compiled code under the hood, so they run much faster than looping through each row in Python one at a time. They also tend to produce shorter, more readable code. Loops are still valuable for understanding the underlying logic and for tasks that don't fit neatly into a vectorized operation.

---

## Day 04: Functions for Reusable Data Tasks

### Description
Create reusable Python functions for calculations, data transformation, and simple statistical operations.

### Objective
Learn how functions improve code organization and reusability.

### Tools
- Python
- Jupyter Notebook

### Deliverables
- At least five custom functions
- Functions for calculating mean, maximum, minimum, and percentage
- Examples showing function parameters and return values

### Hints / Mini Guide
- Use `def` to define functions
- Use parameters for reusable logic
- Return calculated values instead of only printing them

### Suggested Datasets
- Student Marks Dataset
- Employee Dataset

### Approach
I used the `Employee_Dataset.csv` file, which contains employee `Age`, `ExperienceInCurrentDomain`, `LeaveOrNot`, and other fields. I built seven custom functions with `def`: `calculate_mean`, `calculate_maximum`, `calculate_minimum`, and `calculate_percentage` (the four required calculations), plus `calculate_range` (which reuses `calculate_maximum` and `calculate_minimum` internally), `count_above_threshold` (which uses a default parameter value), and `summarize_column` (which combines several of the other functions and returns a dictionary of results). Every function takes one or more parameters and **returns** its result rather than only printing it, so the returned value could be stored in a variable and reused in later calculations. I then demonstrated calling the same function with different arguments (e.g., on the `Age` column versus the `ExperienceInCurrentDomain` column) and showed the difference between positional arguments and keyword arguments, as well as overriding a function's default parameter value.

### Outcome
By the end of this task, I was comfortable defining functions with `def`, using parameters to make the same logic reusable across different columns of data, and returning calculated values instead of just printing them. I saw how returning a value (rather than printing it) lets one function's output feed directly into another function or calculation, and how default parameter values and keyword arguments make functions more flexible to call. This showed why functions are central to organizing data science code since the same well-tested calculation can be reused everywhere it's needed instead of being rewritten each time.

### Interview Questions
1. **What is a function in Python?**
   A function is a named, reusable block of code defined with `def` that performs a specific task. It can accept input values (parameters), run some logic, and optionally `return` a result, so the same logic can be called multiple times without rewriting it.
2. **What is the difference between a parameter and an argument?**
   A parameter is the placeholder name listed in the function's definition (e.g. `def calculate_mean(values):` — `values` is the parameter). An argument is the actual value passed in when the function is called (e.g. `calculate_mean(ages)` — `ages` is the argument).
3. **Why are functions useful in data science projects?**
   Functions let you write a calculation or transformation once and reuse it across many columns, datasets, or projects, which reduces repeated code and bugs. They also make notebooks easier to read and test, since each function has a clear, single responsibility, and returning values (instead of just printing them) lets results be chained into further analysis.

---

## Day 05: Lists, Tuples, Sets and Dictionaries

### Description
Work with Python collection data structures and perform operations such as adding, removing, searching, and updating elements.

### Objective
Develop practical skills for handling structured data using Python collections.

### Tools
- Python
- Jupyter Notebook

### Deliverables
- Examples of all four collection types
- Programs demonstrating common methods
- A comparison table explaining their differences

### Hints / Mini Guide
- Practice `append()`, `remove()`, and `sort()` with lists
- Use dictionary keys to access values
- Use sets when unique values are required

### Suggested Datasets
- Student Dataset
- Employee Dataset

### Approach
I used the `Employee_Dataset.csv` file to build examples of all four Python collection types. For **lists**, I pulled real columns (`City`, `Age`) into lists and practiced `append()`, `remove()`, `sort()`, `insert()`, `pop()`, `count()`, and `index()`. For **tuples**, I paired real employee values together and practiced `count()` and `index()`, and showed how to work around a tuple's immutability by converting it to a list, modifying it, and converting it back. For **sets**, I built unique collections of cities and education levels, and used `add()`, `remove()`, `discard()`, `union()`, `intersection()`, `difference()`, and `issubset()` to compare groups of employees by payment tier. For **dictionaries**, I built a real employee record as a dictionary and practiced `get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`, and checking for a key with `in`. Finally, I put together a comparison table summarizing how each collection type differs in ordering, mutability, duplicate handling, and typical use case.

### Outcome
By the end of this task, I could confidently create and manipulate all four of Python's core collection types and knew which common methods apply to each one. I learned that lists are best for ordered data you plan to change, tuples are best for fixed data that shouldn't change, sets are best for uniqueness and comparing groups, and dictionaries are best for looking up values by a meaningful key. Building the comparison table made it clear how to choose the right collection type for a given data task.

### Interview Questions
1. **What is the difference between a list, tuple, set, and dictionary?**
   A list is ordered, mutable, and allows duplicates — good for data you plan to add to or reorder. A tuple is ordered but immutable — good for fixed data that shouldn't change. A set is unordered, mutable, and only stores unique values — good for removing duplicates or comparing groups. A dictionary stores `key: value` pairs with unique keys — good for looking up a value by a meaningful name instead of a numeric position.
2. **Why are sets useful for finding unique values?**
   A set automatically discards duplicate entries as soon as they're added, so converting any list or column of data into a set instantly gives you only the distinct values, without needing to write a loop to check for repeats manually. Sets also make operations like `union()`, `intersection()`, and `difference()` very efficient for comparing two groups.
3. **How do you access a dictionary value?**
   By using its key inside square brackets, like `employee_dict["City"]`, or with the `.get()` method, like `employee_dict.get("City")`. `.get()` is safer because it returns `None` (or a default value you specify) instead of raising an error if the key doesn't exist.

---

## Day 06: List and Dictionary Comprehensions

### Description
Use list and dictionary comprehensions to create collections efficiently from existing data.

### Objective
Learn concise Python techniques commonly used in data preprocessing.

### Tools
- Python
- Jupyter Notebook

### Deliverables
- At least five list comprehension examples
- At least three dictionary comprehension examples
- Examples involving filtering and transformation

### Hints / Mini Guide
- Use `[expression for item in iterable]`
- Add conditions using `if`
- Compare comprehension with traditional loops

### Suggested Datasets
- Student Marks Dataset
- Product Dataset

### Approach
I used the `Student_Marks_Dataset.csv` file to build six list comprehension examples and four dictionary comprehension examples, covering plain transformation (rounding marks), filtering (`if mark >= 40`), combined filtering-and-transformation, conditional expressions (`"Pass" if ... else "Fail"`), comprehensions built from `range()`, and comprehensions built by iterating two lists together with `zip()`. For dictionaries, I built examples that map a student's position to their mark, filter down to only passing students, label each student Pass/Fail, and count how many students took each number of courses. For one list example and one dictionary example, I wrote the equivalent traditional `for` loop right alongside the comprehension to directly compare the two approaches.

### Outcome
By the end of this task, I was comfortable writing both list and dictionary comprehensions to filter and transform data in a single line. Comparing each comprehension to its traditional loop equivalent made it clear that comprehensions produce the exact same result in far fewer lines, which is why they're such a common technique for cleaning and preparing data before analysis. I also learned that a comprehension can include a filtering condition, a transformation expression, or both at once, and that the same `for ... in ...` pattern works whether you're building a list or a dictionary.

### Interview Questions
1. **What is list comprehension?**
   List comprehension is a concise way to build a new list from an existing iterable in a single line, using the form `[expression for item in iterable]`. It replaces the more verbose pattern of creating an empty list and appending to it inside a `for` loop.
2. **How can you filter values using list comprehension?**
   By adding an `if` condition at the end of the comprehension, e.g. `[mark for mark in marks if mark >= 40]`. Only items where the condition evaluates to `True` are included in the resulting list.
3. **What is dictionary comprehension?**
   Dictionary comprehension is the same idea as list comprehension, but it builds a dictionary instead of a list, using the form `{key_expression: value_expression for item in iterable}`. It can also include an `if` condition to filter which items are included, just like a list comprehension.

---

## Day 07: String Processing for Data Cleaning

### Description
Practice string operations such as trimming spaces, changing case, replacing characters, splitting text, and extracting information.

### Objective
Build basic text-cleaning skills needed for real-world datasets.

### Tools
- Python
- Jupyter Notebook

### Deliverables
- A notebook demonstrating common string methods
- A small text-cleaning function
- Examples of cleaning names, emails, and categories

### Hints / Mini Guide
- Use `strip()`, `lower()`, `upper()`, `replace()`, and `split()`
- Check whether strings contain unwanted spaces
- Create standardized categorical values

### Suggested Datasets
- Customer Dataset
- Employee Dataset

### Approach
I used the `Customer_Dataset.csv` file, which is an intentionally messy customer records dataset containing inconsistent name casing, extra spaces, mixed gender labels (`"M"`, `"male"`, `"Female"`), city values with different casing and abbreviations (`"LA"`, `"new york"`, `"Los Angeles"`), missing values, invalid emails (`"bad-email"`, blanks), and purchase amounts formatted as text with `$` signs and commas. I demonstrated `strip()`, `lower()`, `upper()`, `replace()`, and `split()` directly on real values from the dataset, including splitting three different real date formats (`/`, `-`, and `.` separators) found in the `Signup Date` column. I wrote a `has_unwanted_spaces()` check, a reusable `clean_text()` function that trims whitespace while safely handling missing values, and an `extract_amount()` function that strips `$` and `,` characters from purchase amounts and converts them to numbers. For the names/emails/categories deliverable, I built `clean_email()` (trims, lowercases, and flags values without an `@` as invalid), `standardize_gender()`, and `standardize_city()` functions that map inconsistent raw text down to one clean, standardized label, and combined everything into a set of fully cleaned customer records.

### Outcome
By the end of this task, I was comfortable using `strip()`, `lower()`, `upper()`, `replace()`, and `split()` to clean and standardize real, messy text data, and could write small reusable functions to apply that cleaning consistently and safely (including handling missing values without errors). I learned that checking for unwanted spaces is as simple as comparing a string to its own `.strip()`'d version, that `replace()` is useful for stripping out formatting characters like `$` and `,` before converting text to numbers, and that mapping inconsistent category text (`"LA"`, `"Los Angeles"`, `"la"`) down to one standardized label is essential before any grouping or analysis can be trusted.

### Interview Questions
1. **Why is string cleaning important in data science?**
   Real-world text data is rarely consistent, i.e., the same value can show up with extra spaces, mixed casing, or different spellings (e.g. `"LA"`, `"Los Angeles"`, `"la"`). If it isn't cleaned first, operations like grouping, filtering, or joining on that text will silently treat those as different values, leading to incorrect counts and analysis. Cleaning strings early ensures the data is consistent and reliable before anything else is built on top of it.
2. **What does `strip()` do?**
   `strip()` removes any leading and trailing whitespace (spaces, tabs, newlines) from a string, without touching whitespace in the middle. For example, `" miami ".strip()` returns `"miami"`.
3. **How can you convert a string to lowercase?**
   By calling the `.lower()` method on it, e.g. `"JOHN.SMITH@EXAMPLE.COM".lower()` returns `"john.smith@example.com"`. This is especially useful for emails and categories, where case shouldn't matter but inconsistent casing is common in raw data.

---

## Day 08: Exception Handling for Data Programs

### Description
Learn how to handle common Python errors using try, except, else, and finally while processing data.

### Objective
Make data-processing programs more reliable and resistant to invalid input.

### Tools
- Python
- Jupyter Notebook

### Deliverables
- Examples of common Python exceptions
- A program using try-except
- A data conversion program that safely handles invalid values

### Hints / Mini Guide
- Practice handling `ValueError` and `TypeError`
- Keep error handling specific
- Use `finally` when cleanup is required

### Suggested Datasets
- Sample Customer Data
- Student Data

### Approach
I used the `Student_Performance_Dataset.csv` file, which contains real missing values across almost every column and one genuinely corrupted `math_score` entry (a garbled value containing stray tab/newline characters). I demonstrated five common exceptions with `try`/`except`, namely, `ValueError` (converting the corrupted value and a missing value to a number), `TypeError` (adding a number and a string together), `ZeroDivisionError` (dividing by zero), `KeyError` (accessing a missing dictionary key), and `IndexError` (accessing an out-of-range list position). I then wrote a `process_score()` program using `try`/`except`/`else` that only catches the specific exception it expects (`ValueError`), and a data conversion program that processed the entire `math_score` column, safely skipping invalid or missing values while counting how many conversions succeeded versus failed. Finally, I used `finally` in two places — once as a no-op placeholder to show where cleanup code would run on every attempt, and once to print a "Finished attempt" message after every single conversion, whether it succeeded or failed.

### Outcome
By the end of this task, I was comfortable catching specific exceptions with `try`/`except` rather than catching everything blindly, using `else` to run code only when no exception occurred, and using `finally` for cleanup that must always run regardless of outcome. Working with a dataset that had real missing values and one genuinely corrupted entry made it clear why this matters in practice: without exception handling, that single bad `math_score` value would have crashed the entire program the moment it was converted to a number. Instead, the program could catch the problem, skip or log it, and keep processing the remaining thousands of rows.

### Interview Questions
1. **Why is exception handling important?**
   Real-world data almost always contains unexpected or invalid values (missing data, corrupted entries, wrong types). Without exception handling, a single bad value (e.g., corrupted `math_score` entry in this dataset) would crash the entire program. `try`/`except` lets the program catch the problem, decide how to respond (skip it, log it, use a default value), and keep running instead of stopping completely.
2. **What is the difference between `ValueError` and `TypeError`?**
   A `ValueError` occurs when a value has the right type but an inappropriate value for the operation. For example, calling `float("\t41\n1")` fails because that text isn't a valid number, even though it's a string. A `TypeError` occurs when an operation is applied to an object of the wrong type entirely. For example, trying to add a number and a string together (`5.0 + "points"`) fails because addition isn't defined between those two types.
3. **What is the purpose of `finally`?**
   The `finally` block always runs after a `try`/`except`, whether an exception was raised or not, even if the `try` succeeded, even if an exception was caught, and even if an exception wasn't caught at all. It's used for cleanup code that must always happen, such as closing a file, releasing a resource, or logging that an attempt was made, regardless of whether that attempt succeeded.
