def maxheapify (array):
	i = int(len(array)/2)
	while (i>=0):
		leftchild = (2*i)+1
		rightchild = (2*i)+2
		if (leftchild<len(array) and array[i]<array[leftchild]):
			temp = array[i]
			array[i] = array[leftchild]
			array[leftchild] = temp
		if (rightchild<len(array) and array[i]<array[rightchild]):
			temp = array[i]
			array[i] = array[rightchild]
			array[rightchild] = temp
		i = i-1
		print(array)
	return array


def heapSort (array):
	maxheapify(array)
	i = len(array)-1

	while(i>=1):
		print(array)
		temp = array[0] 
		array[0] = array[i]
		array[i] = temp
		array[0:i] = maxheapify(array[0:i])
		i = i - 1

	print(array)




