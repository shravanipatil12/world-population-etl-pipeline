USE country_pipeline;

-- 1. Total number of countries
SELECT COUNT(*) AS total_countries
FROM world_population;

-- 2. Total world population
SELECT SUM(population_2023) AS total_world_population
FROM world_population;

-- 3. Average population
SELECT AVG(population_2023) AS average_population
FROM world_population;

-- 4. Top 10 most populated countries
SELECT country, population_2023
FROM world_population
ORDER BY population_2023 DESC
LIMIT 10;

-- 5. Top 10 highest population density
SELECT country, density
FROM world_population
ORDER BY density DESC
LIMIT 10;

-- 6. Top 10 largest countries by land area
SELECT country, land_area
FROM world_population
ORDER BY land_area DESC
LIMIT 10;

-- 7. Top 10 highest fertility rate
SELECT country, fertility_rate
FROM world_population
ORDER BY fertility_rate DESC
LIMIT 10;

-- 8. Top 10 highest urban population percentage
SELECT country, urban_population
FROM world_population
ORDER BY urban_population DESC
LIMIT 10;

-- 9. Top 10 highest population growth
SELECT country, yearly_change, population_2023
FROM world_population
ORDER BY yearly_change DESC
LIMIT 10;

-- 10. Countries with negative population growth
SELECT country, yearly_change
FROM world_population
WHERE yearly_change < 0
ORDER BY yearly_change ASC;

-- 11. Average median age
SELECT AVG(median_age) AS average_median_age
FROM world_population;

-- 12. Top 10 countries by world population share
SELECT country, world_share
FROM world_population
ORDER BY world_share DESC
LIMIT 10;

-- 13. Top 10 countries by net migration
SELECT country, migrants
FROM world_population
ORDER BY migrants DESC
LIMIT 10;

-- 14. 10 least populated countries
SELECT country, population_2023
FROM world_population
ORDER BY population_2023 ASC
LIMIT 10;

-- 15. Countries with density greater than 500
SELECT country, density
FROM world_population
WHERE density > 500
ORDER BY density DESC;

-- 16. Population statistics: minimum, maximum, average
SELECT
    MIN(population_2023) AS min_population,
    MAX(population_2023) AS max_population,
    AVG(population_2023) AS avg_population
FROM world_population;

-- 17. Average fertility rate
SELECT AVG(fertility_rate) AS average_fertility_rate
FROM world_population;

-- 18. Average urban population percentage
SELECT AVG(urban_population) AS average_urban_population
FROM world_population;

-- 19. Average yearly population change
SELECT AVG(yearly_change) AS average_yearly_change
FROM world_population;

-- 20. A combined demographic analysis
SELECT
    country,
    population_2023,
    density,
    fertility_rate,
    median_age,
    urban_population,
    yearly_change,
    migrants,
    world_share
FROM world_population
ORDER BY population_2023 DESC
LIMIT 20;
