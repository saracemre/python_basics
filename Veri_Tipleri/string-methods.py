msg = "Python kursumuza hos geldiniz. Ben Sadik Turan."

# sonuc = msg.upper() # Butun harfleri buyuk yazdirir.
# sonuc = msg.lower() # Butun harfleri kucuk yazdirir.
# sonuc = msg.title() # Her kelimenin bas harfini buyuk yazdirir.
# sonuc = msg.capitalize() # Sadece ilk harfi buyuk yazdirir.

# sonuc = "abc".islower()

# sonuc = "   abc ".strip() # Bosluklari kaldirir.
# sonuc = msg.split()   # Her kelimeyi ayri ayri yazdirir.
# sonuc = msg.split('.') # Noktaya gore ayirir.

sonuc = "-".join(msg) 
print(sonuc)

# index = msg.index('hos')

# sonuc = msg.startswith('P')
# sonuc = msg.endswith('.')

# sonuc = msg.replace('Sadik', 'Emre').replace('Turan', 'Sarac')

sonuc = msg.count('e')


print(sonuc)