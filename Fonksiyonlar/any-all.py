# All'da hepsinin True olmasi gerekir True yazabilmesi icin(And gibi)
# Any'de en az biri True olsa yeterlidir.(Or gibi)
sonuc = all([True, True, False]) 
sonuc = all([True, True, True])
sonuc = any([True, True, False])
sonuc = any([True, True, True])

sayilar = [0,1,3,65,4]
sonuc = all([bool(sayi) for sayi in sayilar])
sonuc = all([bool(sayi) for sayi in sayilar if sayi%2==1])
sonuc = any([sayi%2==0 for sayi in sayilar])

kisiler = ['emre','beyza','musti']
sonuc = any([isim[0]=='e' for isim in kisiler])


print(sonuc)