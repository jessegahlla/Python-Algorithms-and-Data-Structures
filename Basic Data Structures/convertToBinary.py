import stack

def convertToBinary(number = None, binaryRep = None):
	binaryRep = stack.stack()
	while number > 0:
		digit = number % 2
		number = number // 2
		binaryRep.push(digit)
	binaryNumber = ""
	for i in range(binaryRep.size()):
		binaryNumber = binaryNumber + str(binaryRep.pop())
	return str(binaryNumber)
	
def baseConverter(number,base):
	digits = "0123456789ABCDEF"
	otherBase = stack.stack()
	while number > 0:
		digit = number % base
		number = number // base
		otherBase.push(digit)
	
	newString = ''
	for i in range(otherBase.size()):
		newString = newString + str(digits[otherBase.pop()])
	return str(newString)