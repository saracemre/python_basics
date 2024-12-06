isim = 'Emre Sarac'

# for harf in isim:
#     if(harf == 'e'):
#         continue
#     print(harf)

# for harf in isim:
#     if(harf == 'e'):
#         break
#     print(harf)

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1
# print('dongu bitti')

# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)  
# print('dongu bitti')

toplam = 0
i = 0

while i < 99:
    i += 1
    if i % 2 == 1:
        continue
    toplam = toplam + i
print(toplam)
