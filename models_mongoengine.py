from mongoengine import (
    connect,
    Document,
    EmbeddedDocument,
    StringField,
    IntField,
    EmbeddedDocumentField,
    EmailField,
    ValidationError,
)



connect(
    db="AhmedDB",
    host="localhost",
    port=27017,
    username="Ahmed",
    password="ahmed123",
)


class Profile(EmbeddedDocument):
    age = IntField(min_value=0, required=True)
    city = StringField(required=True, max_length=100)


class User(Document):
    name = StringField(required=True, max_length=100)
    email = EmailField(required=True, unique=True)
    profile = EmbeddedDocumentField(Profile, required=True)

    meta = {"collection": "users"}
