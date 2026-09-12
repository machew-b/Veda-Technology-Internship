# Day 5: Lists, Tuples, Sets and Dictionaries

## Description
Work with Python collection data structures and perform operations such as adding, removing, searching, and updating elements.

## Objective
Develop practical skills for handling structured data using Python collections.

## Tools
- Python
- Jupyter Notebook

## Deliverables
- Examples of all four collection types
- Programs demonstrating common methods
- A comparison table explaining their differences

## Hints / Mini Guide
- Practice `append()`, `remove()`, and `sort()` with lists
- Use dictionary keys to access values
- Use sets when unique values are required

## Suggested Datasets
- Student Dataset
- Employee Dataset

## Approach
I used the `Employee_Dataset.csv` file to build examples of all four Python collection types. For **lists**, I pulled real columns (`City`, `Age`) into lists and practiced `append()`, `remove()`, `sort()`, `insert()`, `pop()`, `count()`, and `index()`. For **tuples**, I paired real employee values together and practiced `count()` and `index()`, and showed how to work around a tuple's immutability by converting it to a list, modifying it, and converting it back. For **sets**, I built unique collections of cities and education levels, and used `add()`, `remove()`, `discard()`, `union()`, `intersection()`, `difference()`, and `issubset()` to compare groups of employees by payment tier. For **dictionaries**, I built a real employee record as a dictionary and practiced `get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`, and checking for a key with `in`. Finally, I put together a comparison table summarizing how each collection type differs in ordering, mutability, duplicate handling, and typical use case.

## Outcome
By the end of this task, I could confidently create and manipulate all four of Python's core collection types and knew which common methods apply to each one. I learned that lists are best for ordered data you plan to change, tuples are best for fixed data that shouldn't change, sets are best for uniqueness and comparing groups, and dictionaries are best for looking up values by a meaningful key. Building the comparison table made it clear how to choose the right collection type for a given data task.

## Interview Questions
1. **What is the difference between a list, tuple, set, and dictionary?**
   A list is ordered, mutable, and allows duplicates — good for data you plan to add to or reorder. A tuple is ordered but immutable — good for fixed data that shouldn't change. A set is unordered, mutable, and only stores unique values — good for removing duplicates or comparing groups. A dictionary stores `key: value` pairs with unique keys — good for looking up a value by a meaningful name instead of a numeric position.
2. **Why are sets useful for finding unique values?**
   A set automatically discards duplicate entries as soon as they're added, so converting any list or column of data into a set instantly gives you only the distinct values, without needing to write a loop to check for repeats manually. Sets also make operations like `union()`, `intersection()`, and `difference()` very efficient for comparing two groups.
3. **How do you access a dictionary value?**
   By using its key inside square brackets, like `employee_dict["City"]`, or with the `.get()` method, like `employee_dict.get("City")`. `.get()` is safer because it returns `None` (or a default value you specify) instead of raising an error if the key doesn't exist.