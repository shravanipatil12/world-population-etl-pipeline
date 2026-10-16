# World Population Dashboard

An interactive dashboard built with Streamlit and Plotly. It reads the cleaned dataset produced by the ETL pipeline (`data/processed/clean_world_population.csv`) and lets you explore 2023 population figures for 234 countries and territories.

## What it shows

**Summary numbers:** number of countries and territories, total population, average population, highest population, average median age, average fertility rate, average yearly change, and the number of shrinking countries.

**Charts:**
- Top 10 most populated countries (bar chart)
- Population share of the top 10 (donut chart)
- Top 10 countries by yearly growth (bar chart)
- Fertility rate against median age, sized by population (scatter plot)
- World map coloured by population
- Top 10 countries by population density (bar chart)

**Country explorer:** a sortable table of all matching countries, with a button to download the filtered data as a CSV file.

## Filters

The sidebar lets you:
- search for a country by name
- pick one or more countries
- set a median age range
- show only growing or only shrinking countries

All numbers and charts update to match the filters.

## How to run

From the project folder, with the virtual environment active:

```
pip install streamlit plotly pandas
streamlit run dashboard/app.py
```

The dashboard opens in your browser, usually at `localhost:8501`. It runs on your own computer and is not hosted online.

## Notes

- The map matches countries by name, so a few countries or territories may not appear on it.
- Values that were `N.A.` in the source data are empty in the cleaned file and are left out of averages.

## Credits

Data: *World Population by Country 2023* by Joakim Arvidsson, Kaggle, based on UN Population Division estimates.
