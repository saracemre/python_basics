import mysql.connector

def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "",database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name, price, imageUrl, description) VALUES (%s,%s,%s,%s)"
    values = (name, price, imageUrl, description)

    cursor.execute(sql, values)

    try:
        connection.commit()
        print(f"Added {cursor.rowcount} record.")
        print(f"Last added record id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print(f"error: {err}")
    finally:
        connection.close()
        print("Database connection closed.")

def insertProducts(array):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "",database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name, price, imageUrl, description) VALUES (%s,%s,%s,%s)"
    values = array

    cursor.executemany(sql, values)

    try:
        connection.commit()
        print(f"Added {cursor.rowcount} records.")
        print(f"First added record id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print(f"error: {err}")
    finally:
        connection.close()
        print("Database connection closed.")

array = []

while True:
    name = input("Product name: ")
    price = float(input("Product price: "))
    imageUrl = input("Product image: ")
    description = input("Product description: ")

    array.append((name, price, imageUrl, description))

    result = input("Do you want to continue? (y/n)")
    if result == "n":
        print("Your records are being transferring to the database...")
        print(array)
        insertProducts(array)
        break

# insertProduct(name, price, imageUrl, description)
