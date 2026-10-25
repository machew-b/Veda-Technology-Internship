# Veda Technology Internship: Data Science Track

This repository contains data science learning notebooks and four end-to-end analytics projects completed during the Veda Technology internship.

## Repository structure

| Folder | What it covers | Original day range |
|---|---|---|
| [`01-python-fundamentals/`](./01-python-fundamentals/) | Python data types, conditionals, loops, functions, collections, comprehensions, string processing, and exception handling | Days 01–08 |
| [`02-numpy/`](./02-numpy/) | NumPy arrays, indexing, vectorization, aggregation, random sampling, reshaping, and stacking | Days 09–14 |
| [`03-pandas-data-cleaning/`](./03-pandas-data-cleaning/) | DataFrames, selection, filtering, sorting, missing and duplicate data, type conversion, and date parsing | Days 15–21 |
| [`04-ab-testing-and-regression/`](./04-ab-testing-and-regression/) | A/B testing, multiple linear regression, and regression metrics | Days 22–24 |
| [`05-classification-models/`](./05-classification-models/) | Logistic regression, classification metrics, threshold tuning, decision trees, random forests, and K-nearest neighbors | Days 25–30 |
| [`student-performance-learning-analytics/`](./student-performance-learning-analytics/) | Student data cleaning, exploratory and learning analytics, feature engineering, prediction, and reporting | Days 31–33 |
| [`veda-business-service-analytics/`](./veda-business-service-analytics/) | Veda business, service, marketing, segmentation, demand, and executive analytics | Days 35–38 |
| [`customer-segmentation-recommendation-system/`](./customer-segmentation-recommendation-system/) | Customer behavior analysis, clustering, segment profiles, recommendations, and dashboards | Days 40–43 |
| [`sales-service-demand-forecasting/`](./sales-service-demand-forecasting/) | Sales and service demand analysis, forecast modeling, validation, and business planning | Days 45–48 |
| [`datasets/`](./datasets/) | Shared source datasets and project data files; notebooks refer to this folder using relative paths | Shared |

The project notebooks are named by part and should generally be run in order. Some later parts read intermediate datasets created by earlier parts. In particular, the student analytics project creates its cleaned and feature datasets as it runs.

## Tools and libraries

The notebooks use Python and Jupyter with NumPy, pandas, Matplotlib, Seaborn, SciPy, scikit-learn, and statsmodels. The Streamlit dashboards also use Streamlit and Altair. A few notebooks and apps use Python's standard-library modules, including `sqlite3` and `pathlib`.

## How to use this repository

1. Clone the repository and enter its folder:

   ```bash
   git clone https://github.com/machew-b/Veda-Technology-Internship.git
   cd Veda-Technology-Internship
   ```

2. Create and activate a virtual environment, then install the notebook dependencies:

   ```bash
   python -m venv .venv
   # Windows PowerShell:
   .\.venv\Scripts\Activate.ps1
   # macOS/Linux:
   source .venv/bin/activate
   python -m pip install -r requirements.txt
   ```

3. Start JupyterLab:

   ```bash
   jupyter lab
   ```

4. Open a topic or project folder and run its notebook. Run multi-part project notebooks in order when a later part depends on generated files.

The shared `datasets/` folder stays at the repository root. From a notebook in any topic or project folder, the relative path to it is `../datasets/`.
