import sqlite3

def create_student():
    # Connect to the database
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    # Create the students table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,age INTEGER NOT NULL,grade TEXT NOT NULL)""")

    # Get input from the user
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")

    # Insert student details into the database
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    connection.commit()

    # Close the database connection
    connection.close()
