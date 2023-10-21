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
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))

while True:
    # Send a message to the server
    message = input("You: ")
    message = message.encode()
    message = cs.encrypt(message)
    client_socket.send(message)

    # Receive a reply from the server
    reply = client_socket.recv(1024)
    print(reply)
    reply = cs.decrypt(reply)
    reply = reply.decode()
    print(f"Server: {reply}")

# Close the socket
client_socket.close()
