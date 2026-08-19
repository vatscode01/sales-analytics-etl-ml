# Sales Analytics ETL + Machine Learning Platform

An end-to-end **Sales Analytics, ETL, Business Intelligence, and Machine Learning platform** built using Python, PostgreSQL, SQL, and machine learning.

The project transforms raw e-commerce sales data into a reproducible analytics pipeline, loads cleaned data into PostgreSQL, generates business-focused SQL analytics and KPIs, presents insights through an interactive dashboard, and extends the platform with a time-series sales forecasting model.

```text
Raw CSVs
   ↓
Python ETL
   ↓
PostgreSQL
   ↓
SQL Analytics
   ↓
Dashboard
   ↓
Machine Learning Forecasting
```

---

## 📌 Project Overview

Sales data often contains inconsistent formats, missing values, duplicate records, and multiple related datasets. Simply creating charts from raw CSV files does not provide a reliable analytics system.

This project builds a complete data pipeline that:

* Extracts raw e-commerce data
* Profiles and documents the source datasets
* Cleans and transforms the data reproducibly
* Designs a relational PostgreSQL database
* Loads processed data into PostgreSQL
* Validates the loaded data
* Performs advanced SQL analytics
* Creates reusable analytical views
* Calculates business KPIs
* Builds an interactive dashboard
* Generates evidence-based business insights
* Builds a sales forecasting model
* Stores predictions back in PostgreSQL
* Integrates forecasts into the dashboard

The project is based on the Kaggle **E-Commerce Sales Data** dataset specified in the project roadmap.

---

## 🎯 Objectives

The primary objective is to build a **reproducible, understandable, interview-defensible, and recruiter-ready analytics platform** rather than simply creating a collection of notebooks.

The project focuses on:

1. Reproducible ETL
2. Relational database design
3. Data validation
4. Advanced SQL
5. Business analytics
6. Interactive dashboarding
7. Machine learning forecasting
8. End-to-end integration

The analytics platform is intentionally built **before** the machine learning component. ML is an extension of the analytics system rather than the centerpiece.

---

# 🏗️ System Architecture

```text
                         ┌───────────────────┐
                         │    Raw CSV Files  │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │ Python ETL        │
                         │                   │
                         │ Extract           │
                         │ Transform         │
                         │ Load              │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │    PostgreSQL     │
                         │    sales_db       │
                         └─────────┬─────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    │              │              │
                    ▼              ▼              ▼
             ┌────────────┐ ┌────────────┐ ┌────────────┐
             │ Validation │ │ SQL        │ │ Analytics  │
             │ Framework  │ │ Queries    │ │ Views      │
             └────────────┘ └─────┬──────┘ └─────┬──────┘
                                   │              │
                                   └──────┬───────┘
                                          ▼
                                ┌──────────────────┐
                                │    Dashboard     │
                                │                  │
                                │ KPIs             │
                                │ Trends           │
                                │ Products         │
                                │ Categories       │
                                │ Operations       │
                                └────────┬─────────┘
                                         │
                                         ▼
                                ┌──────────────────┐
                                │ Machine Learning │
                                │                  │
                                │ Feature          │
                                │ Engineering     │
                                │       ↓          │
                                │ Forecasting      │
                                └────────┬─────────┘
                                         │
                                         ▼
                                ┌──────────────────┐
                                │ sales_forecast   │
                                │ PostgreSQL Table │
                                └──────────────────┘
```

---

# 🛠️ Technology Stack

| Layer                | Technology                 |
| -------------------- | -------------------------- |
| Programming          | Python                     |
| Data Processing      | Pandas, NumPy              |
| Database             | PostgreSQL                 |
| Database Client      | pgAdmin                    |
| SQL                  | PostgreSQL SQL             |
| Visualization        | Dashboarding tool          |
| Machine Learning     | Scikit-learn               |
| ML Model Persistence | Joblib                     |
| Exploration          | Jupyter Notebook           |
| Version Control      | Git + GitHub               |
| Environment          | Python Virtual Environment |

The roadmap specifically separates exploratory work in notebooks from repeatable ETL and ML logic implemented in Python modules.

---

# 🔄 ETL Pipeline

## 1. Extract

Raw CSV files are stored under:

```text
data/raw/
```

