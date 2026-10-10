import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError


def get_database_url():
    """Create a MySQL connection URL from environment variables."""
    load_dotenv()

    mysql_user = os.getenv("MYSQL_USER")
    mysql_password = os.getenv("MYSQL_PASSWORD")
    mysql_host = os.getenv("MYSQL_HOST")
    mysql_port = os.getenv("MYSQL_PORT")
    mysql_database = os.getenv("MYSQL_DATABASE")

    required_values = {
        "MYSQL_USER": mysql_user,
        "MYSQL_PASSWORD": mysql_password,
        "MYSQL_HOST": mysql_host,
        "MYSQL_PORT": mysql_port,
        "MYSQL_DATABASE": mysql_database,
    }

    missing = [key for key, value in required_values.items() if not value]
    if missing:
        raise ValueError(
            "Missing MySQL environment variables: " + ", ".join(missing)
            + ". Create a .env file using .env.example or export the values in your shell."
        )

    return (
        f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_database}"
        "?charset=utf8mb4"
    )


def load_data(clean_df, processed_csv_path=None, database_name="country_pipeline", table_name="world_population"):
    """Load the cleaned DataFrame into MySQL using DataFrame.to_sql()."""
    if clean_df is None:
        raise ValueError("No cleaned dataframe was provided for loading.")

    project_root = Path(__file__).resolve().parents[1]
    processed_csv_path = Path(processed_csv_path) if processed_csv_path else project_root / "data" / "processed" / "clean_world_population.csv"

    if not processed_csv_path.exists():
        raise FileNotFoundError(f"Processed CSV not found: {processed_csv_path}")

    required_columns = {
        "rank",
        "country",
        "population_2023",
        "yearly_change",
        "net_change",
        "density",
        "land_area",
        "migrants",
        "fertility_rate",
        "median_age",
        "urban_population",
        "world_share",
    }

    missing_columns = sorted(required_columns - set(clean_df.columns))
    if missing_columns:
        raise ValueError(f"Processed data is missing required columns: {missing_columns}")

    try:
        db_url = get_database_url()
        server_url = db_url.rsplit("/", 1)[0]
        server_engine = create_engine(server_url)

        with server_engine.begin() as connection:
            connection.execute(text(f"CREATE DATABASE IF NOT EXISTS `{database_name}`"))

        engine = create_engine(db_url)
        clean_df.to_sql(name=table_name, con=engine, if_exists="replace", index=False)

        rows_loaded = len(clean_df)
        print(f"Rows loaded: {rows_loaded}")
        print(f"Database: {database_name}")
        print(f"Table: {table_name}")
        print("Database load successful.")
        return True

    except ValueError:
        raise
    except FileNotFoundError:
        raise
    except SQLAlchemyError as exc:
        raise RuntimeError(f"Database connection or load failed: {exc}") from exc
    except Exception as exc:
        raise RuntimeError(f"Unexpected load error: {exc}") from exc


if __name__ == "__main__":
    try:
        processed_csv = Path(__file__).resolve().parents[1] / "data" / "processed" / "clean_world_population.csv"
        df = pd.read_csv(processed_csv)
        load_data(df)
    except Exception as exc:
        print(f"LOAD FAILED: {exc}")
