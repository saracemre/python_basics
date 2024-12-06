urunler = [
    {'name': 'iphone 8', 'price': '4000'},
    {'name': 'iphone 8 Plus', 'price': '5000'},
    {'name': 'iphone X', 'price': '6000'},
    {'name': 'iphone XR', 'price': '7000'},
    {'name': 'iphone 11', 'price': '8000'},
    {'name': 'samsung S10', 'price': '6000'}
]

# for urun in urunler:
#     print(f"urun adi: {urun['name']} ve urun fiyati: {urun['price']} TL")

# toplam = 0
# for urun in urunler:
#     toplam = toplam + int(urun['price'])
# print(f"Urunlerin toplam fiyati: {toplam} TL")

# for urun in urunler:
#     if int(urun['price']) <= 6000:
#         print(f"urun adi: {urun['name']} ve urun fiyati: {urun['price']} TL")

kelime = input('Aramak istediginiz urun: ')

for urun in urunler:
    if urun['name'].find(kelime.lower()) > -1:
        print(f"urun adi: {urun['name']} ve urun fiyati: {urun['price']} TL")

