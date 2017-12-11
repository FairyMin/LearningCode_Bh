import time

#帶有yield的函數就是一個生成器
def A():
	while True:
		print("-----A------")
		#執行到yield這一句代碼時，會結束生成器的執行，回到下面的
		# __next__（）方法下面的代碼繼續執行
		yield
		time.sleep(0.5)

def B(c):
	while True:
		print("-----B------")
		#此處調用__next__()方法，會跳轉到生成器中執行代碼
		c.__next__()
		time.sleep(0.5)

if __name__=='__main__':
	a = A()
	B(a)