The extraction layer reads the source data without manually modifying the original files.

Example:

```text
data/raw/
├── source_file_1.csv
├── source_file_2.csv
└── ...
```

---

## 2. Transform

The transformation stage converts raw data into clean, consistent, analysis-ready datasets.

Transformations include:

* Standardizing column names
* Handling missing values
* Removing justified duplicates
* Converting dates to appropriate formats
* Cleaning string and categorical values
* Validating numeric fields
* Producing before/after row-count summaries
* Documenting transformation decisions

Cleaned files are stored under:

```text
data/cleaned/
```

A key design principle is that **raw CSV files are never manually edited**. Cleaning must be reproducible by rerunning the transformation pipeline.

---

## 3. Load

The cleaned datasets are loaded into PostgreSQL.

The pipeline:

```text
Extract
   ↓
Transform
   ↓
Load
```

is connected through:

```text
etl/main.py
```

The loading process includes validation of:

* Row counts
* Key uniqueness
* NULL values
* Relationships

Validation SQL is maintained separately in:

```text
sql/validation_queries.sql
```

---

# 🗄️ PostgreSQL Database

The project uses PostgreSQL as the analytical database.

The database is:

```text
sales_db
```

The exact relational schema is designed after profiling the actual Kaggle source files rather than assuming a generic schema.

The database design process identifies:

* Transactional information
* Product information
* Financial information
* Inventory information
* Reference information
* Candidate primary keys
* Foreign keys
* Relationships between datasets

The schema and design decisions are documented in:

```text
reports/database_design.md
```

---

# 🧹 Data Quality & Validation

Data quality is treated as part of the pipeline rather than a one-time cleaning step.

The validation framework checks:

* Required columns
* Data types
* Numeric ranges
* Date validity
* Duplicate keys
* Important NULL constraints
* Relationships between tables

The pipeline also produces validation information and uses automated assertions where appropriate.

---

# 📝 Logging & Error Handling

The ETL pipeline includes logging for important events.

Logs include:

* Pipeline start/end
* Source files
* Input row counts
* Transformation actions
* Database loading results
* Errors and exceptions

Logs are stored under:

```text
logs/
```

Database and file operations include exception handling, and database connections are properly closed.

---

# 🔁 Incremental Loading

The project also investigates incremental processing.

The pipeline identifies an appropriate date or transaction field and determines whether new records should be handled through:

* Append
* Upsert

If supported by the dataset, a safe incremental loading strategy is implemented.

An optional pipeline-run metadata table can also be used to track ETL executions.

---

# 📊 SQL Analytics

The project goes beyond basic SQL queries and includes intermediate-to-advanced analytical SQL.

Techniques include:

### Core SQL

* SELECT
* WHERE
* GROUP BY
* ORDER BY
* JOIN
* Aggregations

### Advanced SQL

* CTEs
* CASE expressions
* Subqueries
* Conditional aggregation
* Date functions
* Multi-table joins

### Window Functions

* `ROW_NUMBER()`
* `RANK()`
* `DENSE_RANK()`
* `LAG()`
* `LEAD()`

Additional analysis includes:

* Running totals
* Moving averages
* Month-over-month changes
* Top-N analysis by category

Final SQL queries are maintained as version-controlled `.sql` files.

---

# 📈 Business KPI Layer

The project converts raw data into business-focused metrics.

Depending on what the dataset supports, KPIs include:

* Revenue
* Units sold
* Average order value
* Profit / margin
* Cancellation rate
* Monthly growth
* Category contribution

Every KPI is documented with:

```text
Formula
Source columns
Interpretation
Limitations
```

This ensures that dashboard metrics are not treated as unexplained numbers.

---

# 👁️ Analytics Views

Reusable PostgreSQL views are created for commonly used analytical datasets.

Planned views include:

```text
Monthly Sales Summary
Product / Category Performance
KPI Summary
```

These views provide clean, dashboard-ready datasets while keeping analytical logic inside the database layer.

---

# 📊 Interactive Dashboard

The dashboard is designed to support business decision-making rather than simply display charts.

## Executive Overview

The overview contains:

* Major KPI cards
* Sales / revenue trends
* Product or category performance
* Date filtering
* Explanatory labels

Every displayed number is reconciled against SQL results.

---

