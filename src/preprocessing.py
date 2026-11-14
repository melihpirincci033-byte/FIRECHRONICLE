
import pandas as pd
from pathlib import Path

REQUIRED_COLUMNS = [
    "latitude",
    "longitude",
    "acq_date",
    "acq_time",
    "satellite",
    "instrument",
    "frp"
]

def inspect_firms_file(file_path):
    """Inspect a NASA FIRMS CSV without loading the full file."""

    file_path = Path(file_path)
    sample = pd.read_csv(file_path, nrows=100)

    missing = [
        col for col in REQUIRED_COLUMNS
        if col not in sample.columns
    ]

    if missing:
        raise ValueError(
            f"Missing columns: {missing}"
        )

    return {
        "filename": file_path.name,
        "columns": sample.columns.tolist(),
        "satellites": sample["satellite"].unique().tolist(),
        "instruments": sample["instrument"].unique().tolist()
    }


def clean_firms_chunk(chunk):
    """Perform basic quality checks without altering source data."""

    df = chunk.copy()

    for col in ["latitude", "longitude", "frp"]:
        df[col] = pd.to_numeric(
            df[col], errors="coerce"
        )

    valid = (
        df["latitude"].between(-90, 90)
        & df["longitude"].between(-180, 180)
        & df["frp"].notna()
        & df["frp"].ge(0)
    )

    return df.loc[valid].copy()
