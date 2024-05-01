import socket
import tkinter as tk
from tkinter import scrolledtext

def send_message(event=None):
    message = entry.get()
    s.send(message.encode('utf-8'))
    entry.delete(0, tk.END)

def receive_message():
    while True:
        data = s.recv(BUFFER_SIZE)
        if not data:
            break
        root.after(10, chat_log.insert, tk.END, "Server: " + data.decode('utf-8') + "\n")

def close_window(event=None):
    root.destroy()

def focus_entry(event=None):
    entry.focus_set()

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
s.connect((TCP_IP, TCP_PORT))

# Create GUI
root = tk.Tk()
root.title("Chat Client")
root.state('zoomed')

root.columnconfigure((0,1,2), weight=10)
root.rowconfigure(0, weight=50)
root.rowconfigure((1,2),weight=10)

# Chat Log
chat_log = scrolledtext.ScrolledText(root)
chat_log.grid(row=0, column=1, sticky='nesw', pady=10)

# Input Entry
entry = tk.Entry(root, width=20)
entry.grid(row=2, column=1, padx=5, pady=10, sticky='new')


# Send Button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=2, column=2, padx=10, pady=10, sticky='nw')

#close button 
close_button = tk.Button(root, text='Close', command=close_window)
close_button.grid(row=0, column=2, sticky='ne', pady=10)

# Bind Enter key to send_message function
root.bind('<Return>', send_message)

#Bind Ctrl+m to close root window
root.bind('<Control-m>',close_window)

#Bind '/' key to focus on the entry box
root.bind('<slash>', focus_entry)

# Start receiving messages in a separate thread
import threading
receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

# Run the GUI
root.mainloop()

# Close the socket when the GUI is closed
s.close()
