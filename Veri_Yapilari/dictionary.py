# key - value

# 41 => Kocaeli
# 34 => Istanbul

plakalar = {'Kocaeli': 41, 'Istanbul': 34}

# print(plakalar['Kocaeli'])
# print(plakalar['Istanbul'])

plakalar['Rize'] = 53
# plakalar['Izmir'] = 36

# plakalar['Izmir'] = 35 # 36 to 35
# print(plakalar)

ogrenciler = {
    100: {
        'ad': 'Emre',
        'yas': 18,
        'notlar': [50,90,85]
    },
    101: {
        'ad': 'Beyza',
        'yas': 23}
    }
sonuc = ogrenciler[100]['ad']
sonuc = ogrenciler[101]
sonuc = (ogrenciler[100]['notlar'][0] + ogrenciler[100]['notlar'][1] + ogrenciler[100]['notlar'][2]) / 3


print(sonuc)
