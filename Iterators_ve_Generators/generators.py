def sayi_say(max):
    sayi = 1
    
    while sayi <= max:
        yield sayi
        sayi += 1
    

iterator = sayi_say(10)

# print(next(iterator))
# print(next(iterator))

for i in iterator:
    print(i)

# sonuc = list(iterator)

# print(sonuc)

generator = (i for i in range(1,11))

print(generator)
