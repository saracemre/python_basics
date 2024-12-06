# isim = input('isim: ')
# yas = int(input('yas: '))
# egitimBilgisi = input('Egitim Bilgisi: ')

# if yas >= 18:
#     if egitimBilgisi.strip().lower() == 'lise' or egitimBilgisi.strip().lower() == 'universite':
#         print('Ehliyet alabilirsiniz.')
#     else:
#         print('Egitim bilgisi yetersiz.')
# else:
#     print('Yasiniz tutmuyor.')

# yazili1 = int(input('1. yazili: '))
# yazili2 = int(input('2. yazili: '))
# sozlu = int(input('sozlu: '))
# ort = (yazili1 + yazili2 + sozlu) / 3

# if ort >= 0 and ort < 25:
#     print(f'Ortalamaniz: {ort} ve notunuz 0')
# elif ort >= 25 and ort < 45:
#     print(f'Ortalamaniz: {ort} ve notunuz 1')
# elif ort >= 45 and ort < 55:
#     print(f'Ortalamaniz: {ort} ve notunuz 2')
# elif ort >= 55 and ort < 70:
#     print(f'Ortalamaniz: {ort} ve notunuz 3')
# elif ort >= 70 and ort < 85:
#     print(f'Ortalamaniz: {ort} ve notunuz 4')
# elif ort >= 85 and ort <= 100:
#     print(f'Ortalamaniz: {ort} ve notunuz 5')
# else:
#     print("Notlar yanlis girilmistir")

import datetime

tarih = input('Araciniz hangi tarihte trafige cikti: ')
tarih = tarih.split('/')

simdi = datetime.datetime.now()
trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))

fark = simdi - trafigeCikis
gun = fark.days

if (gun <= 365):
    print('1. servis bakimi')
elif (gun > 365) and (gun <= 365*2):
    print('2. servis bakimi')
elif (gun > 365*2) and (gun <= 365*3):
    print('3. servis bakimi')
else:
    print('Hatali bilgi girdiniz')