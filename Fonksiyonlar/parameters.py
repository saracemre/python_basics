def selamla(isim):
    return "Merhaba, " + isim

sonuc = selamla("Emre")

def toplam(sayi1, sayi2):
    return f"Toplam: {sayi1 + sayi2}"

sonuc = toplam(10,20)

def yasHesapla(dogumYili):
    import datetime
    suankiYil = datetime.datetime.now().year
    return suankiYil - dogumYili

sonuc = yasHesapla(2003)

def emekliligeKacYilKaldi(dogumYili, isim):
    return f"{isim}, emekliliginize {(65 - yasHesapla(2003))} yil kaldi."

sonuc = emekliligeKacYilKaldi(2003, 'Emre')

print(sonuc)