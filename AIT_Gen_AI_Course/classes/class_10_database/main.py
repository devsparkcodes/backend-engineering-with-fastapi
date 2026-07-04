import sqlite3

connection = sqlite3.connect("school.db")
print("Database connected!")

connection.close()
print("Database disconnected!")