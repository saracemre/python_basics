x = int(input("x:"))

def func(x):
    liste = str(x).strip()
    toplam = 0
    for i in liste:
        toplam += int(i)
    print(toplam)

func(x)


