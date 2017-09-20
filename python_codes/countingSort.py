def countingSort(array):
	countarr = []
	#Here 12 is taken assuming no element will be larger.
	countarr = [0]*12
	for i in range(len(array)):
		countarr[array[i]]+=1
	sum=0
	for i in range(len(countarr)):
		sum = sum + countarr[i]
		countarr[i]=sum

	ansarray = []
	print(countarr)
	ansarray = [0]*len(array)
	for i in range(len(array)):
		 ansarray[ countarr[ array[i] ] -1 ] = array[i]
	return ansarray
