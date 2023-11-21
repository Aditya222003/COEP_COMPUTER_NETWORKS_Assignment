import random

def transmission(totalFrames, windowSize):
    receiveWindow = [0] * (totalFrames + 1)
    smallestUnacknowledgedFrame = 1  # Start from frame 1
    tt = 0

    while smallestUnacknowledgedFrame <= totalFrames:
        for k in range(smallestUnacknowledgedFrame, min(smallestUnacknowledgedFrame + windowSize, totalFrames + 1)):
            if receiveWindow[k] == 0:
                print(f"Sending Frame {k}...")
                tt += 1

        for k in range(smallestUnacknowledgedFrame, min(smallestUnacknowledgedFrame + windowSize, totalFrames + 1)):
            f = random.randint(0, 1)
            if not f:
                print(f"Acknowledgment for Frame {k}...")
                receiveWindow[k] = 1
            else:
                if receiveWindow[k] == 0:
                    print(f"Timeout!! Frame Number: {k} Not Received")
                    print("Retransmitting Window...")

        print()

        while smallestUnacknowledgedFrame <= totalFrames and receiveWindow[smallestUnacknowledgedFrame] == 1:
            smallestUnacknowledgedFrame += 1

    return tt

if __name__ == "__main__":
    totalFrames = int(input("Enter the Total number of frames: "))
    windowSize = int(input("Enter the Window Size: "))
    
    tt = transmission(totalFrames, windowSize)
    
    print(f"Total number of frames sent and resent are: {tt}, {tt - totalFrames}")
