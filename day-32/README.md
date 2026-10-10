# Day 32: Student Performance & Learning Analytics

## Description
Build a data science system that analyzes student academic and learning data to identify performance patterns, subject-wise strengths and weaknesses, attendance trends, and factors associated with successful outcomes.

## Objective
Learn the complete basic data science workflow from data cleaning and exploratory analysis to visualization, statistical analysis, and introductory predictive modeling.

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Excel
- Git/GitHub

## Deliverables
- Subject-wise performance analysis
- Correlation analysis
- Student performance visualizations
- Feature engineering

## Hints / Mini Guide
- Use a public or synthetic student dataset.
- Handle missing values and inconsistent records.
- Analyze relationships between attendance, study time and performance.
- Start with linear regression or classification depending on the target variable.
- Clearly separate training and testing data.

## Approach
I continued from the cleaned dataset I saved on Day 31, `Student_Learning_Analytics_Cleaned.csv` (15 columns, with the simulated `attendance_percentage` and `study_hours_per_week` columns added on Day 31). For the subject-wise analysis, I built a summary table (mean, median, standard deviation, minimum, maximum) for the four subjects, calculated pass rates using a simple 50-point mark that I assumed since the dataset has no official passing mark, found each student's strongest and weakest subject with `idxmax()` and `idxmin()`, and compared average subject scores by gender and by grade. For the correlation analysis, I built a correlation matrix and heatmap covering the scores, `average_score`, attendance, study hours, `test_preparation_course`, and `lunch`, ranked every column by its correlation with `average_score`, and used `scipy.stats.pearsonr()` to get r and p-values for four of them. I made five visualizations: the correlation heatmap, a box plot of the subject scores, a grouped bar chart of subject averages by gender, a line chart of subject averages across attendance bands, and a scatter plot of study hours against average score with a trend line from `np.polyfit()`. For feature engineering, I added 13 columns: analysis features from the scores (`best_subject`, `weakest_subject`, `score_range`, `passed_all_subjects`), encoded predictors (`gender_female`, an ordered `parent_education_rank` from 1 to 6, and one-hot `race_group` columns with `group A` as the baseline), engagement predictors (`attendance_level` and an `engagement_score` that averages the z-scores of attendance and study hours), and a `high_performer` target defined as an average score of 70 or higher. I also built a table listing which columns are safe to use as predictors and which are not, then saved everything as `Student_Learning_Analytics_Features.csv` for Day 33.

## Outcome
By the end of this task, I could break student performance down by subject, measure how variables relate to each other, visualize the patterns, and engineer features for a model. Math is the weakest subject on every measure (average 57.2, pass rate 63.8%, and the largest drop between grade A and Fail students), female students lead in math and writing while male students lead slightly in reading, and only 39.9% of students passed all four subjects at a 50-point mark. The four subject scores turned out to be almost uncorrelated with each other, which is unusual for real student data and suggests the scores were generated independently. Attendance (0.37) and study hours (0.36) had the strongest links to average score, while `test_preparation_course` (0.04) and `lunch` (0.06) had almost none, but since attendance and study hours were simulated on Day 31, those two relationships are by construction and show the workflow rather than a real finding. The p-values were also a useful lesson: with about 10,000 students, even a correlation of 0.04 is statistically significant, so the size of r matters more than the p-value. The engineered `engagement_score` ended up as the strongest predictor of average score (correlation 0.48), and the most important takeaway from feature engineering was data leakage, since every column built from the scores must stay out of the predictors on Day 33.

## Interview Questions
1. **What does a correlation coefficient tell you, and what are its limits?**
   The correlation coefficient (Pearson's r) measures the strength and direction of a linear relationship between two numeric variables, from -1 (perfect negative) to +1 (perfect positive), with values near 0 meaning no linear relationship. Its limits are that it only captures linear patterns, it can be distorted by outliers, and it says nothing about causation, i.e., attendance and scores moving together doesn't prove that one causes the other. Also, with a large dataset even a very weak correlation can have a tiny p-value, so the size of r matters more than the significance alone.
2. **What is feature engineering, and why is it useful?**
   Feature engineering is the process of creating new columns, or transforming existing ones, so that a model can learn from the data more easily. Common examples are encoding categories as numbers (for instance, one-hot encoding or an ordered rank), binning a numeric column into groups (like turning attendance into Low, Medium, and High), and combining columns into a single measure (like averaging the z-scores of attendance and study hours into an engagement score). Good features can help a model more than switching to a more complicated algorithm.
3. **What is data leakage, and how can feature engineering cause it?**
   Data leakage happens when a model is trained on information that would not be available when making a real prediction, or that directly contains the answer, which makes its results look much better than they truly are. Feature engineering can cause it when a new column is built from the target, for example, using `average_score`, `grade`, or `high_performer` to predict whether a student is a high performer. The model would just be reading the answer from its inputs, so these columns have to be kept out of the predictors.