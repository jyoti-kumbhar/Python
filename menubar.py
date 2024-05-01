from tkinter import *

def file_new():
    print("New File")

def file_open():
    print("Open File")

def file_save():
    print("Save File")

def menu_window():
    menu_window = Toplevel(root)
    menu_window.title('Menu')
    menu_window.state('zoomed')
    menu_window['bg'] = 'green'

# Create the main window
root = Tk()
root.title("Menu Widget Example")

# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create a File menu with some options
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=file_new)
file_menu.add_command(label="Open", command=file_open)
file_menu.add_command(label="win", command=menu_window)
file_menu.add_command(label="Save", command=file_save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create an Edit menu (just for demonstration)
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

# Run the main loop
root.mainloop()
