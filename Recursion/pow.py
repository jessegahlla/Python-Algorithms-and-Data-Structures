def power(base, power):
	if power == 0:
		return 1
	else:
		return base * pow(base, power - 1)

def exp(base, power):
	if power == 1:
		return base
	elif power % 2 == 0:
		return exp(base*base,power / 2)
	elif power % 2 == 1:
		return base * exp(base*base,(power-1)/2)

print(power(16,2))