import time

def smallestNumber1(someList):
	start = time.time()
	smallestNumber = someList[0]
	for element in someList:
		for otherElement in someList:
			if element < smallestNumber:
				smallestNumber = otherElement
	end = time.time()
	return smallestNumber, end - start

def smallestNumber2(someList):
	start = time.time()
	smallestNumber = someList[0]
	for element in someList:
		if element < smallestNumber:
			smallestNumber = element
	end = time.time()
	return smallestNumber, end - start

a = [12, 43, 2, 1, 45, 1, 59, 199, 93, 0, 12, 34, 3, 6, 7]
print(smallestNumber2(a))