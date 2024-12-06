# serialize

import json

person = {
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

print(person)
print(type(person))

# sonuc = json.dumps(person, ensure_ascii=False) # ascii'dekilerin disinda da karakter kullanimina izin verir.(Tukce karakter gibi...)

# print(sonuc)
# print(type(sonuc))

with open("person.json","w") as file:
    json.dump(person, file, indent=4) # indent, iceri dogru belirtilen sayida bosluk birakir.