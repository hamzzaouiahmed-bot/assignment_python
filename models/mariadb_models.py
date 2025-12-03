from __future__ import annotations

from typing import List, Optional

from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""
    pass


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    articles: Mapped[List["ScientificArticle"]] = relationship(
        back_populates="author",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"Author(id={self.id!r}, full_name={self.full_name!r})"


class ScientificArticle(Base):
    __tablename__ = "scientific_articles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String(500), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    file_path: Mapped[str] = mapped_column(String(500), nullable=False)
    arxiv_id: Mapped[str] = mapped_column(String(100), nullable=False)

    author_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("authors.id", ondelete="CASCADE"),
        nullable=False,
    )

    author: Mapped[Author] = relationship(back_populates="articles")

    def __repr__(self) -> str:
        return (
            f"ScientificArticle(id={self.id!r}, title={self.title!r}, "
            f"arxiv_id={self.arxiv_id!r})"
        )
