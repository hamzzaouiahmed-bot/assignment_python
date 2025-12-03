from __future__ import annotations

from mongoengine import (
    Document,
    EmbeddedDocument,
    EmbeddedDocumentField,
    StringField,
)


class MongoAuthor(EmbeddedDocument):
    full_name = StringField(required=True)
    title = StringField()


class MongoScientificArticle(Document):
    title = StringField(required=True)
    summary = StringField(required=True)
    file_path = StringField(required=True)
    arxiv_id = StringField(required=True)
    text = StringField(required=True)

    author = EmbeddedDocumentField(MongoAuthor, required=True)

    meta = {
        "collection": "scientific_articles",
        "indexes": [
            {
                "fields": ["$text"],   # <-- text index
                "default_language": "english",
            }
        ],
    }
