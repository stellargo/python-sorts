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
	while (i<len(array1))
		array.append(array1[i])
		i+=1
	while (j<len(array2)):
		array.append(array2[j])
		j+=1
	return array

def mergeSort(array):
	if (len(array)==1):
		return array
	half = int(len(array)/2)
	length = int(len(array))
	return merge ( mergeSort( array[0:half] ), mergeSort( array[half:length] ) )
