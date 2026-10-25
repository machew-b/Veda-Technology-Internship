# Sales & Service Demand Forecasting System: Final Report

**Project:** a four-day analytics project (Days 45 to 48) of the Veda Technology Internship, Data Science track  
**Demand analyzed:** four service lines (Internship Programs, Training Programs, IT Services, Digital Services), October 2023 to September 2026 (156 weeks)  
**Forecast:** the 26 weeks from September 28, 2026 to March 22, 2027  
**Data:** simulated (synthetic) demand, generated with a fixed random seed

## 1. Summary

This project built a forecasting system for the demand of four Veda Technology service lines. A Poisson regression (trend, yearly season, campaign days, and holidays) forecast the weekly total of the 26 test weeks with a WAPE of 7.2%, against 10.3% for the best baseline, 10.4% for a random forest, and 11.9% for Holt-Winters. Most of that lead comes from knowing the campaign plan: without the campaigns and holidays the regression's error rises to 9.5%. The forecast for the next 26 weeks is 3,632 units (11.7% above the same weeks a year earlier) but only 2.4% more revenue (INR 65.8 million against INR 64.2 million), because Digital Services are forecast 45% higher while IT Services, which are 64% of the revenue, are forecast 7% lower. The weeks after June 1, 2026 showed why a forecast built on history can fail: Digital Services ran 19% above and IT Services 19% below the forecast, and a simple monitor flagged the changes only 15 and 4 weeks after they began. The recommendations therefore cover planning with ranges and scenarios, watching the forecast against reality every week, and sharing the campaign plan with the forecast. All figures come from a simulated dataset, so they show the workflow and its pitfalls and do not describe the real company.

## 2. What Was Built

| Day | Work | Main output |
|---|---|---|
| 45 | Synthetic demand dataset, time-series preprocessing, monthly and weekly visualization | `demand_raw.csv` (4,404 rows), `demand_daily_cleaned.csv` (4,384 rows), `demand_weekly.csv`, `demand_monthly.csv` |
| 46 | Trend analysis, seasonality analysis, baseline forecasting | `seasonal_index_by_month.csv`, `calendar_effects.csv`, `baseline_forecasts_weekly.csv`, `baseline_metrics.csv` |
| 47 | Statistical and machine-learning models, prediction results, accuracy evaluation | `model_forecasts_test.csv`, `model_metrics.csv`, `model_validation.csv`, `future_demand_forecast_weekly.csv` |
| 48 | Future demand dashboard (static and Streamlit), planning scenarios, business planning recommendations, this report | `future_demand_dashboard.png`, `app.py`, `business_planning_recommendations.csv`, `campaign_scenarios_weekly.csv`, `forecast_monitor_weekly.csv`, `final_report.md` |

## 3. Method in Brief

