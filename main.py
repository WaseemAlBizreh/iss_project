# Read How to Run File Before run the code
import socket
from cryptography.fernet import Fernet

# this is the key ...
key = b'P0qB1OOQ9PZEgNUfB0YhaPx4PO_C_VKjxcJ5MMTG3OY='
cs = Fernet(key)
# Define the server's IP address and port to connect to
server_ip = '127.0.0.1'
server_port = 8000

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections (max 1 connection in this example)
server_socket.listen(1)
print(f"Server is listening on {server_ip}:{server_port}")

# Accept a client.py connection
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

while True:
    # Receive a message from the client.py
    message = client_socket.recv(1024)
    print(message)
    message = cs.decrypt(message)
    message = message.decode()
    if not message:
        break

    print(f"Client: {message}")

    # Send a reply to the client.py
    reply = input("You: ")
    reply = cs.encrypt(reply.encode())
    client_socket.send(reply)

# Close the sockets
client_socket.close()
server_socket.close()
