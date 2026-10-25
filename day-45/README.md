# Day 45: Sales & Service Demand Forecasting System

## Description
Build a forecasting system that predicts future demand for technology services, digital services, training programs, or other business categories using historical time-series data.

## Objective
Introduce time-series analysis, trend detection, seasonality, forecasting, model evaluation, and business planning.

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Statsmodels
- Jupyter Notebook
- Streamlit

## Deliverables
- Historical service-demand dataset
- Time-series preprocessing
- Monthly/weekly demand visualization

## Hints / Mini Guide
- Use synthetic historical data representing Veda Technology service inquiries or demand.
- Start with moving averages and baseline forecasting.
- Compare a simple statistical model with a machine-learning approach.
- Do not make the forecasting system unnecessarily complex.
- Explain why historical trends may not always predict future demand accurately.

## Approach
Since the project asks for synthetic historical data, I generated a three-year daily history (October 1, 2023 to September 30, 2026, which is 1,096 days) of the demand for the four service lines of Veda Technology (Internship Programs, Training Programs, IT Services, and Digital Services), with a fixed random seed. The earlier business project had only one year of data, which is not enough to separate growth from seasonality, so I used three years. Each row holds the day, the service line, the demand in units, the revenue, and whether a marketing campaign was running, and the volume of the final year is set close to the Day 35 dataset. The simulation has a growth trend that differs by line, a yearly pattern with a different peak month for each line, a weekly pattern (weekends are lower, and IT Services drop the most), public holidays with lower demand, campaigns that lift demand by about 30%, day-to-day noise that is larger than a plain count would have, and a change in the last months (a lift for Digital Services from June 2026 and a slowdown for IT Services from July 2026) so that the forecasting days can show why historical trends do not always predict future demand. None of this is saved in the data, so the next days have to find it. I then made the data deliberately messy, like a real export (80 missing rows including five days with no data at all, an outage with six zero days, 12 spikes with an extra zero, 8 negative values, empty cells, 40 demand values and 80 revenue values typed as text, 16 spellings of the four service lines, two date formats, eight spellings of a yes/no campaign flag, and 100 duplicate rows), and saved it as `datasets/veda_demand/raw/demand_raw.csv` (4,404 rows). For the time-series preprocessing, I wrote one function, `clean_demand()`, driven by a short specification, that removes duplicates (exact copies and days exported twice), parses both date formats, standardizes the service line names, converts the numbers typed as text, sets impossible values to missing, rebuilds the complete calendar (one row for every day and line, which makes missing days visible), finds the outage (five or more zero days in a row, because weekends and holidays alone give shorter runs of zeros), finds the spikes (more than four times the typical value of the same weekday in the neighboring weeks, and only when the revenue does not agree with the value), and fills the gaps (from the revenue when it is known, and otherwise with the median of the same weekday in the neighboring weeks, which keeps the weekly pattern), flagging every filled value. It turned 4,404 raw rows into 4,384 clean rows, and all the validation checks pass. Because the data is simulated, I could check the pipeline against the original: 99.98% of the rows that were never damaged are identical, every missing day, outage day, negative value, and empty cell was found, 11 of the 12 spikes were found, and the 157 filled demand values are on average 1.76 units away from the truth, against 2.24 for a plain line average. The first version of the pipeline flagged 26 real zero days (it counted three zeros as an outage) and 12 real high days (it checked the units alone), which is why the final version needs five zero days and a second source (the revenue). I saved the cleaned daily table, a weekly table (156 complete Monday-to-Sunday weeks), a monthly table (36 months), and the holiday calendar in `datasets/veda_demand/`. For the monthly and weekly demand visualization, I plotted the monthly demand by line (adjusted to a 30.4-day month), the weekly demand by line with a 13-week moving average, the demand by weekday relative to an average day, and the shares of demand and of revenue by line, and I repeated the monthly totals in SQL with `sqlite3` to confirm that they match pandas.

## Outcome
By the end of this task, I had a reproducible simulated demand history, a time-series preprocessing pipeline that restored it, and the first look at the demand that prepares Day 46. The history has 17,564 units of demand and INR 349.0 million of revenue. Total demand grew from 4,938 units in the first year to 5,766 and then 6,860 (+38.9% in two years), and the lines grew at very different speeds: Digital Services +75.6%, Training Programs +49.7%, Internship Programs +26.8%, and IT Services +18.1%. Each line has its own peak month (January for Internship Programs, July for Training Programs, March for IT Services, and July and August for Digital Services), Monday to Thursday are 10% to 35% above an average day while the weekend is far lower (only 9.1% of the IT Services demand falls on weekends), and the change built into the last months is visible: from June 2026 Digital Services run 57.5% above the same months of the year before, while IT Services fall 7.7% below. Demand and revenue are very unequal: Internship Programs are 39% of the units and 2.3% of the revenue, while IT Services are 15.8% of the units and 68.4% of the revenue. Because the data is simulated, these findings reflect the assumptions I built into it, so they practice the analysis workflow and do not describe the real company. The main lesson was that time-series cleaning needs time-series logic: every day must exist, a filled value should respect the weekday pattern, and an outage or a spike has to be judged against its neighbors and against a second source, because the same raw value can be a real event or an error.

## Interview Questions
1. **How is cleaning time-series data different from cleaning an ordinary table?**
   In a time series the order and the completeness of the dates matter, so the first step is to rebuild the complete calendar, which makes the missing days visible (here, 80 rows that were simply absent, including five days with no data for any line). Filled values should respect the pattern of the series: a plain average would flatten the weekly rhythm, so I used the same weekday in the neighboring weeks, and the filled values were closer to the truth (an average error of 1.76 units against 2.24 for a plain average). Every filled value should also be flagged, so the models can tell real data from estimates. Finally, the split between training and test data must come before any modeling, so that no information from the future leaks into the model.
2. **How do you tell an outage or a spike from a real event?**
   Compare the value with what is normal for the same weekday in the neighboring weeks, and use a second source when there is one. Here, a run of zeros was only called an outage after five days in a row, because weekends and holidays produce runs of three or four zeros by themselves (counting three flagged 26 real days), and a high value was only called a spike when the revenue did not agree with it (a real high day has a high revenue, a typo does not), which avoided 12 false alarms. Any rule has a price: the one spike that was missed sat exactly on the threshold, and lowering the threshold would have flagged real busy days.
3. **Why look at weekly and monthly demand and not only daily demand?**
   Daily counts are noisy (here only about 4 units on a typical day for one line), so the trend and the yearly pattern are hidden by the randomness, while the weekly and monthly totals show them (the 13-week moving average shows the growth and the yearly waves clearly). Weekly data also shows campaigns and holidays, and monthly data is the right level for planning and for comparing the same month across years. The level should match the decision: staffing needs weekly numbers, a budget needs monthly numbers, and the daily data is kept for the weekday pattern and for building features.
