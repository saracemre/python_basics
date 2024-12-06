Diller = ["Python","C#","Java","Javascript","React"]

sonuc = Diller
sonuc = type(Diller)
sonuc = Diller[0:2]
sonuc = Diller[2:]
sonuc = Diller[:3]
sonuc = Diller[-1]
sonuc = Diller[-4:-1]
# Diller[0] = "Html"
Diller[-1] = "Html"
sonuc = len(Diller)
sonuc = Diller + ["Angular", "Vuejs"]

# if blogu=> Kosul ifadeleri
if "Python" in Diller:
    print("deger listenin bir elemanidir")

#donguler
for x in Diller:
    print(x)

del Diller[0]

sonuc = Diller


print(sonuc)