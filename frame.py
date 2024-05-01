from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Payroll Management System")
root.state('zoomed')
root['bg'] = 'light pink'

# Configuring row and column
root.columnconfigure((0, 1, 2), weight=10)
root.rowconfigure((0, 1, 2, 3, 4), weight=1)
root.rowconfigure(5, weight=5)

# Function to open a new frame within the same window
def open_new_frame():
    # Destroy existing frame if it exists
    for widget in root.winfo_children():
        if isinstance(widget, Frame):
            widget.destroy()

    new_frame = Frame(root, bg='lightblue')
    new_frame.pack(fill='both', expand=True)

    label = Label(new_frame, text="New Frame", font=("Helvetica", 16), bg='lightblue')
    label.pack(pady=10)

    # Add widgets or functionality to the new frame

# Button to open the new frame
open_frame_button = Button(root, text="Open New Frame", command=open_new_frame, padx=10, pady=5)
open_frame_button.pack(pady=20)

def open_new_frame1():
    # Destroy existing frame if it exists
    for widget in root.winfo_children():
        if isinstance(widget, Frame):
            widget.destroy()

    new_frame1 = Frame(root, bg='blue')
    new_frame1.pack(fill='both', expand=True)

    label1 = Label(new_frame1, text="New Frame1", font=("Helvetica", 16), bg='lightblue')
    label1.pack(pady=10)

    # Add widgets or functionality to the new frame

# Button to open the new frame
open_frame_button1 = Button(root, text="Open New Frame1", command=open_new_frame1, padx=10, pady=5)
open_frame_button1.pack(pady=20)

root.mainloop()
