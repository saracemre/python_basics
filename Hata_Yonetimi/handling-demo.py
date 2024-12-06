liste = ['1','2','5a','10b','abc','10','50']

# for eleman in liste:
#     try:
#         sonuc = int(eleman)
#         print(sonuc)
#     except ValueError:
#         continue

# while True:
#     sayi = input('sayi: ')
#     if sayi == 'q':
#         break
#     try:
#         sayi = float(sayi)
#         print(f"Girilen sayi: {sayi}")
#         break
#     except ValueError:
#         print('Gecersiz')
#         continue

d = {'urunAdi':'samsung s10'}
def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

print(get(d,'price'))