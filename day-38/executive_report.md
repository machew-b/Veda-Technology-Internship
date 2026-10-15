# Veda Technology Business & Service Analytics: Executive Report

**Project:** a four-day analytics project (Days 35 to 38) of the Veda Technology Internship, Data Science track  
**Period analyzed:** October 1, 2025 to September 30, 2026  
**Data:** simulated (synthetic) Veda Technology business data, generated with a fixed random seed

## 1. Summary

Veda Technology's simulated business generated 24,000 website visits, 2,600 internship applications, 1,800 training enrollments, 2,400 IT and digital service inquiries, and 3,200 service requests between October 2025 and September 2026. Revenue is highly concentrated: IT services bring in about 78% of the INR 265 million in fees and deal value, although internships and training account for most of the demand by volume. The biggest opportunities are in marketing efficiency (Paid Ads and Social Media take 76% of the budget for 38% of the leads), reply speed (inquiries answered within 4 hours convert far more often), and the mobile website experience (mobile converts at under half the desktop rate). All figures come from a simulated dataset, so they demonstrate the analysis and are not findings about the real company.

## 2. The Business at a Glance

| Measure | Value |
|---|---|
| Website visits | 24,000 |
| Website conversion rate | 3.64% |
| Internship applications | 2,600 |
| Internship selection rate | 36.1% |
| Training enrollments | 1,800 |
| Training fee revenue | INR 24.1 million |
| Training completion rate | 65.8% |
| IT inquiries / conversion rate | 1,100 / 45.7% |
| IT deal value | INR 205.7 million |
| Digital inquiries / conversion rate | 1,300 / 43.1% |
| Digital deal value | INR 35.6 million |
| Service requests resolved | 84.6% of 3,200 |
| Marketing spend / leads | INR 1.60 million / 20,245 |
| Marketing cost per lead | INR 79 |

## 3. Key Insights

1. **Revenue comes from IT services, demand comes from internships and training.** IT deals total INR 205.7 million, against INR 35.6 million for digital deals and INR 24.1 million for training fees. Large inquiries (over INR 500K) are 12% of inquiries but 52% of deal value. Internship applications are 38% of all demand, and the five most valuable services are all IT services.
2. **Marketing money is not going where the leads are.** Paid Ads and Social Media use 76% of the budget for 38% of the leads (about INR 156 per lead), while Referral and Email use 12% of the budget for 47% of the leads (about INR 19 per lead).
3. **Half of website visitors leave after one page, and mobile is the weak spot.** The bounce rate is 47.7% and the conversion rate 3.64%. Mobile is 63% of traffic but converts at 2.68%, against 5.66% on desktop. By channel, Email converts best (8.4%) and Social Media worst (1.7%).
4. **Reply speed is the clearest lever on service inquiries.** Inquiries answered within 4 hours convert at 57% (IT) and 51% (digital), against 42% and 40% for replies in 4 to 24 hours, yet 70% and 67% of inquiries wait longer than 4 hours. Referral is the best channel for both.
5. **Training and internship outcomes depend on attendance, delivery, and source.** Training completion is 65.8%, no student below 60% attendance completed, and offline students complete 9 points more often than online students. Internship selection is 36.1% and follows the assessment score and college tier (Tier 1 at 50% versus Tier 3 at 31%), and Referral and Campus Outreach applicants enroll most often (95% and 92% of those selected).
6. **Customer service is solid, but escalations and Critical requests need attention.** 84.6% of requests are resolved, but escalated requests score 2.83 in satisfaction versus 4.02 for resolved ones, Billing Queries take 27 hours to resolve (others: 22), and only 92% of Critical requests meet an assumed 8-hour target.

## 4. Outlook and Predictive Findings

Demand is seasonal, with internships peaking in January, IT inquiries in March, and training and digital inquiries in July. With one year of history, a fitted forecast cannot learn the seasonal pattern: a trend and weekday model had a 14% average daily error on website visits and underestimated the July and August peak by about 14%. For planning, Q4 2026 demand is therefore given as a range of 1,602 to 1,922 applications, enrollments, and inquiries (last year: 1,602, with growth scenarios of 0%, 10%, and 20%). A model that predicts which service inquiries convert was also tested and found weak (ROC AUC 0.57, where 0.5 is random guessing): conversion depends on reply speed and channel, not on the client or the service, so simple rules work as well as a model.

## 5. Recommendations

