import socket

# Define the server's IP address and port
SERVER_IP = '127.0.0.2'  # Change to the server's IP address
SERVER_PORT = 12345  # Use the same port as the server

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_IP, SERVER_PORT))
print(f"Connected to server at {SERVER_IP}:{SERVER_PORT}")

while True:
    # Get a message from the user
    user_input = input("Client: ")
    
    # Send the user's message to the server
    client_socket.send(user_input.encode('utf-8'))

    # Receive the server's response
    server_response = client_socket.recv(1024).decode('utf-8')
    print(f"Server: {server_response}")

# Close the socket
client_socket.close()
