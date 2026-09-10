# Day 03: Loops for Dataset Processing

## Description
Practice for loops and while loops to process collections of values and perform repetitive data operations.

## Objective
Understand iteration and how loops can be used for basic data processing.

## Tools
- Python
- Jupyter Notebook

## Deliverables
- Examples using for loops and while loops
- A program that processes a list of numerical values
- A program that calculates summary statistics using loops

## Hints / Mini Guide
- Use `range()` for controlled iteration
- Practice iterating through lists and dictionaries
- Use accumulators for totals and averages

## Suggested Datasets
- Student Marks Dataset
- Sales Sample Dataset

## Approach
I used the `Student_Marks_Dataset.csv` file, which contains `number_courses`, `time_study`, and `Marks` data for 99 students. I loaded the dataset with pandas and converted the `Marks` and `number_courses` columns into plain Python lists to loop over. I then wrote several `for` loop examples — looping through a list directly, looping with `range()` (including a stepped range), looping through two lists together with `zip()`, and looping through a dictionary's key-value pairs — followed by `while` loop examples, including one that searches for the first student who scored above 50 and one that counts down remaining items to process. For the two required programs, I used a `for` loop with accumulator variables to count how many students passed versus failed (marks >= 40), and a second program that manually calculated the total, average, highest, and lowest marks using accumulators rather than built-in functions like `sum()` or `max()`. Finally, I built and looped through a dictionary that tallies how many students took each number of courses.

## Outcome
By the end of this task, I was comfortable using both `for` and `while` loops to iterate over lists, paired lists, and dictionaries, using `range()` for controlled iteration, and using accumulator variables to build up totals, averages, and running counts. I learned how loops let a program repeat the same operation across every item in a dataset — one value at a time — which is the foundation for processing much larger datasets before moving on to more efficient, vectorized approaches.

## Interview Questions
1. **What is the difference between a `for` loop and a `while` loop?**
   A `for` loop iterates over a known collection or a fixed range of values. It runs once for each item and stops automatically when the collection is exhausted. A `while` loop instead repeats for as long as a condition stays `True`, which is useful when you don't know in advance exactly how many times you'll need to loop (e.g., searching for a value or counting down).
2. **What does `range()` do?**
   `range()` generates a sequence of numbers, typically used to control how many times a loop runs. `range(5)` produces `0, 1, 2, 3, 4`, and `range(start, stop, step)` lets you control the starting point and the step size between numbers, such as `range(0, 100, 10)` for every 10th value.
3. **Why are vectorized operations generally preferred over loops in data science?**
   Vectorized operations (like pandas/NumPy operations that act on an entire column at once) are implemented in optimized, compiled code under the hood, so they run much faster than looping through each row in Python one at a time. They also tend to produce shorter, more readable code. Loops are still valuable for understanding the underlying logic and for tasks that don't fit neatly into a vectorized operation.