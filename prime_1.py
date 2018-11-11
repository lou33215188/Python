def isPrime(i):     # 判断素数的函数
	flag = 1			#一个flag标记，用来判断素数，如果是1就是素数，如果不是0，就不是素数
	for each in range(i-2):		# 从2到i-1遍历 如果能出现一个数能整除，则不是素数，flag置0，并且退出循环
		if i % (each+2) == 0:	
			flag = 0 
			break
	return flag			#返回 flag

