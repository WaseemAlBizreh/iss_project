import socket

# Define the server's IP address and port to connect to
server_ip = 'YOUR_SERVER_IP'  # Replace with the actual IP address of the server device
server_port = 12345  # Use the same port number as in the server

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))

while True:
    # Send a message to the server
    message = input("You: ")
    client_socket.send(message.encode())

    # Receive a reply from the server
    reply = client_socket.recv(1024).decode()
    print(f"Server: {reply}")

# Close the socket
client_socket.close()
