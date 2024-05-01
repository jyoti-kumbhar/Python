import tkinter as tk
from tkinter import ttk

def on_dropdown_change(event):
    selected_value = dropdown_var.get()

root = tk.Tk()
root.title("Sidebar with dropdown")

sidebar_frame = ttk.Frame(root, width=200, padding=(10,10,0,10))
sidebar_frame.grid(row=0, column=0, sticky='nesw')

label = ttk.Label(sidebar_frame, text='sidebar')
label.grid(row=0, column=0, pady=(0,10))

options=['option1', 'option2','option3']
dropdown_var = tk.StringVar()
dropdown = ttk.Combobox(sidebar_frame, textvariable=dropdown_var , values=options)
dropdown.grid(row=1, column=0, pady=(0,10))
dropdown.set(options[0])

dropdown.bind("<<Combobox>>", on_dropdown_change)

content_frame=ttk.Frame(root, padding=(10,10,10,10))
content_frame.grid(row=0, column=1, sticky='nesw')

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1,weight=1)

root.mainloop()