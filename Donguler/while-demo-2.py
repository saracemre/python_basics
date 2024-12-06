i = 0
urunler = []
urunAdeti = int(input('Kac tane urun girmek istiyorsunuz: '))

while i < urunAdeti:
    urunAdi = input('urun adi: ')
    fiyat = input('urun fiyati: ')
    urunler.append({
        'urunAdi': urunAdi,
        'fiyat': fiyat
    })
    i += 1

for urun in urunler:
    print(f"urun adi: {urun['urunAdi']} urun fiyati: {urun['fiyat']}")