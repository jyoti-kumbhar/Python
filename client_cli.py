import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
 
# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect((TCP_IP, TCP_PORT))
print("Connected to server at {}:{}".format(TCP_IP, TCP_PORT))

while True:
    # Send a message to the server
    message = input("you: ")
    s.send(message.encode('utf-8'))

    # Receive the server's response
    data = s.recv(BUFFER_SIZE)
    print("server:", data.decode('utf-8'))