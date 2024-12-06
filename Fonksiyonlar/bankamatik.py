# Bankamatik Uygulamasi

EmreHesap = {
    'ad': 'Emre Sarac',
    'hesapNo': '14513451',
    'bakiye': 3000,
    'ekHesap': 2000
}

BeyzaHesap = {
    'ad': 'Beyza Sarac',
    'hesapNo': '23412454',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('Paranizi alabilirsiniz.')
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if toplam >= miktar:
            ekHesapKullanimi = input('ek hesap kullanilsin mi (e/h)')

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('Paranizi albilirsiniz.')
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir.")
        else:
            print('Hesapta yeterli para bulunmamaktadir.')

paraCek(EmreHesap, 3000)
paraCek(EmreHesap, 1000)

