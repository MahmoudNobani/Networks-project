from socket import *

def errorMessage(response):
    SocketConnect.send("HTTP/1.1 404 Not Found\r\n".encode("UTF-8"))
    SocketConnect.send("Content-Type: text/html \r\n".encode("UTF-8"))
    response = "<html><head><title>Error 404</title></head><body> <p style='color: red;'>THE FILE IS NOT FOUND </p><p><b>Mahmoud nobani-1180729</b></p><p>IP ADDRESS: " + \
               address[0] + "</p><p>PORT:" + str(
        address[1])
    response = response.encode()
    sendresponse(response)

def sendresponse(response):
    # Send a carriage return and line feed to the client
    SocketConnect.send("\r\n".encode("UTF-8"))

    # Send the response to the client
    SocketConnect.send(response)

    # Close the connection with the client
    SocketConnect.close()


# Set the server port number
svrPort = 9977

# Create a new socket object, first arg for ipv4, second for tcp
Socket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to a specific address and port
Socket.bind(("", svrPort))

# Put the socket in a listening state
Socket.listen(1)

# Print a message indicating the server is ready
print("Connection Established, Go to the local host server.")

# Start an infinite loop to handle incoming connections
while True:
    # Accept a client connection and get the client's address, first arg repesents socket connect, used for communication b/w
    # server and client, second is ip address
    SocketConnect, address = Socket.accept()

    # Receive the HTTP request from the client
    request1h = SocketConnect.recv(1024).decode()

    # Print the HTTP request
    print("HTTP REQUEST: \n", request1h)

    requestedFile = ""
    response = ""
    tempRF = ""

    # Check if a request was received
    if request1h:
        # Extract the requested file name from the HTTP request
        requestedFile = request1h.split(' ', 2)[1]

        # Check if the file name contains a file extension
        if '.' in requestedFile:
            # Extract the file extension
            tempRF = requestedFile[requestedFile.index('.'):]


    try:#handling requests
        if requestedFile == "/" or requestedFile == "/index.html" or requestedFile == "/main_en.html" or requestedFile == "/en":
            SocketConnect.send("HTTP/1.1 200 OK\r\n".encode("UTF-8"))
            myfile = open("main_en.html", 'rb')
            response = myfile.read()

            SocketConnect.send("Content-Type: text/html \r\n".encode("UTF-8"))
            sendresponse(response)

        elif requestedFile == "/ar":
            SocketConnect.send("HTTP/1.1 200 OK\r\n".encode("UTF-8"))
            myfile = open("main_ar.html", 'rb')
            response = myfile.read()

            SocketConnect.send("Content-Type: text/html \r\n".encode("UTF-8"))
            sendresponse(response)

        elif tempRF == ".html":
            SocketConnect.send("HTTP/1.1 200 OK\r\n".encode("UTF-8"))
            myfile = open(requestedFile.strip('/'), 'rb')
            response = myfile.read()

            SocketConnect.send("Content-Type: text/html \r\n".encode("UTF-8"))
            sendresponse(response)

        elif tempRF == ".css":
            SocketConnect.send("HTTP/1.1 200 OK\r\n".encode("UTF-8"))
            myfile = open(requestedFile.strip('/'), 'rb')
            response = myfile.read()

            SocketConnect.send("Content-Type: text/css \r\n".encode("UTF-8"))
            sendresponse(response)

        elif tempRF == ".jpg":
            SocketConnect.send("HTTP/1.1 200 OK\r\n".encode("UTF-8"))
            SocketConnect.send("Content-Type: image/jpeg \r\n".encode("UTF-8"))
            myfile = open(requestedFile.strip('/'), 'rb')
            response = myfile.read()
            sendresponse(response)

        elif tempRF == ".png":
            SocketConnect.send("HTTP/1.1 200 OK\r\n".encode("UTF-8"))
            SocketConnect.send("Content-Type: image/png \r\n".encode("UTF-8"))
            myfile = open(requestedFile.strip('/'), 'rb')
            response = myfile.read()
            sendresponse(response)

        elif requestedFile == "/yt":
            redirect_url = "https://www.youtube.com/"
            response = "HTTP/1.1 307 Temporary Redirect\r\n"
            response += "Location: " + redirect_url + "\r\n"
            sendresponse(response.encode())

        elif requestedFile == "/so":
            redirect_url = "https://stackoverflow.com/"
            response = "HTTP/1.1 307 Temporary Redirect\r\n"
            response += "Location:  " + redirect_url + "\r\n"
            sendresponse(response.encode())

        elif requestedFile == "/rt":
            redirect_url = "https://ritaj.birzeit.edu"
            response = "HTTP/1.1 307 Temporary Redirect\r\n"
            response += "Location: " + redirect_url + "\r\n"
            sendresponse(response.encode())

        else:
            SocketConnect.send("HTTP/1.1 200 OK\r\n".encode("UTF-8"))
            errorMessage(response)
    except:
        SocketConnect.send("HTTP/1.1 200 OK\r\n".encode("UTF-8"))
        errorMessage(response)
