def selamlama(fn):
    def wrapper(ad):
        print('hos geldiniz')
        fn(ad)
        print('gorusmek uzere')
    return wrapper

@selamlama
def gunaydin(ad):
    print(f'gunaydin benim adim {ad}')

@selamlama
def iyiGunler(ad):
    print(f'iyi gunler benim adim {ad}')

gunaydin('musti')
iyiGunler('emre')