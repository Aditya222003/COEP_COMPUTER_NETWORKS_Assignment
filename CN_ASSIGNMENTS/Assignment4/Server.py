import socket
import threading
import datetime

# Define the server's IP address and an initial port
SERVER_IP = '127.0.0.1'
INITIAL_PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Function to attempt binding to a port and handle errors
def bind_to_port(port):
    try:
        server_socket.bind((SERVER_IP, port))
        return True
    except OSError as e:
        if e.errno == 98:  # Address already in use
            return False
        else:
            raise

# Find an available port
def find_available_port():
    port = INITIAL_PORT
    while not bind_to_port(port):
        port += 1
    return port

# Try to find an available port to bind
SERVER_PORT = find_available_port()

# Listen for incoming connections
server_socket.listen()

# Lists to store client sockets and their usernames
client_sockets = []
client_usernames = {}

# Function to broadcast messages to all clients
def broadcast(message, sender_socket):
    for client in client_sockets:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                # If there is an issue with a client socket, remove it
                remove_client(client)

# Function to remove a client
def remove_client(client_socket):
    if client_socket in client_sockets:
        username = client_usernames[client_socket]
        client_sockets.remove(client_socket)
        del client_usernames[client_socket]
        broadcast(f"{username} has left the chat.\n".encode('utf-8'), client_socket)

# Function to handle individual clients
def client_handler(client_socket):
    username = client_socket.recv(1024).decode('utf-8')
    client_usernames[client_socket] = username
    welcome_message = f"Welcome, {username}!\n"
    client_socket.send(welcome_message.encode('utf-8'))
    broadcast(f"{username} has joined the chat.\n".encode('utf-8'), client_socket)

    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                broadcast(f"[{timestamp}] {username}: {message.decode('utf-8')}".encode('utf-8'), client_socket)
            else:
                remove_client(client_socket)
                break
        except:
            remove_client(client_socket)
            break

# Main server loop
print(f"Server is listening on {SERVER_IP}:{SERVER_PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    client_sockets.append(client_socket)

    # Create a thread to handle the client
    client_thread = threading.Thread(target=client_handler, args=(client_socket,))
    client_thread.start()
