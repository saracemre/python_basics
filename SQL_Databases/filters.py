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


def getProducts():
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "",database = "node-app")
    cursor = connection.cursor()

    # cursor.execute("SELECT * FROM products WHERE price >= 3000 and price <= 5000")
    # cursor.execute("SELECT * FROM products WHERE name LIKE '%Samsung%'") # Herhangi bir yerde Samsung gecenleri getir.
    # cursor.execute("SELECT * FROM products WHERE name LIKE 'Samsung%'") # Basi Samsung olanlari getir.
    cursor.execute("SELECT * FROM products WHERE name LIKE '%Samsung%' and price <= 2000 and price >= 1500")

    # result = cursor.fetchone() # Sartlara uyan ilk elemani verir. Liste seklinde gelmez.
    result = cursor.fetchall() # Sartlara uyan butun elemanlar liste seklinde gelir.
    
    for product in result:
        print(f"id: {product[0]}, name: {product[1]}, price: {product[2]}")

def getProductById(id):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "",database = "node-app")
    cursor = connection.cursor()
    sql = "SELECT * FROM products WHERE id=%s"
    params = (id,)

    cursor.execute(sql, params)

    result = cursor.fetchone()

    print(f"id: {result[0]}, name: {result[1]}, price: {result[2]}")

    

getProductById(6)