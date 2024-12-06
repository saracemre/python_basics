isimler = ["Ahmet","ali","Cinar","deNiz"]
string = "Hello 12345 World"
yillar = [1983, 1999,2008,1956,1986]
dereceler = [20,5,15,-2,0,-6]

# sayilar = [sayi for sayi in range(1,101) if sayi%12==0]
# print(sayilar)

# isimlerYeni = [isim.lower()[::-1] for isim in isimler]
# print(isimlerYeni)

# liste = [a for a in string if a.isnumeric()]
# print(liste)

# import datetime
# sonuc = datetime.datetime.now().year

# yaslar = [sonuc-yas for yas in yillar]

# print(yaslar)

sonuc = [sicaklik if sicaklik >= 0 else 'Buzlanma tehlikesi' for sicaklik in dereceler]

print(sonuc)