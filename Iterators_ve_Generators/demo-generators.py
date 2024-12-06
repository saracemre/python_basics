# def sonsuz_sayi_uret():
#     sayi = 1
#     while True:
#         yield sayi * sayi
#         sayi += 1

# generator = sonsuz_sayi_uret()

# print(next(generator))
# print(next(generator))
# print(next(generator))


def fibonacci(max):
    fibonacciSayilari = [1]
    sayi = 1
    a = 0
    while len(fibonacciSayilari) <= max-1:
        fibonacciSayilari.append(sayi)
        sayi += fibonacciSayilari[a]
        a += 1
    return(fibonacciSayilari)

# print(fibonacci(10))
        
def fib_list(max):
    sayilar = []
    a, b = 0, 1
    while len(sayilar) < max:
        sayilar.append(b)
        a, b = b, a+b
    return sayilar

# print(fib_list(10))

def fib_gen(max):
    a, b = 0, 1
    count = 0
    while count < max:
        yield b
        a, b = b, a+b
        count += 1

# for i in fib_gen(10):
#     print(i)

# print([i for i in fib_gen(10)])

# import sys
# liste = [i**2 for i in range(10000)]
# print(sys.getsizeof(liste))

# gen = (i**2 for i in range(10000))
# print(sys.getsizeof(gen))

import time

list_start_time = time.time()
sum([i**2 for i in range(10000)])
list_stop = time.time() - list_start_time

gen_start_time = time.time()
sum((i**2 for i in range(10000)))
gen_stop = time.time() - gen_start_time

print(list_stop, gen_stop)