Impacts are illustrative upper-end scenarios from simulated data and should be tested before they are scaled.

| Priority | Area | Recommendation | Illustrative impact |
|---|---|---|---|
| High | Marketing | Move part of the Paid Ads and Social Media budget to Referral (a referral program) and Email, and track results by channel. | Moving 15% of that spend (INR 182K) could add about 3,540 leads a year (+17%), even if the new channels keep only 50% of their current efficiency. |
| High | Sales and service | Set a 4-hour first-response target and alert the team on new inquiries, then prioritize by budget, channel (Referral first), and reply speed. The lead-scoring model is not yet reliable enough to rank individual inquiries. | If slower replies converted at the 4-hour rate, that would mean about 234 more deals (+22%) and roughly INR 59 million in deal value. |
| High | Website | Review the mobile experience of the application and inquiry forms (speed, form length, button placement) and test changes. | Reaching 75% of the desktop rate on mobile would add about 236 conversions a year (+27%). |
| Medium | Sales | Give Large inquiries a dedicated fast track and a senior contact, and promote Cybersecurity to Enterprise and SME clients. | Each +5 points of conversion on Large inquiries is worth about INR 14.0 million. |
| Medium | Training | Flag students whose attendance drops toward 60% and contact them early, and offer more offline or hybrid cohorts for the biggest programs. | Recovering half of the 150 low-attendance students would add about 46 completions (+4%). |
| Medium | Customer service | Create a faster billing process, find why requests escalate, and add alerts for Critical requests approaching the target. | Fewer escalations would lift satisfaction directly, since escalated requests score more than a full point lower. |
| Medium | Operations | Plan staffing, trainers, and campaigns around each line's peak, and use the Q4 2026 scenarios for capacity planning. | A planning range of 1,602 to 1,922 applications, enrollments, and inquiries for Q4 2026. |
| Foundation | Data | Replace the simulated data with real tracking (channel attribution, response times, attendance), run A/B tests before large changes, and re-fit the models quarterly. | Turns these scenarios into measured results. |

## 6. Risks and Limitations

- All data is simulated, so every relationship reflects assumptions built into the simulation and not the behavior of real customers.
- One year of history cannot separate growth from seasonality, and the demand forecast is a planning range, not a prediction.
- The impact figures in the recommendations are upper-end scenarios that assume the relationships are causal and keep working at a larger scale. They should be tested before they are scaled.
- Some thresholds are assumptions: the service-level targets for requests, the budget bands, and the 4-hour reply target.
- The lead-scoring model is weak (ROC AUC about 0.57) and should not be used to rank individual inquiries.

## 7. Next Steps

1. Replace the simulated data with real tracking: channel attribution, response times, attendance, and spend by campaign.
2. Test the three high-priority recommendations with controlled changes (a 4-hour reply target, a budget shift, and a mobile form redesign) and measure the results.
3. Build the Power BI dashboard from the prepared tables and review it monthly.
4. Re-fit the demand forecast once a second year of data is available, and re-test the conversion model on real inquiries.

## 8. Project Documentation

**Repository:** `Veda-Technology-Internship`

```
Veda-Technology-Internship/
├── datasets/veda_business/
│   ├── raw/        # 7 messy tables created on Day 35
│   ├── cleaned/    # 7 cleaned tables (input for Days 36 to 38)
│   └── powerbi/    # 6 tables for the Power BI dashboard (Day 37)
├── day-35/   # simulated dataset, cleaning pipeline, website and internship analyses
├── day-36/   # training, IT inquiry, digital inquiry, and service request analyses
├── day-37/   # marketing, segmentation, service demand, KPI dashboard
└── day-38/   # predictive analysis, recommendations, this report
```

Each day folder contains a `README.md` and a notebook named `veda_technology_business_and_service_analytics.ipynb`.

**How to reproduce:**

1. Install Python 3 with `pandas`, `numpy`, `matplotlib`, `scikit-learn`, and `jupyter` (`sqlite3` is part of Python).
2. Run the notebooks in order: `day-35`, `day-36`, `day-37`, `day-38`. Day 35 generates and cleans the data, and the later days read the cleaned tables from `datasets/veda_business/cleaned/`.
3. The simulation uses a fixed random seed (`42`), so the data and the results are reproducible.
4. The Power BI dashboard is built in Power BI Desktop from the Day 37 tables, following `day-37/power_bi_dashboard_guide.md`.
