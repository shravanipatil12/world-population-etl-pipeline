from pathlib import Path

from extract import extract_data
from load import load_data
from transform import transform_data


def main():
    """Run the ETL pipeline: extract -> transform -> load."""
    project_root = Path(__file__).resolve().parents[1]
    raw_csv_path = project_root / "data" / "raw" / "world_population.csv"
    processed_csv_path = project_root / "data" / "processed" / "clean_world_population.csv"

    try:
        print("[1/3] EXTRACT")
        raw_df = extract_data(raw_csv_path)

        print("[2/3] TRANSFORM")
        clean_df = transform_data(raw_df, output_path=processed_csv_path)

        print("[3/3] LOAD")
        load_data(clean_df, processed_csv_path=processed_csv_path)

        print("ETL PIPELINE COMPLETED SUCCESSFULLY")
        return 0

    except FileNotFoundError as exc:
        print(f"ERROR: {exc}")
        print("Ensure the raw data file exists at data/raw/world_population.csv before running the pipeline.")
        return 1
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1
    except RuntimeError as exc:
        print(f"ERROR: {exc}")
        return 1
    except Exception as exc:
        print(f"UNEXPECTED ERROR: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
