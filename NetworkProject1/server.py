import socket
import time


def udp_server():
    server_ip = "0.0.0.0"  # Listen on all available network interfaces
    server_port = 8855

    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the IP address and port
    server_socket.bind((server_ip, server_port))

    # Dictionary to store the last received message from each client
    client_messages = {}

    while True:
        # Receive data from the client
        data, client_address = server_socket.recvfrom(2048)
        message = data.decode()

        # Store the last received message from the client with the current timestamp
        client_messages[client_address[0]] = (message, time.strftime("%Y-%m-%d %H:%M:%S"))

        # Display the received messages with timestamps
        print("Server - Last received messages:")
        for i, (client_ip, (message, timestamp)) in enumerate(client_messages.items(), start=1):
            print(f"{i}- Received message from {client_ip} at {timestamp}: {message}")
        print()


udp_server()
