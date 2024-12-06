# def kelime(txt, adet):
#     print(txt * adet)
# kelime('Merhaba\n', 3)

# def alan(a,b):
#     dikdortgenAlani = a*b
#     return f"Diktorgenin alani: {dikdortgenAlani}"
# print(alan(20,30))


# def yaziTura():
#     import random
#     sayi = random.randrange(0,100)
#     if sayi % 2 == 1:
#         print('Yazi')
#     else:
#         print('Tura')
# yaziTura()

# def asalSayilariBul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if sayi>1:
#             for i in range(2,sayi):
#                 if sayi % i ==0:
#                     break
#             else:
#                 print(sayi)

# asalSayilariBul(2,1000)

def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(1,sayi+1):
        if sayi % i ==0:
            tamBolenler.append(i)
    return tamBolenler
print(tamBolenleriBul(12))

