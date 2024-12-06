sayilar = [1,5,15,35,57,72]

# for sayi in sayilar:
#     print(sayi)

# for sayi in sayilar:
#     if (sayi % 5 == 0):
#         print(sayi)

# toplam = 0
# for sayi in sayilar:
#     toplam = toplam + sayi
# print(toplam)


# for sayi in sayilar:
#     if (sayi % 2 == 0):
#         print(sayi, sayi ** 2)

urunler = ['iphone 8', 'iphone X', 'iphone XR', 'samsung S10']

# for urun in urunler:
#     print(i[1])

count = 0
for urun in urunler:
    index = urun.find('iphone')
    if (index >= 0):
        count += 1
print(count)
        
