import csv

def update_users(firstname, lastname, newfirstname, newlastname):
    with open("users.csv",'r') as file:
        csv_reader = csv.reader(file)
        users = list(csv_reader)
    count = 0
    with open("users.csv","w") as file:
        csv_writer = csv.writer(file)
        for user in users:
            if user[0] == firstname and user[1] == lastname:
                csv_writer.writerow([newfirstname, newlastname])
                count += 1
            else:
                csv_writer.writerow(user)
    return f"{count} tane kayit guncellendi."


# print(update_users('Emre', 'Sarac', 'Beyza', 'Sarac'))


def delete_users(firstname, lastname):
    with open("users.csv",'r') as file:
        csv_reader = csv.reader(file)
        users = list(csv_reader)
    count = 0
    with open("users.csv","w") as file:
        csv_writer = csv.writer(file)
        for user in users:
            if user[0] == firstname and user[1] == lastname:
                count += 1
            else:
                csv_writer.writerow(user)
    return f"{count} tane kayit silindi."

print(delete_users("Beyza","Sarac"))