def countingSortRadix(array,exp):
	countarr = []
	#Here 12 is taken assuming no element will be larger.
	countarr = [0]*10
	for i in range(len(array)):
		pos = int((array[i]/exp)%10)
		countarr[pos]+=1
	sum=0

	for i in range(len(countarr)):
		sum = sum + countarr[i]
		countarr[i]=sum

	ansarray = []
	ansarray = [0]*len(array)
	i=len(array)-1
	while (i>=0):
		pos = int((array[i]/exp)%10)
		ansarray[ countarr[ pos ] -1 ] = array[i]
		countarr[ pos ] -= 1
		i -= 1
	return ansarray

def radixSort(array):
	for i in range(3):
		array = countingSortRadix(array,10**(i))
	print (array)
	return array
		


