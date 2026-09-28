# Day 21: Date Parsing and Datetime Basics

## Description
Convert text-based dates into Pandas datetime values, extract calendar information, validate dates, and use dates to analyze orders.

## Objective
Learn how to work with date and time data in data science.

## Tools
- Python
- Pandas
- Jupyter Notebook

## Deliverables
- Parsed `Order Date` and `Ship Date` columns
- New columns for order year, month, day, and weekday
- A check for missing or invalid dates
- A short analysis based on dates

## Hints / Mini Guide
- Use `pd.to_datetime()` to convert text into datetime values.
- Use `errors="coerce"` to convert invalid values to `NaT`.
- Use the `.dt` accessor to extract `.year`, `.month`, `.day`, and `.day_name()`.
- Subtract datetime columns to calculate elapsed time.

## Suggested Datasets
- Superstore Dataset
- Online Retail Dataset

## Approach
I used `Superstore_Dataset.csv`, specifying its `cp1252` text encoding while loading it. I converted `Order Date` and `Ship Date` with `pd.to_datetime()` and the explicit `%m/%d/%Y` format, using `errors="coerce"` so unparseable values would be visible as `NaT`. I created order year, month, day, and weekday columns with `.dt`, then calculated shipping duration by subtracting the order date from the ship date. Finally, I checked for missing or invalid dates and ship dates earlier than order dates, and grouped sales by year and month while counting unique orders by weekday.

## Outcome
The date-quality checks found no missing or invalid dates and no ship-before-order records. 2017 had the highest annual sales at `$733,215.26`; November 2017 was the highest-sales month at `$118,447.82`. Average shipping time was about `3.96` days. Converting the text columns into datetimes made date arithmetic and calendar-based summaries straightforward.

## Interview Questions
1. **Why should dates be converted from text to datetime?**
	Datetime values support chronological sorting, date arithmetic, filtering by time period, and extracting calendar fields. Text values do not reliably support these operations.
2. **What does `errors="coerce"` do in `pd.to_datetime()`?**
	It converts values that cannot be parsed into `NaT` (Not a Time), allowing the invalid values to be identified and handled without stopping the conversion.
3. **What is the `.dt` accessor used for?**
	It provides vectorized datetime properties and methods for a datetime Series, such as `.dt.year`, `.dt.month`, `.dt.day`, and `.dt.day_name()`.
