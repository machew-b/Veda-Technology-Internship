# Day 10: NumPy Indexing and Slicing

## Description
Practice selecting individual elements, rows, columns, and ranges from NumPy arrays using indexing and slicing.

## Objective
Develop the ability to efficiently access numerical data stored in arrays.

## Tools
- Python
- NumPy
- Jupyter Notebook

## Deliverables
- Examples of one-dimensional indexing
- Examples of two-dimensional indexing
- At least five slicing examples

## Hints / Mini Guide
- Remember that Python indexing starts at zero
- Use `array[row, column]` for two-dimensional arrays
- Practice positive and negative indexing

## Suggested Datasets
- Iris Dataset
- Wine Dataset

## Approach
I used the `Wine_Dataset.csv` file, creating a 1D array from the real `Alcohol` column and a 2D array from five real feature columns (`Alcohol`, `Malic acid`, `Ash`, `Magnesium`, `Color intensity`). For one-dimensional indexing, I practiced accessing elements with positive indices (the first and fifth values) and negative indices (the last and second-to-last values), reinforcing that indexing starts at zero. For two-dimensional indexing, I used `array[row, column]` to select individual elements, an entire row, an entire column, and an element using negative indices on both axes at once. For slicing, I wrote eight examples covering basic `start:stop` ranges, open-ended slices, negative slicing from the end, stepped slices, and three 2D slices selecting a range of rows, a range of columns, and a rectangular sub-block of both.

## Outcome
By the end of this task, I was comfortable using both indexing and slicing to pull exactly the data I needed out of a NumPy array, whether that was a single value, an entire row or column, or any rectangular sub-section, without writing a loop. Working through positive and negative indices on both 1D and 2D arrays made the zero-based indexing rule and the `array[row, column]` pattern feel natural, and practicing slicing showed how a single `start:stop:step` expression can replace what would otherwise take several lines of manual selection.

## Interview Questions
1. **What is zero-based indexing?**
   Zero-based indexing means the first element in a sequence is at position `0`, not `1`. So in an array of 178 wines, the first wine is `array[0]` and the last is `array[177]` (or equivalently `array[-1]`).
2. **How do you select a column from a two-dimensional NumPy array?**
   By using `array[:, column_index]`, where the colon (`:`) before the comma means "all rows" and the number after the comma selects that specific column. For example, `features[:, 2]` selects every row's value in column index 2.
3. **What is slicing?**
   Slicing is selecting a range of elements from an array using the `start:stop` (and optional `:step`) syntax, instead of a single index. It returns every element from `start` up to, but not including, `stop`, stepping by `step` if one is given (e.g. `alcohol[0:10:2]` returns every second value from index 0 up to index 9).