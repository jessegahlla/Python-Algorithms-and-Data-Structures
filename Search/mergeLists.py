def mergeLists(l1, l2):
	newList = []
	pos1 = 0
	pos2 = 0
	pos3 = 0
	while len(newList) < len(l1 + l2):
		if pos1 < len(l1) and pos2 == len(l2):
			while pos1 < len(l1):
				newList.append(l1[pos1])
				pos1 = pos1 + 1
			break
		if pos1 == len(l1) and pos2 < len(l2):
			while pos2 < len(l2):
				newList.append(l2[pos2])
				pos2 = pos2 + 1
			break
		if l1[pos1] < l2[pos2]:
			newList.append(l1[pos1])
			pos1 = pos1 + 1
		else:
			newList.append(l2[pos2])
			pos2 = pos2 + 1
		pos3 = pos3 + 1
	return newList

ll1 = [1, 2, 4, 9, 13, 20]
ll2 = [3, 5]
print(mergeLists(ll1,ll2))