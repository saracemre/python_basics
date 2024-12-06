db = {
    "users": {
        "emresarac": {
            "firstName": "Emre",
            "lastName": "Sarac"
        },
        "mustafasarac": {
            "firstName": "Mustafa",
            "lastName": "Sarac"
        }
    },
    "products": {
        "1": {
            "productName": "IPhone 13",
            "price": "20000"
        },
        "2": {
            "productName": "IPhone 13 Pro",
            "price": "28000"
        }
    }
}

import json

# with open("db.json", "w") as file:
#     json.dump(db, file, ensure_ascii=False, indent=4)

with open("db.json") as file:
    db = json.load(file)

# print(db["users"]["mustafasarac"]["firstName"])
# print(db["products"]["1"]["price"])

db["products"].update({
    "3": {
            "productName": "IPhone 13 Pro Max",
            "price": "38000"
        }
})

with open("db.json", "w") as file:
    json.dump(db, file, ensure_ascii=False, indent=4)
