data = [
    {
        "userName": "emresarac",
        "firstName": "Emre",
        "lastName": "Sarac"
    },
    {
        "userName": "mustafasarac",
        "firstName": "Mustafa",
        "lastName": "Sarac"
    }

]

import json



user = {
        "userName": "elifsarac",
        "firstName": "Elif",
        "lastName": "Sarac"
    }

with open("users.json", "r") as file:
    users = json.load(file)

for user in users:
    if user["userName"] == "emresarac":
        user["userName"] = "emre_sarac"

# users.remove(users[0])

# users.append(user)

with open("users.json", "w") as file:
    json.dump(users, file, ensure_ascii=False, indent=2)