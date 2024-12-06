import sqlite3

connection = sqlite3.connect("node_app.db")

cursor = connection.cursor()

connection.close()