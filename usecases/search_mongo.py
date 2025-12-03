from __future__ import annotations

from models.mongo_models import ScientificArticleDoc


def search_scientific_articles(q: str):
    return list(ScientificArticleDoc.objects.search_text(q).limit(20))
