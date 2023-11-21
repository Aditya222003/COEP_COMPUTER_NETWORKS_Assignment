import socket

def server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    expected_packet_num = 0

    while True:
        data, sender_address = server_socket.recvfrom(1024)
        packet = data.decode()
        packet_num, packet_data, packet_checksum = packet.split(":")

        if int(packet_num) == expected_packet_num:
            if is_corrupted(packet_data, packet_checksum):
                ack = f"{packet_num}:NACK"
                server_socket.sendto(ack.encode(), sender_address)
            else:
                ack = f"{packet_num}:ACK"
                server_socket.sendto(ack.encode(), sender_address)
                print(packet_data, end="")
                expected_packet_num += 1
        else:
            ack = f"{expected_packet_num - 1}:ACK"
            server_socket.sendto(ack.encode(), sender_address)

def is_corrupted(data, checksum):
    # Check if the data is corrupted by comparing the checksum
    # You can implement your own checksum calculation method
    return int(checksum) != calculate_checksum(data)

def calculate_checksum(data):
    # Calculate the checksum of the data
    # You can implement your own checksum calculation method
    checksum = sum(ord(c) for c in data)
    return checksum

if __name__ == "__main__":
    host = "localhost"
    port = 12345
    server(host, port)
