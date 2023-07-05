from socket import *
serverPort = 9977
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
while True:
    try:
        connectionSocket, addr= serverSocket.accept()
        sentence = connectionSocket.recv(2048).decode()
        print (addr)
        print (sentence)
        ip = addr[0]
        port = addr[1]
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
        connectionSocket.send("\r\n".encode())
        f1 = open("index.html", "rb")
        data=f1.read()
        connectionSocket.send(data)
        #s="<html><head> <title>Simple Webserver</title></head><body> Hello  <font color=\"red\"> ENCS3320 Computer Networks </font> IP="+str(ip) +"Port=" +str(port)   + " </body></html>\r\n"
        #connectionSocket.send(s)
        connectionSocket.close()
    except OSError:
        print ("IO error")
    else:
        print ("OK")