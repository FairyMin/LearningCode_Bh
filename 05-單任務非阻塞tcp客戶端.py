from socket import *
#1.創建socket
serSocket = socket(AF_INET,SOCK_STREAM)

#2.綁定本地ip以及port
serSocket.bind(('',7788))

#3.讓這個socket 變爲非堵塞
serSocket.setblocking(False)

#4.將socket變爲監聽(被動)套接字
serSocket.listen(100)
'''
#用來保存所有已經鏈接的客戶端的信息
#若沒有保存信息，當一個下一個客戶端到來時,
前一個客戶端的引用技術便會變爲0,從而丟失信息
'''
clientAddrList = []

while True:
	'''
	#等待一個新的客戶端的到來(即完成3次握手的客戶端)
	#此處的try是捕獲服務器在非阻塞狀態下沒有收到新的客戶端鏈接請求
	時產生的異常
	'''
	try:
		clientSocket,clientAddr = serSocket.accept()
	except:
		pass
	else:
		print("一個新的客戶端到來:%s"%str(clientAddr))
		clientSocket.setblocking(False)
		clientAddrList.append((clientSocket,clientAddr))

	for clientSocket,clientAddr in clientAddrList:
		'''
		此處的try捕捉套接字在非阻塞狀態下
		沒有收到消息的異常
		'''
		try:
			recvData = clientSocket.recv(1024)
		except:
			pass
		else:
			if len(recvData)>0:
				print("%s:%s"%(str(clientAddr),recvData))
			else:
				clientSocket.close()
				clientAddrList.remove((clientSocket,clientAddr))
				print("%s 已經下線"%str(clientAddr))



	
