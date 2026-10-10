import re
from pathlib import Path

import pandas as pd


EXPECTED_COLUMNS = [
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
]

COLUMN_ALIASES = {
    "rank": {"rank"},
    "country": {"country"},
    "population_2023": {"population2023", "population_2023"},
    "yearly_change": {"yearlychange", "yearly_change", "yearlychangepercent", "yearly_change_percent"},
    "net_change": {"netchange", "net_change"},
    "density": {"density", "densitypkm2", "density_p_km2", "density_p_km_2"},
    "land_area": {"landarea", "land_area", "land_area_km2", "landarea_km2"},
    "migrants": {"migrants", "migrantsnet", "migrants_net"},
    "fertility_rate": {"fertilityrate", "fertility_rate", "fert_rate", "fertilityrate_", "fert_rate_"},
    "median_age": {"medianage", "median_age"},
    "urban_population": {"urbanpop", "urban_population", "urbanpoppercent", "urbanpop_percent", "urban_population_percent"},
    "world_share": {"worldshare", "world_share", "worldsharepercent", "worldshare_percent", "world_share_percent"},
}

NUMERIC_COLUMNS = [
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
]


def normalize_column_name(column_name):
    """Convert CSV headers to a consistent, comparable format."""
    cleaned = str(column_name).strip()
    cleaned = cleaned.replace("%", " percent ")
    cleaned = cleaned.replace("/", "_")
    cleaned = cleaned.replace("-", "_")
    cleaned = cleaned.replace("(", " ")
    cleaned = cleaned.replace(")", " ")
    cleaned = cleaned.replace("²", "2")
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", cleaned)
    cleaned = cleaned.strip("_").lower()
    return cleaned


def standardize_columns(df):
    """Map raw CSV headers to the required canonical names."""
    renamed = {}
    for column in df.columns:
        normalized = normalize_column_name(column)
        matched_name = None

        for canonical_name, aliases in COLUMN_ALIASES.items():
            if normalized in aliases or normalized == canonical_name:
                matched_name = canonical_name
                break

        renamed[column] = matched_name if matched_name else str(column).strip()

    df = df.rename(columns=renamed)
    return df


def clean_numeric_values(series):
    """Convert strings like '12.5%' or '1,234' to numeric values and preserve missing values."""
    cleaned = series.astype(str).str.strip().replace({"nan": None, "NaN": None, "null": None, "None": None})
    cleaned = cleaned.str.replace(",", "", regex=False)
    cleaned = cleaned.str.replace("%", "", regex=False)
    cleaned = cleaned.str.replace("+", "", regex=False)
    return pd.to_numeric(cleaned, errors="coerce")


def transform_data(raw_df, output_path=None):
    """Clean and transform the raw DataFrame and save a processed CSV."""
    if raw_df is None:
        raise ValueError("No raw data was provided for transformation.")

    project_root = Path(__file__).resolve().parents[1]
    output_path = Path(output_path) if output_path else project_root / "data" / "processed" / "clean_world_population.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    original_rows = len(raw_df)
    df = raw_df.copy()
    df = standardize_columns(df)

    missing_columns = [column for column in EXPECTED_COLUMNS if column not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns after standardization: {missing_columns}")

    duplicate_rows_removed = int(df.duplicated().sum())
    df = df.drop_duplicates().reset_index(drop=True)

    df["country"] = df["country"].astype(str).str.strip().replace({"nan": pd.NA, "None": pd.NA})
    df = df.dropna(subset=["country"]).reset_index(drop=True)

    missing_values_before = int(df.isna().sum().sum())

    for column in NUMERIC_COLUMNS:
        if column in df.columns:
            df[column] = clean_numeric_values(df[column])

    missing_values_after = int(df.isna().sum().sum())
    missing_values_handled = max(missing_values_before - missing_values_after, 0)

    final_rows = len(df)
    final_columns = list(df.columns)

    print("Transformation Summary")
    print(f"Original rows: {original_rows}")
    print(f"Duplicate rows removed: {duplicate_rows_removed}")
    print(f"Missing values handled: {missing_values_handled}")
    print(f"Final rows: {final_rows}")
    print(f"Final columns: {final_columns}")

    df.to_csv(output_path, index=False)
    return df


if __name__ == "__main__":
    try:
        import pandas as pd

        project_root = Path(__file__).resolve().parents[1]
        csv_path = project_root / "data" / "raw" / "world_population.csv"
        if not csv_path.exists():
            raise FileNotFoundError(f"Raw CSV not found: {csv_path}")

        df = pd.read_csv(csv_path)
        transform_data(df)
    except Exception as exc:
        print(f"TRANSFORMATION FAILED: {exc}")
