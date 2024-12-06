# def selamlama(isim='Kullanici', mesaj='Iyi gunler'):
#     print(f"{mesaj} {isim}")
# selamlama()
# selamlama('Emre')
# selamlama('Emre','Gunaydin')

# def usAlma(taban, us=2):
#     return taban ** us
# sonuc = usAlma(2,2)

def toplam(a,b):
    return a + b
def cikarma(a,b):
    return a - b
def islem(a,b,fn = toplam):
    return fn(a,b)
sonuc = islem(5,3)




print(sonuc)
