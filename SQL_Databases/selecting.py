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

    # cursor.execute("SELECT * FROM products")
    cursor.execute("SELECT name, price FROM products")


    # result = cursor.fetchall()
    
    result = cursor.fetchone()
    print(f"product name: {result[0]}, price: {result[1]}")


    # for product in result:
    #     # print(f"product name: {product[1]}, price: {product[2]}")
    #     print(f"product name: {product[0]}, price: {product[1]}")

getProducts()


    