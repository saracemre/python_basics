def urun_ekle(ad, fiyat):
    with open('urunler.txt', 'a', encoding="UTF-8") as file:
        file.write(f"urun adi: {ad} ve fiyati: {fiyat}\n")
        
# ad = input('ad: ')
# fiyat = input('fiyat: ')
# urun_ekle(ad, fiyat)
        
def bul_ve_degistir(dosya_ismi, eski_kelime, yeni_kelime):
    with open(dosya_ismi, "r+", encoding="UTF-8") as file:
        text = file.read()
        yeni_text = text.replace(eski_kelime, yeni_kelime)
        file.seek(0)
        file.write(yeni_text)
        file.truncate()

bul_ve_degistir("urunler.txt", "IPhone", "Samsung")