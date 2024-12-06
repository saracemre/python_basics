# Fonksiyondan Fonksyiona Dondurme

# def usAlma(number):

#     def inner(power):
#         return number ** power
    
#     return inner

# two = usAlma(2)
# print(two(4))

# three = usAlma(3)
# print(three(5))

# def yetki_sorgula(page):
#     def inner(role):
#         if role == "Admin".lower():
#             return f"{role.capitalize()} rolu {page} sayfasina ulasabilir."
#         else:
#             return f"{role.capitalize()} rolu {page} sayfasina ulasamaz."
    
#     return inner    

# user1 = yetki_sorgula('Product Edit')
# print(user1('admin'))
# print(user1('user'))

def islem(islem_adi):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim

    if islem_adi == 'toplama':
        return toplama
    elif islem_adi == 'carpma':
        return carpma

toplama = islem('toplama')
print(toplama(1,2,34,5,2))

carpma = islem('carpma')
print(carpma(1,2,34,5,2))