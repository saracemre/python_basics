adi, soyadi = 'Emre', 'Sarac'

numarasi = '150210027'

e = 'Erkek'

cinsiyet = e

dogumYili = 2003

from datetime import date
today = date.today()
yil = today.strftime("%Y")

yasi = int(yil) - dogumYili

print(adi, soyadi, yasi, (yasi + float(numarasi)))


urun1 = 50
urun2 = 60.5
urun3 = 356.45
toplam = urun1 + urun2 + urun3
print("Urun toplami:", toplam)

