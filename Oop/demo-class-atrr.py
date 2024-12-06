class Pet:
    cinsler = ["kedi", "kopek", "kus"]
    
    def __init__(self, isim, cins):
        if cins not in Pet.cinsler:
            raise ValueError(f"{cins} bir evcil hayvan degildir.")
        self.isim = isim
        self.cins = cins

boncuk = Pet("Boncuk", "kedi")
pasa = Pet("Pasa", "kopek")
# mavis = Pet("Mavis", "kaplan")

Pet.cinsler.append('balik')

print(Pet.cinsler)
print(boncuk.cinsler)
print(pasa.cinsler)