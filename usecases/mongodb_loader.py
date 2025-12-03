from __future__ import annotations

import pandas as pd
from bs4 import BeautifulSoup

from models.mongo_models import ScientificArticleDoc, AuthorEmbedded


def extract_text(html: str) -> str:
    return BeautifulSoup(html, "html.parser").get_text(" ", strip=True)


def _save_row_to_mongodb(row: pd.Series) -> str:
    txt = extract_text(row["html_content"]) if row["html_content"] else ""

    author = AuthorEmbedded(
        full_name=str(row["author_full_name"]),
        title=str(row["author_title"]),
    )

    doc = ScientificArticleDoc(
        mariadb_article_id=int(row["article_id"]),
        mariadb_author_id=int(row["author_id"]),
        title=str(row["title"]),
        summary=str(row["summary"]),
        text=txt,
        arxiv_id=str(row["arxiv_id"]),
        author=author,
    )
    doc.save()
    return str(doc.id)


def load_dataframe_to_mongodb(df: pd.DataFrame) -> pd.DataFrame:
    ids = df.apply(_save_row_to_mongodb, axis=1)
    df2 = df.copy()
    df2["mongodb_id"] = ids.astype("string")
    return df2
