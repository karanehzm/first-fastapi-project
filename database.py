import sqlite3

connection = sqlite3.connect("app.db")
cursor = connection.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               age INTEGER
               )
               """)

def add_user():
    cursor.execute("""
        INSERT INTO users (name, age)
        VALUES ('Alice', 23)
               """)
    connection.commit()
    


cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
print(users)