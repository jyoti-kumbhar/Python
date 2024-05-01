import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
s.bind((TCP_IP, TCP_PORT))

# Enable the server to accept connections
s.listen(1)

print("Server listening on {}:{}".format(TCP_IP, TCP_PORT))

# Accept a connection from a client
conn, addr = s.accept()
print('Connection address:', addr)

while True:
    # Receive data from the client
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    print("client:", data.decode('utf-8'))

    # Send a response back to the client
    message = input("you: ")
    conn.send(message.encode('utf-8'))

# Close the connection
conn.close()