1. **Data and preprocessing.** Three years of daily demand were simulated for four lines, with growth, yearly and weekly patterns, holidays, campaigns, noise, and a change in the last months. The data was then made deliberately messy (missing days, an outage, spikes, text numbers, duplicates, many spellings), and one pipeline cleaned it back into daily, weekly, and monthly tables.
2. **Trend and seasonality.** STL decomposition, the rolling 52-week total, and year-over-year growth described the trend; a seasonal index by calendar month, seasonal strength, and a Poisson regression described the yearly, weekly, holiday, and campaign effects.
3. **Baselines and models.** Six baselines (naive, two moving averages, three seasonal naive variants) were scored first. Then Holt-Winters, a Poisson regression, and a random forest were compared on the same split: 130 weeks for training and the next 26 weeks for the test, with every choice made on a validation period inside the training data.
4. **Evaluation.** MAE, WAPE, and bias, per line and for the weekly total, by period (before and after June 1) and by how far ahead the forecast looks, plus 80% ranges built from the validation errors.
5. **Planning.** The selected model was refitted on all 156 weeks and forecast the next 26 weeks, with a level correction (the ratio of the last 13 weeks' actual to fitted demand). The same model was run under three campaign plans, units were converted to revenue with the revenue per unit of each line, and a monitor compared the forecast with reality.

## 4. What the Demand Looks Like

- **Growth.** Over the last 52 weeks demand was higher than in the first 52 weeks by 75.0% in Digital Services, 49.6% in Training Programs, 26.5% in Internship Programs, and 17.6% in IT Services. Before June 2026 the regression finds growth of about 10% to 25% a year.
- **Yearly pattern.** Each line has its own peak: January for Internship Programs, July for Training Programs and Digital Services, and March for IT Services. The yearly pattern is strong (strength 0.79 to 0.91) and the weekday pattern is weaker (0.25 to 0.37).
- **Holidays and campaigns.** A holiday removes 44% to 55% of the demand of that day, and a campaign adds 16% to 35% to the demand of a full campaign week.
- **Money.** Demand and revenue are very unequal: IT Services are 15.8% of the units and 68.4% of the revenue, while Internship Programs are 39% of the units and 2.3% of the revenue.

## 5. How Accurate Were the Forecasts?

WAPE over the 26 test weeks (lower is better), on the weekly total of all lines and by line:

| Method | All lines | Internship | Training | IT | Digital |
|---|---|---|---|---|---|
| Moving average (13 weeks) | 12.5% | 21.1% | 25.9% | 26.0% | 45.9% |
| Smoothed seasonal naive with growth (best baseline) | 10.3% | 14.9% | 26.7% | 27.1% | 26.9% |
| Holt-Winters | 11.9% | 19.9% | 23.3% | 27.4% | 31.2% |
| **Poisson regression (selected)** | **7.2%** | **10.5%** | 19.0% | **23.3%** | **20.7%** |
| Random forest | 10.4% | 20.0% | **18.3%** | 29.0% | 25.4% |

- The regression was selected on the validation period (18.3% against 21.4% for the random forest and 22.2% for Holt-Winters), so the test was looked at only after the choice.
- Its lead is mostly information: without the campaign days and holidays its error on the test total rises from 7.2% to 9.5%. Spring 2026 had about half the campaign days of spring 2025 in two lines, and the methods that copy last year over-forecast; the regression was told the real plan.
- The errors of the lines are close to the randomness of the data: the regression is off by 14.5% to 20.9% even on the weeks it was fitted on.
- The 80% ranges contained 76.9% of the test weeks, but only 52.9% of the Digital Services weeks after June 1.

## 6. Why Historical Trends Do Not Always Predict Future Demand

After June 1, 2026, the demand of two lines changed level, which no model fitted on the earlier weeks could know. Against the forecast of the selected model, Digital Services demand was 19% higher (646 units against 544) and IT Services demand was 19% lower (284 against 352), while Internship Programs (+7%) and Training Programs (-5%) stayed close. A monitor that compares the demand of the last 8 weeks with the forecast and flags a gap of more than 20% raised no flag for the stable lines, flagged IT Services on July 27 (4 weeks after its slowdown began), and flagged Digital Services on September 14 (15 weeks after its lift began). The delay comes from the noise of weekly counts (15% to 20% for one line-week), which means that a real change needs weeks of evidence to be seen. The band of 20% was chosen after seeing these lines, so it needs calibration on more history.

The other reasons seen in this project were a change in the plan (fewer campaign days in spring 2026), a seasonal pattern learned from only three cycles, and a growth rate that cannot say when the growth stops. The practical answer is to put known future drivers into the model, report ranges and scenarios and not a single number, compare the forecast with reality every week, retrain every month, and keep the horizon short.

## 7. Business Planning Recommendations

The full text, with evidence and an impact scenario for each, is in `business_planning_recommendations.csv`. In summary:

| Priority | Area | Recommendation |
|---|---|---|
| High | IT Services (revenue risk) | IT Services are 64% of the forecast revenue and the forecast is 7% lower in units (465 against 498): find the cause of the slowdown, watch the 8-week ratio, and do not cut capacity until it stays below -20% for a longer period. Every 10% of IT units is about INR 4.2 million over 26 weeks. |
| High | Digital Services (capacity) | Plan capacity from the corrected forecast (778 units, +45%) with a reserve for the top of the range in busy weeks. Planning from last year's 538 units would leave 240 units, about INR 2.9 million, without capacity. |
| High | Forecast monitoring | Run the 8-week ratio every week for every line and retrain every month; keep the forecast with and without the level correction. |
| High | Campaign plan | Share the campaign calendar with the forecast: the 26-week total is 3,375 units without campaigns, 3,632 with the typical load, and 3,768 with 50% more campaign days. Place extra campaign days where they add revenue and not only units: the typical campaigns are worth about INR 1.4 million in IT Services and INR 0.1 million in Internship Programs, although the IT campaign effect is the least certain. |
| Medium | Internship Programs (seasonal capacity) | The busiest weeks are in January (up to 68 units, 1.3 times the average week); size mentors and seats for the peak, but keep the cost low because the revenue is only 2.6% of the total. |
| Medium | Training Programs (calendar) | December is about 10% quieter per week for all lines because of the holidays: use it for course preparation and prepare the July peak early. |
| Medium | Data and model limits | Plan about 26 weeks ahead and not beyond, read forecasts with their ranges, and replace the simulated history with real data. |

The impacts are scenarios with stated assumptions (for example, the revenue per unit of the last 52 weeks), not forecasts of money.

## 8. Risks and Limitations

- **Simulated data.** The patterns were built into the data, so recovering them is easier than in real data, and all figures describe the workflow and not the real company.
- **Three years of history.** Each month has only three observations, so the seasonal pattern is uncertain, and a trend cannot be extended with confidence.
- **The forecast needs the campaign plan.** The regression's advantage depends on knowing the plan; a wrong plan gives a wrong forecast. The future campaign load is an assumption (the typical load of the last 52 weeks).
- **The level correction is a judgment.** On five past starting weeks it cost half a point of WAPE on average when nothing had changed (19.0% against 18.5%); it is applied because it protects against a stale level, and the forecast without it is saved too.
- **Ranges describe ordinary randomness.** They did not cover the change after June 1.
- **Scenario assumptions.** The campaign scenarios assume each extra campaign day adds the same percentage and ignore the cost of campaigns.
- **The monitor band is not validated.** The 20% band was chosen after seeing the lines.

## 9. Next Steps

1. Replace the simulated history with the real inquiry and sales history, and repeat the validation and test.
2. Keep the campaign calendar and the forecast together, and test the scenarios against real campaign results.
3. Calibrate the monitor band on more history and add an automatic weekly run.
4. Add more drivers (prices, marketing spending, the academic calendar) when real data is available, and compare the regression with the random forest again on the larger data.

## 10. Project Documentation

The notebooks and deliverables are kept together in `09-sales-service-demand-forecasting/`:

- `part-1-demand-data-cleaning-and-eda.ipynb`
- `part-2-seasonality-and-baseline-forecasting.ipynb`
- `part-3-forecast-modeling-and-validation.ipynb`
- `part-4-forecasting-and-business-planning.ipynb`
- `app.py`, `future_demand_dashboard.png`, and `business_planning_recommendations.csv`

The raw, cleaned, reference, analysis, and forecast data remain in `../datasets/veda_demand/`.

Run the notebooks in part order. To launch the dashboard from the repository root, run `streamlit run 09-sales-service-demand-forecasting/app.py`.
