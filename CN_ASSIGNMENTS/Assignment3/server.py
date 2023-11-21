import socket

# Define host and port to listen on
HOST = '127.0.0.2'  # Change to the server's IP address if needed
PORT = 12345  # You can choose any available port

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f"Server is listening on {HOST}:{PORT}")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

while True:
    # Receive data from the client
    client_message = client_socket.recv(1024).decode('utf-8')
    if not client_message:
        break  # Connection closed by client

    print(f"Client: {client_message}")

    # Get a message from the server user
    server_response = input("Server: ")
    
    # Send the server's response back to the client
    client_socket.send(server_response.encode('utf-8'))

# Close the sockets
client_socket.close()
server_socket.close()
