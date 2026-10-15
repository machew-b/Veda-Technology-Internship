# Day 37: Veda Technology Business & Service Analytics

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
- Marketing-channel performance analysis
- Customer segmentation
- Service demand analysis
- Business KPI dashboard

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
I continued from the seven cleaned tables saved on Day 35. For the marketing-channel performance analysis, I calculated the click-through rate, cost per click, lead rate, and cost per lead for each of the five channels with a marketing cost, compared each channel's share of spend with its share of leads, looked at monthly spend, leads, and cost per lead, and linked the spend to the website by calculating the cost per website visit and per website conversion. For the customer segmentation, I used two approaches. First, I clustered website visitors with `KMeans` on the pages viewed and the log of the session duration (both standardized with `StandardScaler`), compared silhouette scores for 2 to 6 segments on a sample of 5,000 visits, and chose 3 segments even though 2 scored highest, because the 2-segment solution agreed with the existing `bounced` flag for 99.3% of visits and added nothing new. I named the segments Quick leavers, Focused readers, and Deep explorers from their profiles. Second, I split the IT and digital inquiries into Small, Medium, and Large budget bands with `pd.cut()` and compared their conversion rate, response time, and deal value. For the service demand analysis, I combined internship applications, training enrollments, and IT and digital inquiries into monthly demand by business line and a demand index, ranked every individual service by demand and by value, and compared the channels that each line's demand comes from. For the business KPI dashboard, I built a scorecard of 26 KPIs across six business areas, a static dashboard in Matplotlib (saved as `business_kpi_dashboard.png`), and six tables for Power BI (a date table, a channel table, a monthly summary, a channel performance table, the service demand table, and the KPI scorecard), with a consistency check that the exported totals match the cleaned tables. Because a Power BI file has to be built in Power BI Desktop, I wrote `power_bi_dashboard_guide.md` with the import steps, relationships, DAX measures, page layout, and the expected values to check the result against.

## Outcome
By the end of this task, I had analyzed marketing, segmented customers in two ways, measured service demand, and prepared the business dashboard. Paid Ads and Social Media use 76% of the marketing budget for only 38% of the leads, while Referral and Email deliver 29% and 19% of the leads from 7% and 5% of the spend, at about INR 19 to 20 per lead. 48% of website visits are Quick leavers who produce 0.7% of conversions, and Large inquiries are only 12% of the inquiries but 52% of the deal value. Internships and training dominate demand by volume, but the five most valuable services are all IT services, and each business line draws on a different mix of channels. The dashboard tables reconcile exactly with the cleaned data. Because the data is simulated, these findings reflect the assumptions I built into it, so they practice the analysis workflow and do not describe the real company. The main lesson was that no single measure tells the whole story: volume, conversion, cost, and value pointed to different channels and services, so a dashboard has to show them together.

## Interview Questions
1. **What do click-through rate, lead rate, and cost per lead each tell you about a marketing channel?**
   The click-through rate is the share of impressions that become clicks, so it shows how attractive the ad or message is. The lead rate is the share of clicks that become leads, so it shows how well the landing experience turns interest into contact details. The cost per lead combines the cost and the results into one figure for comparing channels. Looking at all three matters: Social Media had the lowest click-through rate (1.47%) and lead rate (3.48%), so its cost per lead was the highest (INR 168), while Referral was strong on both and cost only INR 19 per lead.
2. **What is k-means clustering, and how do you choose the number of clusters?**
   K-means groups records into a chosen number of clusters by assigning each record to the nearest cluster center and moving the centers until the groups stop changing, so features should be standardized first. The number of clusters can be guided by the silhouette score (how well separated the clusters are), but it should also make business sense. Here, 2 clusters scored highest but only recreated the bounce flag, so 3 were used to split the engaged visitors into two useful groups, which shows that the score informs the decision and does not make it.
3. **Why does a Power BI model need a date table and relationships?**
   A date table gives every table the same calendar to filter by, so one month or quarter slicer can control the visitors, applications, enrollments, inquiries, and requests together. Relationships (a date table linked to each table's date column, and a channel table linked to every table that has a channel) let a single slicer or chart combine measures from different tables correctly. Without them, each table would have to be filtered separately, and measures from different tables could not be shown on the same axis.