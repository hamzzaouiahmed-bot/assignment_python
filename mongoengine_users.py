from typing import Optional, List
from mongoengine import DoesNotExist, ValidationError
from models_mongoengine import User, Profile


def create_user(name: str, email: str, age: int, city: str) -> Optional[str]:

    try:
        profile = Profile(age=age, city=city)
        user = User(name=name, email=email, profile=profile)
        user.save()
        return str(user.id)
    except ValidationError as e:
        print("Validation error while creating user:", e)
        return None
    except Exception as e:
        print("Unexpected error:", e)
        return None


def get_user_by_id(user_id: str) -> Optional[User]:
    try:
        return User.objects.get(id=user_id)
    except (DoesNotExist, ValidationError):
        return None


def get_users_by_city(city: str) -> List[User]:
    return list(User.objects(profile__city=city))


def update_user_city(user_id: str, new_city: str) -> bool:
    try:
        user = User.objects.get(id=user_id)
        user.profile.city = new_city
        user.save()
        return True
    except (DoesNotExist, ValidationError) as e:
        print("Error while updating city:", e)
        return False


def increment_user_age(user_id: str, years: int = 1) -> bool:
    try:
        user = User.objects.get(id=user_id)
        user.profile.age += years
        user.save()
        return True
    except (DoesNotExist, ValidationError) as e:
        print("Error while incrementing age:", e)
        return False
