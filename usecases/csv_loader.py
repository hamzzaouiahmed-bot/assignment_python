from __future__ import annotations

from pathlib import Path

import pandas as pd

CSV_PATH = Path("data") / "articles.csv"


def load_csv_dataframe() -> pd.DataFrame:
    df = pd.read_csv(CSV_PATH, dtype="string")
    required_columns = [
        "title",
        "summary",
        "file_path",
        "arxiv_id",
        "author_full_name",
        "author_title",
    ]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")
    return df
