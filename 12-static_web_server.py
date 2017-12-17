#coding:utf-8
import socket
import re

from multiprocessing import Process

# 設置靜態文件根目錄
HTML_ROOT_DIR = "./html"

def handle_client(client_socket):
	"""處理客戶端請求"""
	# 獲取客戶端請求數據
	request_data = client_socket.recv(1024)
	print("request data: ",request_data)
	request_lines = request_data.splitlines()
	for line in request_lines:
		print(line)
	
	# 解析請求報文
	request_start_line = request_lines[0]
	# 提取用戶請求的文件名
	file_name = re.match(r"\w+ +(/[^ ]*) ",request_start_line.decode("utf-8")).group(1)
	if "/" == file_name:
		file_name = "/index.html"

	#打開文件，讀取內容
	try:
		file = open(HTML_ROOT_DIR + file_name,"rb")
	except IOError:
		response_start_line = "HTTP/1.1 404 NOt Found\r\n"
		response_headers = "Server: My server\r\n"
		response_body = "The file is not found!"
	else:
		file_data = file.read()
		file.close()



		# 構造響應數據
		response_start_line = "HTTP/1.1 200 OK\r\n"
		response_headers = "Server:My server\r\n"
		response_body = file_data.decode("utf-8")
	response = response_start_line + response_headers + "\r\n" + response_body
	print("response data:",response)

	# 向客戶端返回響應數據
	client_socket.send(bytes(response,"utf-8"))
	
	# 關閉客戶端鏈接
	client_socket.close()

if __name__=="__main__":
	server_socket = socket.socket(socket.AF_INET,
		socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	server_socket.bind(("",8000))
	server_socket.listen(128)

	while True:
		client_socket,client_addr = server_socket.accept()
		print("[%s,%s]用戶已鏈接"%client_addr)
		handle_client_process = Process(target=handle_client,
			args=(client_socket,))
		handle_client_process.start()
		client_socket.close()


