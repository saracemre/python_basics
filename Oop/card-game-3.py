from random import shuffle
class Kart:
    def __init__(self, tip, deger):
        self.tip = tip
        self.deger = deger

    def __repr__(self):
        return f"{self.tip} {self.deger}"


class Deste:
    tipler = ['karo', 'sinek', 'kupa', 'maca']
    degerler = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    def __init__(self):
        self.kartlar = [Kart(tip, deger) for tip in Deste.tipler for deger in Deste.degerler]

    def kartSayisi(self):
        return len(self.kartlar)

    def kartlariKaristir(self):
        if self.kartSayisi() < 52:
            raise ValueError("Basladiktan sonra kartlari karistiramazsiniz.")
        shuffle(self.kartlar)

    def kartDagit(self, adet):
        kartSayisi = self.kartSayisi()
        if kartSayisi == 0:
            raise ValueError("Butun kartlar dagitildi.")
        adet = min([kartSayisi, adet])
        kartlar = self.kartlar[-adet:]
        self.kartlar = self.kartlar[:-adet]
        return kartlar
        
deste1 = Deste()

deste1.kartlariKaristir()
print(deste1.kartDagit(5))
print(deste1.kartSayisi())
print(deste1.kartDagit(3))
print(deste1.kartSayisi())

print(deste1.kartlar)