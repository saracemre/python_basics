from csv import DictReader

with open("products.csv") as file:
    csv_reader = DictReader(file) # DictReader(file, delimiter="x") ile virgul yerine kullandigimiz x'ten ayirabiliriz.
    for p in csv_reader:
        if p["Category"] == "Telefon":
            print(p["ProductName"], p["Price"])