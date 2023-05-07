import sqlite3

def delete_student():
    # Connect to the database
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Get input from the user
    student_id = input("Enter student ID to delete: ")

    # Delete student from the database
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    connection.commit()

    # Close the database connection
    connection.close()
