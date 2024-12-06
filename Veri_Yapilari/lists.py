msg = "Python Kursumuza Hos Geldiniz. Ben Sadik Turan".split()

sayilar = [1,3,5,7,9]

sonuc = sayilar
sonuc = sayilar[0]
sonuc = sayilar[4]
# sonuc = sayilar[5] # IndexError: list index out of range

isimler = ['ahmet','ali','can','ada']
sonuc = isimler[0]
# print(type(isimler[0]))
# print(type(sayilar[0]))

listeAli = ['Ali', 20]
listeAhmet = ['Ahmet', 22]

sonuc = listeAli[0]
sonuc = listeAli[1]

# ogrenciler = [["Ali", 20],["Ahmet", 22]]
ogrenciler = [listeAli, listeAhmet]

sonuc = ogrenciler[0][0]
sonuc = ogrenciler[1][0]


print(sonuc)
