import sqlite3

conncetion = sqlite3.connect("school.db")

cursor = conncetion.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS students (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER
# )
# """)

# cursor.execute("""
# INSERT INTO students (name, age)
# VALUES ("Umar", 20)
# """)

cursor.execute("""
SELECT * FROM students
""")

# students = cursor.fetchall()
students = cursor.fetchmany()
students = cursor.fetchone()

# conncetion.commit()

print(students)