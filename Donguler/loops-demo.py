import random

randomsayi = random.randint(1,100)

hakSayisi = int(input('Kac hakkiniz olmasini istediginizi girin: '))

for i in range(1,hakSayisi+1):
    girilenSayi = int(input('Tahmin: '))
    puan = 100 - ((i-1) * (100/hakSayisi))
    if girilenSayi == randomsayi:
        print(f'Dogru! {i}. tahmininizde buldunuz ve puaniniz: {puan}, tutulan sayi: {randomsayi}')
        break
    elif girilenSayi < randomsayi:
        print('Yukari')
    else:
        print('Asagi')
else:
    print(f'Hakkiniz bitti. Tutulan sayi: {randomsayi}')
    

# hak = 5
# sayac = 0 

# while hak > 0:
#     hak -= 1
#     sayac += 1
#     tahmin = int(input('Tahmin: '))

#     if tahmin == randomsayi:
#         print(f'Tebrikler {sayac}. tahminde bildiniz. Toplam puaniniz: {100 - (20 * (sayac-1))}')
#         break
#     elif randomsayi > tahmin:
#         print('yukari')
#     else:
#         print('asagi')

#     if hak == 0:
#         print(f'Hakkiniz bitti. Tutulan sayi: {randomsayi}')
    