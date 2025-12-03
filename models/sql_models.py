from __future__ import annotations

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(255))
    title: Mapped[str | None] = mapped_column(String(255))

    articles = relationship("ScientificArticle", back_populates="author")


class ScientificArticle(Base):
    __tablename__ = "scientific_articles"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(500))
    summary: Mapped[str | None] = mapped_column(String(2000))
    file_path: Mapped[str | None] = mapped_column(String(500))
    arxiv_id: Mapped[str | None] = mapped_column(String(100))

    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author = relationship("Author", back_populates="articles")
