def sequentialSearch(aList, item):
	pos = 0
	found  = False
	while pos < len(aList) and not found:
		if aList[pos] == item:
			found = True
		else:
			pos = pos + 1
	return found

def orderedSequentialSearch(aList, item):
	pos = 0
	found = False
	while pos < len(aList) and not found:
		if aList[pos] == item:
			found = True
		else:
			if aList[pos] > item:
				found = False
			else:
				pos = pos + 1
	return found

def binarySearch(aList, item):
	first = 0
	last = len(aList) - 1
	found = False

	while first <= last and not found:
		midpoint = (last + first) // 2
		if aList[midpoint] == item:
			found = True
		else: 
			if item < aList[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	return found	

def recursiveBinarySearch(aList, item):
	if len(aList) == 0:
		return False
	else:
		midpoint = len(aList) // 2
		if aList[midpoint] == item:
			return True
		else:
			if aList[midpoint] > item:
				return recursiveBinarySearch(aList[:midpoint], item)
			else:
				return recursiveBinarySearch(aList[midpoint+1:], item)

l = [1, 3, 54, 6, 75, 2, 34, 8]
ol = [1,2,3,6,8,34,54,75]
print(sequentialSearch(l, 2))
print(orderedSequentialSearch(ol,8))
print(binarySearch(ol,34))
print(recursiveBinarySearch(ol,334))