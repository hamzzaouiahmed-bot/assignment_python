from __future__ import annotations

import pandas as pd
import requests

URL = "https://arxiv.org/abs/{arxiv_id}"


def fetch_html(arxiv_id: str) -> str:
    if not arxiv_id:
        return ""
    r = requests.get(URL.format(arxiv_id=arxiv_id), timeout=30)
    r.raise_for_status()
    return r.text


def add_html_column(df: pd.DataFrame) -> pd.DataFrame:
    df2 = df.copy()
    df2["html_content"] = df2.apply(
        lambda row: fetch_html(row["arxiv_id"]),
        axis=1,
    )
    return df2
