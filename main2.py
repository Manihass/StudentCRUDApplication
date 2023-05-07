from tkinter import *
from tkinter.ttk import *
from create import create_student
from read import read_student
from update import update_student
from delete import delete_student
from PIL import ImageTk, Image

def create_button_clicked():
    create_student()
    status_label.config(text="Student created successfully.")

def read_button_clicked():
    students = read_student()
    if students:
        status_label.config(text="Student details retrieved successfully.")
        output_text.config(state=NORMAL)
        output_text.delete("1.0", END)
        for student in students:
            output_text.insert(END, f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}\n")
        output_text.config(state=DISABLED)
    else:
        status_label.config(text="No student details found.")

def update_button_clicked():
    update_student()
    status_label.config(text="Student details updated successfully.")

def delete_button_clicked():
    delete_student()
    status_label.config(text="Student deleted successfully.")

# Create the GUI window
window = Tk()
window.title("Student Management System")
window.geometry("400x400")

# Configure styles
window_style = Style()
window_style.configure("TFrame", background="#4CAF50")
window_style.configure("TButton", background="#4CAF50", foreground="#000000", padding=(10, 5), font=("Arial", 12))
window_style.configure("TLabel", background="#F8F8F8", font=("Arial", 12))

# Load and display an image
image = Image.open("student.png")
image = image.resize((100, 100), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
image_label = Label(window, image=photo)
image_label.pack(pady=10)

# Create labels
status_label = Label(window, text="Status: Ready")

# Create buttons
create_button = Button(window, text="Create Student", command=create_button_clicked)
read_button = Button(window, text="Read Student", command=read_button_clicked)
update_button = Button(window, text="Update Student", command=update_button_clicked)
delete_button = Button(window, text="Delete Student", command=delete_button_clicked)

# Create output text area
output_text = Text(window, height=10, width=50)
output_text.config(state=DISABLED)

# Add labels, buttons, and output text area to the window
status_label.pack()
create_button.pack(pady=5)
read_button.pack(pady=5)
update_button.pack(pady=5)
delete_button.pack(pady=5)
output_text.pack()

# Start the GUI event loop
window.mainloop()
