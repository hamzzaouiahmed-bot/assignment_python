from __future__ import annotations

import pandas as pd
from sqlalchemy.orm import Session

from models.sql_models import Author, ScientificArticle


def _save_row_to_mariadb(row: pd.Series, session: Session) -> tuple[int, int]:
    author_full_name = str(row["author_full_name"])
    author_title = row.get("author_title")

    author = (
        session.query(Author)
        .filter(Author.full_name == author_full_name)
        .one_or_none()
    )

    if author is None:
        author = Author(
            full_name=author_full_name,
            title=str(author_title) if author_title else None,
        )
        session.add(author)
        session.flush()

    article = ScientificArticle(
        title=str(row["title"]),
        summary=str(row.get("summary")),
        file_path=str(row.get("file_path")),
        arxiv_id=str(row.get("arxiv_id")),
        author=author,
    )
    session.add(article)
    session.flush()

    return author.id, article.id
