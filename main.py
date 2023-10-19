import socket

server_ip = '192.168.137.97'
server_port = 2001

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections (max 1 connection in this example)
server_socket.listen(1)
print(f"Server is listening on {server_ip}:{server_port}")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

while True:
    # Receive a message from the client
    message = client_socket.recv(1024).decode()
    if not message:
        break

    print(f"Client: {message}")

    # Send a reply to the client
    reply = input("You: ")
    client_socket.send(reply.encode())

# Close the sockets
client_socket.close()
server_socket.close()
