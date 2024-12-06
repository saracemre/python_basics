# "a": (Append) en sona ekleme. Dosya konumda yoksa olusturur.
# "r+": Hem okuma hem yazma modunda acilir. Dosya konumda yoksa hata verir.

# with open("msg.txt", "a") as file:
#     file.write("altinci satir.\n")
#     file.write("yedinci satir.\n")

# with open("msg.txt", "a") as file:
#     file.seek(0)
#     file.write("yeni satir.\n")

with open("msg.txt", "r+") as file:
    file.read()
    file.write("yeni satir.\n")