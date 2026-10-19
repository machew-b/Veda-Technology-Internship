# Day 41: Customer Segmentation & Service Recommendation System

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
- Feature engineering
- K-Means clustering
- Cluster evaluation

## Hints / Mini Guide
- Use synthetic or public customer data.
- Possible segments can include highly engaged customers, occasional users, new customers, and service-focused customers.
- Standardize numerical features before clustering.
- Use the elbow method or silhouette score to evaluate clusters.
- Create meaningful names for the resulting customer segments.
- Recommendations can be rule-based rather than requiring a complex recommendation algorithm.

## Approach
I continued from the cleaned customer table saved on Day 40 in `datasets/veda_customers/cleaned/`. For the feature engineering, I first checked why the raw columns cannot go into K-Means directly (different scales, skew, and overlapping measures), and then applied a `log(1 + x)` transform to website visits, recency, inquiries, tickets, and spending, which reduced the skew of spending from 10.81 to -0.27. I checked whether the counts should be divided by tenure to make rates and decided against it, because the counts barely grow with tenure (correlations of 0.05 to 0.14), so tenure became a feature of its own. Because the four engagement measures (visits, session length, pages per visit, and email open rate) are all related (0.53 to 0.60), I merged them into one engagement score, so engagement would not count four times against spending. The clustering uses six features (engagement score, recency, inquiries, tickets, spending, and tenure), and I left out purchases (0.94 correlated with spending), the average order value and the buyer flag, the satisfaction rating (45% missing), and the categories, which are used to describe the segments on Day 42. The features were standardized with `StandardScaler`, and the feature table is saved as `datasets/veda_customers/features/customer_features.csv`. For the K-Means clustering, I ran `KMeans` with 20 starts for 2 to 8 clusters and judged each solution with the elbow method, the silhouette score, the Davies-Bouldin and Calinski-Harabasz indexes, and two stability tests with the adjusted Rand index (ten different random starts, and twenty samples of 80% of the customers). I chose 4 clusters, because the elbow, the Davies-Bouldin index, and stability agree on it (the groups become unstable from 5 clusters), and its silhouette is practically tied with the best value, which belongs to 3 clusters. The final clusters are numbered from the largest to the smallest. For the cluster evaluation, I looked at the cluster centers in standardized and original units, drew a silhouette plot with the score of each cluster, checked how the clusters change when the feature choices change (without tenure, without the log transform, with the four engagement measures separately, and with all the raw columns), and compared the clusters with customer type, primary interest, and acquisition channel, which were not used for clustering. The clustered customers (with each customer's cluster and silhouette) and the evaluation by number of clusters are saved in `datasets/veda_customers/clustered/`.

## Outcome
By the end of this task, I had an engineered feature table, four customer clusters, and an evaluation that shows both what works and the limits of the result. The clusters are an engaged group (1,517 customers, 30%, with 19.4 website visits on average and 95% having bought), an inactive group (1,369, 27%, last active 86 days ago on average), recent sign-ups (1,243, 25%, an average of 32 days since signing up), and a service-heavy group (871 customers, 17%, with 6.1 inquiries each on average, mostly business customers) that accounts for 73% of all spending. The solution is stable (an adjusted Rand index of 0.95 across random starts and 0.99 across samples) and agrees 0.68 to 0.88 with the clusters from other feature choices. The average silhouette is only 0.29, so the groups overlap and are not sharply separated, and the service-heavy cluster is the least well defined (12.7% of its customers are closer to another cluster). Because the data is simulated with four hidden behavior patterns, finding four clusters is partly built in, so these results show that the method works and not that real Veda Technology customers form four groups. The main lesson was that no single score picks the number of clusters: the silhouette preferred 3 by a hair, the Davies-Bouldin index and the elbow preferred 4, and stability ruled out 5 or more, so the choice had to combine them.

## Interview Questions
1. **Why do you standardize features before K-Means?**
   K-Means assigns each customer to the nearest cluster center using distances, so a feature with large numbers dominates the distance. Here, total spend reaches millions of INR, while an email open rate stops at 100 and tenure at 364 days, so without scaling the clusters would mostly be a split by spending. Standardizing gives every feature a mean of 0 and a standard deviation of 1, so a difference of one standard deviation counts the same in each. Skewed features should also be transformed first (here with a log), because standardizing does not fix a long tail.
2. **How do you choose the number of clusters, and why not use only one measure?**
   K-Means needs the number in advance, and each measure looks at a different aspect: the elbow of the inertia shows where extra clusters stop tightening the groups, the silhouette shows how clearly customers belong to their cluster, the Davies-Bouldin index shows how much the clusters overlap, and stability shows whether the groups are real or an accident of the random start. They often disagree slightly, as they did here: the silhouette was highest for 3 clusters (0.294) and practically tied for 4 (0.292), the Davies-Bouldin index and the elbow pointed to 4, and from 5 clusters on the groups became unstable. The final choice also has to make business sense, for example by giving groups big enough to act on.
3. **How can you tell whether a clustering result is trustworthy?**
   Check the average silhouette and the silhouette of each cluster, test stability (different random starts, samples of the customers, and other reasonable feature choices), and compare the clusters with variables that were not used for clustering. Here, the average silhouette was only 0.29, which means overlapping groups, the service-heavy cluster was the least well defined, and the clusters agreed 0.68 to 0.88 with those from other feature choices. The clusters also differed clearly in customer type, interest, and channel, which were not used. Even so, clusters that look sensible can be an artifact of the method, so a result like this should be presented as a useful grouping and not as proof that the customers fall into exactly four types.