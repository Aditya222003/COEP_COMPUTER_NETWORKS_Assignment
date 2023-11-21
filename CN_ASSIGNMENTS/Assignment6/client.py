import socket
import random
import time
import sys

# Simulated network delay
NETWORK_DELAY = 0.1

def simulate_network_delay():
    time.sleep(NETWORK_DELAY)

def stop_and_wait_client():
    print("Stop and Wait Protocol Client")
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

def go_back_n_client():
    print("Go Back N Protocol Client")
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

def selective_repeat_client():
    print("Selective Repeat Protocol Client")
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

def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 12345))

        print("Select a flow control protocol:")
        print("1. Stop and Wait")
        print("2. Go Back N")
        print("3. Selective Repeat")

        choice = input("Enter your choice: ")
        client_socket.send(choice.encode())

        if choice == '1':
            stop_and_wait_client()
        elif choice == '2':
            go_back_n_client()
        elif choice == '3':
            selective_repeat_client()

        client_socket.close()

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        # Add cleanup code if needed
        sys.exit(0)  # Exit the program gracefully

if __name__ == "__main__":
    main()