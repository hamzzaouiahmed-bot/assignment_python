from mongoengine_users import (
    create_user,
    get_user_by_id,
    get_users_by_city,
    update_user_city,
    increment_user_age,
)
from models_mongoengine import User



for u in User.objects():
    print(u.to_json())


user_id = create_user("Alex2", "alex2@example.com", age=35, city="Sfax")
print("Inserted user with id:", user_id)


user = get_user_by_id(user_id)
if user:
    print(user.to_json())


for u in get_users_by_city("Sfax"):
    print(u.to_json())


updated = update_user_city(user_id, "Monastir")
print("Updated:", updated)
user = get_user_by_id(user_id)
if user:
    print(user.to_json())


incremented = increment_user_age(user_id, 3)
print("Age incremented:", incremented)
user = get_user_by_id(user_id)
if user:
    print(user.to_json())
