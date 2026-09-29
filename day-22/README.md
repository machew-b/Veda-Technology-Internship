# Day 22: A/B Test Analysis

## Description
Analyze an A/B test comparing two groups and determine whether observed differences in a selected metric are statistically meaningful.

## Objective
Apply statistical testing to a practical experimentation problem.

## Tools
- Python
- Pandas
- NumPy
- SciPy
- Jupyter Notebook

## Deliverables
- A/B test dataset analysis
- Descriptive statistics for both groups
- Appropriate statistical test
- Final recommendation based on evidence

## Hints / Mini Guide
- Clearly define the control and treatment groups
- Compare both effect size and statistical significance
- Avoid making decisions based only on p-values

## Suggested Datasets
- A/B Testing Sample Dataset
- Marketing Campaign Dataset

## Approach
I used the `AB_Testing_Sample_Dataset.csv` file (294,478 users), clearly defining the `control` group (shown the `old_page`) and `treatment` group (shown the `new_page`), and confirming the groups matched their landing pages with a crosstab. I computed descriptive statistics for both groups on the primary metric (`converted`) and a secondary metric (`purchase_amount`). For `converted`, a binary outcome, I ran a two-proportion z-test, and computed the absolute difference, relative lift, and a 95% confidence interval for the difference in conversion rates. For `purchase_amount`, a continuous metric, I ran a Welch's t-test and computed Cohen's d as the effect size. I specifically compared the two results to demonstrate why a p-value alone isn't sufficient evidence, since both metrics came back statistically significant despite having very different effect sizes.

## Outcome
The conversion rate was 11.87% in the control group versus 17.95% in the treatment group — a ~6.1 percentage point absolute lift, a ~51% relative lift, and a 95% confidence interval of roughly (5.8, 6.3) percentage points that clearly excludes zero (z ≈ 46, p ≈ 0). Purchase amount was also significantly higher in the treatment group (p ≈ 0), but with a Cohen's d of only about 0.15 — a small effect by Cohen's own convention, despite the p-value looking just as extreme as the conversion result. This was a direct, real demonstration of why effect size matters alongside significance: with almost 300,000 users, even a small, possibly unimportant difference will register as "statistically significant," so the p-value alone can't distinguish a strong result from a weak one. **Final recommendation: launch the new page** — the conversion rate improvement is both statistically significant and practically large, which is a much stronger basis for the decision than the p-value alone would suggest.

## Interview Questions
1. **What is A/B testing?**
   A/B testing is a controlled experiment that compares two versions of something, typically a "control" (the existing version) and a "treatment" (a new version being tested), by randomly splitting users between them and measuring whether a chosen metric (like conversion rate) differs meaningfully between the two groups. It's used to make evidence-based decisions about changes before rolling them out to everyone.
2. **What is the control group?**
   The control group is the baseline group in an experiment. They are the users who experience the existing, unchanged version (in this dataset, the `old_page`). It's what the treatment group's results are compared against to determine whether the new version actually made a difference.
3. **Why should effect size be considered alongside statistical significance?**
   A p-value only tells you how likely the observed difference would be if there were truly no difference between groups (i.e., it doesn't tell you how *large* or *practically meaningful* that difference actually is). With a large enough sample size, even a tiny, unimportant difference can become "statistically significant." Effect size (like a percentage-point lift, relative lift, or Cohen's d) measures the actual magnitude of the difference, which is what ultimately matters for deciding whether a change is worth making.