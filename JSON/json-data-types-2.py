data = {
    "emresarac":{
        "firstName": "Emre",
        "lastName": "Sarac"   
    },
    "mustafasarac":{
        "firstName": "Mustafa",
        "lastName": "Sarac"
    }
}
import json
with open("users2.json", "w") as file:
    json.dump(data, file, indent=4)

with open("users2.json") as file:
    users = json.load(file)

# print(users["emresarac"])
# print(users["emresarac"]["firstName"])

users.update({
    "elifsarac": {
        "firstName": "Elif",
        "lastName": "Sarac"
    }
})

users.pop("emresarac")

with open("users2.json", "w") as file:
    json.dump(users, file, indent=4)