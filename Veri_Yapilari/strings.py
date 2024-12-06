ad = 'Emre'
soyad = 'Sarac'
yas = '18'


msj = 'Benim adim ' + ad + ' ve soyadim ' + soyad + '. Yasim ise ' + yas + '.'
karakterSayisi = len(msj)

print(len(msj)) # karakter sayisini yazdirir.


print(msj[-1])
print(msj[1])
print(msj[karakterSayisi - 1])

print(msj[0:5])    # 0. karakterden 4. karaktere kadar yazdirir.
print(msj[6:15])   # 6'dan 14'e yazdirdik.
print(msj[:10])    # baslangictan 9'a yazdirir.
print(msj[10:])    # 10'dan baslayip en sona yazdirir.
print(msj[-10:-1]) # sagdan 10. harften sagdan 2.ye yazdirir.
print(msj[0:40:2]) # 0'dan 39'a ikiser adimla yazar.
print(msj[::1])    # soldan saga dogru hepsini yazdirir.
print(msj[::-1])   # tersten yazdirir.
