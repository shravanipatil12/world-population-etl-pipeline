# World Population ETL Pipeline

A small ETL project built with Python, Pandas and MySQL. It takes a raw CSV of 2023 population figures for 234 countries and territories, cleans it, loads it into a MySQL database, and uses SQL to look at population, density, fertility, migration and urbanisation.

Raw CSV → Python / Pandas (extract, transform) → cleaned CSV → MySQL → SQL queries


## What the pipeline does

1. **Extract:** reads the raw CSV into a Pandas DataFrame.
2. **Transform:** cleans the data and saves the result to `data/processed/`.
3. **Load:** writes the cleaned data into a MySQL database.
4. **Analyse:** SQL queries answer questions about the data.

## Dataset

The data is the *World Population by Country 2023* dataset by Joakim Arvidsson on Kaggle, which is based on United Nations Population Division estimates. Kaggle lists its licence as Open Database. The raw file is included in this repository at `data/raw/world_population.csv`.

Columns: rank, country, population, yearly change, net change, density, land area, net migrants, fertility rate, median age, urban population %, world share %.

## Cleaning steps

- Column names are standardised, for example `Fert.Rate` becomes `fertility_rate`.
- Duplicate rows are removed. None were found in this dataset.
- Spaces around country names are trimmed.
- Text values such as `2.70 %` and `1,234` are converted to numbers.
- Values that aren't numbers, such as `N.A.`, are left empty and are not filled in or guessed.

On this dataset, all 234 rows were kept after cleaning.

## Project structure

## Project structure

```
world-population-etl-pipeline/
├── data/
│   ├── raw/world_population.csv
│   └── processed/clean_world_population.csv
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
├── sql/
│   ├── database.sql
│   └── queries.sql
├── .env.example
├── requirements.txt
└── README.md
```

## Tools used

Python, Pandas, SQLAlchemy, PyMySQL, MySQL, SQL.

## Setup

From the project folder:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate the environment with `.venv\Scripts\activate` instead.

### Database settings

Make a copy of `.env.example`, name it `.env`, and fill in your own MySQL details:

```
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=country_pipeline
```

The `.env` file is listed in `.gitignore`, so your password is never uploaded.

## How to run

Create the database first:
mysql -u root -p < sql/database.sql

Then run the full pipeline:
python scripts/main.py

To run only the cleaning step, which doesn't need MySQL:
python scripts/transform.py

To run the SQL analysis after the data is loaded:
mysql -u root -p country_pipeline < sql/queries.sql

To open the dashboard:
streamlit run dashboard/app.py

## SQL analysis

`sql/queries.sql` contains queries on country counts, total population, density, fertility rate, migration, urban population and growth.

## Possible improvements

- Add population data for earlier years
- Add a continent or region column
- Add automated data checks
- Schedule the pipeline to run regularly

## Credits

Dataset: *World Population by Country 2023* by Joakim Arvidsson, Kaggle, based on UN Population Division estimates.
