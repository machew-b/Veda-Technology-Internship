# Day 40: Customer Segmentation & Service Recommendation System

## Description
Develop a customer analytics system that groups customers based on behavior, interests, engagement, service inquiries, spending, or interaction patterns and recommends suitable Veda Technology services or learning programs.

## Objective
Learn unsupervised learning, customer segmentation, feature engineering, clustering evaluation, and recommendation logic.

## Tools
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- K-Means
- PCA
- Jupyter Notebook
- Streamlit

## Deliverables
- Customer dataset
- Data preprocessing pipeline
- Customer behavior analysis

## Hints / Mini Guide
- Use synthetic or public customer data.
- Possible segments can include highly engaged customers, occasional users, new customers, and service-focused customers.
- Standardize numerical features before clustering.
- Use the elbow method or silhouette score to evaluate clusters.
- Create meaningful names for the resulting customer segments.
- Recommendations can be rule-based rather than requiring a complex recommendation algorithm.

## Approach
Since the project asks for synthetic or public data, I generated a synthetic customer dataset of 5,000 customers and 16 columns (sign-up date, customer type, region, acquisition channel, primary interest, website visits, session length, pages per visit, email open rate, days since last activity, service inquiries, support tickets, purchases, total spend, and a satisfaction rating) with a fixed random seed. Each customer is generated from one of four hidden behavior patterns (highly engaged learners, occasional visitors, new customers, and service-focused business clients), which is not saved in the data, so the segmentation on Day 41 has to find the groups from behavior alone. I then made the table deliberately messy (duplicate rows, missing values, two date formats, inconsistent labels like `SMB` and `Google Ads`, spending typed as text like `₹12,500`, impossible numbers such as negative session lengths, and contradictory values such as spending without purchases) and saved it as `datasets/veda_customers/raw/customers_raw.csv`. For the data preprocessing pipeline, I wrote one function, `clean_customers()`, driven by a short specification, that removes duplicates, parses both date formats, converts numbers typed as text, standardizes labels, sets impossible numbers to missing, applies logic rules (a customer cannot be inactive for longer than they have been a customer, and no purchases means no spending), fills gaps with the median of the customer type (or `Unknown` for labels), and converts whole-number columns back to integers. It turned 5,100 raw rows into 5,000 clean rows, removing 100 duplicates, converting 56 text numbers, standardizing 2,305 labels, and handling 114 impossible numbers and 25 contradictory values. The satisfaction survey gaps were left on purpose, because the gap itself means the customer did not answer. I checked the result with validation checks and by comparing the cleaned table with the original clean one, which only a simulation allows, and saved it as `datasets/veda_customers/cleaned/customers_cleaned.csv`. For the customer behavior analysis, I calculated key figures (active, inactive, and buying customers, spending, and survey response), looked at who the customers are by type, channel, region, interest, and sign-up month, and compared engagement (visits, session length, email opens, and days since last activity) and spending by customer type, channel, and interest. Because spending is very skewed, I used medians, a logarithmic axis, and a concentration curve, and I used the Spearman correlation for the relationships. I also looked at inquiries, support tickets, and satisfaction, and at scatter plots to see whether natural groups appear before any clustering, and I repeated the spending summary by customer type in SQL with `sqlite3` to confirm it matches pandas.

## Outcome
By the end of this task, I had a reproducible simulated customer dataset, a preprocessing pipeline that recovered every original customer, and the behavior analysis that prepares Day 41. The 5,000 customers produced INR 206.3 million in total spending, 60% of customers had bought, and 69% were active in the last 30 days. The typical customer engages lightly (a median of 6 website visits and a 30% email open rate). Students are the most engaged type, business customers ask the most service inquiries, and customers who came through Email or Referral engage and buy the most. Spending is extremely concentrated: the top 10% of customers hold 74% of it, business customers and IT and Digital Services interests account for about 79% of it, and the median customer spent INR 5,900 against an average of INR 41,254. The engagement measures move together, but no pair of measures separates the customers into clear groups, so the segmentation needs several standardized measures (with spending log-transformed) at once. Because the data is simulated, these findings reflect the assumptions I built into it, so they practice the analysis workflow and do not describe the real customers of Veda Technology. The main lesson was that averages mislead with customer data: the average customer spent about seven times the median, so the segmentation has to deal with the skew and cannot rely on any single measure.

## Interview Questions
1. **Why is customer spending data usually skewed, and how do you handle it?**
   A few customers, such as large business clients, spend far more than most, so the distribution has a long right tail and the average is pulled up by them. Here, the average customer spent INR 41,254, but the median customer spent INR 5,900, and the top 10% of customers held 74% of all spending. For describing the data, medians, percentiles, and concentration curves are more honest than the mean. For methods based on distances, such as K-Means, a log transform reduces the pull of the biggest spenders so they do not dominate the clusters.
2. **How do you clean numbers that are impossible or contradict each other?**
   First define what is valid for each column (for example, an email open rate must be between 0 and 100) and set the values outside that range to missing instead of keeping them. Then check rules that involve more than one column, such as "a customer cannot have been inactive for longer than they have been a customer" and "a customer with no purchases cannot have spent money". The flagged values are then handled like any other gap (here, filled with the median of the customer type, or with zero spending for customers without purchases), and the counts are logged so the cleaning can be checked. Gaps that carry meaning, such as customers who did not answer a survey, are left unfilled.
3. **Why look at customer behavior before running a clustering algorithm?**
   Exploration shows what the data looks like and what has to be fixed first: which measures are skewed, whether they are on very different scales, which ones carry almost the same information (purchases and total spend have a 0.94 correlation, so using both would count the same thing twice), and whether any groups are visible at all. Here, no pair of measures showed clear separate groups, which means K-Means has to use several measures together, and they need to be standardized first. Clustering without this step risks groups that only reflect the scale or skew of one column.