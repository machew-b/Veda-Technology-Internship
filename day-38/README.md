# Day 38: Veda Technology Business & Service Analytics

## Description
Build a complete data science analytics solution for Veda Technology by analyzing simulated business data related to website visitors, internship applications, training programs, IT services, digital services, inquiries, customer/service requests, marketing channels, and business performance.

## Objective
Give interns practical exposure to how data science can support a growing technology and service organization through business intelligence, customer analysis, service analytics, marketing analysis, forecasting, and data-driven decision making.

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Excel
- Power BI
- SQL
- Git/GitHub

## Deliverables
- Predictive analysis
- Business recommendations
- Executive-level analytics report

## Hints / Mini Guide
- Do not use private or confidential Veda Technology data.
- Create a realistic synthetic dataset representing Veda Technology's business operations.
- Include multiple business areas such as internships, training, website traffic and IT/digital services.
- Analyze which services generate the highest demand.
- Analyze where website visitors and inquiries originate.
- Identify patterns in customer or student inquiries.
- Use segmentation to group customers or service inquiries.
- Create KPIs such as applications, inquiries, conversion rate, service demand and engagement.
- Use Power BI for the final business dashboard.
- The project should demonstrate how data science can help Veda Technology make business and service decisions.

## Approach
I continued from the cleaned tables saved on Day 35 and did two predictive analyses. For the demand forecast, I built the daily website visits series and ran a backtest, training on October to June and testing on the last 92 days (July to September), with two models: a weekday average of the last 28 training days and a `LinearRegression` on the day number and weekday dummies. Because one year of data cannot teach a model the yearly seasonal pattern, I then made a planning forecast for October to December 2026 as a seasonal naive forecast (the same months of last year) with three growth scenarios of 0%, 10%, and 20%. For the inquiry conversion model, I combined the IT and digital inquiries, trained only on inquiries with an outcome (`Converted` or `Lost`, since inquiries still in progress have no outcome yet), and used a stratified 80/20 split. The predictors were the service line, service type, client type, channel, the budget, and the response time (as a number and as flags for replies within 4 hours and after more than 24 hours), with the status and deal value deliberately excluded to avoid leakage. I compared a `LogisticRegression` and a `RandomForestClassifier` inside `ColumnTransformer` pipelines with a baseline and with a model that only knows the reply speed, used repeated 5-fold cross-validation because a single test set this size is noisy, and checked how well the model ranks inquiries with a lift table by predicted-probability group. I also scored the 604 inquiries still in progress. For the business recommendations, I turned the findings of the four days into eight recommendations, each with evidence, an action, and an illustrative impact calculated from the data (for example, a marketing budget shift, a 4-hour reply target, and a mobile conversion gap), and saved them as `business_recommendations.csv`. For the executive-level analytics report, I wrote `executive_report.md` and a PDF version, `executive_report.pdf`, with a summary, KPIs, key insights, the outlook, the recommendations, limitations, next steps, and the project documentation (repository structure and how to reproduce the results).

## Outcome
By the end of this task, I had finished the project with a forecast, a tested prediction model, recommendations, and an executive report. The demand backtest showed that a trend and weekday model captures the weekly pattern (14% average daily error) but misses the July and August peak, so the Q4 2026 plan is a range of 1,602 to 1,922 applications, enrollments, and inquiries. The conversion model turned out to be weak (ROC AUC 0.57, cross-validated mean 0.58), no better than a model that only knows whether the reply was fast, and its lift table was irregular, so I concluded that it cannot rank individual inquiries, and that the useful finding is that conversion depends on reply speed and channel and not on the client or the service. The three high-priority recommendations are rebalancing the marketing budget (about 3,540 more leads a year in the scenario), answering inquiries within 4 hours (about 234 more deals), and improving the mobile experience (about 236 more conversions), all upper-end scenarios that should be tested before they are scaled. Because the data is simulated, these findings reflect the assumptions I built into it and practice the analysis workflow, but they do not describe the real company. The main lesson was that an honest negative result is still a result: reporting that the model was weak, and why, was more useful than presenting a model that only looked good.

## Interview Questions
1. **How do you decide whether a predictive model is actually useful?**
   Compare it with a simple baseline, check it on data it was not trained on, and judge it with measures that fit the use. A model that beats the baseline by a hair is not useful even if it looks fine on its own. Here, the lead-scoring model had 59.7% accuracy against 59.2% for always predicting the majority outcome and a ROC AUC of only 0.57, and its lift table did not rise steadily from the lowest to the highest group, so it could not be trusted to rank inquiries. Cross-validation is also important, because a single small test set can give a lucky or unlucky score.
2. **Why is it hard to forecast seasonal demand with only one year of data?**
   A model can only learn a seasonal pattern from several repeats of it. With one year, each month has been seen only once, so growth and seasonality cannot be told apart, and a peak such as July looks like noise before it happens. In the backtest, a model trained on October to June underestimated July and August by about 14%. With so little history, a seasonal naive forecast with growth scenarios is more honest than a fitted model.
3. **How do you turn an analysis into recommendations that a manager can act on?**
   Each recommendation should state the evidence, a specific action, and an estimated impact, and it should be ranked by priority. The impact should be labeled as a scenario with its assumptions, and a test should be suggested before the change is scaled, since a pattern in the data is not proof that changing it will cause the same result. For example, moving 15% of the Paid Ads and Social Media budget to Referral and Email could add about 3,540 leads in the scenario, but it assumes the new channels keep half of their current efficiency, so it should be tried on a small budget first.