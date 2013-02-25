import time

def sumOfN3(n):
	start = time.time()
	theSum = n*(n+1)/2
	end = time.time()
	return(theSum, end-start)

def sumOfN2(n):
	start = time.time()
	theSum = sumOfN(n)
	end = time.time()
	return theSum, end-start

def sumOfN(n):
	theSUM = 0
	for i in range(1, n+1):
		theSUM = theSUM + i
	return theSUM