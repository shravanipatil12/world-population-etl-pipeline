# 🌍 World Population ETL Pipeline & Analytics Dashboard

An end-to-end data engineering and analytics project that processes 2023 population data for 234 countries and territories. Built using Python, Pandas, MySQL, SQL, and Streamlit, this project combines data extraction, transformation, database loading, SQL analysis, and interactive visualization.

## Live Dashboard

### [🌐 View the Interactive World Population Analytics Dashboard](https://shravanipatil12-world-population-etl-pipeli-dashboardapp-mtjok6.streamlit.app)

Explore population statistics, compare countries, and interact with demographic visualizations through the deployed Streamlit dashboard.

## Dashboard Preview

![World Population Analytics Dashboard](dashboard/dashboard.png)

## 🎯 Project Objectives

- Build an end-to-end ETL pipeline using real-world population data.
- Clean and standardize raw data using Python and Pandas.
- Store structured population data in MySQL.
- Perform SQL-based analysis of population and demographic indicators.
- Present population insights through an interactive Streamlit dashboard.

## 🔄 ETL Workflow

**Raw CSV → Extract → Transform → Cleaned CSV → MySQL → SQL Analysis → Interactive Dashboard**

1. **Extract:** Read the raw population dataset into a Pandas DataFrame.
2. **Transform:** Standardize column names, clean text values, convert numeric fields, and preserve missing values appropriately.
3. **Load:** Load the cleaned dataset into a MySQL database.
4. **Analyse:** Execute SQL queries to explore population, density, fertility, migration, urbanization, and population growth.
5. **Visualize:** Explore country-level statistics through the interactive dashboard.

## 📁 Project Structure

```text
world-population-etl-pipeline/
├── dashboard/
│   ├── app.py
│   └── dashboard.png
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
├── .devcontainer/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 🗃️ Dataset

The project uses the *World Population by Country 2023* dataset attributed to Joakim Arvidsson on Kaggle, based on United Nations Population Division estimates.

- **Coverage:** 234 countries and territories
- **Reference year:** 2023
- **Raw data:** `data/raw/world_population.csv`
- **Cleaned data:** `data/processed/clean_world_population.csv`

### Key Attributes

- Country and rank
- Population in 2023
- Yearly population change and net change
- Population density and land area
- Net migrants
- Fertility rate and median age
- Urban population percentage
- World population share

## Data Cleaning and Transformation

The transformation process includes:

- Standardizing column names, such as `Fert.Rate` to `fertility_rate`.
- Removing duplicate rows.
- Trimming whitespace from country names.
- Converting comma-separated numeric values and percentage strings into numeric values.
- Preserving unavailable values such as `N.A.` as missing rather than inventing data.

All 234 records were retained after cleaning.

## 📈 Dashboard Features

The Streamlit dashboard provides interactive country-level population analysis, including:

- **Population overview:** country count, total population, average median age, fertility rate, and growth indicators.
- **Country filters:** search and select countries for focused comparisons.
- **Population ranking:** compare the most populated countries.
- **Population share:** explore the relative contribution of selected countries.
- **Growth analysis:** compare yearly population change.
- **Fertility vs. median age:** explore demographic relationships.
- **World population map:** visualize population distribution geographically.
- **Population density:** compare countries by people per square kilometer.
- **Country explorer:** inspect filtered data and download the results as CSV.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | ETL and data processing |
| Pandas | Data cleaning and transformation |
| MySQL | Relational data storage |
| SQL | Data analysis and querying |
| SQLAlchemy | Database integration |
| PyMySQL | MySQL connectivity |
| Streamlit | Interactive dashboard |
| Plotly | Interactive charts and visualizations |
| Git and GitHub | Version control and project hosting |

## ⚙️ Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/shravanipatil12/world-population-etl-pipeline.git
cd world-population-etl-pipeline
```

### 2. Create and activate a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🗄️ MySQL Configuration

To run the database-loading and SQL-analysis stages, install and start MySQL.

Create a `.env` file using `.env.example` as a template and configure your database credentials:

```env
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=country_pipeline
```

**Security:** Never commit your `.env` file or real database credentials. The file should remain excluded through `.gitignore`.

## ▶️ Running the Project

### Run the complete ETL pipeline

Create the database:

```bash
mysql -u root -p < sql/database.sql
```

Run the pipeline:

```bash
python3 scripts/main.py
```

### Run only the transformation step

This step does not require MySQL:

```bash
python3 scripts/transform.py
```

### Run SQL analysis

After loading the data into MySQL:

```bash
mysql -u root -p country_pipeline < sql/queries.sql
```

### Run the dashboard locally

```bash
streamlit run dashboard/app.py
```

You can also access the deployed dashboard using the live link at the top of this README.

## 🔍 SQL Analysis

The SQL queries explore:

- Country and territory counts
- Total population
- Population density
- Fertility rates
- Net migration
- Urban population
- Population growth

## 🔮 Future Enhancements

- Add historical population data to analyze trends across multiple years.
- Include continent and regional classifications.
- Implement automated data-quality checks and validation.
- Add unit tests for ETL transformations.
- Automate pipeline execution and scheduled refreshes.
- Expand dashboard filters and demographic comparisons.

## 📚 Credits

**Dataset:** *World Population by Country 2023*, attributed to Joakim Arvidsson on Kaggle and based on United Nations Population Division estimates.

This project was developed for data engineering, SQL analytics, and interactive data visualization practice.
