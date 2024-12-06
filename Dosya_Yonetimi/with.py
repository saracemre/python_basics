# with open('msg.txt') as file:
#     print(file.read(10))
#     print(file.tell()) # Cursor'un nerede oldugunu soyler
#     print(file.read(10))

try:
    with open("msg.txt", "r", encoding="UTF-8") as file:
        for i in file:
            print(i, end="")
except FileNotFoundError as e:
    print("dosya okuma hatasi: ", e)
finally:
    print("dosya kapandi.")    
