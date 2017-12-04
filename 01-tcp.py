from socket import*
serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(("",7788))

serverSocket.listen(5)

clientSocket,clientInfo = serverSocket.accept()

recvData = clientSocket.recv(1024)

print("%s:%s"%(str(clientInfo),recvData))

clientSocket.close()
serverSocket.close()
