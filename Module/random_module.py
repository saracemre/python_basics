import random
import math

# result = dir(random)
# result = help(random)

result = random.random() # 0 - 1
result = random.random() * 100
result = random.uniform(1,100)
result = random.randint(1,10) # 10 dahil
result = random.randrange(1,10) # 10 dahil degil

names = ['emre', 'elif','beyza','musti']
result = names[random.randint(0,len(names) - 1)]
result = random.choice(names)

greeting = 'Hello there'
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste)
result = liste

liste = range(100)
result = random.sample(liste, 3)

print(result)