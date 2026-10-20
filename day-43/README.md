# Day 43: Customer Segmentation & Service Recommendation System

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
- Customer segment dashboard
- Business recommendations
- Final report

## Hints / Mini Guide
- Use synthetic or public customer data.
- Possible segments can include highly engaged customers, occasional users, new customers, and service-focused customers.
- Standardize numerical features before clustering.
- Use the elbow method or silhouette score to evaluate clusters.
- Create meaningful names for the resulting customer segments.
- Recommendations can be rule-based rather than requiring a complex recommendation algorithm.

## Approach
I continued from the segmented customers and recommendations saved on Day 42 in `datasets/veda_customers/segments/`. For the customer segment dashboard, I built it in two forms. The static one is a picture, `customer_segment_dashboard.png`, with six headline numbers, the 2D customer map, the share of customers against the share of spending, a heatmap of what each segment looks like (in standard deviations from the average), the recommended offer family of each segment, and the campaign workload (customers per action). Each segment keeps the same color and marker shape in every panel, so color is never the only cue, the heatmaps use one blue hue for amounts and a blue-red scale with a gray middle for values above or below average, and the palette was checked for color-blind safety with a validator. The interactive one is a Streamlit app, `app.py`, with filters (segment, customer type, and acquisition channel), key numbers that update with the filters, and five tabs (overview, segment map, segment profiles, recommendations, and about), a customer lookup by ID, and a CSV download of the filtered recommendations. I tested the app by simulating the filters and the lookup with `streamlit.testing`, by starting it in a browser, and by checking that its numbers match the notebook. For the business recommendations, I calculated the evidence from the saved tables (for example, the spending held by Service-Focused Clients with many tickets or a low rating, the customers who have not bought yet, and the buying rate by acquisition channel), wrote a scenario with a stated assumption for each recommendation (such as 10% of the New Customers who have not bought making a first purchase at the median spending), ranked them by the value at stake and the strength of the evidence, and saved them as `business_recommendations.csv` with the evidence, the action, and the estimated impact. For the final report, I wrote `final_report.md` with a summary, the method, the four segments, the recommendation logic, the business recommendations, the limitations, next steps, and the project documentation (repository structure and how to reproduce and run the dashboard). I re-ran the notebook from a clean copy to confirm that the saved recommendations are identical, and recalculated the cited figures independently from the saved tables.

## Outcome
By the end of this task, the project was complete: an interactive dashboard, a static dashboard picture, eight business recommendations, and a final report. The dashboard shows that the 5,000 simulated customers fall into four segments of very different value. The 871 Service-Focused Clients (17% of the customers) hold 72.7% of the INR 206.3 million in spending, and 343 of them, who hold INR 63.2 million (30.6% of all spending), have 3 or more support tickets or a rating of 2 or less, so service recovery for them is the first priority (losing 10% of that spending would cost about INR 6.3 million). The other high-priority actions are a learning path for the 1,517 Engaged Learners (about INR 1.4 million if 10% bought one more program) and a referral invitation to the 887 who rated Veda Technology 4 or 5 (about INR 0.8 million if 5% brought one customer). The medium-priority actions are a welcome series for the 738 New Customers who have not bought, a low-cost re-engagement email for the Occasional Visitors, a shift of marketing budget toward Referral and Email, and better survey and offer tracking. The impact figures are scenarios with stated assumptions and not forecasts. Because the data is simulated, the segments overlap (average silhouette 0.29), and the recommendations have never been tested on real customers, the first next step is a controlled campaign, such as sending the recommended offer to half of a segment and comparing the responses. The main lesson was that a segmentation is only useful when it ends in actions: the segments became lists of customers per campaign, and the honest limits had to travel with them.

## Interview Questions
1. **How do you turn a customer segmentation into business recommendations?**
   Each segment needs a profile (size, value, behavior, and needs) and then a concrete action with the evidence behind it and an estimated impact. Here, the Service-Focused Clients are only 17% of the customers but hold 72.7% of the spending, and 343 of them hold 30.6% of all spending while having many tickets or a low rating, so the first recommendation was service recovery for them and not a campaign for the biggest segment. The impact should be written as a scenario with its assumptions (for example, 10% of the New Customers who have not bought making a first purchase at the median spending), the recommendations should be ranked by the value at stake, and a test should be proposed before they are scaled.
2. **How would you design a dashboard for the people who will use these segments?**
   Start from the questions they ask: how big is the business, where is the money, who are the segments, and what should be done for each. Put the headline numbers first, then the segment comparison, and keep one color and one marker shape per segment in every chart so segments are recognized at a glance and color is not the only cue. An interactive version (here, Streamlit) adds filters, a lookup of one customer, and a download of the filtered list, and its numbers should be checked against the analysis notebook so the two never disagree. The dashboard should also say what it cannot show, such as the fact that the data is simulated and the clusters overlap.
3. **How would you evaluate a rule-based recommendation system after launch?**
   Without a record of accepted offers it can only be checked for consistency, so the first step after launch is to start recording which offers each customer saw and accepted. Then run a controlled test: send the recommended offer to half of a segment and a default offer to the other half, and compare the acceptance, purchases, and satisfaction. The rules (the thresholds for tickets and ratings, and the offers) can then be adjusted, and the clustering should be re-run regularly to check that the segments remain stable. Until then, the recommendations and the impact figures should be described as scenarios.