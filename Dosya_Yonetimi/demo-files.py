def dosya_kopyala(dosya_ismi, yeni_dosya_ismi):
    with open(dosya_ismi, "r+") as file:
        icerik = file.read()
    
    with open(yeni_dosya_ismi, "w") as newfile:
        newfile.write(icerik)

# dosya_kopyala("msg.txt", "msg_copy.txt")

def ters_cevir(dosya_ismi, yeni_dosya_ismi):
    with open(dosya_ismi, "r+") as file:
        icerik = file.read()
    
    with open(yeni_dosya_ismi, "w") as newfile:
        newfile.write(icerik[::-1])

# ters_cevir("msg.txt", "msg_copy2.txt")

def bilgilendir(dosya_ismi):
    with open(dosya_ismi) as file:
        satirlar = file.readlines()
        satir_sayisi = len(satirlar)
        kelime_sayisi = sum(len(satir.split(' ')) for satir in satirlar)
        karakter_sayisi = sum(len(satir) for satir in satirlar)
    sonuc = ({
        "satir_sayisi": satir_sayisi,
        "kelime_sayisi": kelime_sayisi,
        "karakter_sayisi": karakter_sayisi
    })
    return sonuc

        
print(bilgilendir("msg.txt"))
        