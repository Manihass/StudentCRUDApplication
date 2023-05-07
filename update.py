import sqlite3

def update_student():
    # Connect to the database
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Get input from the user
    student_id = input("Enter student ID to update: ")
    name = input("Enter updated student name: ")
    age = input("Enter updated student age: ")
    grade = input("Enter updated student grade: ")

    # Update student details in the database
    cursor.execute("UPDATE students SET name=?, age=?, grade=? WHERE id=?", (name, age, grade, student_id))
    connection.commit()

    # Close the database connection
    connection.close()
