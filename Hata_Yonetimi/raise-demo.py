# def faktoriyel(x):
#     x = int(x)

#     if x<0:
#         raise ValueError("Negatif deger")

#     sonuc = 1
#     for i in range(1,x+1):
#         sonuc *= i
#     return sonuc 

# for i in [5,7,'a',2,-4,'10a']:
#     try:
#         x = faktoriyel(i)
#     except ValueError as e:
#         print(e)
#         continue
#     else:
#         print(x)

turkceKarakterler = ['ç','ğ','ı','ö','ş','ü']

def parolaKontrol(parola):
    turkceKarakterler = "şçğüöıİ"

    for i in parola:
        if i in turkceKarakterler:
            raise TypeError("Parola turkce karakter iceremez.")
    print('Gecerli parola')        

parola = input('parola: ')

try:
    parolaKontrol(parola)
except Exception as e:
    print(e)

