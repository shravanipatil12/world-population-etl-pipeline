# World Population ETL & Analytics Pipeline

## 1. Project Overview
This project builds an end-to-end data pipeline for a world population dataset. It covers extraction from a raw CSV file, data cleaning and transformation with Python and Pandas, validation of output quality, load into a MySQL database, and SQL-based analysis for business and demographic insights.

## 2. Objective
The objective of this portfolio project is to demonstrate practical Data Engineering and Data Analytics skills using a realistic CSV-based ETL workflow. The project is designed to be easy to explain in interviews and suitable for GitHub, LinkedIn, and resume work.

## 3. Architecture
CSV
 ↓
Python / Pandas
 ↓
Extract
 ↓
Transform
 ↓
Processed Data
 ↓
MySQL
 ↓
SQL Analytics
 ↓
Power BI

## 4. Dataset
The project uses a World Population 2023 dataset stored in the file:

- data/raw/world_population.csv

The file should include the following columns:
- Rank
- Country
- Population2023
- YearlyChange
- NetChange
- Density(P/Km²)
- Land Area(Km²)
- Migrants(net)
- Fert.Rate
- MedianAge
- UrbanPop%
- WorldShare

The ETL scripts are designed to handle minor header formatting differences while keeping the expected column names consistent.

## 5. Technologies Used
- Python
- Pandas
- NumPy
- SQLAlchemy
- PyMySQL
- MySQL
- SQL
- Power BI
- Git / GitHub

## 6. ETL Workflow
1. Extract the raw CSV file into a Pandas DataFrame.
2. Validate the CSV exists and inspect the file metadata.
3. Clean and transform the dataset.
4. Save the processed result to the processed data folder.
5. Load the processed data into MySQL.
6. Run SQL analytical queries.
7. Use the output for reporting and dashboarding in Power BI.

## 7. Data Preprocessing
The transformation stage performs the following tasks:
- Remove duplicate rows
- Standardize column names
- Strip percentage symbols from relevant columns
- Convert numeric values using safe numeric conversion
- Preserve missing values instead of silently changing the data
- Write the cleaned dataset to the processed folder

## 8. MySQL Database
The database used in this project is:
- country_pipeline

The table used for loading is:
- world_population

A database script is provided at:
- sql/database.sql

## 9. SQL Analysis
The project includes a SQL script with analytical queries for:
- country counts
- total population
- population density
- fertility rate
- migration metrics
- urban population
- growth analysis
- demographic summaries

The queries are stored in:
- sql/queries.sql

## 10. Power BI Dashboard
The dashboard documentation is available in:
- dashboard/README.md

The dashboard is planned to include KPI cards, ranking visuals, demographic scatter plots, migration analysis, and slicers for interactive filtering.

## 11. Key Insights
This project is designed to surface insights such as:
- highest population countries
- population share concentration
- growth and decline patterns
- urbanization trends
- migration trends
- demographic differences by country

## 12. Project Structure
world-population-etl/
├── data/
│   ├── raw/
│   │   └── world_population.csv
│   └── processed/
│       └── clean_world_population.csv
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
├── sql/
│   ├── database.sql
│   └── queries.sql
├── dashboard/
│   └── README.md
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md

## 13. Installation
From the project root, run:

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

On Windows:

.venv\Scripts\activate
pip install -r requirements.txt

## 14. Configuration
Before loading data into MySQL, create a .env file based on .env.example.

Example:

MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=country_pipeline

Do not commit the real .env file to Git. It is intentionally excluded by .gitignore.

## 15. How to Run
From the project root:

python scripts/main.py

## 16. Example SQL Analysis
After creating the database and loading the data:

mysql -u root -p < sql/database.sql

Then run:

mysql -u root -p country_pipeline < sql/queries.sql

## 17. Future Improvements
- Add historical population data by year
- Add continent or region mapping
- Add automated validation tests
- Add a scheduled ETL pipeline
- Publish the Power BI dashboard to the cloud

## 18. Important Notes
- The project does not use an API; it uses a CSV source.
- No fake or invented data is included in this project.
- A template CSV is provided in the raw folder so the project structure is complete and the ETL code can be validated without introducing fabricated records.
- If MySQL credentials are not configured, the pipeline will stop cleanly after transformation and explain the missing configuration.

## 19. Project Execution Commands
Create virtual environment:

python3 -m venv .venv

Activate on macOS/Linux:

source .venv/bin/activate

Windows:

.venv\Scripts\activate

Install:

pip install -r requirements.txt

Run:

python scripts/main.py

SQL database setup:

mysql -u root -p < sql/database.sql

Then execute:

mysql -u root -p country_pipeline < sql/queries.sql
