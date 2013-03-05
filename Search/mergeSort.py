def mergeSort(aList):
	print("Splitting %s" % aList)
	if len(aList) > 1:
		mid = len(aList) // 2
		leftHalf = aList[:mid]
		rightHalf = aList[mid:]
		print("Left Half: %s" % leftHalf)
		print("Right Half: %s" % rightHalf)
		mergeSort(leftHalf)
		mergeSort(rightHalf)
		i = 0
		j = 0
		k = 0
		while i<len(leftHalf) and j < len(rightHalf):
			if leftHalf[i] < rightHalf[j]:
				aList[k] = leftHalf[i]
				i = i + 1
			else:
				aList[k] = rightHalf[j]
				j = j + 1
			k = k + 1
		while i < len(leftHalf):
			aList[k] = leftHalf[i]
			i = i + 1
			k = k + 1
		while j < len(rightHalf):
			aList[k] = rightHalf[j]
			j = j + 1
			k = k + 1
	print("Merging %s" % aList)

alist = [54,26,93,17,77,31,44,55,20]
l = [2, 3, 8, 6, 10] [75, 34, 54]
mergeSort(alist)
print(alist)