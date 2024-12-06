markalar = ['opel', 'bmw', 'mercedes']

# index = 0
# for marka in markalar:
#     print(f"{index+1}-{marka}")
#     index += 1

#enumerate

# obj1 = enumerate(markalar)

# print(type(obj1))
# print(list(obj1))

# for index,value in enumerate(markalar):
#     print(f"{index+1}-{value}")

# for index,value in enumerate(markalar,1):
#     print(f"{index}-{value}")

# zip

liste1 = [1,2,3,4,5]
liste2 = ['a','b','c','d','e']
liste3 = [100,200,300,400,500]

# sonuc = list(zip(liste1,liste2,liste3))
# print(sonuc)

# for i in sonuc:
#     print(i)

for item in zip(liste1,liste2):
    print(item)

for a,b,c in zip(liste1,liste2,liste3):
    print(a,b,c)