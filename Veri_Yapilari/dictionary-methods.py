opelOBJ = {
    "marka": "Opel",
    "model": "Corsa",
    "yil": 2020
}

sonuc = opelOBJ["marka"]
sonuc = opelOBJ.get("marka")

# for x in opelOBJ:
#      print(x) # ilk bastakileri yazdirir(marka, model, yil)

# for x in opelOBJ:
#     print(opelOBJ[x]) # ikicileri yazdirir

# for x in opelOBJ.values():
#     print(x) # ikicileri yazdirir

# for x,y in opelOBJ.items():
#     print(x,y) # hepsini alt alta yazdirir

# sonuc = "marka" in opelOBJ # var mi yok mu diye sorar
# sonuc = len(opelOBJ)
# opelOBJ["renk"] = "beyaz" # ekleme yapar
# opelOBJ.pop("renk") # cikarma yapar
# opelOBJ.popitem() # en sondakini cikartir

# del opelOBJ["marka"]
# del opelOBJ
# opelOBJ.clear()

obj = opelOBJ.copy() # Birine yaptigimiz degisiklik digerini etkilemez


obj["marka"] = "Mazda"

opelOBJ.update({
    "marka": "BMW",
    "renk": "kirmizi"
})


# print(sonuc)
print(obj)
print(opelOBJ)