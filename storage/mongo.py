import mongoengine as me

def init_mongo() -> None:
    me.connect(
        db="assignment07",
        host="localhost",
        port=27018,
    )
