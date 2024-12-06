# for i in range(1,11):
#     print('************')
#     for k in range(1,11):
#         print(f"{i} x {k} = {i*k}")


sayi = int(input('sayi: '))

asalmi = True

if sayi == 1:
    asalmi = False

for i in range(2,sayi):
    if sayi % i == 0:
        asalmi = False
        break

if asalmi:
    print('sayi asaldir')
else:
    print('sayi asal degildir')

