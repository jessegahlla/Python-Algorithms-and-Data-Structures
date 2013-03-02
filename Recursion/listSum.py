class stack:
	def __init__ (self):
		self.items = []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()

def listSum(numList):
	if len(numList) == 1:
		return numList[0]
	else:
		return numList[0] + listSum(numList[1:])

def factorial(number):
	if number == 0:
		return 1
	else:
		return number * factorial(number - 1)

def convertToBase(number, base):
	convertString = "0123456789ABCDEF"
	rStack = stack()
	if number < base:
		rStack.push(convertString[number])
	else:
		rStack.push(convertString[number % base])
		convertToBase(number // base, base)

def reverseMe(string):
	if len(string) == 1:
		return string
	else:
		return string[-1] + reverseMe(string[:-1])

def palin(string):
	string = string.replace(" ", "")
	string = string.lower()
	if len(string) <= 1:
		return True
	else:
		if string[0] == string[-1]:
			return palin(string[1:-1])
		else:
			return False

print(convertToBase(1453,16))