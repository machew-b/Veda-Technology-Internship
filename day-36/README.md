# Day 36: Veda Technology Business & Service Analytics

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
- Training program performance analysis
- IT service inquiry analysis
- Digital service inquiry analysis
- Customer/service request analysis

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
I continued from the cleaned tables saved on Day 35 in `datasets/veda_business/cleaned/`, loading `training_enrollments`, `it_service_inquiries`, `digital_service_inquiries`, and `service_requests` with `parse_dates`. A few gaps were left in those tables on purpose (survey non-responses and the resolution time of requests that are still open), so I excluded open requests from every resolution-time figure instead of filling them. For the training program performance analysis, I calculated KPIs (enrollments, fee revenue, completion rate, attendance, final score, satisfaction), compared the six programs on enrollments, revenue share, completion, and satisfaction, and then looked at delivery mode, lead source, completion rate by attendance band, the attendance-score and score-satisfaction correlations, and enrollments by month. For the IT and digital service inquiry analyses, I wrote shared helper functions (`prepare_inquiries()`, `inquiry_kpis()`, `inquiry_summary()`, and `plot_inquiries()`) so that both tables are analyzed in exactly the same way: an inquiry counts as converted when its status is `Converted`, and the response time is grouped into three bands (within 4 hours, 4 to 24 hours, over 24 hours) with `pd.cut()` to test whether speed affects conversion. I then compared conversion, average budget, and deal value by service, client type, and channel, and put the IT and digital KPIs side by side. For the customer and service request analysis, I calculated the resolved, escalated, and open shares, compared the service areas and request types, and checked resolution time and satisfaction by priority and status. I also added a service-level check with assumed targets (Critical within 8 hours, High within 24, Medium within 48, Low within 72), since the data has no official targets, and I repeated the resolution time by priority in SQL with `sqlite3` to confirm it matches pandas. Monthly volume and escalation charts finish the analysis.

## Outcome
By the end of this task, I had analyzed four more business areas of the project with the same workflow. The 1,800 training enrollments brought in INR 24.1 million, led by Full Stack Web Development (29.2% of revenue). The completion rate was 65.8% and was similar across programs, but higher for offline students (72.9% versus 63.7% online), and no student with under 60% attendance completed. IT and digital inquiries converted at 45.7% and 43.1%, in both cases faster responses converted better and Referral was the best channel, and IT deals were worth about 5.8 times the total value of digital deals, with Enterprise clients giving 39% of IT deal value from 13% of the inquiries. Of the 3,200 service requests, 84.6% were resolved, escalated requests left customers far less satisfied (2.83 versus 4.02), Billing Queries were the slowest to resolve, and Critical requests had the lowest compliance with the assumed targets (91.8%). Because the data is simulated, these findings reflect the assumptions I built into it, so they practice the analysis workflow and do not describe the real company. The main lesson was that volume alone can mislead: the busiest channel, service, or client group is often not the one that converts best or brings in the most money.

## Interview Questions
1. **Why look at deal value and conversion rate, and not only the number of inquiries?**
   The number of inquiries only shows interest, not business results. A group can send many inquiries and bring in little money, or send few and bring in a lot, e.g., Enterprise clients sent only 13% of the IT inquiries but accounted for 39% of the deal value, while Individuals sent 13% of the inquiries and only 1% of the value. Conversion rate shows how well inquiries turn into deals, and deal value shows how much each deal is worth, so both are needed to decide where to spend effort.
2. **What is a service-level target (SLA), and how would you monitor it?**
   A service-level target is a promised standard for a service, such as resolving a critical request within a set number of hours. To monitor it, you compare each request's actual resolution time with the target for its priority and track the share that meets it, overall and by priority, month, or team. In this analysis, Critical requests had the lowest compliance (91.8%) even though they were resolved fastest, because their target was tight compared to their typical resolution time, which shows why the percentage meeting the target matters more than the average time.
3. **Why should you be careful when comparing groups with small sample sizes?**
   The rate of a small group can swing a lot from chance alone, so a large gap may not be real. For example, only 51 IT inquiries waited more than 24 hours, so their 25.5% conversion rate is much less reliable than the rate for the 1049 faster ones. The usual response is to check how many records are behind each figure, avoid over-reading small differences, and use larger samples or statistical tests before drawing conclusions.