from __future__ import annotations

import os
from typing import List

from sqlalchemy.orm import joinedload

from models.mariadb_models import ScientificArticle
from models.mongodb_models import MongoAuthor, MongoScientificArticle
from storage.mariadb import get_session


def pdf_to_markdown_text(pdf_path: str) -> str:
    """Convert PDF to Markdown text.

    For now, just read file content as plain text (simple version).
    """
    if not os.path.exists(pdf_path):
        msg = f"PDF file not found: {pdf_path}"
        raise FileNotFoundError(msg)

    try:
        with open(pdf_path, "rb") as f:
            content = f.read().decode(errors="ignore")
    except Exception:
        # fallback if pdf is binary
        content = "[PDF content not readable as text]"

    return content


def transfer_mariadb_to_mongodb() -> None:
    """Transfer articles + authors from MariaDB to MongoDB."""
    with get_session() as session:

        articles: List[ScientificArticle] = (
            session.query(ScientificArticle)
            .options(joinedload(ScientificArticle.author))
            .all()
        )

        for article in articles:
            pdf_path = os.path.join("papers", article.file_path)

            markdown_text = pdf_to_markdown_text(pdf_path)

            mongo_article = MongoScientificArticle(
                title=article.title,
                summary=article.summary,
                arxiv_id=article.arxiv_id,
                file_path=article.file_path,
                text=markdown_text,
                author=MongoAuthor(
                    full_name=article.author.full_name,
                    title=article.author.title,
                ),
            )

            mongo_article.save()

    print("Done transferring data to MongoDB.")