## Product & Category Analysis

The dashboard includes analysis such as:

* Top products
* Bottom products
* Category contribution
* Product trends
* Price versus sales where meaningful
* Interactive filtering

---

## Operational & Channel Analysis

Where supported by the source data, the dashboard analyzes:

* Fulfilment
* Shipping / delivery
* Cancellations
* Marketplace/channel performance
* Geographic performance
* Operational bottlenecks

The dashboard only uses analyses supported by the available dataset fields.

---

# 💡 Business Insights

The project does not stop at visualization.

A dedicated business-insights report translates analytics into decisions.

Each insight follows:

```text
Observation
     ↓
Evidence
     ↓
Implication
     ↓
Recommended Action
```

The target is **10–15 evidence-based insights**, including important trends, anomalies, and data limitations.

---

# 🤖 Machine Learning Forecasting

Machine learning is used to extend the analytics platform with sales forecasting.

## Feature Engineering

The modeling dataset is created without data leakage.

Depending on the dataset's available time granularity, forecasting may use:

* Daily aggregation
* Weekly aggregation
* Monthly aggregation

Features include:

* Lag features
* Rolling means
* Rolling sums
* Calendar features where useful

The target variable is explicitly defined.

Most importantly, training and testing are split **chronologically rather than randomly**.

---

# 📐 Model Development

## Baseline Model

A naive baseline is established before evaluating machine-learning models.

A simple:

```text
Linear Regression
```

model is then trained.

Evaluation metrics include:

* MAE
* RMSE
* R² where meaningful

Actual versus predicted values are also visualized.

---

## Model Comparison

A stronger tree-based model may be evaluated against the baseline where appropriate.

Models are compared using the **same chronological holdout period**.

Model selection is based on:

* Validation performance
* Error metrics
* Overfitting checks
* Feature importance where available
* Practical interpretability

The most complex model is not automatically selected.

---

# 🔮 Prediction Pipeline

The ML pipeline is separated into reusable modules:

```text
ml/
├── feature_engineering.py
├── train_model.py
└── predict.py
```

The prediction workflow is:

```text
PostgreSQL
    ↓
Model-ready Data
    ↓
Feature Engineering
    ↓
Trained Model
    ↓
Future Predictions
    ↓
sales_forecast
```

Predictions are written back to PostgreSQL into a table such as:

```text
sales_forecast
```

This allows the dashboard to consume forecasts directly from the analytics platform.

---

# 📊 ML + Dashboard Integration

The dashboard integrates historical and predicted sales.

It can display:

* Historical sales
* Forecasted sales
* Forecast horizon
* Actual vs predicted values when actuals are available
* Model evaluation metrics

Historical and predicted values are clearly distinguished.

The ML component is intended to **support the business dashboard rather than overwhelm it**.

---

# 📁 Project Structure

```text
sales-analytics-etl-ml/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── etl/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── ml/
│   ├── feature_engineering.py
│   ├── train_model.py
│   └── predict.py
│
├── sql/
│   ├── create_tables.sql
│   ├── validation_queries.sql
│   ├── basic_analysis.sql
│   ├── advanced_analysis.sql
│   └── views.sql
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_model_training.ipynb
│
├── dashboard/
│
├── reports/
│
├── images/
│
├── logs/
│
├── requirements.txt
├── .gitignore
└── README.md
```

This structure separates exploratory notebooks, reusable ETL/ML modules, SQL, dashboard code, reports, images, and logs.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd sales-analytics-etl-ml
```

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The planned environment includes packages such as:

```text
pandas
numpy
matplotlib
scikit-learn
psycopg2-binary
jupyter
```

---

# 🐘 PostgreSQL Setup

Install and verify PostgreSQL and pgAdmin.

Create the project database:

```sql
CREATE DATABASE sales_db;
```

The project uses **pgAdmin for database exploration and debugging**, while final SQL is maintained in version-controlled `.sql` files.

Configure your database connection according to your local PostgreSQL setup.

Example configuration:

```text
Host: localhost
Port: 5432
Database: sales_db
User: <YOUR_USERNAME>
Password: <YOUR_PASSWORD>
```

**Do not commit credentials to GitHub.**

---

# ▶️ Running the ETL Pipeline

Place the original dataset files under:

```text
data/raw/
```

Then run:

```bash
python etl/main.py
```

The pipeline should:

```text
Read raw CSVs
     ↓
