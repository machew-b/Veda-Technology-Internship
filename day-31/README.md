# Day 31: Student Performance & Learning Analytics

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
- Student dataset
- Data cleaning pipeline
- Exploratory data analysis
- Attendance analysis

## Hints / Mini Guide
- Use a public or synthetic student dataset.
- Handle missing values and inconsistent records.
- Analyze relationships between attendance, study time and performance.
- Start with linear regression or classification depending on the target variable.
- Clearly separate training and testing data.

## Approach
I used the `Student_Performance_Dataset.csv` file from the shared `datasets/` folder, a 10,000-row student dataset with four subject scores, `total_score`, `grade`, and background columns such as `lunch` and `test_preparation_course`. It turned out to be intentionally messy: 213 rows have at least one missing value, `gender` mixes `male`/`female` with `Boy`, `Girl`, and a stray `\tmale`, `race_ethnicity` mixes `group C` with bare letters like `D` and a stray `group C\n`, and `math_score` loaded as text because of a single `\t41` entry. I built the data cleaning pipeline as three small functions chained with `.pipe()`: `fix_text_labels()` standardizes the labels and converts `math_score` to numeric, `recover_missing_values()` rebuilds what the data itself can tell us (one missing `roll_no` from its `std-01`, `std-02` pattern, 80 missing subject scores from `total_score` minus the other three scores, 16 missing `total_score` values from the sum of the four scores, and 3 missing `grade` values from the score bands, a rule I confirmed reproduces all 9,994 existing grades), and `handle_remaining_missing()` drops the 9 rows whose scores could not be recovered and fills the small number of missing category and 0/1 values with the mode. Eight validation checks on the cleaned data all returned zero failing rows. Since the real dataset has no attendance or study-time column, I added a clearly labeled simulated `attendance_percentage` and `study_hours_per_week` using a fixed random seed, built to rise modestly with performance plus random noise. I then explored the cleaned data with summary statistics, score distributions, a grade distribution, and group averages, and analyzed attendance using its distribution, average attendance by grade, attendance bands compared to average score, a scatter plot, the correlation, and a comparison of students below and above a 75% attendance line. The cleaned data was saved as `Student_Learning_Analytics_Cleaned.csv` so that Day 32 and Day 33 can start from it.

## Outcome
By the end of this task, I could take a messy student dataset through a full cleaning workflow and begin analyzing it. Recovering values from the data itself (subject scores from `total_score`, totals from the four scores, grades from score bands) kept 100 values that would otherwise have meant dropping rows or guessing, and only 9 rows (0.09% of the data) had to be dropped, leaving 9,991 students. The exploration showed that math is the weakest subject (average 57.2, versus 71.4 for writing), that grade B is by far the most common (5,654 students), and that female students average about 6.1 points higher than male students, while test preparation, lunch type, and parental education made very little difference. The attendance analysis showed average attendance falling steadily from 85.9% for grade A to 69.0% for Fail, average scores rising from 55.9 to 71.9 across the attendance bands, and a correlation of 0.37 with average score. Because the dataset had no attendance column, that attendance data was simulated with a built-in link to performance, so these results demonstrate the analysis workflow rather than a real-world finding. This also reinforced how much of data science is cleaning: most of the work here was making the data trustworthy before any analysis could mean anything.

## Interview Questions
1. **Why is data cleaning important before analysis?**
   Data cleaning makes sure the data is accurate, consistent, and usable before any conclusions are drawn from it. That is, inconsistent labels like `Boy` and `male` get counted as separate groups, a score stored as text can't be averaged, and missing values can silently distort summary statistics or break a model. Skipping cleaning means every later result, from a simple average to a trained model, rests on data that can't be trusted.
2. **What is exploratory data analysis (EDA), and what does it usually include?**
   EDA is the process of examining a dataset to understand its structure, quality, and patterns before building any model. It usually includes summary statistics (`describe()`), checking data types and missing values, looking at distributions with histograms or bar charts, comparing groups (for instance, average score by gender), and looking for relationships between variables. The goal is to learn what the data looks like and to form questions worth testing, rather than to prove anything yet.
3. **How would you analyze the relationship between attendance and student performance, and what should you be careful about?**
   Start by looking at the distribution of attendance, then compare performance across attendance levels (for instance, average score for each attendance band), plot attendance against score in a scatter plot, and measure the strength of the relationship with a correlation coefficient. The main caution is that correlation does not mean causation. Students who attend more may also study more or be more motivated, so attendance alone may not explain better scores, and the relationship found is only as reliable as the data behind it (here, the attendance values were simulated).