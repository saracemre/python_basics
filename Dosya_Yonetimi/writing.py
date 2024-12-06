# "w": (Write) yazma modu.
#    ** Dosyayi konumda olusturur.
#    ** Eger konumda ayni dosya varsa dosyayi siler ve yeni olusturur.

with open("/Users/emresarac/desktop/newfile.txt", "w", encoding="UTF-8") as file:
    file.write("Emre Sarac\n")
    file.write("Mustafa Sarac\n")
    file.write("Elif Sarac")

    print(file) 

with open("/Users/emresarac/desktop/newfile.txt") as file:
    print(file.read())