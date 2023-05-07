import sqlite3

def read_student():
    # Connect to the database
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Retrieve all student details from the database
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    # Display the student details
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")

    # Close the database connection
    connection.close()
