# Day 35: Veda Technology Business & Service Analytics

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
- Simulated Veda Technology business dataset
- Data cleaning and preprocessing pipeline
- Website visitor analysis
- Internship application analysis

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
Since the project forbids private data, I generated a synthetic dataset of seven tables for one year (October 2025 to September 2026) with a fixed random seed: `website_visits` (24,000 visits), `internship_applications` (2,600), `training_enrollments`, `it_service_inquiries`, `digital_service_inquiries`, `service_requests`, and `marketing_campaigns`. The tables follow simple rules I chose (a growth trend, busier weekdays, seasonal peaks, and relationships such as bounce depending on channel and device, or selection depending on the assessment score). I then made each table deliberately messy (duplicate rows, missing values, two date formats, inconsistent labels like `FB` and `Google Ads`, and impossible numbers such as negative session durations) and saved them as raw CSV files in `datasets/veda_business/raw/`. For the data cleaning and preprocessing pipeline, I wrote one function, `clean_table()`, driven by a short specification for each table, that removes duplicates, parses both date formats, standardizes labels, sets impossible numbers to missing, fills gaps with group medians (or `Unknown` for labels), and converts whole-number columns back to integers. It turned 34,269 raw rows into 34,060 clean rows, removing 209 duplicates, standardizing 5,041 labels, and handling 195 impossible numbers. Two gaps were left on purpose, survey non-responses and the resolution time of requests that are still open, because the gap itself carries meaning. I checked the result with validation checks and by comparing the cleaned tables against the original clean ones, which only a simulation allows. For the website visitor analysis, I calculated KPIs (visits, bounce rate, pages per visit, session duration, conversion rate) and broke traffic down by month, weekday, channel, device, landing page, region, and conversion type. For the internship application analysis, I looked at applications by month and domain, selection rates by college tier, education level, and program length, the link between assessment score and outcome, and the selection and enrollment rate of each application source, and I repeated the domain analysis in SQL with `sqlite3` to confirm it matches pandas. The cleaned tables are saved in `datasets/veda_business/cleaned/` for the next days of the project.

## Outcome
By the end of this task, I had a reproducible simulated business dataset, a reusable cleaning pipeline that recovered every original record, and the first two analyses of the project. The website received 24,000 visits with a 47.7% bounce rate and a 3.64% conversion rate. Email (8.38%) and Referral (6.35%) converted best, while Social Media (1.71%) and Paid Ads (2.05%) converted worst even though Social Media supplied 24% of the traffic. Mobile visitors, who make up 63% of visits, convert at less than half the desktop rate. For internships, 36.1% of the 2,600 applicants were selected, selection followed the assessment score and the college tier (Tier 1 at 50% versus Tier 3 at 31%), and Referral and Campus Outreach applicants enrolled most often (95% and 92% of those selected). Because the data is simulated, these findings reflect the assumptions I built into it, so they practice the analysis workflow and do not describe the real company. The main lesson was how much of the work is making messy data trustworthy before any analysis, and how a specification-driven pipeline handles seven tables with one function.

## Interview Questions
1. **Why use a synthetic dataset, and what are its limits?**
   A synthetic dataset lets you practice the full workflow when real data is private, unavailable, or too sensitive to share, and it lets you control the data so you can check your methods against the known truth. Its limit is that it only contains the patterns that were put into it, i.e., any finding mostly reflects the assumptions of whoever built the simulation. It can show whether an analysis works, but it cannot show what is true about real customers.
2. **What is the difference between bounce rate and conversion rate, and how do you read them together?**
   Bounce rate is the share of visits where the visitor leaves after viewing one page, and conversion rate is the share of visits that end in a desired action, such as an application or an inquiry. Read together, they show channel quality: Social Media brought lots of traffic but had the highest bounce rate and the lowest conversion rate, while Email brought little traffic with the lowest bounce rate and the highest conversion rate. Traffic volume alone would have pointed to the wrong channel.
3. **How do you decide whether to drop, fill, or keep missing values?**
   It depends on why the value is missing and how much it matters. Duplicates and rows with an unreadable key (like a date) can be dropped, a number that is missing at random can be filled with a sensible estimate such as the median of a related group, and a missing label can be marked `Unknown` so it is not mistaken for a real category. Some gaps should be kept, such as a customer who did not answer a survey or a request that is still open, because filling them would invent information.