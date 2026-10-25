# Customer Segmentation & Service Recommendation System: Final Report

**Project:** a four-day analytics project (Days 40 to 43) of the Veda Technology Internship, Data Science track  
**Customers analyzed:** 5,000 simulated customers who signed up between October 2025 and September 2026  
**Data:** simulated (synthetic) customer data, generated with a fixed random seed

## 1. Summary

This project grouped 5,000 simulated Veda Technology customers into four segments with K-Means clustering and built a rule-based system that recommends a service or learning program to each customer. The segments differ greatly in value: the 871 Service-Focused Clients are 17% of the customers but hold 72.7% of the INR 206.3 million in spending, while the 1,369 Occasional Visitors are 27% of the customers and hold 1.2%. The most urgent finding is that 343 Service-Focused Clients, who have 3 or more support tickets or a satisfaction rating of 2 or less, hold INR 63.2 million (30.6% of all spending), so service recovery for them is the first priority. The other recommendations are a learning path and a referral program for the 1,517 Engaged Learners, a welcome series for the 1,243 New Customers (738 of whom have not bought yet), and a low-cost re-engagement email for the Occasional Visitors. All figures come from a simulated dataset, the segments overlap (average silhouette 0.29), and the recommendations were never tested on real customers, so they are a starting point to test and not proven results.

## 2. What Was Built

| Day | Work | Main output |
|---|---|---|
| 40 | Synthetic customer dataset, preprocessing pipeline, behavior analysis | `customers_raw.csv` (5,100 rows) and `customers_cleaned.csv` (5,000 rows, 16 columns) |
| 41 | Feature engineering, K-Means clustering, cluster evaluation | `customer_features.csv` and `customers_clustered.csv` (4 clusters) |
| 42 | Segment profiles, 2D visualization (PCA), service recommendation logic | `segment_profiles.csv`, `service_recommendations.csv`, `customer_segments_pca.png` |
| 43 | Segment dashboard (static and Streamlit), business recommendations, this report | `app.py`, `customer_segment_dashboard.png`, `business_recommendations.csv`, `final_report.md` |

## 3. Method in Brief