Extract
     ↓
Transform
     ↓
Validate
     ↓
Save cleaned data
     ↓
Load PostgreSQL
     ↓
Validate database
```

The intended result is a repeatable pipeline that can recreate the cleaned datasets and database state without manual editing.

---

# 🧪 Validation

Run the SQL validation queries:

```text
sql/validation_queries.sql
```

Validation should cover:

* Row counts
* NULL constraints
* Duplicate keys
* Data types
* Numeric ranges
* Relationships

The dashboard should also reconcile with independently calculated SQL results.

---

# 📊 Running the Dashboard

Launch the dashboard according to the dashboard implementation in:

```text
dashboard/
```

The dashboard should consume PostgreSQL analytical outputs or prepared analytical datasets.

Before considering the dashboard complete, verify that displayed totals match the corresponding SQL calculations.

---

# 🤖 Training the ML Model

The machine-learning workflow is separated into:

```text
1. Feature Engineering
2. Model Training
3. Prediction
```

Feature engineering:

```bash
python ml/feature_engineering.py
```

Training:

```bash
python ml/train_model.py
```

Prediction:

```bash
python ml/predict.py
```

The exact commands may be adjusted according to the final implementation.

---

# 📏 Model Evaluation

The forecasting model is evaluated on a chronological holdout period.

Primary metrics:

### Mean Absolute Error — MAE

Measures the average absolute difference between actual and predicted values.

### Root Mean Squared Error — RMSE

Penalizes larger prediction errors more heavily.

### R²

Used where meaningful to evaluate explained variance.

The project avoids random train/test splitting for forecasting because chronological ordering is important for preventing future information from leaking into model training.

---

# 🔐 Security & Data Handling

The repository should never contain:

* Database passwords
* API keys
* Credentials
* Private configuration files
* Other secrets

Before pushing to GitHub:

```text
✓ Check .gitignore
✓ Remove credentials
✓ Remove API keys
✓ Check notebooks
✓ Check configuration files
```

The project roadmap explicitly requires that no secrets or credentials be committed to GitHub.

---

# 📈 Expected Project Outcomes

By the end of the project, the repository should contain:

* A reproducible ETL pipeline
* Cleaned datasets
* PostgreSQL database
* Validation framework
* Analytical SQL queries
* PostgreSQL analytical views
* Business KPI layer
* Interactive dashboard
* Business insights report
* One defensible forecasting model
* Prediction pipeline
* Forecast data stored in PostgreSQL
* Dashboard integration
* Professional documentation

---

# 🎓 Skills Demonstrated

| Skill               | Project Application          |
| ------------------- | ---------------------------- |
| Python              | ETL and ML pipeline          |
| Pandas              | Data cleaning and analysis   |
| SQL                 | Analytics and KPI generation |
| PostgreSQL          | Relational data storage      |
| ETL                 | Extract, Transform, Load     |
| Data Validation     | Pipeline quality checks      |
| Logging             | ETL observability            |
| Git/GitHub          | Version control              |
| Dashboarding        | Business intelligence        |
| Scikit-learn        | Forecasting                  |
| Feature Engineering | ML preparation               |
| Model Evaluation    | MAE, RMSE, R²                |
| Data Visualization  | Trends and comparisons       |
| Business Analytics  | KPIs and recommendations     |

The target outcome is comfortable Python/pandas, intermediate-to-advanced SQL, PostgreSQL schema/querying, end-to-end ETL understanding, reproducible data cleaning, automated validation, dashboarding, business analytics, and one defensible forecasting model.

---

# 💼 Business Questions

The project is designed to answer business questions such as:

* How are sales changing over time?
* Which products generate the most sales?
* Which products underperform?
* Which categories contribute the most revenue?
* How does product price relate to sales?
* Which channels or marketplaces perform best?
* Where are operational bottlenecks?
* How frequently are orders cancelled?
* Which periods show unusual sales behavior?
* What does the historical data suggest about future sales?

The exact questions and KPIs should be finalized based on the actual fields available in the selected dataset.

---

# 💡 Business Insights

The final project includes a dedicated business-insights report containing approximately **10–15 evidence-based insights**.

Each insight follows:

```text
Observation
     ↓
