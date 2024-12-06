# deserialize

import json

# with open("person.json") as file:
#     data = json.load(file)

data = """
    {
        "firstName":"Mustafa",
        "lastName":"Sarac",
        "hobbies":["yazilim","dizi"],
        "age":37,
        "children":[
            {
                "firstName":"Emre",
                "age":18
            },
            {
                "firstName":"Beyza",
                "age":23
            }
        ]
    }
    """
data = json.loads(data)

print(data)
print(type(data))
print(data["firstName"])
print(data["hobbies"])
print(data["hobbies"][0])
