import socket
import random
import time

# Simulated network delay
NETWORK_DELAY = 0.1

def simulate_network_delay():
    time.sleep(NETWORK_DELAY)

def stop_and_wait_server():
    print("Stop and Wait Protocol Server")
    sender_window = ["Packet1", "Packet2", "Packet3", "Packet4", "Packet5"]
    ack_received = False
    while sender_window:
        packet = sender_window[0]
        print(f"Sending: {packet}")
        simulate_network_delay()
        if random.random() < 0.8:
            print("Packet lost! Retrying...")
        else:
            print("Packet received!")
            ack_received = True
        if ack_received:
            sender_window.pop(0)
            ack_received = False

def go_back_n_server():
    print("Go Back N Protocol Server")
    sender_window = ["Packet1", "Packet2", "Packet3", "Packet4", "Packet5"]
    next_seq_num = 0
    ack_received = False
    while sender_window:
        for i in range(next_seq_num, min(next_seq_num + 3, len(sender_window))):
            packet = sender_window[i]
            print(f"Sending: {packet}")
            simulate_network_delay()
            if random.random() < 0.8:
                print(f"Packet {i+1} lost! Retrying...")
            else:
                print(f"Packet {i+1} received!")
                ack_received = True
            if ack_received:
                next_seq_num += 1
                ack_received = False

def selective_repeat_server():
    print("Selective Repeat Protocol Server")
    sender_window = ["Packet1", "Packet2", "Packet3", "Packet4", "Packet5"]
    ack_received = [False] * len(sender_window)
    while any(not ack for ack in ack_received):
        for i in range(len(sender_window)):
            if not ack_received[i]:
                packet = sender_window[i]
                print(f"Sending: {packet}")
                simulate_network_delay()
                if random.random() < 0.8:
                    print(f"Packet {i+1} lost! Retrying...")
                else:
                    print(f"Packet {i+1} received!")
                    ack_received[i] = True

def handle_client_connection(client_socket, choice):
    if choice == '1':
        stop_and_wait_server()
    elif choice == '2':
        go_back_n_server()
    elif choice == '3':
        selective_repeat_server()
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)
    print("Server listening on port 12345...")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")
        choice = client_socket.recv(1024).decode()
        handle_client_connection(client_socket, choice)

if __name__ == "__main__":
    start_server()