Evidence
     ↓
Business Implication
     ↓
Recommended Action
```

This ensures the project demonstrates not only technical data skills but also the ability to translate data into business decisions.

---

# 🚧 Limitations

Potential limitations include:

* The dataset is historical rather than a live production data source.
* Forecast quality depends on the available historical observations.
* The forecasting model may not capture external factors affecting sales.
* Some operational analyses depend on whether the relevant fields exist in the source data.
* Incremental loading depends on the availability of an appropriate transaction/date field.
* Dashboard conclusions are limited by the quality and completeness of the source dataset.

The project intentionally documents these limitations instead of overstating model or business conclusions.

---

# 🔮 Future Improvements

Possible future improvements include:

* Automated scheduled ETL runs
* Production-grade orchestration
* Cloud deployment
* More sophisticated forecasting models
* Additional external data sources
* Automated data-quality monitoring
* Real-time or near-real-time ingestion
* More advanced anomaly detection
* Role-based dashboard access
* Automated business reports
* CI/CD for ETL and ML pipelines

These are intentionally outside the initial four-week scope.

---

# 🧠 Key Engineering Principles

This project follows several important principles:

### 1. Reproducibility

The raw data is never manually modified.

```text
Raw Data
   ↓
Code
   ↓
Cleaned Data
```

### 2. Separation of Concerns

Exploration is performed in notebooks, while repeatable ETL and ML logic is implemented in Python modules.

### 3. Validation

Every major transformation should have a validation step.

### 4. Version-Controlled SQL

SQL developed during exploration is ultimately saved into `.sql` files and committed to Git.

### 5. Analytics Before ML

The business analytics platform is completed before forecasting is introduced.

### 6. No Data Leakage

Forecasting uses chronological train/test splits.

### 7. Interview Defensibility

Every major transformation, KPI, query, feature, metric, and architectural decision should be explainable.

These principles are explicitly part of the project's development roadmap.

---

# 🏁 Definition of Done

The project is considered complete when:

* [ ] ETL runs reproducibly from raw data to PostgreSQL
* [ ] Raw files are never manually edited
* [ ] Transformations are documented
* [ ] Validation rules are implemented
* [ ] PostgreSQL tables and relationships are documented
* [ ] SQL answers meaningful business questions
* [ ] Dashboard values reconcile with SQL
* [ ] ML is evaluated on a chronological holdout period
* [ ] Predictions are stored in PostgreSQL
* [ ] Predictions are visualized in the dashboard
* [ ] No secrets are committed to GitHub
* [ ] README explains setup, architecture, usage, and results
* [ ] Every major technical decision can be defended in an interview

These completion criteria follow the project's defined "Definition of Done."

---

# 📚 Interview Preparation

This project is designed to provide strong discussion points for data engineering, data analytics, ML, and SDE interviews.

Be prepared to explain:

1. Why this dataset and business problem were selected
2. How the Extract, Transform, and Load stages work
3. Why notebooks were used for exploration but Python modules for ETL
4. How missing values and duplicates were handled
5. How transformed data was validated
6. Why PostgreSQL was selected
7. The difference between PostgreSQL and pgAdmin
8. Primary and foreign keys
9. How incremental loading would work
10. How the KPIs were defined
11. How ML data leakage was prevented
12. Why the final forecasting model was selected
13. Which evaluation metrics were used and why
14. Forecast limitations
15. Which business decisions the dashboard supports
16. What could be improved with additional development time

These questions directly reflect the project's interview-preparation requirements.

---

# 👨‍💻 Author

**Your Name**

GitHub: `<YOUR_GITHUB_PROFILE>`

LinkedIn: `<YOUR_LINKEDIN_PROFILE>`

---

# ⭐ Project Status

**Status:** In Development

**Duration:** 4 Weeks

**Project Type:** End-to-End Data Analytics + ETL + Machine Learning

**Primary Pipeline:**

```text
Raw CSV
 → Python ETL
 → PostgreSQL
 → SQL Analytics
 → Dashboard
 → ML Forecasting
 → PostgreSQL
 → Dashboard
```

The final goal is a portfolio project that demonstrates the ability to build a complete analytics system rather than an isolated data-science notebook.
