# x = int(input('x: '))

# sonuc = (x > 50) and (x < 100)

# sonuc = (x % 2 == 1) and (x > 0)

# username = input('username: ')
# password = input('password: ')

# isCorrect = (username == 'emre') and (password == '123')

# sonuc = f"Girdiginiz bilgiler: {isCorrect}"

# x = int(input('x: '))
# y = int(input('y: '))
# z = int(input('z: '))

# sonuc = (x > y) and (x > z) # x en buyuk
# print("x en buyuk sayi: ", sonuc)

# sonuc = (y > x) and (y > z) # y en buyuk
# print("y en buyuk sayi: ", sonuc)

# sonuc = (z > y) and (z > x) # z en buyuk
# print("z en buyuk sayi: ", sonuc)


# vize1 = int(input('1. vize: '))
# vize2 = int(input('2. vize: '))
# final = int(input('final: '))

# ort = (((vize1 + vize2) / 2)) * 0.6 + (final * 0.4)
# gecmeDurumu = ((ort >= 50) and (final >= 50)) or (final >= 70)
# sonuc = f"Ortalamaniz {ort} ve gecme durumunuz: {gecmeDurumu}"

# print(sonuc)

ad = (input('ad: '))
kilo = float((input('kilo: ')))
boy = float((input('boy: ')))

kiloEndeksi = (kilo / (boy ** 2))

if kiloEndeksi <= 18.4:
    print(f"Sayin {ad} kilo endeksiniz {kiloEndeksi} ve kilo endeksine gore zayifsiniz.")
if (kiloEndeksi >= 18.5) and (kiloEndeksi <=24.9):
    print(f"Sayin {ad} kilo endeksiniz {kiloEndeksi} ve kilo endeksine gore normalsiniz.")
if (kiloEndeksi >= 25) and (kiloEndeksi <=29.9):
    print(f"Sayin {ad} kilo endeksiniz {kiloEndeksi} ve kilo endeksine gore fazla kilolusunuz.")
if (kiloEndeksi >= 30) and (kiloEndeksi <=34.9):
    print(f"Sayin {ad} kilo endeksiniz {kiloEndeksi} ve kilo endeksine gore obezsiniz.")

