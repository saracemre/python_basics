import csv

# with open("products.csv") as file:
#     print(file.read())

with open("products.csv") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for p in csv_reader:
        if p[2] == "True":
            print(f"urun adi: {p[0]} ve urun fiyati: {p[1]}")