1. **Data and cleaning.** The 5,100 raw rows (deliberately messy) became 5,000 clean rows after removing 100 duplicates, converting 56 numbers typed as text, standardizing 2,305 labels, and handling 114 impossible numbers and 25 contradictory values. The survey gaps in the satisfaction rating were left on purpose, because not answering is itself information (45% of the ratings are missing).
2. **Features.** Skewed measures were log-transformed, four related engagement measures were merged into one engagement score, and six features were standardized for the clustering: engagement, recency, inquiries, tickets, spending, and tenure.
3. **Clustering.** K-Means with 4 clusters was chosen because the elbow, the Davies-Bouldin index, and stability agree on it (from 5 clusters the groups become unstable), and its silhouette (0.292) is practically tied with the best value (0.294, for 3 clusters).
4. **Segments and recommendations.** The clusters were named by rules on their centers, drawn in 2D with PCA, and given a rule-based recommender with seven rules (the customer's interest, a cross-sell in the neighboring family, the most demanded offer of the family, a segment action, service recovery, a referral invitation, and a confidence level).

## 4. The Four Segments

| Segment | Customers | Have bought | Share of spending | Satisfaction | Profile |
|---|---|---|---|---|---|
| Engaged Learners | 1,517 (30%) | 95% | 22.8% | 4.3 | 19.4 visits, 54.6% email opens, last active 6 days ago; mostly students and working professionals (84%) |
| Occasional Visitors | 1,369 (27%) | 23% | 1.2% | 3.6 | 3.1 visits, 15% email opens, last active 86 days ago; 65% inactive for more than 60 days |
| New Customers | 1,243 (25%) | 41% | 3.3% | 3.9 | Signed up 32 days ago on average (others: 165 to 201); moderately engaged |
| Service-Focused Clients | 871 (17%) | 87% | 72.7% | 3.6 | 6.1 inquiries and 2.4 support tickets each; 85% business customers; IT Services interest (50%) |

The PCA map keeps 59.6% of the variance of the six features. The nearest 2D center gives the same segment for 89.0% of the customers, so the segments are visible but touch each other, most of all the Service-Focused Clients and the Engaged Learners. The interactive version of this view is the Streamlit app (`app.py`), and the static version is `customer_segment_dashboard.png`.

## 5. The Recommendation Logic

Every customer receives a primary offer, a cross-sell offer, an action, and a confidence level. The primary offer family follows the customer's stated interest (or the most common interest of the segment when it is unknown), and the offer inside a family is the most demanded one (Data Science for internships, Full Stack Web Development for training, Software Development for IT services, and Website Design & Development for digital services), because the selection, completion, and conversion rates of the offers do not differ significantly (p-values of 0.24 to 0.92). Service recovery applies to 457 customers (9.1%), the referral invitation to 887 Engaged Learners, and the confidence is High for 63% of the customers, Medium for 26%, and Low for 11%. The confidence says how clearly a customer belongs to its segment and not how likely the customer is to accept the offer.

## 6. Business Recommendations

Impacts are illustrative scenarios with stated assumptions, calculated from the simulated data, and should be tested before they are scaled. The full list with the evidence is in `business_recommendations.csv`.

| Priority | Area | Recommendation | Illustrative impact |
|---|---|---|---|
| High | Service-Focused Clients | Start service recovery with the customers flagged by rule R5 (resolve the open tickets and contact the customer personally), assign an account manager to every Service-Focused Client, and keep the 4-hour first-response target from the Day 38 analysis. | Losing 10% of the at-risk spending would cost about INR 6.3 million, more than the revenue added in any of the scenarios below. |
| High | Engaged Learners | Offer the cross-sell as part of a learning path (for example a training program followed by the matching internship) and test it on a share of the segment first. | If 10% of the segment (152 customers) bought one more program at the median order value, that would add about INR 1.4 million. |
| High | Engaged Learners | Invite the satisfied Engaged Learners to a referral program (rule R6), and track how many new customers each invitation brings. | If 5% of the 887 invited customers brought one new customer who spends like the median Referral customer, that would add 44 customers and about INR 0.79 million. |
| Medium | New Customers | Run a welcome series that introduces the recommended offer of each customer (rules R1 to R3) and aims at the first purchase, with a small incentive such as a free trial session for training programs. | If 10% of them (74 customers) made a first purchase at the median spend of current New Customer buyers (INR 6,100), that would add about INR 0.45 million. |
| Medium | Occasional Visitors | Send a low-cost re-engagement email that features the recommended offer for the customer's interest, and stop contacting customers who do not respond after two emails. | If 10% of the customers who never bought (106) bought once at the median spend of the segment's buyers (INR 5,000), that would add about INR 0.53 million. |
| Medium | Marketing | Move part of the Paid Ads and Social Media budget to Referral and Email, and track the segment of each new customer, so channels are judged by the segments they bring and not only by the number of leads. | Not calculated separately, because the budget effect is already estimated on Day 38 (about 3,540 more leads a year in the upper scenario); test on a small budget first. |
| Medium | Data and measurement | Send a short survey after each purchase or ticket, record the offer each customer viewed and accepted, and record the interest at the level of the individual program or service. | Makes it possible to score the recommendations and to personalize the offer inside each family. |
| Foundation | Validation | Replace the simulated data with real customer records, test each recommendation in a controlled campaign (send the recommended offer to half of a segment and compare responses), and re-run the clustering every quarter, checking that the segments stay stable. | Turns these scenarios into measured results. |

## 7. Risks and Limitations

- All customers are simulated, and four behavior patterns were built into the simulation, so finding four clusters is partly circular. The results show that the method works and not that real Veda Technology customers form four groups.
- The clusters overlap: the average silhouette is 0.29, the Service-Focused Clients are the least well defined group (12.7% of them are closer to another cluster), and the clusters agree 0.68 to 0.88 with the clusters from other reasonable feature choices. The solution itself is stable (adjusted Rand index of 0.95 across random starts and 0.99 across samples).
- The recommendations are rule-based design choices. The data has no record of which offers customers accepted, so they cannot be scored, and the interest is recorded only at the level of the offer family, which means that customers with the same interest get the same lead offer.
- The impact figures assume that the relationships are causal and keep working at a larger scale, and they are not forecasts. The thresholds (3 tickets, a rating of 2, and the confidence levels) are assumptions.
- The satisfaction rating is missing for 45% of the customers, so the satisfaction figures describe the customers who answered the survey.

## 8. Next Steps

1. Replace the simulated data with real customer records and re-run the pipeline.
2. Test the recommendations in a controlled campaign: send the recommended offer to half of a segment and compare the responses.
3. Record the offers each customer viewed and accepted, so the recommendations can be scored and personalized inside each family.
4. Start with the service recovery of the 343 at-risk Service-Focused Clients, and measure whether their spending and satisfaction hold.
5. Re-run the clustering every quarter and check that the segments stay stable.

## 9. Project Documentation

**Repository:** `Veda-Technology-Internship`

```
Veda-Technology-Internship/
├── datasets/veda_customers/
│   ├── raw/          # messy customer table created on Day 40
│   ├── cleaned/      # cleaned customer table (Day 40)
│   ├── features/     # engineered and standardized features (Day 41)
│   ├── clustered/    # customers with their cluster, and the evaluation by number of clusters (Day 41)
│   └── segments/     # segment profiles, service catalog, segmented customers, recommendations (Day 42)
└── 08-customer-segmentation-recommendation-system/
    ├── part-1-customer-data-and-behavior-analysis.ipynb
    ├── part-2-feature-engineering-and-k-means-clustering.ipynb
    ├── part-3-segment-profiles-and-service-recommendations.ipynb
    ├── part-4-dashboard-and-business-recommendations.ipynb
    ├── app.py
    ├── customer_segment_dashboard.png
    └── business_recommendations.csv
```

The notebooks and project deliverables are kept together in `08-customer-segmentation-recommendation-system/`.

**How to reproduce:** run the `part-1` through `part-4` notebooks in order. They use relative paths such as `../datasets/veda_customers/`. The random seeds are fixed, so the tables are identical on every run.

**How to run the dashboard:**

```
pip install streamlit pandas altair
streamlit run 08-customer-segmentation-recommendation-system/app.py
```
