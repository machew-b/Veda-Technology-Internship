# Day 48: Sales & Service Demand Forecasting System (Part 4)

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
- Future demand dashboard
- Business planning recommendations

## Hints / Mini Guide
- Use synthetic historical data representing Veda Technology service inquiries or demand.
- Start with moving averages and baseline forecasting.
- Compare a simple statistical model with a machine-learning approach.
- Do not make the forecasting system unnecessarily complex.
- Explain why historical trends may not always predict future demand accurately.

## Approach
I started from the forecast of the next 26 weeks (September 28, 2026 to March 22, 2027) saved on Day 47 and first used the test weeks to explain why historical trends do not always predict future demand: after June 1, 2026 the demand of two lines changed level, and I measured how far the forecast of the selected model was from what happened, plotted the cumulative miss, and built a simple monitor (the demand of the last 8 weeks against the forecast for the same weeks, with a band of +/-20%) to see how long it takes to notice such a change. For planning, I refitted the selected Poisson regression on all 156 weeks exactly as on Day 47 (the same trend, season, and level correction, and I checked that it reproduces the saved forecast) and ran it under three campaign plans (no campaigns, the typical load of the last 52 weeks, and 50% more campaign days), converted units to rupees with the revenue per unit of each line over the last 52 weeks, compared everything with the same 26 weeks one year earlier, and found the busiest weeks with the top of their ranges as the demand to plan capacity for. Months have four or five weeks, so the plan by month is shown in units per week, with each week assigned to the month of its Thursday. From these tables I wrote seven business planning recommendations, each with the evidence calculated from the data, an action, and an impact that is labeled as a scenario with its assumptions, and saved them in `business_planning_recommendations.csv`. The future demand dashboard exists in two forms: a static page (`future_demand_dashboard.png`) with the demand tiles, the weekly forecasts with their ranges, the plan by month, the accuracy of the methods, the value of the campaign plan, and the monitor, and an interactive Streamlit app (`app.py`) with filters for the service lines, the campaign plan, the range, and the alert band, which I tested with Streamlit's test runner and by opening it in a browser. I also wrote a final report (`final_report.md`) that summarizes the four days. A mistake that I found on the way: the monthly table of Day 47 counted weeks in the month of their Monday, which made November look like a peak and December like a dip only because of five and four weeks, so I corrected that table and its observation (the forecast files did not change).

## Outcome
By the end of this task, I had a complete forecasting system with a dashboard and planning recommendations. The forecast for the next 26 weeks is 3,632 units, 11.7% more than the same weeks a year earlier, but the revenue is only 2.4% higher (INR 65.8 million against INR 64.2 million), because Digital Services are forecast 45% higher (778 units) while IT Services, which are 64% of the revenue, are forecast 7% lower (465 units). Per week, demand is highest in January and February (about 150 units) and lowest in December (about 126). The campaign plan alone moves the 26-week total from 3,375 units (no campaigns) to 3,632 (typical) and 3,768 (50% more campaign days), and it is worth the most money in IT Services (INR 1.4 million for the typical campaigns, with a very uncertain effect) and the least in Internship Programs (INR 0.1 million). The weeks after June 1 showed the limit of history: Digital Services ran 19% above and IT Services 19% below the forecast, and the monitor flagged them only 15 and 4 weeks after the changes began, while it never flagged the two stable lines. Because the data is simulated, these results show the workflow and the pitfalls, and the monitor band was chosen after seeing the lines, so it is an illustration. The main lesson was that the useful output of a forecast is a decision under uncertainty: ranges, scenarios, revenue and not only units, and a weekly check against reality.

## Interview Questions
1. **Why can a forecast based on historical trends be wrong, and how do you find out in time?**
   A model assumes that the patterns of the past continue, and it cannot know about a change that is not in its history. Here, Digital Services ran 19% above and IT Services 19% below the forecast after June 1, while the other two lines stayed close. To find out in time, compare the demand of the last few weeks with the forecast every week (here, an 8-week ratio with a band of +/-20%), but expect a delay: the IT slowdown was flagged after 4 weeks and the Digital lift after 15 weeks, because weekly counts are noisy. A band that is too narrow gives false alarms and one that is too wide is late, so it must be calibrated on more history. Putting known drivers (the campaign plan, the holidays) into the model, retraining often, and keeping the horizon short reduce the problem but do not remove it.
2. **How do you turn a forecast into business planning?**
   Convert units into the money and capacity that the decision depends on, and show the uncertainty. Here, units went up 11.7% but revenue only 2.4%, because the fall is in IT Services (64% of the revenue, INR 89,818 per unit) and the growth in cheaper lines, so the plan that looks good in units is almost flat in money. Capacity should be planned with the top of the range in the busiest weeks, and decisions that the business controls (the campaign plan) should be tested as scenarios (no campaigns, typical, +50%), with the assumptions stated: each extra campaign day adds the same percentage, and the cost of the campaigns is not in the data. A recommendation needs the evidence, an action, and an impact that is labeled as a scenario and not as a prediction.
3. **What makes a forecasting dashboard useful and honest?**
   It should answer the questions of the user (how much, when, how sure, and is it still on track) and show the uncertainty next to the number: the ranges, the accuracy on weeks that the model had not seen (WAPE 7.2% for the total, 10% to 23% by line), and a monitor that compares the forecast with reality. It should compare months per week and not per month (months have four or five weeks, which fooled my first monthly table), use the same color for the same line everywhere, and state the assumptions (here, the campaign plan and the simulated data) and what the forecast cannot know. An interactive version lets the planner change the plan, the lines, and the alert band, but the static page must be understandable alone.
