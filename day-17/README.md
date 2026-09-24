# Day 17: Filtering and Sorting DataFrames

## Description
Filter rows using conditions and sort DataFrame values in ascending and descending order.

## Objective
Learn fundamental techniques for retrieving specific records from datasets.

## Tools
- Python
- Pandas
- Jupyter Notebook

## Deliverables
- At least five filtering examples
- Multiple sorting examples
- A short analysis of filtered records

## Hints / Mini Guide
- Use boolean conditions
- Use `sort_values()`
- Combine multiple conditions when required

## Suggested Datasets
- Titanic Dataset
- Superstore Dataset

## Approach
I used the `Superstore_Dataset.csv` file (9,994 orders across 21 columns), writing six filtering examples: orders with Sales over 500, orders in the Furniture category, loss-making orders (Profit < 0), loss-making Technology orders combined with `&` (AND), orders from the West or East region combined with `|` (OR), and orders in specific sub-categories using `.isin()`. For sorting, I used `sort_values()` to sort by Sales descending, by Profit ascending (to surface the biggest losses first), by two columns at once (Category ascending, then Sales descending within each category), and to sort the already-filtered loss-making orders by loss size. For the analysis, I took a closer look at the loss-making orders using `.value_counts()` and `.groupby()`, finding that 1,871 of the 9,994 orders (about 19%) lost money, totaling roughly -$156,131 in lost profit, with Office Supplies having the most loss-making orders overall.

## Outcome
By the end of this task, I was comfortable filtering DataFrame rows with single and combined boolean conditions, and sorting by one or multiple columns with independent ascending/descending directions. Filtering down to the loss-making orders and analyzing them further showed that filtering isn't just an isolated skill. That is, it's usually the first step toward answering a real question about the data, like which product category is losing the most money and whether that's explained by order volume or something else worth investigating further.

## Interview Questions
1. **How do you filter rows in Pandas?**
   By placing a boolean condition inside `df[...]`, such as `df[df["Sales"] > 500]`. Pandas evaluates the condition for every row, producing a Series of `True`/`False` values, and then returns only the rows where the result was `True`. `df.loc[condition]` works the same way and also lets you select specific columns at the same time.
2. **How do you sort a DataFrame?**
   Using `sort_values()`, passing the column name (or a list of column names) to sort by, e.g. `df.sort_values("Sales", ascending=False)`. Sorting is ascending by default; passing `ascending=False` reverses it, and passing a list for both the column names and the `ascending` parameter lets you sort by multiple columns with different directions at once.
3. **How do you combine multiple filtering conditions?**
   By wrapping each condition in parentheses and joining them with `&` for AND or `|` for OR, for example, `df[(df["Category"] == "Technology") & (df["Profit"] < 0)]`. The parentheses are required because Python's operator precedence would otherwise evaluate `&`/`|` before the comparison operators, causing an error or an incorrect result.