# Bubble Sort is the simplest sorting algorithm that works by repeatedly
# swapping the adjacent elements if they are in wrong order.

def bubbleSort(array):
	for j in range (len(array)):
		for i in range (len(array)-1-j):
			if array[i]>array[i+1]:
				k = array[i];
				array[i] = array[i+1]
				array[i+1] = k
