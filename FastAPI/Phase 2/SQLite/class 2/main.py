import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
""")

# cursor.execute("INSERT INTO students (name, age) VALUES ('Usman2', null)")
# cursor.execute("SELECT name, age FROM students")

# cursor.execute("SELECT * FROM students WHERE id = 10")

# cursor.execute("UPDATE students SET age = 28 WHERE id = 4")



# cursor.execute("UPDATE students SET age = 18 WHERE age IS NULL")

# cursor.execute("SELECT * FROM students WHERE age IS NULL")

# cursor.execute("DELETE FROM students")

cursor.execute("DROP TABLE students")

# cursor.execute("SELECT * FROM students")

# rows = cursor.fetchall()

# for row in rows:
#     print(row)

connection.commit()