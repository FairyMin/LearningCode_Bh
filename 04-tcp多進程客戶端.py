from socket import *
from multiprocessing import Process

def ser_child_thread(clientSocket,clientInfo):
	while True:
		#接收數據
		recvData = 	clientSocket.recv(1024)
		#判斷客戶端是否斷開
		if len(recvData) > 0:
			#打印服務器信息以及接收到的數據信息
			print("%s,%s"%(str(clientInfo),recvData))
		else:
			print("[%s]客戶端已經關閉"%str(clientInfo))
			break
	#關閉子線程的套接字
	clientSocket.close()

def main():
	#創建套接字
	serverSocket = socket(AF_INET,SOCK_STREAM)
	#這句不知爲何
	serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	#綁定ip和端口
	serverSocket.bind(("",7788))
	#設置套接字爲listen狀態
	serverSocket.listen(5)

	while True:
		#accpet 爲新的需要被服務的客戶端創建套接字
		clientSocket,clientInfo = serverSocket.accept()
		#創建並啓動子線程
		chi_ser	= Process(target = ser_child_thread,
		args = (clientSocket,clientInfo))
		chi_ser.start()
		#關閉主進程的clientSocket套接字
		clientSocket.close()
		
	#關閉套接字
	serverSocket.close()
if __name__ == '__main__':
	main()
