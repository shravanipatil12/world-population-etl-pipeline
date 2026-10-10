CREATE DATABASE IF NOT EXISTS country_pipeline;
USE country_pipeline;

-- Optional table definition for reference/documentation.
-- The Python ETL process uses DataFrame.to_sql() to create or replace the table.
CREATE TABLE IF NOT EXISTS world_population (
    rank INT,
    country VARCHAR(255) NOT NULL,
    population_2023 BIGINT,
    yearly_change DECIMAL(10,4),
    net_change INT,
    density DECIMAL(10,2),
    land_area BIGINT,
    migrants INT,
    fertility_rate DECIMAL(10,2),
    median_age DECIMAL(10,2),
    urban_population DECIMAL(10,2),
    world_share DECIMAL(10,4)
);
