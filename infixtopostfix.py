import stack

def postfoxThis(infixEquation = None):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	opstack = stack.stack()
	output = []
	infixList = infixEquation.split()
	operand = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	operanum = "0123456789"
	operator = ["*","/","+","-"]
	op = ""
	for i in infixList[0]:
		if i in operand or i in operanum:
			output.append(i)
		elif i == "(":
			opstack.push(i)
		elif i == ")":
			while opstack.peek() != "(":
				op = opstack.pop()
				output.append(op)
			opstack.pop()
		else:
			while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[i]):
				output.append(opstack.pop())
			opstack.push(i)
	while not opstack.isEmpty():
		output.append(opstack.pop())
	return " ".join(output)