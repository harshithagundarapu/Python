import socket

HOST = "127.0.0.1"
PORT = 8020

# Create sender socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)

print("Waiting for receiver...")

# Accept receiver connection
c, address = s.accept()
print("Connection to", address, "established")

total_frames = int(input("Enter total number of frames: "))
sequence_number = 0

# Send frames one by one
for frame_number in range(1, total_frames + 1):
    while True:
        print("Sending frame", frame_number, "-->", sequence_number)
        c.send(str(sequence_number).encode())

        # Wait for ACK for 5 seconds
        c.settimeout(5)

        try:
            ack = c.recv(1).decode()

            if not ack:
                raise ConnectionError("Receiver disconnected")

            print("ACK -->", ack)
            expected_ack = str(1 - sequence_number)

            if ack == expected_ack:
                sequence_number = 1 - sequence_number
                break

        except socket.timeout:
            print("Timeout")
            print("Sending frame again -->", sequence_number)

# Notify receiver that transmission is complete
c.send(b"E")
print("All frames sent successfully")

c.close()
s.close()
