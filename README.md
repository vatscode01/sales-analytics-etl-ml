Sales Analytics ETL + Machine Learning Platform

An end-to-end Sales Analytics, ETL, Business Intelligence, and Machine Learning platform built with Python, PostgreSQL, SQL, and Scikit-learn.

The project transforms raw e-commerce sales data into a reproducible analytics pipeline, generates business KPIs and SQL insights, provides an interactive dashboard, and extends the platform with sales forecasting.

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
ML Forecasting

🎯 Objectives

The project focuses on building a complete, reproducible analytics system rather than an isolated notebook.

Key objectives:

Build a reproducible Python ETL pipeline
Clean and validate raw sales data
Design and populate a PostgreSQL database
Perform intermediate-to-advanced SQL analytics
Create reusable analytical views and KPIs
Build an interactive business dashboard
Develop and evaluate a sales forecasting model
Store predictions in PostgreSQL
Integrate forecasts into the dashboard
🏗️ Architecture

                    ┌──────────────┐
                    │   Raw CSVs   │
                    └──────┬───────┘
                           ↓
                    ┌──────────────┐
                    │  Python ETL  │
                    └──────┬───────┘
                           ↓
                    ┌──────────────┐
                    │  PostgreSQL  │
                    └──────┬───────┘
                           ↓
                 ┌─────────┴─────────┐
                 ↓                   ↓
          ┌─────────────┐     ┌─────────────┐
          │ SQL / KPIs  │     │ ML Forecast │
          └──────┬──────┘     └──────┬──────┘
                 └─────────┬──────────┘
                           ↓
                    ┌──────────────┐
                    │  Dashboard   │
                    └──────────────┘

🛠️ Tech Stack
Area	Technology
Programming	Python
Data Processing	Pandas, NumPy
Database	PostgreSQL
SQL	PostgreSQL SQL
Visualization	Dashboarding tool
Machine Learning	Scikit-learn
Model Persistence	Joblib
Exploration	Jupyter
Version Control	Git + GitHub
🔄 ETL Pipeline

The ETL process follows:

Extract → Transform → Validate → Load

Extract

Reads the original CSV files from data/raw/ without modifying them.

Transform

Cleans and standardizes the data, including:

Column names and data types
Missing values
Duplicates
Dates
Categorical and numeric fields

Cleaned datasets are saved under data/cleaned/.

Load

Loads the processed data into PostgreSQL and validates:

Row counts
Key uniqueness
NULL values
Table relationships

The main pipeline is executed through:

python etl/main.py

🗄️ PostgreSQL & SQL Analytics

PostgreSQL acts as the central analytical database.

SQL analysis includes:

Joins and aggregations
CTEs
CASE expressions
Subqueries
Conditional aggregation
Date analysis
Window functions
Running totals
Moving averages
Month-over-month analysis
Top-N analysis

Reusable analytical views are also created for dashboard consumption.

📊 Business KPIs

Depending on the available dataset fields, the project analyzes metrics such as:

Revenue
Units sold
Average order value
Profit / margin
Cancellation rate
Monthly growth
Category contribution
Product performance

Dashboard metrics are reconciled against SQL calculations.

📈 Dashboard

The interactive dashboard focuses on business decision-making and includes areas such as:

Executive KPIs
Sales trends
Product performance
Category analysis
Operational/channel analysis
Interactive filtering
Historical vs forecasted sales
🤖 Machine Learning Forecasting

The ML component extends the analytics platform with time-series sales forecasting.

Feature engineering may include:

Lag features
Rolling averages
Rolling sums
Calendar features

Models are evaluated using a chronological train/test split to prevent future-data leakage.

Evaluation metrics include:

MAE
RMSE
R² where appropriate

The ML workflow is separated into:

```text
Feature Engineering
        ↓
Model Training
        ↓
Prediction
        ↓
PostgreSQL
        ↓
Dashboard


ML modules:

ml/
├── feature_engineering.py
├── train_model.py
└── predict.py

📁 Project Structure
sales-analytics-etl-ml/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── etl/
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
├── dashboard/
├── reports/
├── images/
├── logs/
│
├── requirements.txt
├── .gitignore
└── README.md

```
⚙️ Installation
1. Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd sales-analytics-etl-ml

2. Create a virtual environment
python -m venv venv


Activate it:

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Configure PostgreSQL

Create the database:

CREATE DATABASE sales_db;


Configure the local PostgreSQL connection and never commit credentials or secrets to GitHub.

▶️ Running the Project

Place the source CSV files in:

data/raw/


Run the ETL pipeline:

python etl/main.py


Run ML components as implemented:

python ml/feature_engineering.py
python ml/train_model.py
python ml/predict.py


Launch the dashboard using the implementation inside dashboard/.

💡 Business Questions

The platform is designed to answer questions such as:

How are sales changing over time?
Which products and categories perform best?
Which products underperform?
Which channels perform best?
Where are operational bottlenecks?
How frequently are orders cancelled?
What trends can be identified in historical sales?
What does the data suggest about future sales?
🧠 Engineering Principles

The project emphasizes:

Reproducibility — raw data is never manually edited
Separation of concerns — notebooks for exploration, modules for production logic
Validation — transformations and database loads are checked
Analytics before ML — forecasting extends the analytics platform
No data leakage — forecasting uses chronological validation
Interview defensibility — technical and business decisions should be explainable
📌 Expected Outcomes

The completed project will demonstrate:

Python and Pandas
ETL development
PostgreSQL
Intermediate-to-advanced SQL
Data validation
Business intelligence
Dashboard development
Feature engineering
Machine learning
Time-series forecasting
Model evaluation
End-to-end data pipeline design
🚧 Limitations
The dataset is historical rather than live production data.
Forecast quality depends on the available historical observations.
External factors affecting sales may not be represented.
Some analyses depend on fields available in the source dataset.
Incremental loading depends on suitable transaction/date fields.
🔮 Future Improvements

Potential extensions include:

Scheduled ETL
Workflow orchestration
Cloud deployment
Advanced forecasting models
Automated data-quality monitoring
External data integration
Anomaly detection
Automated business reporting
CI/CD
👨‍💻 Author

Ayush Vats

GitHub: https://github.com/vatscode01

LinkedIn: https://www.linkedin.com/in/ayushvats952/

⭐ Project Status

Status: In Development
Duration: 4 Weeks
Type: End-to-End Data Analytics + ETL + Machine Learning

Raw CSV
 → Python ETL
 → PostgreSQL
 → SQL Analytics
 → Dashboard
 → ML Forecasting
 → PostgreSQL
 → Dashboard


The goal is to demonstrate the ability to build a complete, reproducible analytics platform from raw data to business insights and forecasting.
