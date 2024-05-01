import socket
import tkinter as tk
from tkinter import scrolledtext

def send_message(event=None):
    message = entry.get()
    conn.send(message.encode('utf-8'))
    entry.delete(0, tk.END)

def receive_message():
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        chat_log.insert(tk.END, "Client: " + data.decode('utf-8') + "\n")

def close_window(event=None):
    conn.close()
    root.destroy()

def focus_entry(event=None):
    entry.focus_set()

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

# Bind the socket to a specific address and port
s.bind((TCP_IP, TCP_PORT))

# Enable the server to accept connections
s.listen(1)

# Accept a connection from a client
conn, addr = s.accept()
print('Connection address:', addr)

# Create GUI
root = tk.Tk()
root.title("Chat Server")
root.state('zoomed')

root.columnconfigure((0, 1, 2), weight=1)
root.rowconfigure((0, 1, 2), weight=1)

# Chat Log
chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat_log.grid(row=0, column=1, sticky='nesw', pady=10)

# Input Entry
entry = tk.Entry(root, width=20)
entry.grid(row=2, column=1, padx=5, pady=10, sticky='new')

# Send Button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=2, column=2, padx=10, pady=10, sticky='nw')

# Close Button
close_button = tk.Button(root, text='Close', command=close_window)
close_button.grid(row=0, column=2, sticky='ne', pady=10)

# Bind Enter key to send_message function
root.bind('<Return>', send_message)

# Bind Ctrl+m to close root window
root.bind('<Control-m>', close_window)

# Bind '/' key to focus on the entry box
root.bind('<slash>', focus_entry)

# Start receiving messages in a separate thread
import threading
receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

# Run the GUI
root.mainloop()
