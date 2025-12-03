import mongoengine as me


class AuthorEmbedded(me.EmbeddedDocument):
    full_name = me.StringField()
    title = me.StringField()


class ScientificArticleDoc(me.Document):
    mariadb_article_id = me.IntField()
    mariadb_author_id = me.IntField()

    title = me.StringField()
    summary = me.StringField()
    text = me.StringField()
    arxiv_id = me.StringField()

    author = me.EmbeddedDocumentField(AuthorEmbedded)

    meta = {
        "collection": "scientific_articles",
        "indexes": [{"fields": ["$text"]}],
    }
