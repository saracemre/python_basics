# sets => indekslenemez, siralanamaz
meyveler = { "elma", "kiraz", "kavun", "karpuz" }
sebzeler = { "bezelye", "sogan"}

sonuc = meyveler
# sonuc = meyveler[0] indekslenemez
sonuc = "elma" in meyveler

meyveler.add("armut")
meyveler.update(["visne", "kavun"]) # ayni elemani update edersek bir degisiklik olmaz

meyveler.remove("karpuz")
# meyveler.remove("karpuzz") # KeyError
# meyveler.discard("karpuzz") # listede olmayan bir elemani silmeye calissak bile error vermez

sonuc = len(meyveler)
meyveler.pop() # rastgele bir eleman siler

# meyveler.clear()

sonuc = meyveler

sonuc = meyveler.union(sebzeler) # birlestirir
# for x in meyveler:
#     print(x)

print(sonuc)