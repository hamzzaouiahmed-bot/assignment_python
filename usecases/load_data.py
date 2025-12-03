from __future__ import annotations

from pathlib import Path
from typing import Final

import pandas as pd

DATA_DIR: Final[Path] = Path("data")
CSV_PATH: Final[Path] = DATA_DIR / "articles.csv"


def load_csv_to_dataframe() -> pd.DataFrame:

    df = pd.read_csv(CSV_PATH, dtype="string")
 
    required_columns = [
        "title",
        "summary",
        "file_path",
        "arxiv_id",
        "author_full_name",
        "author_title",
    ]
    missing = set(required_columns) - set(df.columns)
    if missing:
        msg = f"Missing columns in CSV: {missing}"
        raise ValueError(msg)
    return df
