sayilar = [1,2,5,-7,-9]
str_sayilar = ['1','2','5','7','9']
isimler = ['Mustafa','Emre','Beyza','Elif']
kullanicilar = [
    {'ad':'Emre', 'soyad':'Sarac'},
    {'ad':'Mustafa', 'soyad':'Sarac'}
]
# kareleri = []

# for sayi in sayilar:
#     kareleri.append(sayi**2)
# print(kareleri)

# kareleri = [sayi**2 for sayi in sayilar]
# print(kareleri)

# def kareAl(sayi):
#     return sayi**2
# sonuc = list(map(kareAl, sayilar))

sonuc = list(map(lambda sayi: sayi**2, sayilar))
sonuc = list(map(int,str_sayilar))
sonuc = list(map(lambda sayi: int(sayi)**2, str_sayilar))
sonuc = list(map(abs, sayilar))
sonuc = list(map(float, sayilar))
sonuc = list(map(len, isimler))
sonuc = list(map(str.upper, isimler))
sonuc = list(map(lambda x: x['ad'], kullanicilar))

print(sonuc)