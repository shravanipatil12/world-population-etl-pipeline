# World Population Analytics Dashboard

This document outlines the planned Power BI dashboard for the World Population ETL project.

## Dashboard purpose
The dashboard will visualize the cleaned and loaded world population dataset to help stakeholders understand demographic differences, growth patterns, and urbanization trends across countries.

## KPI cards
1. Total Population
2. Countries Covered
3. Average Median Age
4. Average Fertility Rate

## Visuals
### 1. Top 10 Most Populated Countries
- Chart type: Horizontal bar chart
- Purpose: Compare population totals across the largest countries.

### 2. Population Share by Top 10 Countries
- Chart type: Donut chart
- Purpose: Show the share of the global population represented by the top 10 countries.

### 3. Top 10 Highest Population Density
- Chart type: Bar/column chart
- Purpose: Highlight countries with the highest population density.

### 4. Relationship Between Median Age & Fertility Rate
- Chart type: Scatter plot
- X-axis: Median Age
- Y-axis: Fertility Rate
- Size: Population
- Tooltip: Country
- Purpose: Explore the relationship between demographic age profile and fertility trends.

### 5. Top Countries by Net Migration
- Chart type: Bar chart
- Purpose: Identify countries with the strongest net migration inflows or outflows.

### 6. Population by Continent
- Chart type: Bar/column chart or map-based summary
- Purpose: Compare country totals by region when a continent mapping table is available.

Note: The current dataset does not include a continent column. A continent mapping table can be added in a future enhancement if needed.

## Slicers
- Country
- Population
- Median Age
- Fertility Rate

## Dashboard color palette
- Primary: #1565C0
- Secondary: #26A69A
- Accent: #FB8C00
- Background: #F8F9FA
- Card background: #FFFFFF
- Border: #E5E7EB
- Text: #212121
- Secondary text: #616161

## Planned layout
- Top row: KPI cards
- Middle row: Population rankings and density chart
- Lower row: Fertility vs median age scatter plot and net migration chart
- Side panel: Country, population, median age, and fertility slicers

## Future improvements
- Add continent mapping and regional analysis
- Add historical population trends over time
- Publish the dashboard to Power BI Service
- Add executive commentary and annotations for key findings
