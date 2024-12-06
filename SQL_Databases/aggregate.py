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

    # cursor.execute("SELECT * FROM products ORDER BY price")  # Artan sekilde siralar.  
    # cursor.execute("SELECT * FROM products ORDER BY price DESC") # Azalan sekilde siralar.
    cursor.execute("SELECT * FROM products ORDER BY name, price") # Adi ayni olanlari da fiyata gore siralar.

    
    result = cursor.fetchall() 
    
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

def getProductInfo():

    connection = mysql.connector.connect(host = "localhost", user = "root", password = "",database = "node-app")
    cursor = connection.cursor()

    # sql = "SELECT COUNT(*) FROM products"
    # sql = "SELECT AVG(price) FROM products"
    # sql = "SELECT SUM(price) FROM products"
    # sql = "SELECT MIN(price) FROM products"
    # sql = "SELECT MAX(price) FROM products"
    sql = "SELECT name, price FROM products WHERE price = (SELECT MAX(price) FROM products)"


    cursor.execute(sql)

    result = cursor.fetchone()

    print(f"result: {result[0]} {result[1]}")

getProductInfo()