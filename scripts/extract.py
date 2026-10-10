from pathlib import Path

import pandas as pd


def extract_data(csv_path=None):
    """Read and validate the raw world population CSV."""
    project_root = Path(__file__).resolve().parents[1]
    csv_path = Path(csv_path) if csv_path else project_root / "data" / "raw" / "world_population.csv"

    try:
        if not csv_path.exists():
            raise FileNotFoundError(f"Raw CSV not found: {csv_path}")

        df = pd.read_csv(csv_path)
        print(f"Rows: {len(df)}")
        print(f"Columns: {len(df.columns)}")
        print("Column names:")
        for column in df.columns:
            print(f" - {column}")
        return df

    except FileNotFoundError:
        raise
    except pd.errors.EmptyDataError as exc:
        raise ValueError(f"CSV is empty or missing headers: {csv_path}") from exc
    except Exception as exc:
        raise RuntimeError(f"Error reading raw CSV: {exc}") from exc


if __name__ == "__main__":
    try:
        extract_data()
    except Exception as exc:
        print(f"EXTRACTION FAILED: {exc}")
