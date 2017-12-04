from socket import *

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(("192.168.50.1",8686))

clientSocket.send("haha".encode("gb2312"))
recvData = clientSocket.recv(1024)

print("recvData:%s"%recvData)

clientSocket.close()

