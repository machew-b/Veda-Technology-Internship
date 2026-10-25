# Day 47: Sales & Service Demand Forecasting System (Part 3)

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
- Forecasting model
- Prediction results
- Forecast accuracy evaluation

## Hints / Mini Guide
- Use synthetic historical data representing Veda Technology service inquiries or demand.
- Start with moving averages and baseline forecasting.
- Compare a simple statistical model with a machine-learning approach.
- Do not make the forecasting system unnecessarily complex.
- Explain why historical trends may not always predict future demand accurately.

## Approach
I used the same split as Day 46 (the 130 weeks until March 23, 2026 for training, and the next 26 weeks for the test), so the new models are scored on the same weeks as the baselines and can be compared with them. Choosing a model by looking at the test would be cheating, so every choice was made on a validation period inside the training data (models fitted on the first 104 weeks and tried on the next 26), and the test was looked at only after the choices were made. I compared two statistical models and one machine-learning model. Holt-Winters (exponential smoothing with a 52-week season) uses only the past of each line. A Poisson regression for each line (a model for counts, in `statsmodels`) models the expected weekly demand as the exponential of a trend, a yearly season described by three pairs of sine and cosine waves (the number of pairs was chosen on the validation), the number of campaign days in the week, and the number of public holidays in the week; it can use the campaign plan and the holiday calendar of the weeks to be forecast, which are known in advance. The machine-learning model is a random forest in `scikit-learn` that forecasts every horizon from 1 to 26 weeks with one model (the direct method): each example is a pair (week the forecast starts, week to forecast), the target is the demand as a multiple of the average of the last 52 weeks (a forest cannot extrapolate a trend, so a relative target solves this), and the features are the horizon, the recent level against the year level, the same week of last year (with its neighbors), the campaign days and holidays, and the season; its depth was chosen on the validation. I scored the models with MAE, WAPE, and bias on each line and on the weekly total, compared them with the best baselines of Day 46, split the error by period (before and after the change in the last months) and by how far ahead the forecast looks, checked what the random forest relies on, and tested how much of the regression's advantage comes from the planned campaigns and holidays by refitting it without them. I also built 80% prediction ranges from the validation errors and checked them on the test weeks. Finally, I refitted the selected model on all 156 weeks and forecast the next 26 weeks (September 28, 2026 to March 22, 2027) with the campaign load of the last year assumed, adding a level correction (the ratio of the actual to the fitted demand over the last 13 weeks), which a backtest at five starting weeks showed to cost half a point of error on average when nothing has changed, and I saved the forecasts with and without the correction. All the results are in `datasets/veda_demand/forecasts/` (the validation scores, the forecasts and scores for the test weeks, and the forecast of the next 26 weeks).

## Outcome
By the end of this task, I had a forecasting model selected on a validation period and tested on weeks it had never seen. The Poisson regression was the best model: its WAPE on the weekly total of the four lines was 7.2%, against 10.3% for the best baseline of Day 46, 10.4% for the random forest, 11.9% for Holt-Winters, and 12.5% for the 13-week average, with almost no bias (-0.3%). By line, its error was 10.5% for Internship Programs, 19.0% for Training Programs, 23.3% for IT Services, and 20.7% for Digital Services; the regression is off by 14.5% to 20.9% even on the weeks it was fitted on, so the errors of the lines are close to the randomness of the data. Most of the regression's advantage comes from knowing the plan: without the campaign days and holidays, its error on the test total rises from 7.2% to 9.5%, and the advantage was concentrated before June (4.8% against 13.9% to 17.2% for the other methods), because spring 2026 had about half the campaign days of spring 2025 in two lines. From June 1, when Digital Services lifted and IT Services slowed down, all methods were within 8.1% to 9.7% on the total, and every method under-forecast Digital Services; the 80% ranges contained 76.9% of the test line-weeks, but only 52.9% of the Digital Services weeks after June 1. The forecast for the next 26 weeks has 1,410 units for Internship Programs, 979 for Training Programs, 465 for IT Services, and 778 for Digital Services (+5%, +11%, -7%, and +45% against the same weeks a year earlier), with the busiest weeks in January and February and the quietest in December. Because the data is simulated, these results show that the methods work and where they break; they do not describe the real company. The main lesson was that a forecast is only as good as the information given to it: the plan of the weeks to forecast helped more than a more flexible model, and no model could foresee a change that is not in its history.

## Interview Questions
1. **How do you choose between a statistical model and a machine-learning model for forecasting?**
   Compare them on the same weeks, with the choices made on a validation period and a single look at the test. Here, the Poisson regression (7.2% error on the weekly total) beat the random forest (10.4%) and Holt-Winters (11.9%), because the data is small (130 weeks per line, about two and a half yearly cycles) and has a simple structure (a trend, a yearly pattern, campaigns, and holidays), which a model with a few parameters can learn but a forest with many examples of the same weeks can overfit. The forest needs care: it cannot extrapolate a trend, so I made its target relative to the recent level, and one model forecasts every horizon. The forest was still better for one line (Training Programs, 18.3% against 19.0%), so no model wins everywhere. With more data, more lines, or more drivers, the answer can change, and the simple model and its baselines remain the benchmark.
2. **How do you evaluate a forecast honestly?**
   Keep the order of time (train, validate, test), choose settings on the validation and look at the test once, and compare with a simple baseline. Then ask what the model knew that the others did not: the regression knows the campaign plan, and without it its error on the test total rises from 7.2% to 9.5%, so the lead is mostly information and not a cleverer method. Compare the error with the randomness of the data: the regression is off by 14.5% to 20.9% even on the weeks it was fitted on, so 10.5% for Internship Programs is probably partly luck and 19% to 23% for the other lines is close to what is possible. Report the error per line and by period, because the weekly total hides compensating errors, and the advantage of a model can sit in one period (here, before June).
3. **What does a prediction range tell you, and what does it not tell you?**
   A range built from past errors (here, the 10th and 90th percentile of the ratio actual over forecast on the validation weeks) describes ordinary randomness, and it worked as intended in normal weeks: 76.9% of the test line-weeks fell inside an 80% range. It does not cover a change in the pattern: after June 1 only 52.9% of the Digital Services weeks were inside, because demand moved above the whole range. A range also depends on the assumptions behind it, such as the campaign plan, so a planner should read it as the uncertainty if the pattern holds, and should watch the recent weeks against the forecast to notice when it stops holding (which is what the level correction does in a simple way).
