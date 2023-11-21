import socket
import threading
import sys

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((SERVER_IP, SERVER_PORT))
except ConnectionRefusedError:
    print("Error: The server is not running.")
    sys.exit()

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Disconnected from the server.")
            client_socket.close()
            sys.exit()

def send_messages():
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

username = input("Enter your username: ")
client_socket.send(username.encode('utf-8'))

# Create threads for sending and receiving messages
receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

# Start the threads
receive_thread.start()
send_thread.start()
