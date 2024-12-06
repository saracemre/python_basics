benzin = 8.42
motorin = 8.21

aracYakmaMiktari = float(input("Aracinizin 100 km'de yaktigi yakit miktari: "))
aracinTipi = (input('Aracinizin tipi: '))
mesafe = float(input('Aracin gittigi mesafe: '))
benzinliAracinYaktigiYakitMasrafi = (aracYakmaMiktari / 100) * mesafe * benzin
dizelAracinYaktigiYakitMasrafi = (aracYakmaMiktari / 100) * mesafe * motorin

if aracinTipi == 'Benzinli'.strip().lower():
    print(f"Gittiginiz mesafeye gore yaktiginiz yakit masrafi: {benzinliAracinYaktigiYakitMasrafi}")
elif aracinTipi == 'Dizel'.strip().lower():
    print(f"Gittiginiz mesafeye gore yaktiginiz yakit masrafi: {dizelAracinYaktigiYakitMasrafi}")
else:
    print("Girdiginiz arac tipi bulunmamaktadir")