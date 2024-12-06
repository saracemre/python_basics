from csv import writer, reader


# with open("users.csv","a") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Ad","Soyad"])

def add_user(first, last):
    with open("users.csv","a") as file:
        csv_writer = writer(file)
        csv_writer.writerow([first, last])


def get_users():
    with open("users.csv","r") as file:
        csv_reader = reader(file)
        for p in csv_reader:
            print(p[0], p[1])

def find_user(first, last):
    with open("users.csv") as file:
        csv_reader = reader(file)
        for index,row in enumerate(csv_reader):
            if first == row[0] and last == row[1]:
                return index
        return -1

# add_user("Emre", "Sarac")
# add_user("Mustafa", "Sarac")
# add_user("Elif","Sarac")
# get_users()

print(find_user("Ad","Soyad"))