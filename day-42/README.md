# Day 42: Customer Segmentation & Service Recommendation System

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
- Customer segment profiles
- 2D cluster visualization
- Service recommendation logic

## Hints / Mini Guide
- Use synthetic or public customer data.
- Possible segments can include highly engaged customers, occasional users, new customers, and service-focused customers.
- Standardize numerical features before clustering.
- Use the elbow method or silhouette score to evaluate clusters.
- Create meaningful names for the resulting customer segments.
- Recommendations can be rule-based rather than requiring a complex recommendation algorithm.

## Approach
I continued from the clustered customers saved on Day 41 in `datasets/veda_customers/clustered/` and the standardized feature table in `datasets/veda_customers/features/`. For the customer segment profiles, I named the four clusters with a rule that reads each cluster's center instead of its number (the most inquiries gives the Service-Focused Clients, the shortest tenure the New Customers, the highest engagement the Engaged Learners, and the remaining one the Occasional Visitors, which I then checked has the lowest engagement and the longest inactivity). I profiled each segment by its size, buyers, spending (median, average, and share of the total), satisfaction, survey response, behavior (visits, session length, pages, email opens, inactivity, inquiries, tickets, and tenure), and make-up by customer type, interest, and channel, which were not used for the clustering, and saved the profiles as `datasets/veda_customers/segments/segment_profiles.csv`. For the 2D cluster visualization, I used `PCA` on the six standardized features, drew the customers with the segment centers (and a second picture colored by silhouette), saved it as `customer_segments_pca.png`, read what the two axes mean from their loadings, and measured how faithful the picture is (59.6% of the variance is kept, and the nearest 2D center gives the same segment for 89.0% of the customers). For the service recommendation logic, I built a catalog of the 24 offers of Veda Technology (internship domains, training programs, IT services, and digital services) from the business data of Days 35 to 38, and tested with chi-square whether the outcome rates (selection, completion, and conversion) differ between the offers of a family. They do not (p-values of 0.24, 0.92, 0.27, and 0.59), so the offers are ranked by demand and not by outcome. The recommender is a list of seven rules in a function `recommend()`: the primary family follows the customer's interest (or the most common interest of the segment when it is unknown), the cross-sell is the neighboring family, the offer is the most demanded one of the family, each segment has an action, service recovery comes first for customers with 3 or more tickets or a rating of 2 or less, Engaged Learners with a rating of 4 or more are invited to the referral program, and every recommendation gets a confidence level from the silhouette and whether the interest is known. I checked that all 5,000 customers get a complete recommendation, that the offer follows the interest, and how often each exception applies. The results are saved in `datasets/veda_customers/segments/` as `customers_segmented.csv`, `service_catalog.csv`, and `service_recommendations.csv`.

## Outcome
By the end of this task, the four clusters from Day 41 became four named segments with profiles, a 2D map, and a rule-based service recommendation for every customer. The Engaged Learners (1,517 customers, 30%) are active students and professionals, 95% of whom have bought, and they hold 22.8% of the spending. The Occasional Visitors (1,369, 27%) were last active 86 days ago on average and hold 1.2% of the spending. The New Customers (1,243, 25%) signed up 32 days ago on average, and 41% have bought. The Service-Focused Clients (871, 17%) are mostly business customers with 6.1 inquiries each, and they hold 72.7% of the spending but are the least satisfied group together with the Occasional Visitors (3.6). The PCA picture keeps 59.6% of the variance and gives the same segment for 89.0% of the customers: the Occasional Visitors are the clearest group, while the Service-Focused Clients overlap the Engaged Learners. In the recommendations, 88% of the Service-Focused Clients are pointed to IT or digital services and 84% of the Engaged Learners to training or internships, service recovery applies to 457 customers (39.4% of the Service-Focused Clients), the referral invitation to 887 Engaged Learners, and the confidence is High for 63% of the customers and Low for 11%. Because the customers and offers are simulated and the data has no record of which offers customers accepted, the recommendations cannot be scored, and customers who share an interest get the same lead offer because the interest is recorded only at the level of the family. So the rules are a documented starting point to test in real campaigns. The main lesson was to check what the data can support before ranking: the offers looked different by outcome, but the differences were within chance, so ranking by demand was the honest choice.

## Interview Questions
1. **How do you turn clusters into customer segments that a business can use?**
   A cluster is only a number until it is profiled and named. I compared the cluster centers and the real-unit averages (visits, inactivity, inquiries, spending, and tenure), described each group in plain words, and gave it a name that tells the business what to do, such as Engaged Learners or Service-Focused Clients. I did the naming with rules on the cluster centers, so the names stay correct if the cluster numbers change when the model is re-run. The profile should also include the size and the value of each segment: here the Service-Focused Clients are only 17% of the customers but hold 72.7% of the spending, which changes how much attention they deserve. Variables that were not used for clustering, such as customer type and channel, then confirm that the segments are meaningful.
2. **How do you visualize clusters built on many features, and what are the limits of the picture?**
   PCA projects the standardized features onto the two directions with the most variance, so each customer can be drawn on a flat chart. The picture should state how much of the variance it keeps (59.6% here) and what the axes mean from their loadings (the first axis is engagement, spending, and activity, and the second is service use and tenure). The limit is that overlap in 2D can be partly an effect of the lost variance, and clusters can be separate in the full data while touching in the picture. As a check, I counted how often the nearest segment center in 2D gives the real segment (89.0%), which was lowest for the New Customers (80.6%).
3. **Why can a recommendation system be rule-based, and how do you evaluate it without outcome data?**
   When the data has no record of which offers customers accepted, a complex model cannot be trained or scored, but a short set of explicit rules can still be useful, and each rule is easy to explain, audit, and change. Here, the rules use the customer's interest, the segment, and the most demanded offer of the family (the outcome rates of the offers did not differ significantly, so ranking by outcome would only follow chance). Without outcomes, I could only check that the rules behave as designed (complete recommendations, offers that follow the interest, and exceptions that apply to the right customers) and I added a confidence level that is honest about uncertain customers. To measure whether the recommendations really work, the rules should be tested with a controlled campaign, such as sending the recommended offer to half of a segment and comparing the responses.