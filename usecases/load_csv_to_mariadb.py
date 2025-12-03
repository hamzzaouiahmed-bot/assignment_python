from __future__ import annotations

import csv
from pathlib import Path
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.mariadb_models import Author, ScientificArticle
from storage.mariadb import get_session

DATA_DIR = Path("data")
CSV_PATH = DATA_DIR / "articles.csv"


def _get_or_create_author(
    session: Session,
    full_name: str,
    title: Optional[str],
) -> Author:
    stmt = select(Author).where(
        Author.full_name == full_name,
        Author.title == title,
    )
    author: Optional[Author] = session.scalar(stmt)

    if author is None:
        author = Author(full_name=full_name, title=title)
        session.add(author)
        session.flush() 
    return author


def load_csv_to_mariadb() -> None:
  
    if not CSV_PATH.exists():
        msg = f"CSV file not found: {CSV_PATH}"
        raise FileNotFoundError(msg)

    with get_session() as session:
        with open(CSV_PATH, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                title = row["title"].strip()
                summary = row["summary"].strip()
                file_path = row["file_path"].strip()
                arxiv_id = row["arxiv_id"].strip()
                author_full_name = row["author_full_name"].strip()
                author_title = row.get("author_title", "").strip() or None

                author = _get_or_create_author(
                    session=session,
                    full_name=author_full_name,
                    title=author_title,
                )

                article = ScientificArticle(
                    title=title,
                    summary=summary,
                    file_path=file_path,
                    arxiv_id=arxiv_id,
                    author=author,
                )
                session.add(article)

            session.commit()
