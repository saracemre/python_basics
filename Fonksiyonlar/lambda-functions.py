

# sonuc = (lambda a: a ** 2)(4)

# multiply = lambda a: a ** 2
# sonuc = multiply(3)

# toplama = lambda a,b,c: a+b+c
# sonuc = toplama(1,5,3)

# tersCevir = lambda s: s[::-1] 
# sonuc = tersCevir('Emre')

def myFunc(n):
    return lambda a: a*n

multiply2 = myFunc(2)

sonuc = multiply2(10)



print(sonuc)


