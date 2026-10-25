# Day 46: Sales & Service Demand Forecasting System (Part 2)

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
- Trend analysis
- Seasonality analysis
- Baseline forecasting model

## Hints / Mini Guide
- Use synthetic historical data representing Veda Technology service inquiries or demand.
- Start with moving averages and baseline forecasting.
- Compare a simple statistical model with a machine-learning approach.
- Do not make the forecasting system unnecessarily complex.
- Explain why historical trends may not always predict future demand accurately.

## Approach
I started from the cleaned daily, weekly, and monthly tables of Day 45. For the trend analysis, I plotted the rolling 52-week total of each line (which removes the yearly pattern, so the line shows only growth) and decomposed the monthly series, on a log scale so that seasonality is a percentage, with STL (trend, season, and remainder). I fitted a straight line to the seasonally adjusted months before June 2026 and extended it, to show what a forecaster who trusted the old trend would expect, and I computed the year-over-year growth, which cancels the season. For the seasonality analysis, I turned the seasonal part of STL into a seasonal index by calendar month (1.00 is an average month) and showed it as a heatmap, measured the strength of the yearly and weekly patterns (1 minus the variance of the remainder over the variance of the seasonal part plus the remainder), and fitted a Poisson regression for each line (a model for counts, with robust standard errors) on the days before June 2026 with the trend, month, weekday, holiday, and campaign together, which separates a campaign in July from a July effect and gives confidence intervals. Because the data is simulated, I could grade all of this against the values used to generate it. The first version of the decomposition used robust STL, and the seasonally adjusted line on the chart was visibly wrong: with only 36 months, the robust version of this statsmodels release returned residuals of exactly zero at both ends of the series, so I switched to the standard version and checked that the residuals were no longer zero at the ends. For the baseline forecasting model, I forecast weekly demand and split the history in time, never at random: the 130 weeks until March 23, 2026 for training and the last 26 weeks (March 30 to September 27, 2026) for testing, which includes 17 weeks after the change in the last months, so the models of Day 47 are judged on the same weeks. I built six baselines using only the training weeks: the naive forecast (the last week), moving averages of 4 and 13 weeks, the seasonal naive forecast (the same week one year earlier), the seasonal naive forecast multiplied by the growth of the last 52 weeks, and the same forecast smoothed over three weeks. I evaluated them with MAE, WAPE (the total error over the total demand), and bias, and avoided MAPE because weekly counts can be small. I saved the seasonal index, the regression effects, the baseline forecasts, and the baseline metrics in `datasets/veda_demand/analysis/` and `forecasts/`.

## Outcome
By the end of this task, I had a trend analysis, a seasonality analysis, and a set of baseline forecasts with a score for each. Before June 2026, demand grew by about 10% to 25% a year depending on the line, with Digital Services and Training Programs growing fastest and IT Services almost flat since late 2025. The yearly pattern is strong (strength 0.79 to 0.91) and its peaks are right for all four lines, the weekly pattern is weaker (0.25 to 0.37), holidays remove 44% to 55% of the demand, and campaigns add 16% to 35%; all the confidence intervals of the regression contain the true values, and the regression recovered the growth better than the STL line for every line. Among the baselines, the seasonal naive forecast was 15.3% too low in total, multiplying it by the recent growth removed that bias, and smoothing it over three weeks gave the best result, a WAPE of 10.3% for the weekly total, against 12.5% for the 13-week average. The total hides the weakness of every baseline: after June 1, the best baseline is 21.5% too low for Digital Services and 24.3% too high for IT Services, and the two errors cancel in the total. Each line also misses by 15% to 27% per week even in the best case, because weekly counts are noisy. Because the data is simulated, these results show that the methods work, and the best baseline was chosen by its test result, so its score is the benchmark for Day 47, not a promise. The main lesson was to check every chart against the numbers behind it, because a decomposition can fail silently, and to look at the lines separately, because a good total can hide large errors in the parts.

## Interview Questions
1. **How do you separate the trend from seasonality in a time series?**
   Seasonality repeats at a fixed period (here, 12 months), so a decomposition such as STL estimates a repeating seasonal part and a slowly changing trend, and the remainder is what neither explains. On a log scale the parts are additive, so seasonality becomes a percentage of the level. A simpler check is to compare each month with the same month one year earlier, or to use a rolling total over a full year, because both cancel the yearly pattern. A regression with a time term and month terms does the same and also gives confidence intervals. Here, the STL growth missed by up to 8 points, while the regression missed by up to 5, because it also took holidays and campaigns out of the trend. With only three years of history, there are only three observations of each month, so every seasonal estimate is uncertain.
2. **Why start with baseline forecasts, and why split the data in time?**
   A baseline gives the score that a more complex model must beat, and it shows how much of the pattern is simple repetition: here, repeating last year's week with the recent growth, smoothed over three weeks, gave a WAPE of 10.3% for the weekly total, so a model that does not beat it has not earned its complexity. The split must follow time because the forecast always predicts the future from the past: a random split would let the model see weeks after the ones it is tested on, and the scores would be too good. I used WAPE and bias instead of MAPE, because MAPE explodes when a week has few units, and the bias shows whether a method is systematically too high or too low, which MAE does not.
3. **A forecast has a low error in total. Is it good enough?**
   Not necessarily, because errors in different lines can cancel. After June 1, the best baseline had a total error of only -6.0%, but it was 21.5% too low for Digital Services and 24.3% too high for IT Services, which would mean too few staff in one line and too many in the other. The error should be reported at the level at which the decision is made (per line, and per week if the staffing is weekly), together with the bias. The result also depends on the period: the same baseline over-forecast the weeks before June (+14.2% in total), so one score for the whole test is a summary, not a guarantee.
