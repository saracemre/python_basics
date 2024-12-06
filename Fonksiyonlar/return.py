# def toplam():
#     return f"Toplam: {10+20}"

# print(toplam())

# def yil():
#     import datetime
#     return datetime.datetime.now().year

# def yasHesapla():
#     return yil() - 2003

# sonuc = yasHesapla()

def saat():
    import datetime
    return datetime.datetime.now().hour

def selamla():
    if saat()<12 and saat>6:
        return "Gunaydin"
    elif saat >12 and saat<20:
        return "Tunaydin"
    else:
        return "Iyi Geceler"

name = input('Adiniz: ')
sonuc = f"{selamla()}, {name}"

print(sonuc)


