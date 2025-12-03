from pymongo_users import (
    create_user,
    get_user_by_id,
    get_users_by_city,
    update_user_city,
    increment_user_age,
)
from pymongo_users import get_users_collection



print("Existing users")
for u in get_users_collection().find():
    print(u)


user_id = create_user("Ahmed2", "ahmed2@example.com", age=30, city="Sfax")
print("Inserted user with _id:", user_id)


user = get_user_by_id(user_id)
print(user)


for u in get_users_by_city("Sfax"):
    print(u)


updated = update_user_city(user_id, "Monastir")
print("Updated:", updated)
print(get_user_by_id(user_id))


incremented = increment_user_age(user_id, 2)
print("Age incremented:", incremented)
print(get_user_by_id(user_id))
