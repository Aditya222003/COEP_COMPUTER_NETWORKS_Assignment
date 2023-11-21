import random

class GBN:
    def __init__(self, window_size):
        self.window_size = window_size
        self.sender_base = 0
        self.next_sequence_number = 0
        self.receiver_base = 0
        self.buffer = [None] * window_size

    def send(self, data):
        if self.next_sequence_number < self.sender_base + self.window_size:
            self.buffer[self.next_sequence_number % self.window_size] = (data, self.next_sequence_number)
            print(f"Sending frame {self.next_sequence_number}")
            self.next_sequence_number += 1
        else:
            print("Sender window is full. Waiting for acknowledgments.")

    def receive(self, ack):
        ack_sequence_number = ack[1]
        if self.receiver_base <= ack_sequence_number < self.receiver_base + self.window_size:
            self.buffer[ack_sequence_number % self.window_size] = None
            print(f"Received acknowledgment for frame {ack_sequence_number} successfully.")
            while self.buffer[self.receiver_base % self.window_size] is None:
                self.receiver_base += 1
        else:
            print(f"Discarding out-of-order acknowledgment for frame {ack_sequence_number}.")

    def acknowledge(self):
        ack = (random.randint(0, 1), self.sender_base)
        return ack

if __name__ == "__main__":
    sender = GBN(window_size=4)
    receiver = GBN(window_size=4)

    while sender.sender_base < 10:
        if sender.next_sequence_number < sender.sender_base + sender.window_size:
            sender.send(sender.next_sequence_number)
        ack = sender.acknowledge()
        receiver.receive(ack)
