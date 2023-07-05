import socket

# Define the redirect mappings
redirect_mappings = {
    '/yt': 'https://www.youtube.com',
    '/so': 'https://stackoverflow.com',
    '/rt': 'https://ritaj.birzeit.edu'
}

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 9977)

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server is listening on {}:{}'.format(*server_address))

while True:
    # Wait for a connection
    print('Waiting for a connection...')
    client_socket, client_address = server_socket.accept()
    print('Accepted connection from {}:{}'.format(*client_address))

    # Receive the request from the client
    request = client_socket.recv(1024).decode()
    print('Received request:\n{}'.format(request))

    # Extract the requested URL from the request
    requested_url = request.split()[1]

    # Check if the requested URL is in the redirect mappings
    if requested_url in redirect_mappings:
        # Create the response headers
        response_headers = [
            'HTTP/1.1 307 Temporary Redirect',
            'Location: {}'.format(redirect_mappings[requested_url]),
            'Connection: close',
            ''
        ]

        # Send the response headers to the client
        response = '\r\n'.join(response_headers)
        client_socket.sendall(response.encode())

    # Close the connection
    client_socket.close()
