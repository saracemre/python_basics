# def hangisiBuyuk(a,b):
#     if a==b:
#         return f"Sayilar esit"
#     elif a>b:
#         return f"Buyuk olan sayi {a}"
#     else:
#         return f"Buyuk olan sayi {b}"
# sonuc = hangisiBuyuk(30,20)
# print(sonuc)
    

# def tekrarlanmaSayisi(string):
#     return { letter: string.count(letter) for letter in string}
# sonuc = tekrarlanmaSayisi('Merhaba ben Emre')
# print(sonuc)


# def update_list(liste, command, position, value=None):
#     if (command=="remove" and position=="end"):
#         return liste.pop()
#     elif (command=="remove" and position=="beginning"):
#         return liste.pop(0)
#     elif (command=="add" and position=="beginning"):
#         liste.insert(0,value)
#         return liste
#     elif (command=="add" and position=="end"):
#         liste.append(value)
#         return liste
# sonuc = update_list([1,2,3], "add", "end", 4)
# sonuc = update_list([1,2,3], "remove", "end")
# sonuc = update_list([1,2,3], "add", "beginning", 4)
# print(sonuc)


def contains_blue(*renkler):
    if "blue" in renkler:
        return True
    return False
sonuc = contains_blue('red','blue','brown')
print(sonuc)
