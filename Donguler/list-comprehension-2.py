# for item in liste:
#     if(kosul):
#         expression

# [expression for item in liste if kosul]

sayilar  = [2,3,5,8,11]
# sonuc = []

# for sayi in sayilar:
#     if sayi % 2 ==0:
#         sonuc.append(sayi)

# print(sonuc)

# sonuc = [sayi for sayi in sayilar if sayi%2==0]
# sonuc = [sayi if sayi%2==0 else "tek sayi" for sayi in sayilar]

# print(sonuc)

# fiyatlar = [1000,3000,5000,0,4000]
# vergiliFiyatlar = []

# for fiyat in fiyatlar:
#     if fiyat > 0:
#         vergili = fiyat*1.18 
#         vergiliFiyatlar.append(vergili)

# vergiliFiyatlar = [fiyat*1.18 for fiyat in fiyatlar if fiyat>0]
# vergiliFiyatlar = [fiyat*1.18 if fiyat>0 else "vergi hesaplanmadi" for fiyat in fiyatlar]

# sonuc = []

# for x in range(3):
#     for y in range(3):
#         sonuc.append((x,y))

sonuc = [(x,y) for x in range(3) for y in range(3)]
print(sonuc)