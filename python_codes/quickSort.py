def merge(array1,array2):
	i = 0
	j = 0
	array = []
	while (i<len(array1) and j<len(array2)):
		if (array1[i]<array2[j]):
			array.append(array1[i])
			i+=1
		else:
			array.append(array2[j])
			j+=1
	while (i<len(array1)):
		array.append(array1[i])
		i+=1
	while (j<len(array2)):
		array.append(array2[j])
		j+=1
	return array

def quickSort(array):
	if (len(array)<=1):
		return array
	array1 = []
	array2 = []
	pivot = array[int(len(array))-1]

	#Calling merge on the two broken down lists
	for i in range (len(array)-1):
		if (array[i]<pivot):
			array1.append(array[i])
		else:
			array2.append(array[i])
	quickSorted1 = quickSort(array1)
	quickSorted2 = quickSort(array2)
	arraytemp = merge(quickSorted1,quickSorted2)

	#Ensuring pivot is added in between
	pivotpos = len(quickSorted1)
	arrayans = []
	for i in range(len(arraytemp)):
		if (i==pivotpos):
			arrayans.append(pivot)
		arrayans.append(arraytemp[i])
	if (pivotpos==len(arraytemp)):
		arrayans.append(pivot)

	return arrayans



		
		
