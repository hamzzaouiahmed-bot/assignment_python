from mongoengine import connect


def init_mongodb(host: str = "localhost", port: int = 27018, db_name: str = "assignment07") -> None:
    """
    Initialize MongoDB connection using mongoengine.
    Default port = 27018 because Docker uses 27018:27017
    """
    connect(
        db=db_name,
        host=host,
        port=port,
    )
