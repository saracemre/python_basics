modeller = ["Samsung S5", "Samsung S6", "Samsung S7", "Samsung S8"]

sonuc = len(modeller)

sonuc = modeller[0]
sonuc = modeller[-1]

modeller[0] = "Samsung S9"

# if "Samsung S6" in modeller:
    # print("Samsung S6 listenin bir elemanidir.")

sonuc = modeller[-3]

sonuc = modeller[0:2]

modeller[-2:] = ["Samsung S9","Samsung S10"]

modeller = modeller + ["Iphone X", "Iphone XR" ]

del modeller[-1]

sonuc = modeller[::-1]

# print(sonuc)


kullaniciA = ["Yigit Bilgi", 2010, [70,60,70]]
kullaniciB = ["Sena Turan", 1999, [80,80,70]]
kullaniciC = ["Ahmet Turan", 1998, [80,70,90]]

kullanicilar = [kullaniciA,kullaniciB,kullaniciC]

for kullanici in kullanicilar:
    print(f"{kullanici[0]} {2021-kullanici[1]} {(kullanici[2][0] + kullanici[2][1] + kullanici[2][2])/3}")


# for a in modeller:
#     print(a)