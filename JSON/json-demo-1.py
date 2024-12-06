import json

def urun_ekle(urunAdi, fiyat, satistami, kategori):
    urun = {
            "urunAdi":urunAdi,
            "fiyat":fiyat,
            "satistami":satistami,
            "kategori":kategori 
    }

    with open("urunler.json","w") as file:
        json.dump(urun, file, ensure_ascii=False, indent=4)

urun_ekle("IPhone 13", 20000, True, "Telefon")

def get_urun():
    with open("urunler.json") as file:
        urun = json.load(file)
        print(f"urun adi: {urun['urunAdi']}, urun fiyati: {urun['fiyat']}, urun satista mi: {urun['satistami']}, urunun kategorisi: {urun['kategori']}")

get_urun()

