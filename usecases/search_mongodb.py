from __future__ import annotations

from typing import List

from models.mongodb_models import MongoScientificArticle


def search_mongodb(query: str) -> List[MongoScientificArticle]:
    """Search MongoDB using full-text index."""
    results = MongoScientificArticle.objects.search_text(query).all()
    return list(results)
