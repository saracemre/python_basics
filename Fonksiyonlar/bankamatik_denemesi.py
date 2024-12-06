# Bankamatik Uygulamasi

EmreHesap = {
    'ad': 'Emre Sarac',
    'hesapNo': '134523412',
    'bakiye': '5000',
    'ekHesap': '2000'
}

MustafaHesap = {
    'ad': 'Mustafa Sarac',
    'hesapNo': '199872346',
    'bakiye': '7000',
    'ekHesap': '3000'
}

def paraCek(hesap, miktar):
    if hesap == EmreHesap:
        print(f"Merhaba {EmreHesap['ad']}")
        if miktar>5000 and miktar<=7000:
            print("Bakiyenizde yeterli para yok.")
            soru = input("Ek hesaptan cekmek ister misiniz? (e/h):")
            if soru == 'e':
                print(f"Para cekme islemi gerceklestirilmistir, ek hesabinizda kalan para: {7000-miktar}")
            else:
                print(f"Para cekme islemi gerceklestirilmemistir.")    
        elif miktar<=5000:
            print(f"Para cekme islemi gerceklestirilmistir, bakiyenizde kalan para: {5000-miktar}")
        elif miktar>7000:
            print(f"Para cekme islemi gerceklestirilememistir. Hesabinizda yeterli para yoktur.")

paraCek(EmreHesap, 6000)
