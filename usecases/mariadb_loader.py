from __future__ import annotations

import pandas as pd
from sqlalchemy.orm import Session

from storage.sql import get_session
from .load_to_mariadb import _save_row_to_mariadb


def load_dataframe_to_mariadb(df: pd.DataFrame) -> pd.DataFrame:
    with get_session() as session:
        ids = df.apply(
            lambda row: _apply_wrapper(row, session),
            axis=1,
            result_type="expand",
        )
        ids.columns = ["author_id", "article_id"]

    df_out = df.copy()
    df_out["author_id"] = ids["author_id"].astype("int64")
    df_out["article_id"] = ids["article_id"].astype("int64")
    return df_out


def _apply_wrapper(row: pd.Series, session: Session) -> tuple[int, int]:
    return _save_row_to_mariadb(row, session)
