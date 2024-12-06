sayilar = []
liste =  [10,4,7,9,70]

for i in liste:
    i *= 2
    sayilar.append(i)

# [expression for item in list]

# sayilar = [i for i in range(10)]
# sayilar = [i*2 for i in liste]

isim = "Ahmet"
isimler = ['Ahmet','ali','ciNar','DenIz']

# sonuc = []
# for c in isim:
#     sonuc.append(c.upper())

sonuc = [c.upper() for c in isim]
sonuc = [str(sayi) for sayi in liste]
sonuc = [a.capitalize() for a in isimler]

print(sonuc)