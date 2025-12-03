from typing import Optional, List, Dict, Any
from pymongo import MongoClient
from bson import ObjectId


def get_client() -> MongoClient:
    return MongoClient("mongodb://Ahmed:ahmed123@localhost:27017/")


def get_users_collection():
    client = get_client()
    db = client["AhmedDB"]
    return db["users"]


def create_user(name: str, email: str, age: int, city: str) -> str:

    users = get_users_collection()
    user_doc = {
        "name": name,
        "email": email,
        "profile": {
            "age": age,
            "city": city
        }
    }
    result = users.insert_one(user_doc)
    return str(result.inserted_id)


def get_user_by_id(user_id: str) -> Optional[Dict[str, Any]]:

    users = get_users_collection()
    try:
        oid = ObjectId(user_id)
    except Exception:
        return None

    return users.find_one({"_id": oid})


def get_users_by_city(city: str) -> List[Dict[str, Any]]:

    users = get_users_collection()
    return list(users.find({"profile.city": city}))


def update_user_city(user_id: str, new_city: str) -> bool:

    users = get_users_collection()
    try:
        oid = ObjectId(user_id)
    except Exception:
        return False

    result = users.update_one({"_id": oid}, {"$set": {"profile.city": new_city}})
    return result.modified_count == 1


def increment_user_age(user_id: str, years: int = 1) -> bool:

    users = get_users_collection()
    try:
        oid = ObjectId(user_id)
    except Exception:
        return False

    result = users.update_one({"_id": oid}, {"$inc": {"profile.age": years}})
    return result.modified_count == 1
